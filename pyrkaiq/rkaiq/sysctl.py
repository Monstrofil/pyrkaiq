from functools import partial
from typing import Callable

from .event import Event
from .rk_types import (
    rk_aiq_sys_ctx_t,
    rk_aiq_metas_t,
    rk_aiq_err_msg_t,
    rk_aiq_working_mode_t,
    CamReturn
)

from pyrkaiq.raw import libaiq_3_0_9_1


def init(sensor_name: str,
         iqdir: str,
         error_callback: Callable[[rk_aiq_err_msg_t], CamReturn] = None,
         meta_callback: Callable[[rk_aiq_metas_t], CamReturn] = None) -> rk_aiq_sys_ctx_t:
    """
    Initialze aiq control system context.

    Should call before any other APIs

    Examples:
    ```python
    def error_cb(error: rk_aiq_err_msg_t):
        return XCamReturn.XCAM_RETURN_BYPASS

    init(
        sensor_name='mimx477',
        iqdir='/etc/iqfiles',
        error_callback=error_cb
    )
    ```

    Args:
        sensor_name (str):
            Active sensor media entity name. This represents the unique camera module
            in system. And the whole active pipeline could be retrieved by this.
        iqdir (str):
            The search directory of the iq files.
        error_callback:
            not mandatory. it's used to return system errors to user.
        meta_callback:
            not mandatory. it's used to return the metas(sensor exposure settings,\n
           isp settings, etc.) for each frame

    Returns:
        return system context if success, or NULL if failure.
    """
    return libaiq_3_0_9_1.rk_aiq_uapi2_sysctl_init(
        sensor_name, iqdir, error_callback, meta_callback)


def prepare(ctx: rk_aiq_sys_ctx_t, width: int, height: int, mode: rk_aiq_working_mode_t) -> CamReturn:
    """
     Prepare aiq control system before running

     Prepare AIQ running environment, should be called before `start`.

     And if re-prepared is required after `start` is called, should call `stop` first.


    Args:
        ctx: context received by the `init`
        width: sensor active output width, just used to check internally
        height: sensor active output height, just used to check internally
        mode: pipeline working mode

    Returns:

    """
    return libaiq_3_0_9_1.rk_aiq_uapi2_sysctl_prepare(ctx, width, height, mode)


def deInit(ctx: rk_aiq_sys_ctx_t) -> CamReturn:
    """
    Deinitialize aiq context.

    Should not be called in started state

    Args:
        ctx:
            the context returned by `init`

    Returns:
        return system context if success, or NULL if failure.
    """
    return libaiq_3_0_9_1.rk_aiq_uapi2_sysctl_deinit(ctx)


def getBindedSnsEntNmByVd(device_path: str) -> str:
    """
    Get sensor entity name from video node

    Args:
        device_path:
            stream video node full path (e.g. /dev/video11)

    Returns:
        return the binded sensor name
    """
    sensor_name = libaiq_3_0_9_1.rk_aiq_uapi2_sysctl_getBindedSnsEntNmByVd(device_path)
    return sensor_name.decode() if sensor_name is not None else sensor_name


def setMulCamConc(ctx: rk_aiq_sys_ctx_t, enabled: bool) -> None:
    """
    Set multiple cameras working concurrently

    Notify this AIQ ctx will run with other sensor's AIQ ctx.
    Should be called before `start``

    Args:
        ctx:
        enabled: set cams concurrently used or not

    Returns:
        Nothing
    """
    return libaiq_3_0_9_1.rk_aiq_uapi2_sysctl_setMulCamConc(ctx, enabled)

def start(ctx: rk_aiq_sys_ctx_t) -> CamReturn:
    """
    start aiq control system

    should be called after 'prepare'. After this call,
    the aiq system repeats getting 3A statistics from ISP driver, running
    aiq algorimths(AE, AWB, AF, etc.), setting new parameters to drivers.

    Args:
        ctx: context returned by `init`

    Returns:
        Nothing
    """
    libaiq_3_0_9_1.rk_aiq_uapi2_sysctl_start(ctx)


def stop(ctx: rk_aiq_sys_ctx_t, keep_external_hw_state: bool) -> CamReturn:
    """
    stop aiq control system

    Args:
        ctx: context returned by `init`
        keep_external_hw_state: do not change external devices status, like ircut/cpsl

    Returns:
        Nothing
    """
    return libaiq_3_0_9_1.rk_aiq_uapi2_sysctl_stop(ctx, False)


def version() -> libaiq_3_0_9_1.rk_aiq_ver_info_t:
    """
    Get information about AIQ components versions.

    Returns:
        `libaiq_3_0_9_1.rk_aiq_ver_info_t`
    """
    info = libaiq_3_0_9_1.rk_aiq_ver_info_t()
    libaiq_3_0_9_1.rk_aiq_uapi2_get_version_info(info)
    return info
