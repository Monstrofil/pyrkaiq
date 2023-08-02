from ctypes import c_char, c_uint, c_int
from enum import IntEnum

from pyrkaiq.base import PrettyStructure


class rk_aiq_ver_info_t(PrettyStructure):
    __slots__ = [
        'aiq_ver',
        'iq_parser_ver',
        'iq_parser_magic_code',
        'awb_algo_ver',
        'ae_algo_ver',
        'af_algo_ver',
        'ahdr_algo_ver',
    ]
    _fields_ = [
        ('aiq_ver', c_char * int(16)),
        ('iq_parser_ver', c_char * int(16)),
        ('iq_parser_magic_code', c_uint),
        ('awb_algo_ver', c_char * int(16)),
        ('ae_algo_ver', c_char * int(16)),
        ('af_algo_ver', c_char * int(16)),
        ('ahdr_algo_ver', c_char * int(16)),
    ]


class rk_aiq_sys_ctx_t(PrettyStructure):
    pass


class rk_aiq_metas_t(PrettyStructure):

    __slots__ = [
        'frame_id',
    ]
    _fields_ = [
        ('frame_id', c_uint),
    ]


class rk_aiq_err_msg_t(PrettyStructure):
    __slots__ = [
        'err_code',
    ]
    _fields_ = [
        ('err_code', c_int),
    ]


class CamReturn(IntEnum):
    XCAM_RETURN_NO_ERROR         = 0
    XCAM_RETURN_BYPASS           = 1

    XCAM_RETURN_ERROR_FAILED     = -1
    XCAM_RETURN_ERROR_PARAM      = -2
    XCAM_RETURN_ERROR_MEM        = -3
    XCAM_RETURN_ERROR_FILE       = -4
    XCAM_RETURN_ERROR_ANALYZER   = -5
    XCAM_RETURN_ERROR_ISP        = -6
    XCAM_RETURN_ERROR_SENSOR     = -7
    XCAM_RETURN_ERROR_THREAD     = -8
    XCAM_RETURN_ERROR_IOCTL      = -9
    XCAM_RETURN_ERROR_ORDER      = -10
    XCAM_RETURN_ERROR_TIMEOUT    = -20
    XCAM_RETURN_ERROR_OUTOFRANGE = -21
    XCAM_RETURN_ERROR_UNKNOWN    = -255

class XCamReturn(c_int):
    pass


class RkAiqAlgoTypeEnum(IntEnum):
    RK_AIQ_ALGO_TYPE_NONE = -1
    RK_AIQ_ALGO_TYPE_AE = 0
    RK_AIQ_ALGO_TYPE_AWB = 1
    RK_AIQ_ALGO_TYPE_AF = 2
    RK_AIQ_ALGO_TYPE_ABLC = 3
    RK_AIQ_ALGO_TYPE_ADPCC = 4
    RK_AIQ_ALGO_TYPE_AMERGE = 5
    RK_AIQ_ALGO_TYPE_ATMO = 6
    RK_AIQ_ALGO_TYPE_ANR = 7
    RK_AIQ_ALGO_TYPE_ALSC = 8
    RK_AIQ_ALGO_TYPE_AGIC = 9
    RK_AIQ_ALGO_TYPE_ADEBAYER = 10
    RK_AIQ_ALGO_TYPE_ACCM = 11
    RK_AIQ_ALGO_TYPE_AGAMMA = 12
    RK_AIQ_ALGO_TYPE_AWDR = 13
    RK_AIQ_ALGO_TYPE_ADHAZ = 14
    RK_AIQ_ALGO_TYPE_A3DLUT = 15
    RK_AIQ_ALGO_TYPE_ALDCH = 16
    RK_AIQ_ALGO_TYPE_ACSM = 17
    RK_AIQ_ALGO_TYPE_ACP = 18
    RK_AIQ_ALGO_TYPE_AIE = 19
    RK_AIQ_ALGO_TYPE_ASHARP = 20
    RK_AIQ_ALGO_TYPE_AORB = 21
    RK_AIQ_ALGO_TYPE_ACGC = 22
    RK_AIQ_ALGO_TYPE_ASD = 23
    RK_AIQ_ALGO_TYPE_ADRC = 24
    RK_AIQ_ALGO_TYPE_ADEGAMMA = 25

    RK_AIQ_ALGO_TYPE_ARAWNR = 26
    RK_AIQ_ALGO_TYPE_AMFNR = 27
    RK_AIQ_ALGO_TYPE_AYNR = 28
    RK_AIQ_ALGO_TYPE_ACNR = 29
    RK_AIQ_ALGO_TYPE_AEIS = 30
    RK_AIQ_ALGO_TYPE_AFEC = 31
    RK_AIQ_ALGO_TYPE_AMD = 32
    RK_AIQ_ALGO_TYPE_AGAIN = 33
    RK_AIQ_ALGO_TYPE_ACAC = 34
    RK_AIQ_ALGO_TYPE_MAX = 35


class RkAiqAlgoType_t(c_int):
    pass


class rk_aiq_working_mode(IntEnum):
    RK_AIQ_WORKING_MODE_NORMAL = 0
    RK_AIQ_WORKING_MODE_ISP_HDR2 = 0x10
    RK_AIQ_WORKING_MODE_ISP_HDR3 = 0x20
    # TODO: is it really working?
    # RK_AIQ_WORKING_MODE_SENSOR_HDR = 10, // sensor built-in hdr mode


class rk_aiq_working_mode_t(c_int):
    pass
