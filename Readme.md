# Introduction

This project is an attempt to create python bindings for Rockchip's
AIQ toolset (including rkisp UAPI calls).

# Support

Rockchip has multiple isp revision, each of them incompatible with previous version.
Code was verified against ISP30, but pull requests agains other SOC are welcome.

| SOC    | ISP   | Support |
|--------|-------|---------|
| RK356x | ISP21 | ☐       |
| RK3588 | ISP30 | ☑       |
| RV1106 | ISP32 | ☐       |

# How this works

Rockchip provides [UAPI](https://gitlab.com/rk3588_linux/linux/external/camera_engine_rkaiq) for 
the rkaiq library, including 3A algorithms controls. Default system configuration includes
[rkaiq_3A_server](https://gitlab.com/rk3588_linux/linux/external/camera_engine_rkaiq/-/blob/linux-5.10/rkaiq_3A_server/rkaiq_3A_server.cpp) 
running in background and watching sensors and loading iq configuration for the sensor.
There are also a lot of other features listed in 
[rkisp_demo](https://gitlab.com/rk3588_linux/linux/external/camera_engine_rkaiq/-/blob/linux-5.10/tests/rkisp_demo/demo/rkisp_demo.cpp?ref_type=heads#L154),
but that demo is mostly not updated to the latest ISP version.

Project contains two parts: 
- raw ctypes bindings to the libaiq.so
- human-friendly python-stylish layer which wraps raw bindings making them less painful to use.


# Examples
TODO: write list of examples