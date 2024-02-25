import logging
import os
import threading
from argparse import ArgumentParser
from dataclasses import dataclass

from v4l2py.device import EventType, Device

from pyrkaiq.base import PrettyStructure
from pyrkaiq.mediactl.libmediactl import (
    struct_media_entity_desc
)
from pyrkaiq.mediactl.sysctl import get_media_entities
from pyrkaiq.raw import libaiq_3_0_9_1
from pyrkaiq.raw.libaiq_3_0_9_1 import *
from pyrkaiq.rkaiq import sysctl
from pyrkaiq.rkaiq.rk_types import CamReturn
from pyrkaiq.rkaiq.sysctl import getBindedSnsEntNmByVd

# some dirty monkey patching to make data types pretty printable
for subclass in libaiq_3_0_9_1.Structure.__subclasses__():
    subclass.__repr__ = PrettyStructure.__repr__
    subclass._asdict = PrettyStructure._asdict

# print(sysctl.version())
#
# print(sysctl.getBindedSnsEntNmByVd('/dev/video11'))
#
#
# def meta_callback(item):
#     print('meta_callback', item.contents)
#     return CamReturn.XCAM_RETURN_NO_ERROR
#
#
# def err_callback(item):
#     print('err_callback', item.contents)
#     return CamReturn.XCAM_RETURN_NO_ERROR
#
#
# ctx = sysctl.init('m00_f_imx477 7-001a', '/etc/iqfiles', err_callback, meta_callback)
# print(ctx)
# print(sysctl.setMulCamConc(ctx, True))
#
# for item in RkAiqAlgoTypeEnum:
#     print(item.name, '=', rk_aiq_uapi2_sysctl_getAxlibStatus(ctx, item, 0))
#
CIFISP_V4L2_EVENT_STREAM_START = EventType.PRIVATE_START + 1
CIFISP_V4L2_EVENT_STREAM_STOP = EventType.PRIVATE_START + 2


#
# rk_aiq_uapi2_sysctl_prepare(ctx, 4048, 3040, 0)
# rk_aiq_uapi2_sysctl_start(ctx)
#
# f = open('/dev/video19')
# event = v4l2_event()
#
# sub = v4l2_event_subscription()
# sub.type = CIFISP_V4L2_EVENT_STREAM_START
# rt = ioctl(f.fileno(), VIDIOC_SUBSCRIBE_EVENT, sub)
# print('IOCTL', rt)
# rt = ioctl(f.fileno(), VIDIOC_DQEVENT, event)
#
# print('IOCTL', rt)
# print('EVENT', event.type)
#
# stats = rk_aiq_isp_stats_t()
# print(rk_aiq_uapi2_sysctl_get3AStats(ctx, stats))
# print(stats)
#
# sof_time = stats.unnamed_2.af_stats.sof_tim / 1000000;
# print("sof_tim %s, sharpness roia: %s-%s roib: %s-%s\n" % (
#     sof_time,
#     stats.unnamed_2.af_stats.roia_sharpness,
#     stats.unnamed_2.af_stats.roia_luminance,
#     stats.unnamed_2.af_stats.roib_sharpness,
#     stats.unnamed_2.af_stats.roib_luminance));
#
# rk_aiq_uapi2_sysctl_stop(ctx, False)
# rk_aiq_uapi2_sysctl_deinit(ctx)

@dataclass
class MediaTree:
    subdev_device: str
    params_device: str
    statistics_device: str
    mainpath_device: str

    sensor_name: str


def mediactl_get_device_name(description: struct_media_entity_desc):
    path = os.path.realpath("/sys/dev/char/%u:%u" % (
        description.v4l.major, description.v4l.minor))
    device_name = path.rsplit('/', 1)[-1]

    return '/dev/' + device_name


def iter_media_devices():
    media_devices = glob.glob('/dev/media*')

    for device_path in media_devices:
        entities = get_media_entities(device_path)

        isp_subdev = next((
            entity for entity in entities
            if entity.name == b"rkisp-isp-subdev"), None)
        input_params = next((
            entity for entity in entities
            if entity.name == b"rkisp-input-params"), None)
        isp_statistics = next((
            entity for entity in entities
            if entity.name == b"rkisp-statistics"), None)
        isp_mainpath = next((
            entity for entity in entities
            if entity.name == b"rkisp_mainpath"), None)

        if any((
                isp_subdev is None, input_params is None,
                isp_statistics is None, isp_mainpath is None
        )):
            logging.info('Device %s does not match rkisp3.x specification', device_path)
            continue

        logging.info('Device %s matches rkisp3.x specification', device_path)
        sensor_name = getBindedSnsEntNmByVd(mediactl_get_device_name(isp_mainpath))

        logging.info('Device is binded to the sensor %s', sensor_name)

        yield MediaTree(
            sensor_name=sensor_name,

            subdev_device=mediactl_get_device_name(isp_subdev),
            params_device=mediactl_get_device_name(input_params),
            statistics_device=mediactl_get_device_name(isp_statistics),
            mainpath_device=mediactl_get_device_name(isp_mainpath),
        )


def wait_for_event(fd: Device, event_type: int):
    while True:
        event = fd.deque_event()

        if event.type == event_type:
            break


def engine_thread(device: MediaTree):
    @libaiq_3_0_9_1.rk_aiq_error_cb
    def g_event_error_callback(item):
        return CamReturn.XCAM_RETURN_NO_ERROR

    @libaiq_3_0_9_1.rk_aiq_metas_cb
    def g_event_metas_callback(item):
        return CamReturn.XCAM_RETURN_NO_ERROR

    with Device(open(device.params_device)) as fd:
        try:
            ctx = sysctl.init(
                device.sensor_name, '/etc/iqfiles',
                g_event_error_callback, g_event_metas_callback)
            sysctl.setMulCamConc(ctx, False)

            # for item in RkAiqAlgoTypeEnum:
            #     print(item.name, '=', rk_aiq_uapi2_sysctl_getAxlibStatus(ctx, item, 0))

            sysctl.prepare(ctx, 4048, 3040, 0)

            logging.info('Subscribing to streaming events on %s', device.params_device)
            fd.subscribe_event(CIFISP_V4L2_EVENT_STREAM_START)
            fd.subscribe_event(CIFISP_V4L2_EVENT_STREAM_STOP)

            wait_for_event(fd, CIFISP_V4L2_EVENT_STREAM_START)
            logging.info('Stream on device %s started', device.sensor_name)

            sysctl.start(ctx)

            wait_for_event(fd, CIFISP_V4L2_EVENT_STREAM_STOP)
            logging.info('Stream on device %s ended', device.sensor_name)

        finally:
            fd.unsubscribe_event(CIFISP_V4L2_EVENT_STREAM_START)
            fd.unsubscribe_event(CIFISP_V4L2_EVENT_STREAM_STOP)


def main():
    device_threads = []
    for device in iter_media_devices():
        thread = threading.Thread(target=engine_thread, args=(device,))
        device_threads.append(thread)
        print(device)

    for thread in device_threads:
        thread.start()

    for thread in device_threads:
        thread.join()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    parser = ArgumentParser()
    parser.add_argument('--width', default=4048)
    parser.add_argument('--height', default=3040)

    args = parser.parse_args()

    main()
