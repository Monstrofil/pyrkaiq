r"""Wrapper for rk_aiq_user_api2_a3dlut.h

Generated with:
/usr/local/bin/ctypesgen -I /root/camera_engine_rkaiq/include/xcore/ -I /root/camera_engine_rkaiq/include/xcore/base/ -I /root/camera_engine_rkaiq/include/aiq_core/ -I /root/camera_engine_rkaiq/include/algos/ -I /root/camera_engine_rkaiq/include/common/ -I /root/camera_engine_rkaiq/include/iq_parser/ -I /root/camera_engine_rkaiq/include/iq_parser2/ -I /root/camera_engine_rkaiq/include/uAPI/ -I /root/camera_engine_rkaiq/include/uAPI2/ -I /root/camera_engine_rkaiq/ -I /root/camera_engine_rkaiq/uAPI/ -I /root/camera_engine_rkaiq/uAPI/include/ -I /root/camera_engine_rkaiq/include/ -I /root/camera_engine_rkaiq/include/iq_parser_v2/ -lrkaiq ../camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_a3dlut.h ../camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_abayer2dnr_v2.h ../camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_abayernr_v2.h ../camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_abayertnr_v2.h ../camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_ablc.h ../camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_accm.h ../camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_acgc.h ../camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_acnr_v1.h ../camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_acnr_v2.h ../camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_acp.h ../camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_acsm.h ../camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_adebayer.h ../camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_adegamma.h ../camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_adehaze.h ../camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_adpcc.h ../camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_adrc.h ../camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_ae.h ../camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_afec.h ../camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_af.h ../camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_again_v2.h ../camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_agamma.h ../camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_agic.h ../camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_aie.h ../camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_aldch.h ../camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_alsc.h ../camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_amerge.h ../camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_anr.h ../camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_asharp_v3.h ../camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_asharp_v4.h ../camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_atmo.h ../camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_awb.h ../camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_aynr_v2.h ../camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_aynr_v3.h ../camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_camgroup.h ../camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_custom_ae.h ../camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_custom_awb.h ../camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_debug.h ../camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_helper.h ../camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h ../camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_sysctl.h ../camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_wrapper.h -o libaiq_3_0_9_1.py

Do not modify this file.
"""

__docformat__ = "restructuredtext"

# Begin preamble for Python

import ctypes
import sys
from ctypes import *  # noqa: F401, F403

_int_types = (ctypes.c_int16, ctypes.c_int32)
if hasattr(ctypes, "c_int64"):
    # Some builds of ctypes apparently do not have ctypes.c_int64
    # defined; it's a pretty good bet that these builds do not
    # have 64-bit pointers.
    _int_types += (ctypes.c_int64,)
for t in _int_types:
    if ctypes.sizeof(t) == ctypes.sizeof(ctypes.c_size_t):
        c_ptrdiff_t = t
del t
del _int_types



class UserString:
    def __init__(self, seq):
        if isinstance(seq, bytes):
            self.data = seq
        elif isinstance(seq, UserString):
            self.data = seq.data[:]
        else:
            self.data = str(seq).encode()

    def __bytes__(self):
        return self.data

    def __str__(self):
        return self.data.decode()

    def __repr__(self):
        return repr(self.data)

    def __int__(self):
        return int(self.data.decode())

    def __long__(self):
        return int(self.data.decode())

    def __float__(self):
        return float(self.data.decode())

    def __complex__(self):
        return complex(self.data.decode())

    def __hash__(self):
        return hash(self.data)

    def __le__(self, string):
        if isinstance(string, UserString):
            return self.data <= string.data
        else:
            return self.data <= string

    def __lt__(self, string):
        if isinstance(string, UserString):
            return self.data < string.data
        else:
            return self.data < string

    def __ge__(self, string):
        if isinstance(string, UserString):
            return self.data >= string.data
        else:
            return self.data >= string

    def __gt__(self, string):
        if isinstance(string, UserString):
            return self.data > string.data
        else:
            return self.data > string

    def __eq__(self, string):
        if isinstance(string, UserString):
            return self.data == string.data
        else:
            return self.data == string

    def __ne__(self, string):
        if isinstance(string, UserString):
            return self.data != string.data
        else:
            return self.data != string

    def __contains__(self, char):
        return char in self.data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.__class__(self.data[index])

    def __getslice__(self, start, end):
        start = max(start, 0)
        end = max(end, 0)
        return self.__class__(self.data[start:end])

    def __add__(self, other):
        if isinstance(other, UserString):
            return self.__class__(self.data + other.data)
        elif isinstance(other, bytes):
            return self.__class__(self.data + other)
        else:
            return self.__class__(self.data + str(other).encode())

    def __radd__(self, other):
        if isinstance(other, bytes):
            return self.__class__(other + self.data)
        else:
            return self.__class__(str(other).encode() + self.data)

    def __mul__(self, n):
        return self.__class__(self.data * n)

    __rmul__ = __mul__

    def __mod__(self, args):
        return self.__class__(self.data % args)

    # the following methods are defined in alphabetical order:
    def capitalize(self):
        return self.__class__(self.data.capitalize())

    def center(self, width, *args):
        return self.__class__(self.data.center(width, *args))

    def count(self, sub, start=0, end=sys.maxsize):
        return self.data.count(sub, start, end)

    def decode(self, encoding=None, errors=None):  # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.decode(encoding, errors))
            else:
                return self.__class__(self.data.decode(encoding))
        else:
            return self.__class__(self.data.decode())

    def encode(self, encoding=None, errors=None):  # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.encode(encoding, errors))
            else:
                return self.__class__(self.data.encode(encoding))
        else:
            return self.__class__(self.data.encode())

    def endswith(self, suffix, start=0, end=sys.maxsize):
        return self.data.endswith(suffix, start, end)

    def expandtabs(self, tabsize=8):
        return self.__class__(self.data.expandtabs(tabsize))

    def find(self, sub, start=0, end=sys.maxsize):
        return self.data.find(sub, start, end)

    def index(self, sub, start=0, end=sys.maxsize):
        return self.data.index(sub, start, end)

    def isalpha(self):
        return self.data.isalpha()

    def isalnum(self):
        return self.data.isalnum()

    def isdecimal(self):
        return self.data.isdecimal()

    def isdigit(self):
        return self.data.isdigit()

    def islower(self):
        return self.data.islower()

    def isnumeric(self):
        return self.data.isnumeric()

    def isspace(self):
        return self.data.isspace()

    def istitle(self):
        return self.data.istitle()

    def isupper(self):
        return self.data.isupper()

    def join(self, seq):
        return self.data.join(seq)

    def ljust(self, width, *args):
        return self.__class__(self.data.ljust(width, *args))

    def lower(self):
        return self.__class__(self.data.lower())

    def lstrip(self, chars=None):
        return self.__class__(self.data.lstrip(chars))

    def partition(self, sep):
        return self.data.partition(sep)

    def replace(self, old, new, maxsplit=-1):
        return self.__class__(self.data.replace(old, new, maxsplit))

    def rfind(self, sub, start=0, end=sys.maxsize):
        return self.data.rfind(sub, start, end)

    def rindex(self, sub, start=0, end=sys.maxsize):
        return self.data.rindex(sub, start, end)

    def rjust(self, width, *args):
        return self.__class__(self.data.rjust(width, *args))

    def rpartition(self, sep):
        return self.data.rpartition(sep)

    def rstrip(self, chars=None):
        return self.__class__(self.data.rstrip(chars))

    def split(self, sep=None, maxsplit=-1):
        return self.data.split(sep, maxsplit)

    def rsplit(self, sep=None, maxsplit=-1):
        return self.data.rsplit(sep, maxsplit)

    def splitlines(self, keepends=0):
        return self.data.splitlines(keepends)

    def startswith(self, prefix, start=0, end=sys.maxsize):
        return self.data.startswith(prefix, start, end)

    def strip(self, chars=None):
        return self.__class__(self.data.strip(chars))

    def swapcase(self):
        return self.__class__(self.data.swapcase())

    def title(self):
        return self.__class__(self.data.title())

    def translate(self, *args):
        return self.__class__(self.data.translate(*args))

    def upper(self):
        return self.__class__(self.data.upper())

    def zfill(self, width):
        return self.__class__(self.data.zfill(width))


class MutableString(UserString):
    """mutable string objects

    Python strings are immutable objects.  This has the advantage, that
    strings may be used as dictionary keys.  If this property isn't needed
    and you insist on changing string values in place instead, you may cheat
    and use MutableString.

    But the purpose of this class is an educational one: to prevent
    people from inventing their own mutable string class derived
    from UserString and than forget thereby to remove (override) the
    __hash__ method inherited from UserString.  This would lead to
    errors that would be very hard to track down.

    A faster and better solution is to rewrite your program using lists."""

    def __init__(self, string=""):
        self.data = string

    def __hash__(self):
        raise TypeError("unhashable type (it is mutable)")

    def __setitem__(self, index, sub):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data):
            raise IndexError
        self.data = self.data[:index] + sub + self.data[index + 1 :]

    def __delitem__(self, index):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data):
            raise IndexError
        self.data = self.data[:index] + self.data[index + 1 :]

    def __setslice__(self, start, end, sub):
        start = max(start, 0)
        end = max(end, 0)
        if isinstance(sub, UserString):
            self.data = self.data[:start] + sub.data + self.data[end:]
        elif isinstance(sub, bytes):
            self.data = self.data[:start] + sub + self.data[end:]
        else:
            self.data = self.data[:start] + str(sub).encode() + self.data[end:]

    def __delslice__(self, start, end):
        start = max(start, 0)
        end = max(end, 0)
        self.data = self.data[:start] + self.data[end:]

    def immutable(self):
        return UserString(self.data)

    def __iadd__(self, other):
        if isinstance(other, UserString):
            self.data += other.data
        elif isinstance(other, bytes):
            self.data += other
        else:
            self.data += str(other).encode()
        return self

    def __imul__(self, n):
        self.data *= n
        return self


class String(MutableString, ctypes.Union):

    _fields_ = [("raw", ctypes.POINTER(ctypes.c_char)), ("data", ctypes.c_char_p)]

    def __init__(self, obj=b""):
        if isinstance(obj, (bytes, UserString)):
            self.data = bytes(obj)
        else:
            self.raw = obj

    def __len__(self):
        return self.data and len(self.data) or 0

    def from_param(cls, obj):
        # Convert None or 0
        if obj is None or obj == 0:
            return cls(ctypes.POINTER(ctypes.c_char)())

        # Convert from String
        elif isinstance(obj, String):
            return obj

        # Convert from bytes
        elif isinstance(obj, bytes):
            return cls(obj)

        # Convert from str
        elif isinstance(obj, str):
            return cls(obj.encode())

        # Convert from c_char_p
        elif isinstance(obj, ctypes.c_char_p):
            return obj

        # Convert from POINTER(ctypes.c_char)
        elif isinstance(obj, ctypes.POINTER(ctypes.c_char)):
            return obj

        # Convert from raw pointer
        elif isinstance(obj, int):
            return cls(ctypes.cast(obj, ctypes.POINTER(ctypes.c_char)))

        # Convert from ctypes.c_char array
        elif isinstance(obj, ctypes.c_char * len(obj)):
            return obj

        # Convert from object
        else:
            return String.from_param(obj._as_parameter_)

    from_param = classmethod(from_param)


def ReturnString(obj, func=None, arguments=None):
    return String.from_param(obj)


# As of ctypes 1.0, ctypes does not support custom error-checking
# functions on callbacks, nor does it support custom datatypes on
# callbacks, so we must ensure that all callbacks return
# primitive datatypes.
#
# Non-primitive return values wrapped with UNCHECKED won't be
# typechecked, and will be converted to ctypes.c_void_p.
def UNCHECKED(type):
    if hasattr(type, "_type_") and isinstance(type._type_, str) and type._type_ != "P":
        return type
    else:
        return ctypes.c_void_p


# ctypes doesn't have direct support for variadic functions, so we have to write
# our own wrapper class
class _variadic_function(object):
    def __init__(self, func, restype, argtypes, errcheck):
        self.func = func
        self.func.restype = restype
        self.argtypes = argtypes
        if errcheck:
            self.func.errcheck = errcheck

    def _as_parameter_(self):
        # So we can pass this variadic function as a function pointer
        return self.func

    def __call__(self, *args):
        fixed_args = []
        i = 0
        for argtype in self.argtypes:
            # Typecheck what we can
            fixed_args.append(argtype.from_param(args[i]))
            i += 1
        return self.func(*fixed_args + list(args[i:]))


def ord_if_char(value):
    """
    Simple helper used for casts to simple builtin types:  if the argument is a
    string type, it will be converted to it's ordinal value.

    This function will raise an exception if the argument is string with more
    than one characters.
    """
    return ord(value) if (isinstance(value, bytes) or isinstance(value, str)) else value

# End preamble

_libs = {}
_libdirs = []

# Begin loader

"""
Load libraries - appropriately for all our supported platforms
"""
# ----------------------------------------------------------------------------
# Copyright (c) 2008 David James
# Copyright (c) 2006-2008 Alex Holkner
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------

import ctypes
import ctypes.util
import glob
import os.path
import platform
import re
import sys


def _environ_path(name):
    """Split an environment variable into a path-like list elements"""
    if name in os.environ:
        return os.environ[name].split(":")
    return []


class LibraryLoader:
    """
    A base class For loading of libraries ;-)
    Subclasses load libraries for specific platforms.
    """

    # library names formatted specifically for platforms
    name_formats = ["%s"]

    class Lookup:
        """Looking up calling conventions for a platform"""

        mode = ctypes.DEFAULT_MODE

        def __init__(self, path):
            super(LibraryLoader.Lookup, self).__init__()
            self.access = dict(cdecl=ctypes.CDLL(path, self.mode))

        def get(self, name, calling_convention="cdecl"):
            """Return the given name according to the selected calling convention"""
            if calling_convention not in self.access:
                raise LookupError(
                    "Unknown calling convention '{}' for function '{}'".format(
                        calling_convention, name
                    )
                )
            return getattr(self.access[calling_convention], name)

        def has(self, name, calling_convention="cdecl"):
            """Return True if this given calling convention finds the given 'name'"""
            if calling_convention not in self.access:
                return False
            return hasattr(self.access[calling_convention], name)

        def __getattr__(self, name):
            return getattr(self.access["cdecl"], name)

    def __init__(self):
        self.other_dirs = []

    def __call__(self, libname):
        """Given the name of a library, load it."""
        paths = self.getpaths(libname)

        for path in paths:
            # noinspection PyBroadException
            try:
                return self.Lookup(path)
            except Exception:  # pylint: disable=broad-except
                pass

        raise ImportError("Could not load %s." % libname)

    def getpaths(self, libname):
        """Return a list of paths where the library might be found."""
        if os.path.isabs(libname):
            yield libname
        else:
            # search through a prioritized series of locations for the library

            # we first search any specific directories identified by user
            for dir_i in self.other_dirs:
                for fmt in self.name_formats:
                    # dir_i should be absolute already
                    yield os.path.join(dir_i, fmt % libname)

            # check if this code is even stored in a physical file
            try:
                this_file = __file__
            except NameError:
                this_file = None

            # then we search the directory where the generated python interface is stored
            if this_file is not None:
                for fmt in self.name_formats:
                    yield os.path.abspath(os.path.join(os.path.dirname(__file__), fmt % libname))

            # now, use the ctypes tools to try to find the library
            for fmt in self.name_formats:
                path = ctypes.util.find_library(fmt % libname)
                if path:
                    yield path

            # then we search all paths identified as platform-specific lib paths
            for path in self.getplatformpaths(libname):
                yield path

            # Finally, we'll try the users current working directory
            for fmt in self.name_formats:
                yield os.path.abspath(os.path.join(os.path.curdir, fmt % libname))

    def getplatformpaths(self, _libname):  # pylint: disable=no-self-use
        """Return all the library paths available in this platform"""
        return []


# Darwin (Mac OS X)


class DarwinLibraryLoader(LibraryLoader):
    """Library loader for MacOS"""

    name_formats = [
        "lib%s.dylib",
        "lib%s.so",
        "lib%s.bundle",
        "%s.dylib",
        "%s.so",
        "%s.bundle",
        "%s",
    ]

    class Lookup(LibraryLoader.Lookup):
        """
        Looking up library files for this platform (Darwin aka MacOS)
        """

        # Darwin requires dlopen to be called with mode RTLD_GLOBAL instead
        # of the default RTLD_LOCAL.  Without this, you end up with
        # libraries not being loadable, resulting in "Symbol not found"
        # errors
        mode = ctypes.RTLD_GLOBAL

    def getplatformpaths(self, libname):
        if os.path.pathsep in libname:
            names = [libname]
        else:
            names = [fmt % libname for fmt in self.name_formats]

        for directory in self.getdirs(libname):
            for name in names:
                yield os.path.join(directory, name)

    @staticmethod
    def getdirs(libname):
        """Implements the dylib search as specified in Apple documentation:

        http://developer.apple.com/documentation/DeveloperTools/Conceptual/
            DynamicLibraries/Articles/DynamicLibraryUsageGuidelines.html

        Before commencing the standard search, the method first checks
        the bundle's ``Frameworks`` directory if the application is running
        within a bundle (OS X .app).
        """

        dyld_fallback_library_path = _environ_path("DYLD_FALLBACK_LIBRARY_PATH")
        if not dyld_fallback_library_path:
            dyld_fallback_library_path = [
                os.path.expanduser("~/lib"),
                "/usr/local/lib",
                "/usr/lib",
            ]

        dirs = []

        if "/" in libname:
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
        else:
            dirs.extend(_environ_path("LD_LIBRARY_PATH"))
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
            dirs.extend(_environ_path("LD_RUN_PATH"))

        if hasattr(sys, "frozen") and getattr(sys, "frozen") == "macosx_app":
            dirs.append(os.path.join(os.environ["RESOURCEPATH"], "../../..", "Frameworks"))

        dirs.extend(dyld_fallback_library_path)

        return dirs


# Posix


class PosixLibraryLoader(LibraryLoader):
    """Library loader for POSIX-like systems (including Linux)"""

    _ld_so_cache = None

    _include = re.compile(r"^\s*include\s+(?P<pattern>.*)")

    name_formats = ["lib%s.so", "%s.so", "%s"]

    class _Directories(dict):
        """Deal with directories"""

        def __init__(self):
            dict.__init__(self)
            self.order = 0

        def add(self, directory):
            """Add a directory to our current set of directories"""
            if len(directory) > 1:
                directory = directory.rstrip(os.path.sep)
            # only adds and updates order if exists and not already in set
            if not os.path.exists(directory):
                return
            order = self.setdefault(directory, self.order)
            if order == self.order:
                self.order += 1

        def extend(self, directories):
            """Add a list of directories to our set"""
            for a_dir in directories:
                self.add(a_dir)

        def ordered(self):
            """Sort the list of directories"""
            return (i[0] for i in sorted(self.items(), key=lambda d: d[1]))

    def _get_ld_so_conf_dirs(self, conf, dirs):
        """
        Recursive function to help parse all ld.so.conf files, including proper
        handling of the `include` directive.
        """

        try:
            with open(conf) as fileobj:
                for dirname in fileobj:
                    dirname = dirname.strip()
                    if not dirname:
                        continue

                    match = self._include.match(dirname)
                    if not match:
                        dirs.add(dirname)
                    else:
                        for dir2 in glob.glob(match.group("pattern")):
                            self._get_ld_so_conf_dirs(dir2, dirs)
        except IOError:
            pass

    def _create_ld_so_cache(self):
        # Recreate search path followed by ld.so.  This is going to be
        # slow to build, and incorrect (ld.so uses ld.so.cache, which may
        # not be up-to-date).  Used only as fallback for distros without
        # /sbin/ldconfig.
        #
        # We assume the DT_RPATH and DT_RUNPATH binary sections are omitted.

        directories = self._Directories()
        for name in (
            "LD_LIBRARY_PATH",
            "SHLIB_PATH",  # HP-UX
            "LIBPATH",  # OS/2, AIX
            "LIBRARY_PATH",  # BE/OS
        ):
            if name in os.environ:
                directories.extend(os.environ[name].split(os.pathsep))

        self._get_ld_so_conf_dirs("/etc/ld.so.conf", directories)

        bitage = platform.architecture()[0]

        unix_lib_dirs_list = []
        if bitage.startswith("64"):
            # prefer 64 bit if that is our arch
            unix_lib_dirs_list += ["/lib64", "/usr/lib64"]

        # must include standard libs, since those paths are also used by 64 bit
        # installs
        unix_lib_dirs_list += ["/lib", "/usr/lib"]
        if sys.platform.startswith("linux"):
            # Try and support multiarch work in Ubuntu
            # https://wiki.ubuntu.com/MultiarchSpec
            if bitage.startswith("32"):
                # Assume Intel/AMD x86 compat
                unix_lib_dirs_list += ["/lib/i386-linux-gnu", "/usr/lib/i386-linux-gnu"]
            elif bitage.startswith("64"):
                # Assume Intel/AMD x86 compatible
                unix_lib_dirs_list += [
                    "/lib/x86_64-linux-gnu",
                    "/usr/lib/x86_64-linux-gnu",
                ]
            else:
                # guess...
                unix_lib_dirs_list += glob.glob("/lib/*linux-gnu")
        directories.extend(unix_lib_dirs_list)

        cache = {}
        lib_re = re.compile(r"lib(.*)\.s[ol]")
        # ext_re = re.compile(r"\.s[ol]$")
        for our_dir in directories.ordered():
            try:
                for path in glob.glob("%s/*.s[ol]*" % our_dir):
                    file = os.path.basename(path)

                    # Index by filename
                    cache_i = cache.setdefault(file, set())
                    cache_i.add(path)

                    # Index by library name
                    match = lib_re.match(file)
                    if match:
                        library = match.group(1)
                        cache_i = cache.setdefault(library, set())
                        cache_i.add(path)
            except OSError:
                pass

        self._ld_so_cache = cache

    def getplatformpaths(self, libname):
        if self._ld_so_cache is None:
            self._create_ld_so_cache()

        result = self._ld_so_cache.get(libname, set())
        for i in result:
            # we iterate through all found paths for library, since we may have
            # actually found multiple architectures or other library types that
            # may not load
            yield i


# Windows


class WindowsLibraryLoader(LibraryLoader):
    """Library loader for Microsoft Windows"""

    name_formats = ["%s.dll", "lib%s.dll", "%slib.dll", "%s"]

    class Lookup(LibraryLoader.Lookup):
        """Lookup class for Windows libraries..."""

        def __init__(self, path):
            super(WindowsLibraryLoader.Lookup, self).__init__(path)
            self.access["stdcall"] = ctypes.windll.LoadLibrary(path)


# Platform switching

# If your value of sys.platform does not appear in this dict, please contact
# the Ctypesgen maintainers.

loaderclass = {
    "darwin": DarwinLibraryLoader,
    "cygwin": WindowsLibraryLoader,
    "win32": WindowsLibraryLoader,
    "msys": WindowsLibraryLoader,
}

load_library = loaderclass.get(sys.platform, PosixLibraryLoader)()


def add_library_search_dirs(other_dirs):
    """
    Add libraries to search paths.
    If library paths are relative, convert them to absolute with respect to this
    file's directory
    """
    for path in other_dirs:
        if not os.path.isabs(path):
            path = os.path.abspath(path)
        load_library.other_dirs.append(path)


del loaderclass

# End loader

add_library_search_dirs([])

# Begin libraries
_libs["rkaiq"] = load_library("rkaiq")

# 1 libraries
# End libraries

# No modules

__uint8_t = c_ubyte# /usr/include/aarch64-linux-gnu/bits/types.h: 38

__uint16_t = c_ushort# /usr/include/aarch64-linux-gnu/bits/types.h: 40

__uint32_t = c_uint# /usr/include/aarch64-linux-gnu/bits/types.h: 42

__uint64_t = c_ulong# /usr/include/aarch64-linux-gnu/bits/types.h: 45

__time_t = c_long# /usr/include/aarch64-linux-gnu/bits/types.h: 160

__suseconds_t = c_long# /usr/include/aarch64-linux-gnu/bits/types.h: 162

uint8_t = __uint8_t# /usr/include/aarch64-linux-gnu/bits/stdint-uintn.h: 24

uint16_t = __uint16_t# /usr/include/aarch64-linux-gnu/bits/stdint-uintn.h: 25

uint32_t = __uint32_t# /usr/include/aarch64-linux-gnu/bits/stdint-uintn.h: 26

uint64_t = __uint64_t# /usr/include/aarch64-linux-gnu/bits/stdint-uintn.h: 27

# /usr/include/aarch64-linux-gnu/bits/types/struct_timeval.h: 8
class struct_timeval(Structure):
    pass

struct_timeval.__slots__ = [
    'tv_sec',
    'tv_usec',
]
struct_timeval._fields_ = [
    ('tv_sec', __time_t),
    ('tv_usec', __suseconds_t),
]

enum_anon_40 = c_int# /root/camera_engine_rkaiq/include/xcore/base/xcam_common.h: 59

XCamReturn = enum_anon_40# /root/camera_engine_rkaiq/include/xcore/base/xcam_common.h: 59

enum_RKAiqOPMode_e = c_int# /root/camera_engine_rkaiq/include/common/rk_aiq_comm.h: 69

RK_AIQ_OP_MODE_MANUAL = 2# /root/camera_engine_rkaiq/include/common/rk_aiq_comm.h: 69

RK_AIQ_OP_MODE_MAX = (RK_AIQ_OP_MODE_MANUAL + 1)# /root/camera_engine_rkaiq/include/common/rk_aiq_comm.h: 69

RKAiqOPMode_t = enum_RKAiqOPMode_e# /root/camera_engine_rkaiq/include/common/rk_aiq_comm.h: 69

sint32_t = c_int# /root/camera_engine_rkaiq/include/common/rk_aiq_comm.h: 104

# /root/camera_engine_rkaiq/include/common/rk_aiq_comm.h: 130
class struct_Cam15x15UCharMatrix_s(Structure):
    pass

struct_Cam15x15UCharMatrix_s.__slots__ = [
    'uCoeff',
]
struct_Cam15x15UCharMatrix_s._fields_ = [
    ('uCoeff', uint8_t * int((15 * 15))),
]

Cam15x15UCharMatrix_t = struct_Cam15x15UCharMatrix_s# /root/camera_engine_rkaiq/include/common/rk_aiq_comm.h: 130

# /root/camera_engine_rkaiq/include/common/rk_aiq_comm.h: 432
class struct_Cam17x17UShortMatrix_s(Structure):
    pass

struct_Cam17x17UShortMatrix_s.__slots__ = [
    'uCoeff',
]
struct_Cam17x17UShortMatrix_s._fields_ = [
    ('uCoeff', uint16_t * int((17 * 17))),
]

Cam17x17UShortMatrix_t = struct_Cam17x17UShortMatrix_s# /root/camera_engine_rkaiq/include/common/rk_aiq_comm.h: 432

enum_anon_42 = c_int# /root/camera_engine_rkaiq/include/common/rk_aiq_comm.h: 439

rk_aiq_working_mode_t = enum_anon_42# /root/camera_engine_rkaiq/include/common/rk_aiq_comm.h: 439

enum_anon_47 = c_int# /root/camera_engine_rkaiq/include/common/rk_aiq_comm.h: 484

rk_aiq_module_id_t = enum_anon_47# /root/camera_engine_rkaiq/include/common/rk_aiq_comm.h: 484

enum_anon_49 = c_int# /root/camera_engine_rkaiq/include/common/rk_aiq_comm.h: 499

rk_aiq_uapi_mode_sync_e = enum_anon_49# /root/camera_engine_rkaiq/include/common/rk_aiq_comm.h: 499

# /root/camera_engine_rkaiq/include/common/rk_aiq_comm.h: 521
class struct_rk_aiq_uapi_sync_s(Structure):
    pass

struct_rk_aiq_uapi_sync_s.__slots__ = [
    'sync_mode',
    'done',
]
struct_rk_aiq_uapi_sync_s._fields_ = [
    ('sync_mode', rk_aiq_uapi_mode_sync_e),
    ('done', c_bool),
]

rk_aiq_uapi_sync_t = struct_rk_aiq_uapi_sync_s# /root/camera_engine_rkaiq/include/common/rk_aiq_comm.h: 521

# /root/camera_engine_rkaiq/include/algos/rk_aiq_algo_des.h: 55
class struct__RkAiqAlgoContext(Structure):
    pass

RkAiqAlgoContext = struct__RkAiqAlgoContext# /root/camera_engine_rkaiq/include/algos/rk_aiq_algo_des.h: 55

# /root/camera_engine_rkaiq/include/algos/rk_aiq_algo_des.h: 58
class struct_RKAiqAecExpInfo_s(Structure):
    pass

RKAiqAecExpInfo_t = struct_RKAiqAecExpInfo_s# /root/camera_engine_rkaiq/include/algos/rk_aiq_algo_des.h: 58

# /root/camera_engine_rkaiq/include/algos/a3dlut/rk_aiq_types_a3dlut_algo.h: 33
class struct_rk_aiq_lut3d_table_s(Structure):
    pass

struct_rk_aiq_lut3d_table_s.__slots__ = [
    'look_up_table_r',
    'look_up_table_g',
    'look_up_table_b',
]
struct_rk_aiq_lut3d_table_s._fields_ = [
    ('look_up_table_r', c_ushort * int(729)),
    ('look_up_table_g', c_ushort * int(729)),
    ('look_up_table_b', c_ushort * int(729)),
]

rk_aiq_lut3d_table_t = struct_rk_aiq_lut3d_table_s# /root/camera_engine_rkaiq/include/algos/a3dlut/rk_aiq_types_a3dlut_algo.h: 33

# /root/camera_engine_rkaiq/include/algos/a3dlut/rk_aiq_types_a3dlut_ext.h: 33
class struct_rk_aiq_lut3d_mlut3d_attrib_s(Structure):
    pass

struct_rk_aiq_lut3d_mlut3d_attrib_s.__slots__ = [
    'look_up_table_r',
    'look_up_table_g',
    'look_up_table_b',
]
struct_rk_aiq_lut3d_mlut3d_attrib_s._fields_ = [
    ('look_up_table_r', c_ushort * int(729)),
    ('look_up_table_g', c_ushort * int(729)),
    ('look_up_table_b', c_ushort * int(729)),
]

rk_aiq_lut3d_mlut3d_attrib_t = struct_rk_aiq_lut3d_mlut3d_attrib_s# /root/camera_engine_rkaiq/include/algos/a3dlut/rk_aiq_types_a3dlut_ext.h: 33

enum_rk_aiq_lut3d_op_mode_s = c_int# /root/camera_engine_rkaiq/include/algos/a3dlut/rk_aiq_types_a3dlut_ext.h: 40

rk_aiq_lut3d_op_mode_t = enum_rk_aiq_lut3d_op_mode_s# /root/camera_engine_rkaiq/include/algos/a3dlut/rk_aiq_types_a3dlut_ext.h: 40

# /root/camera_engine_rkaiq/include/algos/a3dlut/rk_aiq_types_a3dlut_ext.h: 50
class struct_rk_aiq_lut3d_attrib_s(Structure):
    pass

struct_rk_aiq_lut3d_attrib_s.__slots__ = [
    'sync',
    'byPass',
    'mode',
    'stManual',
]
struct_rk_aiq_lut3d_attrib_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('byPass', c_bool),
    ('mode', rk_aiq_lut3d_op_mode_t),
    ('stManual', rk_aiq_lut3d_mlut3d_attrib_t),
]

rk_aiq_lut3d_attrib_t = struct_rk_aiq_lut3d_attrib_s# /root/camera_engine_rkaiq/include/algos/a3dlut/rk_aiq_types_a3dlut_ext.h: 50

# /root/camera_engine_rkaiq/include/algos/a3dlut/rk_aiq_types_a3dlut_ext.h: 64
class struct_rk_aiq_lut3d_querry_info_s(Structure):
    pass

struct_rk_aiq_lut3d_querry_info_s.__slots__ = [
    'lut3d_en',
    'alpha',
    'name',
    'look_up_table_r',
    'look_up_table_g',
    'look_up_table_b',
]
struct_rk_aiq_lut3d_querry_info_s._fields_ = [
    ('lut3d_en', c_bool),
    ('alpha', c_float),
    ('name', c_char * int(25)),
    ('look_up_table_r', c_ushort * int(729)),
    ('look_up_table_g', c_ushort * int(729)),
    ('look_up_table_b', c_ushort * int(729)),
]

rk_aiq_lut3d_querry_info_t = struct_rk_aiq_lut3d_querry_info_s# /root/camera_engine_rkaiq/include/algos/a3dlut/rk_aiq_types_a3dlut_ext.h: 64

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_a3dlut.h: 24
class struct_rk_aiq_sys_ctx_s(Structure):
    pass

rk_aiq_sys_ctx_t = struct_rk_aiq_sys_ctx_s# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_a3dlut.h: 24

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_a3dlut.h: 31
if _libs["rkaiq"].has("rk_aiq_user_api2_a3dlut_SetAttrib", "cdecl"):
    rk_aiq_user_api2_a3dlut_SetAttrib = _libs["rkaiq"].get("rk_aiq_user_api2_a3dlut_SetAttrib", "cdecl")
    rk_aiq_user_api2_a3dlut_SetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), rk_aiq_lut3d_attrib_t]
    rk_aiq_user_api2_a3dlut_SetAttrib.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_a3dlut.h: 33
if _libs["rkaiq"].has("rk_aiq_user_api2_a3dlut_GetAttrib", "cdecl"):
    rk_aiq_user_api2_a3dlut_GetAttrib = _libs["rkaiq"].get("rk_aiq_user_api2_a3dlut_GetAttrib", "cdecl")
    rk_aiq_user_api2_a3dlut_GetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_lut3d_attrib_t)]
    rk_aiq_user_api2_a3dlut_GetAttrib.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_a3dlut.h: 35
if _libs["rkaiq"].has("rk_aiq_user_api2_a3dlut_Query3dlutInfo", "cdecl"):
    rk_aiq_user_api2_a3dlut_Query3dlutInfo = _libs["rkaiq"].get("rk_aiq_user_api2_a3dlut_Query3dlutInfo", "cdecl")
    rk_aiq_user_api2_a3dlut_Query3dlutInfo.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_lut3d_querry_info_t)]
    rk_aiq_user_api2_a3dlut_Query3dlutInfo.restype = XCamReturn

enum_AdpccOPMode_e = c_int# /root/camera_engine_rkaiq/include/algos/adpcc/rk_aiq_types_adpcc_ext.h: 46

AdpccOPMode_t = enum_AdpccOPMode_e# /root/camera_engine_rkaiq/include/algos/adpcc/rk_aiq_types_adpcc_ext.h: 46

enum_Adpcc_onfly_mode_e = c_int# /root/camera_engine_rkaiq/include/algos/adpcc/rk_aiq_types_adpcc_ext.h: 52

Adpcc_onfly_mode_t = enum_Adpcc_onfly_mode_e# /root/camera_engine_rkaiq/include/algos/adpcc/rk_aiq_types_adpcc_ext.h: 52

# /root/camera_engine_rkaiq/include/algos/adpcc/rk_aiq_types_adpcc_ext.h: 60
class struct_CalibDb_Dpcc_Sensor_s(Structure):
    pass

struct_CalibDb_Dpcc_Sensor_s.__slots__ = [
    'en',
    'max_level',
    'iso',
    'level_single',
    'level_multiple',
]
struct_CalibDb_Dpcc_Sensor_s._fields_ = [
    ('en', c_float),
    ('max_level', c_float),
    ('iso', c_float * int(13)),
    ('level_single', c_float * int(13)),
    ('level_multiple', c_float * int(13)),
]

CalibDb_Dpcc_Sensor_t = struct_CalibDb_Dpcc_Sensor_s# /root/camera_engine_rkaiq/include/algos/adpcc/rk_aiq_types_adpcc_ext.h: 60

# /root/camera_engine_rkaiq/include/algos/adpcc/rk_aiq_types_adpcc_ext.h: 71
class struct_CalibDb_Dpcc_Fast_Mode_s(Structure):
    pass

struct_CalibDb_Dpcc_Fast_Mode_s.__slots__ = [
    'fast_mode_en',
    'ISO',
    'fast_mode_single_en',
    'fast_mode_single_level',
    'fast_mode_double_en',
    'fast_mode_double_level',
    'fast_mode_triple_en',
    'fast_mode_triple_level',
]
struct_CalibDb_Dpcc_Fast_Mode_s._fields_ = [
    ('fast_mode_en', c_int),
    ('ISO', c_int * int(13)),
    ('fast_mode_single_en', c_int),
    ('fast_mode_single_level', c_int * int(13)),
    ('fast_mode_double_en', c_int),
    ('fast_mode_double_level', c_int * int(13)),
    ('fast_mode_triple_en', c_int),
    ('fast_mode_triple_level', c_int * int(13)),
]

CalibDb_Dpcc_Fast_Mode_t = struct_CalibDb_Dpcc_Fast_Mode_s# /root/camera_engine_rkaiq/include/algos/adpcc/rk_aiq_types_adpcc_ext.h: 71

# /root/camera_engine_rkaiq/include/algos/adpcc/rk_aiq_types_adpcc_ext.h: 223
class struct_Adpcc_basic_params_select_s(Structure):
    pass

struct_Adpcc_basic_params_select_s.__slots__ = [
    'iso',
    'stage1_enable',
    'grayscale_mode',
    'enable',
    'sw_rk_out_sel',
    'sw_dpcc_output_sel',
    'stage1_rb_3x3',
    'stage1_g_3x3',
    'stage1_incl_rb_center',
    'stage1_incl_green_center',
    'stage1_use_fix_set',
    'stage1_use_set_3',
    'stage1_use_set_2',
    'stage1_use_set_1',
    'sw_rk_red_blue1_en',
    'rg_red_blue1_enable',
    'rnd_red_blue1_enable',
    'ro_red_blue1_enable',
    'lc_red_blue1_enable',
    'pg_red_blue1_enable',
    'sw_rk_green1_en',
    'rg_green1_enable',
    'rnd_green1_enable',
    'ro_green1_enable',
    'lc_green1_enable',
    'pg_green1_enable',
    'sw_rk_red_blue2_en',
    'rg_red_blue2_enable',
    'rnd_red_blue2_enable',
    'ro_red_blue2_enable',
    'lc_red_blue2_enable',
    'pg_red_blue2_enable',
    'sw_rk_green2_en',
    'rg_green2_enable',
    'rnd_green2_enable',
    'ro_green2_enable',
    'lc_green2_enable',
    'pg_green2_enable',
    'sw_rk_red_blue3_en',
    'rg_red_blue3_enable',
    'rnd_red_blue3_enable',
    'ro_red_blue3_enable',
    'lc_red_blue3_enable',
    'pg_red_blue3_enable',
    'sw_rk_green3_en',
    'rg_green3_enable',
    'rnd_green3_enable',
    'ro_green3_enable',
    'lc_green3_enable',
    'pg_green3_enable',
    'sw_mindis1_rb',
    'sw_mindis1_g',
    'line_thr_1_rb',
    'line_thr_1_g',
    'sw_dis_scale_min1',
    'sw_dis_scale_max1',
    'line_mad_fac_1_rb',
    'line_mad_fac_1_g',
    'pg_fac_1_rb',
    'pg_fac_1_g',
    'rnd_thr_1_rb',
    'rnd_thr_1_g',
    'rg_fac_1_rb',
    'rg_fac_1_g',
    'sw_mindis2_rb',
    'sw_mindis2_g',
    'line_thr_2_rb',
    'line_thr_2_g',
    'sw_dis_scale_min2',
    'sw_dis_scale_max2',
    'line_mad_fac_2_rb',
    'line_mad_fac_2_g',
    'pg_fac_2_rb',
    'pg_fac_2_g',
    'rnd_thr_2_rb',
    'rnd_thr_2_g',
    'rg_fac_2_rb',
    'rg_fac_2_g',
    'sw_mindis3_rb',
    'sw_mindis3_g',
    'line_thr_3_rb',
    'line_thr_3_g',
    'sw_dis_scale_min3',
    'sw_dis_scale_max3',
    'line_mad_fac_3_rb',
    'line_mad_fac_3_g',
    'pg_fac_3_rb',
    'pg_fac_3_g',
    'rnd_thr_3_rb',
    'rnd_thr_3_g',
    'rg_fac_3_rb',
    'rg_fac_3_g',
    'ro_lim_3_rb',
    'ro_lim_3_g',
    'ro_lim_2_rb',
    'ro_lim_2_g',
    'ro_lim_1_rb',
    'ro_lim_1_g',
    'rnd_offs_3_rb',
    'rnd_offs_3_g',
    'rnd_offs_2_rb',
    'rnd_offs_2_g',
    'rnd_offs_1_rb',
    'rnd_offs_1_g',
]
struct_Adpcc_basic_params_select_s._fields_ = [
    ('iso', c_int),
    ('stage1_enable', c_ubyte),
    ('grayscale_mode', c_ubyte),
    ('enable', c_ubyte),
    ('sw_rk_out_sel', c_ubyte),
    ('sw_dpcc_output_sel', c_ubyte),
    ('stage1_rb_3x3', c_ubyte),
    ('stage1_g_3x3', c_ubyte),
    ('stage1_incl_rb_center', c_ubyte),
    ('stage1_incl_green_center', c_ubyte),
    ('stage1_use_fix_set', c_ubyte),
    ('stage1_use_set_3', c_ubyte),
    ('stage1_use_set_2', c_ubyte),
    ('stage1_use_set_1', c_ubyte),
    ('sw_rk_red_blue1_en', c_ubyte),
    ('rg_red_blue1_enable', c_ubyte),
    ('rnd_red_blue1_enable', c_ubyte),
    ('ro_red_blue1_enable', c_ubyte),
    ('lc_red_blue1_enable', c_ubyte),
    ('pg_red_blue1_enable', c_ubyte),
    ('sw_rk_green1_en', c_ubyte),
    ('rg_green1_enable', c_ubyte),
    ('rnd_green1_enable', c_ubyte),
    ('ro_green1_enable', c_ubyte),
    ('lc_green1_enable', c_ubyte),
    ('pg_green1_enable', c_ubyte),
    ('sw_rk_red_blue2_en', c_ubyte),
    ('rg_red_blue2_enable', c_ubyte),
    ('rnd_red_blue2_enable', c_ubyte),
    ('ro_red_blue2_enable', c_ubyte),
    ('lc_red_blue2_enable', c_ubyte),
    ('pg_red_blue2_enable', c_ubyte),
    ('sw_rk_green2_en', c_ubyte),
    ('rg_green2_enable', c_ubyte),
    ('rnd_green2_enable', c_ubyte),
    ('ro_green2_enable', c_ubyte),
    ('lc_green2_enable', c_ubyte),
    ('pg_green2_enable', c_ubyte),
    ('sw_rk_red_blue3_en', c_ubyte),
    ('rg_red_blue3_enable', c_ubyte),
    ('rnd_red_blue3_enable', c_ubyte),
    ('ro_red_blue3_enable', c_ubyte),
    ('lc_red_blue3_enable', c_ubyte),
    ('pg_red_blue3_enable', c_ubyte),
    ('sw_rk_green3_en', c_ubyte),
    ('rg_green3_enable', c_ubyte),
    ('rnd_green3_enable', c_ubyte),
    ('ro_green3_enable', c_ubyte),
    ('lc_green3_enable', c_ubyte),
    ('pg_green3_enable', c_ubyte),
    ('sw_mindis1_rb', c_ubyte),
    ('sw_mindis1_g', c_ubyte),
    ('line_thr_1_rb', c_ubyte),
    ('line_thr_1_g', c_ubyte),
    ('sw_dis_scale_min1', c_ubyte),
    ('sw_dis_scale_max1', c_ubyte),
    ('line_mad_fac_1_rb', c_ubyte),
    ('line_mad_fac_1_g', c_ubyte),
    ('pg_fac_1_rb', c_ubyte),
    ('pg_fac_1_g', c_ubyte),
    ('rnd_thr_1_rb', c_ubyte),
    ('rnd_thr_1_g', c_ubyte),
    ('rg_fac_1_rb', c_ubyte),
    ('rg_fac_1_g', c_ubyte),
    ('sw_mindis2_rb', c_ubyte),
    ('sw_mindis2_g', c_ubyte),
    ('line_thr_2_rb', c_ubyte),
    ('line_thr_2_g', c_ubyte),
    ('sw_dis_scale_min2', c_ubyte),
    ('sw_dis_scale_max2', c_ubyte),
    ('line_mad_fac_2_rb', c_ubyte),
    ('line_mad_fac_2_g', c_ubyte),
    ('pg_fac_2_rb', c_ubyte),
    ('pg_fac_2_g', c_ubyte),
    ('rnd_thr_2_rb', c_ubyte),
    ('rnd_thr_2_g', c_ubyte),
    ('rg_fac_2_rb', c_ubyte),
    ('rg_fac_2_g', c_ubyte),
    ('sw_mindis3_rb', c_ubyte),
    ('sw_mindis3_g', c_ubyte),
    ('line_thr_3_rb', c_ubyte),
    ('line_thr_3_g', c_ubyte),
    ('sw_dis_scale_min3', c_ubyte),
    ('sw_dis_scale_max3', c_ubyte),
    ('line_mad_fac_3_rb', c_ubyte),
    ('line_mad_fac_3_g', c_ubyte),
    ('pg_fac_3_rb', c_ubyte),
    ('pg_fac_3_g', c_ubyte),
    ('rnd_thr_3_rb', c_ubyte),
    ('rnd_thr_3_g', c_ubyte),
    ('rg_fac_3_rb', c_ubyte),
    ('rg_fac_3_g', c_ubyte),
    ('ro_lim_3_rb', c_ubyte),
    ('ro_lim_3_g', c_ubyte),
    ('ro_lim_2_rb', c_ubyte),
    ('ro_lim_2_g', c_ubyte),
    ('ro_lim_1_rb', c_ubyte),
    ('ro_lim_1_g', c_ubyte),
    ('rnd_offs_3_rb', c_ubyte),
    ('rnd_offs_3_g', c_ubyte),
    ('rnd_offs_2_rb', c_ubyte),
    ('rnd_offs_2_g', c_ubyte),
    ('rnd_offs_1_rb', c_ubyte),
    ('rnd_offs_1_g', c_ubyte),
]

Adpcc_basic_params_select_t = struct_Adpcc_basic_params_select_s# /root/camera_engine_rkaiq/include/algos/adpcc/rk_aiq_types_adpcc_ext.h: 223

# /root/camera_engine_rkaiq/include/algos/adpcc/rk_aiq_types_adpcc_ext.h: 227
class struct_Adpcc_basic_params_s(Structure):
    pass

struct_Adpcc_basic_params_s.__slots__ = [
    'arBasic',
]
struct_Adpcc_basic_params_s._fields_ = [
    ('arBasic', Adpcc_basic_params_select_t * int(13)),
]

Adpcc_basic_params_t = struct_Adpcc_basic_params_s# /root/camera_engine_rkaiq/include/algos/adpcc/rk_aiq_types_adpcc_ext.h: 227

# /root/camera_engine_rkaiq/include/algos/adpcc/rk_aiq_types_adpcc_ext.h: 481
class struct_Adpcc_basic_cfg_params_s(Structure):
    pass

struct_Adpcc_basic_cfg_params_s.__slots__ = [
    'stage1_enable',
    'grayscale_mode',
    'enable',
    'sw_rk_out_sel',
    'sw_dpcc_output_sel',
    'stage1_rb_3x3',
    'stage1_g_3x3',
    'stage1_incl_rb_center',
    'stage1_incl_green_center',
    'stage1_use_fix_set',
    'stage1_use_set_3',
    'stage1_use_set_2',
    'stage1_use_set_1',
    'sw_rk_red_blue1_en',
    'rg_red_blue1_enable',
    'rnd_red_blue1_enable',
    'ro_red_blue1_enable',
    'lc_red_blue1_enable',
    'pg_red_blue1_enable',
    'sw_rk_green1_en',
    'rg_green1_enable',
    'rnd_green1_enable',
    'ro_green1_enable',
    'lc_green1_enable',
    'pg_green1_enable',
    'sw_rk_red_blue2_en',
    'rg_red_blue2_enable',
    'rnd_red_blue2_enable',
    'ro_red_blue2_enable',
    'lc_red_blue2_enable',
    'pg_red_blue2_enable',
    'sw_rk_green2_en',
    'rg_green2_enable',
    'rnd_green2_enable',
    'ro_green2_enable',
    'lc_green2_enable',
    'pg_green2_enable',
    'sw_rk_red_blue3_en',
    'rg_red_blue3_enable',
    'rnd_red_blue3_enable',
    'ro_red_blue3_enable',
    'lc_red_blue3_enable',
    'pg_red_blue3_enable',
    'sw_rk_green3_en',
    'rg_green3_enable',
    'rnd_green3_enable',
    'ro_green3_enable',
    'lc_green3_enable',
    'pg_green3_enable',
    'sw_mindis1_rb',
    'sw_mindis1_g',
    'line_thr_1_rb',
    'line_thr_1_g',
    'sw_dis_scale_min1',
    'sw_dis_scale_max1',
    'line_mad_fac_1_rb',
    'line_mad_fac_1_g',
    'pg_fac_1_rb',
    'pg_fac_1_g',
    'rnd_thr_1_rb',
    'rnd_thr_1_g',
    'rg_fac_1_rb',
    'rg_fac_1_g',
    'sw_mindis2_rb',
    'sw_mindis2_g',
    'line_thr_2_rb',
    'line_thr_2_g',
    'sw_dis_scale_min2',
    'sw_dis_scale_max2',
    'line_mad_fac_2_rb',
    'line_mad_fac_2_g',
    'pg_fac_2_rb',
    'pg_fac_2_g',
    'rnd_thr_2_rb',
    'rnd_thr_2_g',
    'rg_fac_2_rb',
    'rg_fac_2_g',
    'sw_mindis3_rb',
    'sw_mindis3_g',
    'line_thr_3_rb',
    'line_thr_3_g',
    'sw_dis_scale_min3',
    'sw_dis_scale_max3',
    'line_mad_fac_3_rb',
    'line_mad_fac_3_g',
    'pg_fac_3_rb',
    'pg_fac_3_g',
    'rnd_thr_3_rb',
    'rnd_thr_3_g',
    'rg_fac_3_rb',
    'rg_fac_3_g',
    'ro_lim_3_rb',
    'ro_lim_3_g',
    'ro_lim_2_rb',
    'ro_lim_2_g',
    'ro_lim_1_rb',
    'ro_lim_1_g',
    'rnd_offs_3_rb',
    'rnd_offs_3_g',
    'rnd_offs_2_rb',
    'rnd_offs_2_g',
    'rnd_offs_1_rb',
    'rnd_offs_1_g',
]
struct_Adpcc_basic_cfg_params_s._fields_ = [
    ('stage1_enable', c_ubyte),
    ('grayscale_mode', c_ubyte),
    ('enable', c_ubyte),
    ('sw_rk_out_sel', c_ubyte),
    ('sw_dpcc_output_sel', c_ubyte),
    ('stage1_rb_3x3', c_ubyte),
    ('stage1_g_3x3', c_ubyte),
    ('stage1_incl_rb_center', c_ubyte),
    ('stage1_incl_green_center', c_ubyte),
    ('stage1_use_fix_set', c_ubyte),
    ('stage1_use_set_3', c_ubyte),
    ('stage1_use_set_2', c_ubyte),
    ('stage1_use_set_1', c_ubyte),
    ('sw_rk_red_blue1_en', c_ubyte),
    ('rg_red_blue1_enable', c_ubyte),
    ('rnd_red_blue1_enable', c_ubyte),
    ('ro_red_blue1_enable', c_ubyte),
    ('lc_red_blue1_enable', c_ubyte),
    ('pg_red_blue1_enable', c_ubyte),
    ('sw_rk_green1_en', c_ubyte),
    ('rg_green1_enable', c_ubyte),
    ('rnd_green1_enable', c_ubyte),
    ('ro_green1_enable', c_ubyte),
    ('lc_green1_enable', c_ubyte),
    ('pg_green1_enable', c_ubyte),
    ('sw_rk_red_blue2_en', c_ubyte),
    ('rg_red_blue2_enable', c_ubyte),
    ('rnd_red_blue2_enable', c_ubyte),
    ('ro_red_blue2_enable', c_ubyte),
    ('lc_red_blue2_enable', c_ubyte),
    ('pg_red_blue2_enable', c_ubyte),
    ('sw_rk_green2_en', c_ubyte),
    ('rg_green2_enable', c_ubyte),
    ('rnd_green2_enable', c_ubyte),
    ('ro_green2_enable', c_ubyte),
    ('lc_green2_enable', c_ubyte),
    ('pg_green2_enable', c_ubyte),
    ('sw_rk_red_blue3_en', c_ubyte),
    ('rg_red_blue3_enable', c_ubyte),
    ('rnd_red_blue3_enable', c_ubyte),
    ('ro_red_blue3_enable', c_ubyte),
    ('lc_red_blue3_enable', c_ubyte),
    ('pg_red_blue3_enable', c_ubyte),
    ('sw_rk_green3_en', c_ubyte),
    ('rg_green3_enable', c_ubyte),
    ('rnd_green3_enable', c_ubyte),
    ('ro_green3_enable', c_ubyte),
    ('lc_green3_enable', c_ubyte),
    ('pg_green3_enable', c_ubyte),
    ('sw_mindis1_rb', c_ubyte),
    ('sw_mindis1_g', c_ubyte),
    ('line_thr_1_rb', c_ubyte),
    ('line_thr_1_g', c_ubyte),
    ('sw_dis_scale_min1', c_ubyte),
    ('sw_dis_scale_max1', c_ubyte),
    ('line_mad_fac_1_rb', c_ubyte),
    ('line_mad_fac_1_g', c_ubyte),
    ('pg_fac_1_rb', c_ubyte),
    ('pg_fac_1_g', c_ubyte),
    ('rnd_thr_1_rb', c_ubyte),
    ('rnd_thr_1_g', c_ubyte),
    ('rg_fac_1_rb', c_ubyte),
    ('rg_fac_1_g', c_ubyte),
    ('sw_mindis2_rb', c_ubyte),
    ('sw_mindis2_g', c_ubyte),
    ('line_thr_2_rb', c_ubyte),
    ('line_thr_2_g', c_ubyte),
    ('sw_dis_scale_min2', c_ubyte),
    ('sw_dis_scale_max2', c_ubyte),
    ('line_mad_fac_2_rb', c_ubyte),
    ('line_mad_fac_2_g', c_ubyte),
    ('pg_fac_2_rb', c_ubyte),
    ('pg_fac_2_g', c_ubyte),
    ('rnd_thr_2_rb', c_ubyte),
    ('rnd_thr_2_g', c_ubyte),
    ('rg_fac_2_rb', c_ubyte),
    ('rg_fac_2_g', c_ubyte),
    ('sw_mindis3_rb', c_ubyte),
    ('sw_mindis3_g', c_ubyte),
    ('line_thr_3_rb', c_ubyte),
    ('line_thr_3_g', c_ubyte),
    ('sw_dis_scale_min3', c_ubyte),
    ('sw_dis_scale_max3', c_ubyte),
    ('line_mad_fac_3_rb', c_ubyte),
    ('line_mad_fac_3_g', c_ubyte),
    ('pg_fac_3_rb', c_ubyte),
    ('pg_fac_3_g', c_ubyte),
    ('rnd_thr_3_rb', c_ubyte),
    ('rnd_thr_3_g', c_ubyte),
    ('rg_fac_3_rb', c_ubyte),
    ('rg_fac_3_g', c_ubyte),
    ('ro_lim_3_rb', c_ubyte),
    ('ro_lim_3_g', c_ubyte),
    ('ro_lim_2_rb', c_ubyte),
    ('ro_lim_2_g', c_ubyte),
    ('ro_lim_1_rb', c_ubyte),
    ('ro_lim_1_g', c_ubyte),
    ('rnd_offs_3_rb', c_ubyte),
    ('rnd_offs_3_g', c_ubyte),
    ('rnd_offs_2_rb', c_ubyte),
    ('rnd_offs_2_g', c_ubyte),
    ('rnd_offs_1_rb', c_ubyte),
    ('rnd_offs_1_g', c_ubyte),
]

Adpcc_basic_cfg_params_t = struct_Adpcc_basic_cfg_params_s# /root/camera_engine_rkaiq/include/algos/adpcc/rk_aiq_types_adpcc_ext.h: 481

# /root/camera_engine_rkaiq/include/algos/adpcc/rk_aiq_types_adpcc_ext.h: 523
class struct_Adpcc_bpt_params_s(Structure):
    pass

struct_Adpcc_bpt_params_s.__slots__ = [
    'bpt_rb_3x3',
    'bpt_g_3x3',
    'bpt_incl_rb_center',
    'bpt_incl_green_center',
    'bpt_use_fix_set',
    'bpt_use_set_3',
    'bpt_use_set_2',
    'bpt_use_set_1',
    'bpt_cor_en',
    'bpt_det_en',
    'bp_number',
    'bp_table_addr',
    'bpt_v_addr',
    'bpt_h_addr',
    'bp_cnt',
]
struct_Adpcc_bpt_params_s._fields_ = [
    ('bpt_rb_3x3', c_ubyte),
    ('bpt_g_3x3', c_ubyte),
    ('bpt_incl_rb_center', c_ubyte),
    ('bpt_incl_green_center', c_ubyte),
    ('bpt_use_fix_set', c_ubyte),
    ('bpt_use_set_3', c_ubyte),
    ('bpt_use_set_2', c_ubyte),
    ('bpt_use_set_1', c_ubyte),
    ('bpt_cor_en', c_ubyte),
    ('bpt_det_en', c_ubyte),
    ('bp_number', uint16_t),
    ('bp_table_addr', uint16_t),
    ('bpt_v_addr', uint16_t),
    ('bpt_h_addr', uint16_t),
    ('bp_cnt', c_uint),
]

Adpcc_bpt_params_t = struct_Adpcc_bpt_params_s# /root/camera_engine_rkaiq/include/algos/adpcc/rk_aiq_types_adpcc_ext.h: 523

# /root/camera_engine_rkaiq/include/algos/adpcc/rk_aiq_types_adpcc_ext.h: 530
class struct_dpcc_pdaf_point_s(Structure):
    pass

struct_dpcc_pdaf_point_s.__slots__ = [
    'y',
    'x',
]
struct_dpcc_pdaf_point_s._fields_ = [
    ('y', c_ubyte),
    ('x', c_ubyte),
]

dpcc_pdaf_point_t = struct_dpcc_pdaf_point_s# /root/camera_engine_rkaiq/include/algos/adpcc/rk_aiq_types_adpcc_ext.h: 530

# /root/camera_engine_rkaiq/include/algos/adpcc/rk_aiq_types_adpcc_ext.h: 566
class struct_Adpcc_pdaf_params_s(Structure):
    pass

struct_Adpcc_pdaf_params_s.__slots__ = [
    'sw_pdaf_en',
    'pdaf_point_en',
    'pdaf_offsety',
    'pdaf_offsetx',
    'pdaf_wrapy',
    'pdaf_wrapx',
    'pdaf_wrapy_num',
    'pdaf_wrapx_num',
    'point',
    'pdaf_forward_med',
]
struct_Adpcc_pdaf_params_s._fields_ = [
    ('sw_pdaf_en', c_ubyte),
    ('pdaf_point_en', c_ubyte * int(16)),
    ('pdaf_offsety', uint16_t),
    ('pdaf_offsetx', uint16_t),
    ('pdaf_wrapy', c_ubyte),
    ('pdaf_wrapx', c_ubyte),
    ('pdaf_wrapy_num', uint16_t),
    ('pdaf_wrapx_num', uint16_t),
    ('point', dpcc_pdaf_point_t * int(16)),
    ('pdaf_forward_med', c_ubyte),
]

Adpcc_pdaf_params_t = struct_Adpcc_pdaf_params_s# /root/camera_engine_rkaiq/include/algos/adpcc/rk_aiq_types_adpcc_ext.h: 566

# /root/camera_engine_rkaiq/include/algos/adpcc/rk_aiq_types_adpcc_ext.h: 578
class struct_Adpcc_Auto_Attr_s(Structure):
    pass

struct_Adpcc_Auto_Attr_s.__slots__ = [
    'stBasicParams',
    'stBptParams',
    'stPdafParams',
    'stFastMode',
    'stSensorDpcc',
    'stBasicSelect',
    'stBptSelect',
    'stPdafSelect',
]
struct_Adpcc_Auto_Attr_s._fields_ = [
    ('stBasicParams', Adpcc_basic_params_t),
    ('stBptParams', Adpcc_bpt_params_t),
    ('stPdafParams', Adpcc_pdaf_params_t),
    ('stFastMode', CalibDb_Dpcc_Fast_Mode_t),
    ('stSensorDpcc', CalibDb_Dpcc_Sensor_t),
    ('stBasicSelect', Adpcc_basic_cfg_params_t),
    ('stBptSelect', Adpcc_bpt_params_t),
    ('stPdafSelect', Adpcc_pdaf_params_t),
]

Adpcc_Auto_Attr_t = struct_Adpcc_Auto_Attr_s# /root/camera_engine_rkaiq/include/algos/adpcc/rk_aiq_types_adpcc_ext.h: 578

# /root/camera_engine_rkaiq/include/algos/adpcc/rk_aiq_types_adpcc_ext.h: 595
class struct_Adpcc_fast_mode_attr_s(Structure):
    pass

struct_Adpcc_fast_mode_attr_s.__slots__ = [
    'fast_mode_en',
    'fast_mode_single_en',
    'fast_mode_single_level',
    'fast_mode_double_en',
    'fast_mode_double_level',
    'fast_mode_triple_en',
    'fast_mode_triple_level',
]
struct_Adpcc_fast_mode_attr_s._fields_ = [
    ('fast_mode_en', c_bool),
    ('fast_mode_single_en', c_bool),
    ('fast_mode_single_level', c_int),
    ('fast_mode_double_en', c_bool),
    ('fast_mode_double_level', c_int),
    ('fast_mode_triple_en', c_bool),
    ('fast_mode_triple_level', c_int),
]

Adpcc_fast_mode_attr_t = struct_Adpcc_fast_mode_attr_s# /root/camera_engine_rkaiq/include/algos/adpcc/rk_aiq_types_adpcc_ext.h: 595

# /root/camera_engine_rkaiq/include/algos/adpcc/rk_aiq_types_adpcc_ext.h: 604
class struct_Adpcc_onfly_cfg_s(Structure):
    pass

struct_Adpcc_onfly_cfg_s.__slots__ = [
    'mode',
    'fast_mode',
    'expert_mode',
]
struct_Adpcc_onfly_cfg_s._fields_ = [
    ('mode', Adpcc_onfly_mode_t),
    ('fast_mode', Adpcc_fast_mode_attr_t),
    ('expert_mode', Adpcc_basic_cfg_params_t),
]

Adpcc_onfly_cfg_t = struct_Adpcc_onfly_cfg_s# /root/camera_engine_rkaiq/include/algos/adpcc/rk_aiq_types_adpcc_ext.h: 604

# /root/camera_engine_rkaiq/include/algos/adpcc/rk_aiq_types_adpcc_ext.h: 615
class struct_Adpcc_sensor_dpcc_attr_s(Structure):
    pass

struct_Adpcc_sensor_dpcc_attr_s.__slots__ = [
    'en',
    'max_level',
    'single_level',
    'double_level',
]
struct_Adpcc_sensor_dpcc_attr_s._fields_ = [
    ('en', c_bool),
    ('max_level', c_int),
    ('single_level', c_int),
    ('double_level', c_int),
]

Adpcc_sensor_dpcc_attr_t = struct_Adpcc_sensor_dpcc_attr_s# /root/camera_engine_rkaiq/include/algos/adpcc/rk_aiq_types_adpcc_ext.h: 615

# /root/camera_engine_rkaiq/include/algos/adpcc/rk_aiq_types_adpcc_ext.h: 628
class struct_Adpcc_Manual_Attr_s(Structure):
    pass

struct_Adpcc_Manual_Attr_s.__slots__ = [
    'enable',
    'stOnfly',
    'stBpt',
    'stPdaf',
    'stSensorDpcc',
]
struct_Adpcc_Manual_Attr_s._fields_ = [
    ('enable', c_ubyte),
    ('stOnfly', Adpcc_onfly_cfg_t),
    ('stBpt', Adpcc_bpt_params_t),
    ('stPdaf', Adpcc_pdaf_params_t),
    ('stSensorDpcc', Adpcc_sensor_dpcc_attr_t),
]

Adpcc_Manual_Attr_t = struct_Adpcc_Manual_Attr_s# /root/camera_engine_rkaiq/include/algos/adpcc/rk_aiq_types_adpcc_ext.h: 628

# /root/camera_engine_rkaiq/include/algos/adpcc/rk_aiq_types_adpcc_ext.h: 635
class struct_rk_aiq_dpcc_attrib_V20_s(Structure):
    pass

struct_rk_aiq_dpcc_attrib_V20_s.__slots__ = [
    'eMode',
    'stAuto',
    'stManual',
    'sync',
]
struct_rk_aiq_dpcc_attrib_V20_s._fields_ = [
    ('eMode', AdpccOPMode_t),
    ('stAuto', Adpcc_Auto_Attr_t),
    ('stManual', Adpcc_Manual_Attr_t),
    ('sync', rk_aiq_uapi_sync_t),
]

rk_aiq_dpcc_attrib_V20_t = struct_rk_aiq_dpcc_attrib_V20_s# /root/camera_engine_rkaiq/include/algos/adpcc/rk_aiq_types_adpcc_ext.h: 635

# /root/camera_engine_rkaiq/include/iq_parser/RkAiqCalibDbTypesIsp20.h: 1118
class struct_CalibDb_BayerNR_Params_s(Structure):
    pass

struct_CalibDb_BayerNR_Params_s._pack_ = 4
struct_CalibDb_BayerNR_Params_s.__slots__ = [
    'snr_mode',
    'sensor_mode',
    'iso',
    'filtPara',
    'luLevel',
    'luLevelVal',
    'luRatio',
    'fixW',
    'lamda',
    'gauss_en',
    'RGainOff',
    'RGainFilp',
    'BGainOff',
    'BGainFilp',
    'edgeSoftness',
    'gaussWeight0',
    'gaussWeight1',
    'bilEdgeFilter',
    'bilFilterStreng',
    'bilEdgeSoft',
    'bilEdgeSoftRatio',
    'bilRegWgt',
]
struct_CalibDb_BayerNR_Params_s._fields_ = [
    ('snr_mode', c_char * int(64)),
    ('sensor_mode', c_char * int(64)),
    ('iso', c_float * int(13)),
    ('filtPara', c_float * int(13)),
    ('luLevel', c_float * int(8)),
    ('luLevelVal', c_float * int(8)),
    ('luRatio', (c_float * int(13)) * int(8)),
    ('fixW', (c_float * int(13)) * int(4)),
    ('lamda', c_float),
    ('gauss_en', c_ubyte),
    ('RGainOff', c_float),
    ('RGainFilp', c_float),
    ('BGainOff', c_float),
    ('BGainFilp', c_float),
    ('edgeSoftness', c_float),
    ('gaussWeight0', c_float),
    ('gaussWeight1', c_float),
    ('bilEdgeFilter', c_float),
    ('bilFilterStreng', c_float * int(13)),
    ('bilEdgeSoft', c_float),
    ('bilEdgeSoftRatio', c_float),
    ('bilRegWgt', c_float),
]

CalibDb_BayerNR_Params_t = struct_CalibDb_BayerNR_Params_s# /root/camera_engine_rkaiq/include/iq_parser/RkAiqCalibDbTypesIsp20.h: 1118

# /root/camera_engine_rkaiq/include/iq_parser/RkAiqCalibDbTypesIsp20.h: 1123
class struct_CalibDb_BayerNr_ModeCell_s(Structure):
    pass

struct_CalibDb_BayerNr_ModeCell_s._pack_ = 4
struct_CalibDb_BayerNr_ModeCell_s.__slots__ = [
    'name',
    'setting',
]
struct_CalibDb_BayerNr_ModeCell_s._fields_ = [
    ('name', c_char * int(20)),
    ('setting', CalibDb_BayerNR_Params_t * int(6)),
]

CalibDb_BayerNr_ModeCell_t = struct_CalibDb_BayerNr_ModeCell_s# /root/camera_engine_rkaiq/include/iq_parser/RkAiqCalibDbTypesIsp20.h: 1123

# /root/camera_engine_rkaiq/include/iq_parser/RkAiqCalibDbTypesIsp20.h: 1129
class struct_CalibDb_BayerNr_s(Structure):
    pass

struct_CalibDb_BayerNr_s._pack_ = 4
struct_CalibDb_BayerNr_s.__slots__ = [
    'enable',
    'version',
    'mode_cell',
]
struct_CalibDb_BayerNr_s._fields_ = [
    ('enable', c_int),
    ('version', c_char * int(64)),
    ('mode_cell', CalibDb_BayerNr_ModeCell_t * int(5)),
]

CalibDb_BayerNr_t = struct_CalibDb_BayerNr_s# /root/camera_engine_rkaiq/include/iq_parser/RkAiqCalibDbTypesIsp20.h: 1129

# /root/camera_engine_rkaiq/include/iq_parser/RkAiqCalibDbTypesIsp20.h: 1377
class struct_CalibDb_UVNR_Params_s(Structure):
    pass

struct_CalibDb_UVNR_Params_s._pack_ = 4
struct_CalibDb_UVNR_Params_s.__slots__ = [
    'snr_mode',
    'sensor_mode',
    'ISO',
    'step0_uvgrad_ratio',
    'step0_uvgrad_offset',
    'step1_nonMed1',
    'step1_nonBf1',
    'step1_downSample_w',
    'step1_downSample_h',
    'step1_downSample_meansize',
    'step1_median_ratio',
    'step1_median_size',
    'step1_median_IIR',
    'step1_bf_sigmaR',
    'step1_bf_uvgain',
    'step1_bf_ratio',
    'step1_bf_size',
    'step1_bf_sigmaD',
    'step1_bf_isRowIIR',
    'step1_bf_isYcopy',
    'step2_nonExt_block',
    'step2_nonMed',
    'step2_nonBf',
    'step2_downSample_w',
    'step2_downSample_h',
    'step2_downSample_meansize',
    'step2_median_ratio',
    'step2_median_size',
    'step2_median_IIR',
    'step2_bf_sigmaR',
    'step2_bf_uvgain',
    'step2_bf_ratio',
    'step2_bf_size',
    'step2_bf_sigmaD',
    'step2_bf_isRowIIR',
    'step2_bf_isYcopy',
    'step3_nonBf3',
    'step3_bf_sigmaR',
    'step3_bf_uvgain',
    'step3_bf_ratio',
    'step3_bf_size',
    'step3_bf_sigmaD',
    'step3_bf_isRowIIR',
    'step3_bf_isYcopy',
    'kernel_3x3',
    'kernel_5x5',
    'kernel_9x9',
    'kernel_9x9_num',
    'sigma_adj_luma',
    'sigma_adj_ratio',
    'threshold_adj_luma',
    'threshold_adj_thre',
]
struct_CalibDb_UVNR_Params_s._fields_ = [
    ('snr_mode', c_char * int(64)),
    ('sensor_mode', c_char * int(64)),
    ('ISO', c_float * int(13)),
    ('step0_uvgrad_ratio', c_float * int(13)),
    ('step0_uvgrad_offset', c_float * int(13)),
    ('step1_nonMed1', c_float * int(4)),
    ('step1_nonBf1', c_float * int(4)),
    ('step1_downSample_w', c_float * int(13)),
    ('step1_downSample_h', c_float * int(13)),
    ('step1_downSample_meansize', c_float * int(13)),
    ('step1_median_ratio', c_float * int(13)),
    ('step1_median_size', c_float * int(13)),
    ('step1_median_IIR', c_float * int(13)),
    ('step1_bf_sigmaR', c_float * int(13)),
    ('step1_bf_uvgain', c_float * int(13)),
    ('step1_bf_ratio', c_float * int(13)),
    ('step1_bf_size', c_float * int(13)),
    ('step1_bf_sigmaD', c_float * int(13)),
    ('step1_bf_isRowIIR', c_float * int(13)),
    ('step1_bf_isYcopy', c_float * int(13)),
    ('step2_nonExt_block', c_float * int(4)),
    ('step2_nonMed', c_float * int(4)),
    ('step2_nonBf', c_float * int(4)),
    ('step2_downSample_w', c_float * int(13)),
    ('step2_downSample_h', c_float * int(13)),
    ('step2_downSample_meansize', c_float * int(13)),
    ('step2_median_ratio', c_float * int(13)),
    ('step2_median_size', c_float * int(13)),
    ('step2_median_IIR', c_float * int(13)),
    ('step2_bf_sigmaR', c_float * int(13)),
    ('step2_bf_uvgain', c_float * int(13)),
    ('step2_bf_ratio', c_float * int(13)),
    ('step2_bf_size', c_float * int(13)),
    ('step2_bf_sigmaD', c_float * int(13)),
    ('step2_bf_isRowIIR', c_float * int(13)),
    ('step2_bf_isYcopy', c_float * int(13)),
    ('step3_nonBf3', c_float * int(4)),
    ('step3_bf_sigmaR', c_float * int(13)),
    ('step3_bf_uvgain', c_float * int(13)),
    ('step3_bf_ratio', c_float * int(13)),
    ('step3_bf_size', c_float * int(13)),
    ('step3_bf_sigmaD', c_float * int(13)),
    ('step3_bf_isRowIIR', c_float * int(13)),
    ('step3_bf_isYcopy', c_float * int(13)),
    ('kernel_3x3', c_float * int(3)),
    ('kernel_5x5', c_float * int(5)),
    ('kernel_9x9', c_float * int(8)),
    ('kernel_9x9_num', c_float),
    ('sigma_adj_luma', c_float * int(9)),
    ('sigma_adj_ratio', c_float * int(9)),
    ('threshold_adj_luma', c_float * int(9)),
    ('threshold_adj_thre', c_float * int(9)),
]

CalibDb_UVNR_Params_t = struct_CalibDb_UVNR_Params_s# /root/camera_engine_rkaiq/include/iq_parser/RkAiqCalibDbTypesIsp20.h: 1377

# /root/camera_engine_rkaiq/include/iq_parser/RkAiqCalibDbTypesIsp20.h: 1382
class struct_CalibDb_UVNR_ModeCell_s(Structure):
    pass

struct_CalibDb_UVNR_ModeCell_s._pack_ = 4
struct_CalibDb_UVNR_ModeCell_s.__slots__ = [
    'name',
    'setting',
]
struct_CalibDb_UVNR_ModeCell_s._fields_ = [
    ('name', c_char * int(20)),
    ('setting', CalibDb_UVNR_Params_t * int(6)),
]

CalibDb_UVNR_ModeCell_t = struct_CalibDb_UVNR_ModeCell_s# /root/camera_engine_rkaiq/include/iq_parser/RkAiqCalibDbTypesIsp20.h: 1382

# /root/camera_engine_rkaiq/include/iq_parser/RkAiqCalibDbTypesIsp20.h: 1388
class struct_CalibDb_UVNR_s(Structure):
    pass

struct_CalibDb_UVNR_s._pack_ = 4
struct_CalibDb_UVNR_s.__slots__ = [
    'enable',
    'version',
    'mode_cell',
]
struct_CalibDb_UVNR_s._fields_ = [
    ('enable', c_int),
    ('version', c_char * int(64)),
    ('mode_cell', CalibDb_UVNR_ModeCell_t * int(5)),
]

CalibDb_UVNR_t = struct_CalibDb_UVNR_s# /root/camera_engine_rkaiq/include/iq_parser/RkAiqCalibDbTypesIsp20.h: 1388

# /root/camera_engine_rkaiq/include/iq_parser/RkAiqCalibDbTypesIsp20.h: 1448
class struct_CalibDb_YNR_ISO_s(Structure):
    pass

struct_CalibDb_YNR_ISO_s._pack_ = 4
struct_CalibDb_YNR_ISO_s.__slots__ = [
    'iso',
    'sigma_curve',
    'ynr_lci',
    'ynr_lhci',
    'ynr_hlci',
    'ynr_hhci',
    'lo_lumaPoint',
    'lo_lumaRatio',
    'lo_directionStrength',
    'lo_bfScale',
    'imerge_ratio',
    'imerge_bound',
    'denoise_weight',
    'hi_lumaPoint',
    'hi_lumaRatio',
    'hi_bfScale',
    'hwith_d',
    'hi_denoiseStrength',
    'hi_detailMinAdjDnW',
    'hi_denoiseWeight',
    'y_luma_point',
    'hgrad_y_level1',
    'hgrad_y_level2',
    'hgrad_y_level3',
    'hgrad_y_level4',
    'hi_soft_thresh_scale',
]
struct_CalibDb_YNR_ISO_s._fields_ = [
    ('iso', c_float),
    ('sigma_curve', c_double * int(5)),
    ('ynr_lci', c_float * int(4)),
    ('ynr_lhci', c_float * int(4)),
    ('ynr_hlci', c_float * int(4)),
    ('ynr_hhci', c_float * int(4)),
    ('lo_lumaPoint', c_float * int(6)),
    ('lo_lumaRatio', c_float * int(6)),
    ('lo_directionStrength', c_float),
    ('lo_bfScale', c_float * int(4)),
    ('imerge_ratio', c_float),
    ('imerge_bound', c_float),
    ('denoise_weight', c_float * int(4)),
    ('hi_lumaPoint', c_float * int(6)),
    ('hi_lumaRatio', c_float * int(6)),
    ('hi_bfScale', c_float * int(4)),
    ('hwith_d', c_float * int(4)),
    ('hi_denoiseStrength', c_float),
    ('hi_detailMinAdjDnW', c_float),
    ('hi_denoiseWeight', c_float * int(4)),
    ('y_luma_point', c_float * int(6)),
    ('hgrad_y_level1', c_float * int(6)),
    ('hgrad_y_level2', c_float * int(6)),
    ('hgrad_y_level3', c_float * int(6)),
    ('hgrad_y_level4', c_float * int(6)),
    ('hi_soft_thresh_scale', c_float * int(4)),
]

CalibDb_YNR_ISO_t = struct_CalibDb_YNR_ISO_s# /root/camera_engine_rkaiq/include/iq_parser/RkAiqCalibDbTypesIsp20.h: 1448

# /root/camera_engine_rkaiq/include/iq_parser/RkAiqCalibDbTypesIsp20.h: 1454
class struct_CalibDb_YNR_Setting_s(Structure):
    pass

struct_CalibDb_YNR_Setting_s._pack_ = 4
struct_CalibDb_YNR_Setting_s.__slots__ = [
    'snr_mode',
    'sensor_mode',
    'ynr_iso',
]
struct_CalibDb_YNR_Setting_s._fields_ = [
    ('snr_mode', c_char * int(64)),
    ('sensor_mode', c_char * int(64)),
    ('ynr_iso', CalibDb_YNR_ISO_t * int(13)),
]

CalibDb_YNR_Setting_t = struct_CalibDb_YNR_Setting_s# /root/camera_engine_rkaiq/include/iq_parser/RkAiqCalibDbTypesIsp20.h: 1454

# /root/camera_engine_rkaiq/include/iq_parser/RkAiqCalibDbTypesIsp20.h: 1459
class struct_CalibDb_YNR_ModeCell_s(Structure):
    pass

struct_CalibDb_YNR_ModeCell_s._pack_ = 4
struct_CalibDb_YNR_ModeCell_s.__slots__ = [
    'name',
    'setting',
]
struct_CalibDb_YNR_ModeCell_s._fields_ = [
    ('name', c_char * int(20)),
    ('setting', CalibDb_YNR_Setting_t * int(6)),
]

CalibDb_YNR_ModeCell_t = struct_CalibDb_YNR_ModeCell_s# /root/camera_engine_rkaiq/include/iq_parser/RkAiqCalibDbTypesIsp20.h: 1459

# /root/camera_engine_rkaiq/include/iq_parser/RkAiqCalibDbTypesIsp20.h: 1465
class struct_CalibDb_YNR_s(Structure):
    pass

struct_CalibDb_YNR_s._pack_ = 4
struct_CalibDb_YNR_s.__slots__ = [
    'enable',
    'version',
    'mode_cell',
]
struct_CalibDb_YNR_s._fields_ = [
    ('enable', c_int),
    ('version', c_char * int(64)),
    ('mode_cell', CalibDb_YNR_ModeCell_t * int(5)),
]

CalibDb_YNR_t = struct_CalibDb_YNR_s# /root/camera_engine_rkaiq/include/iq_parser/RkAiqCalibDbTypesIsp20.h: 1465

# /root/camera_engine_rkaiq/include/iq_parser/RkAiqCalibDbTypesIsp20.h: 1518
class struct_CalibDb_awb_uv_ratio_s(Structure):
    pass

struct_CalibDb_awb_uv_ratio_s._pack_ = 4
struct_CalibDb_awb_uv_ratio_s.__slots__ = [
    'illum',
    'ratio',
]
struct_CalibDb_awb_uv_ratio_s._fields_ = [
    ('illum', c_char * int(9)),
    ('ratio', c_float * int(2)),
]

# /root/camera_engine_rkaiq/include/iq_parser/RkAiqCalibDbTypesIsp20.h: 1523
class struct_CalibDb_MFNR_ISO_s(Structure):
    pass

struct_CalibDb_MFNR_ISO_s._pack_ = 4
struct_CalibDb_MFNR_ISO_s.__slots__ = [
    'iso',
    'weight_limit_y',
    'weight_limit_uv',
    'ratio_frq',
    'luma_w_in_chroma',
    'noise_curve',
    'noise_curve_x00',
    'y_lo_noiseprofile',
    'y_hi_noiseprofile',
    'y_lo_denoiseweight',
    'y_hi_denoiseweight',
    'y_lo_bfscale',
    'y_hi_bfscale',
    'y_lumanrpoint',
    'y_lumanrcurve',
    'y_denoisestrength',
    'y_lo_lvl0_gfdelta',
    'y_hi_lvl0_gfdelta',
    'y_lo_lvl1_gfdelta',
    'y_hi_lvl1_gfdelta',
    'y_lo_lvl2_gfdelta',
    'y_hi_lvl2_gfdelta',
    'y_lo_lvl3_gfdelta',
    'y_hi_lvl3_gfdelta',
    'uv_lo_noiseprofile',
    'uv_hi_noiseprofile',
    'uv_lo_denoiseweight',
    'uv_hi_denoiseweight',
    'uv_lo_bfscale',
    'uv_hi_bfscale',
    'uv_lumanrpoint',
    'uv_lumanrcurve',
    'uv_denoisestrength',
    'uv_lo_lvl0_gfdelta',
    'uv_hi_lvl0_gfdelta',
    'uv_lo_lvl1_gfdelta',
    'uv_hi_lvl1_gfdelta',
    'uv_lo_lvl2_gfdelta',
    'uv_hi_lvl2_gfdelta',
    'lvl0_gfsigma',
    'lvl1_gfsigma',
    'lvl2_gfsigma',
    'lvl3_gfsigma',
]
struct_CalibDb_MFNR_ISO_s._fields_ = [
    ('iso', c_float),
    ('weight_limit_y', c_float * int(4)),
    ('weight_limit_uv', c_float * int(3)),
    ('ratio_frq', c_float * int(4)),
    ('luma_w_in_chroma', c_float * int(3)),
    ('noise_curve', c_double * int(5)),
    ('noise_curve_x00', c_double),
    ('y_lo_noiseprofile', c_float * int(4)),
    ('y_hi_noiseprofile', c_float * int(4)),
    ('y_lo_denoiseweight', c_float * int(4)),
    ('y_hi_denoiseweight', c_float * int(4)),
    ('y_lo_bfscale', c_float * int(4)),
    ('y_hi_bfscale', c_float * int(4)),
    ('y_lumanrpoint', c_float * int(6)),
    ('y_lumanrcurve', c_float * int(6)),
    ('y_denoisestrength', c_float),
    ('y_lo_lvl0_gfdelta', c_float * int(6)),
    ('y_hi_lvl0_gfdelta', c_float * int(6)),
    ('y_lo_lvl1_gfdelta', c_float * int(3)),
    ('y_hi_lvl1_gfdelta', c_float * int(3)),
    ('y_lo_lvl2_gfdelta', c_float * int(3)),
    ('y_hi_lvl2_gfdelta', c_float * int(3)),
    ('y_lo_lvl3_gfdelta', c_float * int(3)),
    ('y_hi_lvl3_gfdelta', c_float * int(3)),
    ('uv_lo_noiseprofile', c_float * int(3)),
    ('uv_hi_noiseprofile', c_float * int(3)),
    ('uv_lo_denoiseweight', c_float * int(3)),
    ('uv_hi_denoiseweight', c_float * int(3)),
    ('uv_lo_bfscale', c_float * int(3)),
    ('uv_hi_bfscale', c_float * int(3)),
    ('uv_lumanrpoint', c_float * int(6)),
    ('uv_lumanrcurve', c_float * int(6)),
    ('uv_denoisestrength', c_float),
    ('uv_lo_lvl0_gfdelta', c_float * int(6)),
    ('uv_hi_lvl0_gfdelta', c_float * int(6)),
    ('uv_lo_lvl1_gfdelta', c_float * int(3)),
    ('uv_hi_lvl1_gfdelta', c_float * int(3)),
    ('uv_lo_lvl2_gfdelta', c_float * int(3)),
    ('uv_hi_lvl2_gfdelta', c_float * int(3)),
    ('lvl0_gfsigma', c_float * int(6)),
    ('lvl1_gfsigma', c_float * int(3)),
    ('lvl2_gfsigma', c_float * int(3)),
    ('lvl3_gfsigma', c_float * int(3)),
]

# /root/camera_engine_rkaiq/include/iq_parser/RkAiqCalibDbTypesIsp20.h: 1573
class struct_CalibDb_MFNR_Setting_s(Structure):
    pass

struct_CalibDb_MFNR_Setting_s._pack_ = 4
struct_CalibDb_MFNR_Setting_s.__slots__ = [
    'snr_mode',
    'sensor_mode',
    'mfnr_iso',
]
struct_CalibDb_MFNR_Setting_s._fields_ = [
    ('snr_mode', c_char * int(64)),
    ('sensor_mode', c_char * int(64)),
    ('mfnr_iso', struct_CalibDb_MFNR_ISO_s * int(13)),
]

CalibDb_MFNR_Setting_t = struct_CalibDb_MFNR_Setting_s# /root/camera_engine_rkaiq/include/iq_parser/RkAiqCalibDbTypesIsp20.h: 1573

# /root/camera_engine_rkaiq/include/iq_parser/RkAiqCalibDbTypesIsp20.h: 1581
class struct_CalibDb_MFNR_Dynamic_s(Structure):
    pass

struct_CalibDb_MFNR_Dynamic_s._pack_ = 4
struct_CalibDb_MFNR_Dynamic_s.__slots__ = [
    'enable',
    'lowth_iso',
    'lowth_time',
    'highth_iso',
    'highth_time',
]
struct_CalibDb_MFNR_Dynamic_s._fields_ = [
    ('enable', c_int),
    ('lowth_iso', c_float),
    ('lowth_time', c_float),
    ('highth_iso', c_float),
    ('highth_time', c_float),
]

CalibDb_MFNR_Dynamic_t = struct_CalibDb_MFNR_Dynamic_s# /root/camera_engine_rkaiq/include/iq_parser/RkAiqCalibDbTypesIsp20.h: 1581

# /root/camera_engine_rkaiq/include/iq_parser/RkAiqCalibDbTypesIsp20.h: 1604
class struct_CalibDb_MFNR_Motion_s(Structure):
    pass

struct_CalibDb_MFNR_Motion_s._pack_ = 4
struct_CalibDb_MFNR_Motion_s.__slots__ = [
    'enable',
    'iso',
    'sigmaHScale',
    'sigmaLScale',
    'lightClp',
    'uvWeight',
    'mfnrSigmaScale',
    'yuvnrGainScale0',
    'yuvnrGainScale1',
    'yuvnrGainScale2',
    'reserved0',
    'reserved1',
    'reserved2',
    'reserved3',
    'reserved4',
    'reserved5',
    'reserved6',
    'reserved7',
    'frame_limit_uv',
    'frame_limit_y',
]
struct_CalibDb_MFNR_Motion_s._fields_ = [
    ('enable', c_int),
    ('iso', c_float * int(13)),
    ('sigmaHScale', c_float * int(13)),
    ('sigmaLScale', c_float * int(13)),
    ('lightClp', c_float * int(13)),
    ('uvWeight', c_float * int(13)),
    ('mfnrSigmaScale', c_float * int(13)),
    ('yuvnrGainScale0', c_float * int(13)),
    ('yuvnrGainScale1', c_float * int(13)),
    ('yuvnrGainScale2', c_float * int(13)),
    ('reserved0', c_float * int(13)),
    ('reserved1', c_float * int(13)),
    ('reserved2', c_float * int(13)),
    ('reserved3', c_float * int(13)),
    ('reserved4', c_float * int(13)),
    ('reserved5', c_float * int(13)),
    ('reserved6', c_float * int(13)),
    ('reserved7', c_float * int(13)),
    ('frame_limit_uv', c_float * int(13)),
    ('frame_limit_y', c_float * int(13)),
]

CalibDb_MFNR_Motion_t = struct_CalibDb_MFNR_Motion_s# /root/camera_engine_rkaiq/include/iq_parser/RkAiqCalibDbTypesIsp20.h: 1604

# /root/camera_engine_rkaiq/include/iq_parser/RkAiqCalibDbTypesIsp20.h: 1611
class struct_CalibDb_MFNR_ModeCell_s(Structure):
    pass

struct_CalibDb_MFNR_ModeCell_s._pack_ = 4
struct_CalibDb_MFNR_ModeCell_s.__slots__ = [
    'name',
    'setting',
    'dynamic',
    'motion',
]
struct_CalibDb_MFNR_ModeCell_s._fields_ = [
    ('name', c_char * int(20)),
    ('setting', CalibDb_MFNR_Setting_t * int(6)),
    ('dynamic', CalibDb_MFNR_Dynamic_t),
    ('motion', CalibDb_MFNR_Motion_t),
]

CalibDb_MFNR_ModeCell_t = struct_CalibDb_MFNR_ModeCell_s# /root/camera_engine_rkaiq/include/iq_parser/RkAiqCalibDbTypesIsp20.h: 1611

# /root/camera_engine_rkaiq/include/iq_parser/RkAiqCalibDbTypesIsp20.h: 1624
class struct_CalibDb_MFNR_s(Structure):
    pass

struct_CalibDb_MFNR_s._pack_ = 4
struct_CalibDb_MFNR_s.__slots__ = [
    'enable',
    'version',
    'local_gain_en',
    'motion_detect_en',
    'mode_3to1',
    'max_level',
    'max_level_uv',
    'back_ref_num',
    'uv_ratio',
    'mode_cell',
]
struct_CalibDb_MFNR_s._fields_ = [
    ('enable', c_int),
    ('version', c_char * int(64)),
    ('local_gain_en', c_ubyte),
    ('motion_detect_en', c_ubyte),
    ('mode_3to1', c_ubyte),
    ('max_level', c_ubyte),
    ('max_level_uv', c_ubyte),
    ('back_ref_num', c_ubyte),
    ('uv_ratio', struct_CalibDb_awb_uv_ratio_s * int(4)),
    ('mode_cell', CalibDb_MFNR_ModeCell_t * int(5)),
]

CalibDb_MFNR_t = struct_CalibDb_MFNR_s# /root/camera_engine_rkaiq/include/iq_parser/RkAiqCalibDbTypesIsp20.h: 1624

# /root/camera_engine_rkaiq/include/algos/abayer2dnr2/rk_aiq_types_abayer2dnr_hw_v2.h: 61
class struct_RK_Bayer2dnr_Fix_V2_s(Structure):
    pass

struct_RK_Bayer2dnr_Fix_V2_s.__slots__ = [
    'baynr_lg2_mode',
    'baynr_gauss_en',
    'baynr_log_bypass',
    'baynr_en',
    'baynr_dgain',
    'baynr_pix_diff',
    'baynr_diff_thld',
    'baynr_softthld',
    'bltflt_streng',
    'baynr_reg_w1',
    'sigma_x',
    'sigma_y',
    'weit_d',
    'lg2_lgoff',
    'lg2_off',
    'dat_max',
]
struct_RK_Bayer2dnr_Fix_V2_s._fields_ = [
    ('baynr_lg2_mode', uint8_t),
    ('baynr_gauss_en', uint8_t),
    ('baynr_log_bypass', uint8_t),
    ('baynr_en', uint8_t),
    ('baynr_dgain', uint16_t * int(3)),
    ('baynr_pix_diff', uint16_t),
    ('baynr_diff_thld', uint16_t),
    ('baynr_softthld', uint16_t),
    ('bltflt_streng', uint16_t),
    ('baynr_reg_w1', uint16_t),
    ('sigma_x', uint16_t * int(16)),
    ('sigma_y', uint16_t * int(16)),
    ('weit_d', uint16_t * int(3)),
    ('lg2_lgoff', uint16_t),
    ('lg2_off', uint16_t),
    ('dat_max', uint32_t),
]

RK_Bayer2dnr_Fix_V2_t = struct_RK_Bayer2dnr_Fix_V2_s# /root/camera_engine_rkaiq/include/algos/abayer2dnr2/rk_aiq_types_abayer2dnr_hw_v2.h: 61

# /root/camera_engine_rkaiq/include/iq_parser_v2/bayer2dnr_uapi_head_v2.h: 66
class struct_RK_Bayer2dnr_Params_V2_Select_s(Structure):
    pass

struct_RK_Bayer2dnr_Params_V2_Select_s.__slots__ = [
    'enable',
    'gauss_guide',
    'lumapoint',
    'sigma',
    'filter_strength',
    'edgesofts',
    'ratio',
    'weight',
    'pix_diff',
    'diff_thld',
    'hdrdgain_ctrl_en',
    'hdr_dgain_scale_s',
    'hdr_dgain_scale_m',
]
struct_RK_Bayer2dnr_Params_V2_Select_s._fields_ = [
    ('enable', c_int),
    ('gauss_guide', c_int),
    ('lumapoint', c_int * int(16)),
    ('sigma', c_int * int(16)),
    ('filter_strength', c_float),
    ('edgesofts', c_float),
    ('ratio', c_float),
    ('weight', c_float),
    ('pix_diff', c_int),
    ('diff_thld', c_int),
    ('hdrdgain_ctrl_en', c_bool),
    ('hdr_dgain_scale_s', c_float),
    ('hdr_dgain_scale_m', c_float),
]

RK_Bayer2dnr_Params_V2_Select_t = struct_RK_Bayer2dnr_Params_V2_Select_s# /root/camera_engine_rkaiq/include/iq_parser_v2/bayer2dnr_uapi_head_v2.h: 66

# /root/camera_engine_rkaiq/include/iq_parser_v2/bayer2dnr_uapi_head_v2.h: 107
class struct_RK_Bayer2dnr_Params_V2_s(Structure):
    pass

struct_RK_Bayer2dnr_Params_V2_s.__slots__ = [
    'enable',
    'lumapoint',
    'sigma',
    'iso',
    'filter_strength',
    'edgesofts',
    'ratio',
    'weight',
    'gauss_guide',
    'pix_diff',
    'diff_thld',
    'hdrdgain_ctrl_en',
    'hdr_dgain_scale_s',
    'hdr_dgain_scale_m',
]
struct_RK_Bayer2dnr_Params_V2_s._fields_ = [
    ('enable', c_int),
    ('lumapoint', c_int * int(16)),
    ('sigma', (c_int * int(16)) * int(13)),
    ('iso', c_float * int(13)),
    ('filter_strength', c_float * int(13)),
    ('edgesofts', c_float * int(13)),
    ('ratio', c_float * int(13)),
    ('weight', c_float * int(13)),
    ('gauss_guide', c_int * int(13)),
    ('pix_diff', c_int * int(13)),
    ('diff_thld', c_int * int(13)),
    ('hdrdgain_ctrl_en', c_bool),
    ('hdr_dgain_scale_s', c_float * int(13)),
    ('hdr_dgain_scale_m', c_float * int(13)),
]

RK_Bayer2dnr_Params_V2_t = struct_RK_Bayer2dnr_Params_V2_s# /root/camera_engine_rkaiq/include/iq_parser_v2/bayer2dnr_uapi_head_v2.h: 107

# /root/camera_engine_rkaiq/include/iq_parser_v2/bayer2dnr_uapi_head_v2.h: 134
class struct_Abayer2dnr_ExpInfo_V2_s(Structure):
    pass

struct_Abayer2dnr_ExpInfo_V2_s.__slots__ = [
    'hdr_mode',
    'snr_mode',
    'gray_mode',
    'arTime',
    'arAGain',
    'arDGain',
    'arIso',
    'isoLow',
    'isoHigh',
]
struct_Abayer2dnr_ExpInfo_V2_s._fields_ = [
    ('hdr_mode', c_int),
    ('snr_mode', c_int),
    ('gray_mode', c_int),
    ('arTime', c_float * int(3)),
    ('arAGain', c_float * int(3)),
    ('arDGain', c_float * int(3)),
    ('arIso', c_int * int(3)),
    ('isoLow', c_int),
    ('isoHigh', c_int),
]

Abayer2dnr_ExpInfo_V2_t = struct_Abayer2dnr_ExpInfo_V2_s# /root/camera_engine_rkaiq/include/iq_parser_v2/bayer2dnr_uapi_head_v2.h: 134

# /root/camera_engine_rkaiq/include/iq_parser_v2/bayer2dnr_uapi_head_v2.h: 143
class struct_rk_aiq_bayer2dnr_info_v2_s(Structure):
    pass

struct_rk_aiq_bayer2dnr_info_v2_s.__slots__ = [
    'sync',
    'iso',
    'expo_info',
]
struct_rk_aiq_bayer2dnr_info_v2_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('iso', c_int),
    ('expo_info', Abayer2dnr_ExpInfo_V2_t),
]

rk_aiq_bayer2dnr_info_v2_t = struct_rk_aiq_bayer2dnr_info_v2_s# /root/camera_engine_rkaiq/include/iq_parser_v2/bayer2dnr_uapi_head_v2.h: 143

enum_Abayer2dnr_OPMode_V2_e = c_int# /root/camera_engine_rkaiq/include/algos/abayer2dnr2/rk_aiq_types_abayer2dnr_algo_int_v2.h: 67

Abayer2dnr_OPMode_V2_t = enum_Abayer2dnr_OPMode_V2_e# /root/camera_engine_rkaiq/include/algos/abayer2dnr2/rk_aiq_types_abayer2dnr_algo_int_v2.h: 67

# /root/camera_engine_rkaiq/include/algos/abayer2dnr2/rk_aiq_types_abayer2dnr_algo_int_v2.h: 140
class struct_Abayer2dnr_Manual_Attr_V2_s(Structure):
    pass

struct_Abayer2dnr_Manual_Attr_V2_s.__slots__ = [
    'st2DSelect',
    'st2Dfix',
]
struct_Abayer2dnr_Manual_Attr_V2_s._fields_ = [
    ('st2DSelect', RK_Bayer2dnr_Params_V2_Select_t),
    ('st2Dfix', RK_Bayer2dnr_Fix_V2_t),
]

Abayer2dnr_Manual_Attr_V2_t = struct_Abayer2dnr_Manual_Attr_V2_s# /root/camera_engine_rkaiq/include/algos/abayer2dnr2/rk_aiq_types_abayer2dnr_algo_int_v2.h: 140

# /root/camera_engine_rkaiq/include/algos/abayer2dnr2/rk_aiq_types_abayer2dnr_algo_int_v2.h: 149
class struct_Abayer2dnr_Auto_Attr_V2_s(Structure):
    pass

struct_Abayer2dnr_Auto_Attr_V2_s.__slots__ = [
    'st2DParams',
    'st2DSelect',
]
struct_Abayer2dnr_Auto_Attr_V2_s._fields_ = [
    ('st2DParams', RK_Bayer2dnr_Params_V2_t),
    ('st2DSelect', RK_Bayer2dnr_Params_V2_Select_t),
]

Abayer2dnr_Auto_Attr_V2_t = struct_Abayer2dnr_Auto_Attr_V2_s# /root/camera_engine_rkaiq/include/algos/abayer2dnr2/rk_aiq_types_abayer2dnr_algo_int_v2.h: 149

# /root/camera_engine_rkaiq/include/algos/abayer2dnr2/rk_aiq_types_abayer2dnr_algo_int_v2.h: 176
class struct_rk_aiq_bayer2dnr_attrib_v2_s(Structure):
    pass

struct_rk_aiq_bayer2dnr_attrib_v2_s.__slots__ = [
    'sync',
    'eMode',
    'stAuto',
    'stManual',
]
struct_rk_aiq_bayer2dnr_attrib_v2_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('eMode', Abayer2dnr_OPMode_V2_t),
    ('stAuto', Abayer2dnr_Auto_Attr_V2_t),
    ('stManual', Abayer2dnr_Manual_Attr_V2_t),
]

rk_aiq_bayer2dnr_attrib_v2_t = struct_rk_aiq_bayer2dnr_attrib_v2_s# /root/camera_engine_rkaiq/include/algos/abayer2dnr2/rk_aiq_types_abayer2dnr_algo_int_v2.h: 176

# /root/camera_engine_rkaiq/include/algos/abayer2dnr2/rk_aiq_types_abayer2dnr_algo_int_v2.h: 183
class struct_rk_aiq_bayer2dnr_strength_v2_s(Structure):
    pass

struct_rk_aiq_bayer2dnr_strength_v2_s.__slots__ = [
    'sync',
    'percent',
    'strength_enable',
]
struct_rk_aiq_bayer2dnr_strength_v2_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('percent', c_float),
    ('strength_enable', c_bool),
]

rk_aiq_bayer2dnr_strength_v2_t = struct_rk_aiq_bayer2dnr_strength_v2_s# /root/camera_engine_rkaiq/include/algos/abayer2dnr2/rk_aiq_types_abayer2dnr_algo_int_v2.h: 183

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_abayer2dnr_v2.h: 31
if _libs["rkaiq"].has("rk_aiq_user_api2_abayer2dnrV2_SetAttrib", "cdecl"):
    rk_aiq_user_api2_abayer2dnrV2_SetAttrib = _libs["rkaiq"].get("rk_aiq_user_api2_abayer2dnrV2_SetAttrib", "cdecl")
    rk_aiq_user_api2_abayer2dnrV2_SetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_bayer2dnr_attrib_v2_t)]
    rk_aiq_user_api2_abayer2dnrV2_SetAttrib.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_abayer2dnr_v2.h: 34
if _libs["rkaiq"].has("rk_aiq_user_api2_abayer2dnrV2_GetAttrib", "cdecl"):
    rk_aiq_user_api2_abayer2dnrV2_GetAttrib = _libs["rkaiq"].get("rk_aiq_user_api2_abayer2dnrV2_GetAttrib", "cdecl")
    rk_aiq_user_api2_abayer2dnrV2_GetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_bayer2dnr_attrib_v2_t)]
    rk_aiq_user_api2_abayer2dnrV2_GetAttrib.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_abayer2dnr_v2.h: 37
if _libs["rkaiq"].has("rk_aiq_user_api2_abayer2dnrV2_SetStrength", "cdecl"):
    rk_aiq_user_api2_abayer2dnrV2_SetStrength = _libs["rkaiq"].get("rk_aiq_user_api2_abayer2dnrV2_SetStrength", "cdecl")
    rk_aiq_user_api2_abayer2dnrV2_SetStrength.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_bayer2dnr_strength_v2_t)]
    rk_aiq_user_api2_abayer2dnrV2_SetStrength.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_abayer2dnr_v2.h: 40
if _libs["rkaiq"].has("rk_aiq_user_api2_abayer2dnrV2_GetStrength", "cdecl"):
    rk_aiq_user_api2_abayer2dnrV2_GetStrength = _libs["rkaiq"].get("rk_aiq_user_api2_abayer2dnrV2_GetStrength", "cdecl")
    rk_aiq_user_api2_abayer2dnrV2_GetStrength.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_bayer2dnr_strength_v2_t)]
    rk_aiq_user_api2_abayer2dnrV2_GetStrength.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_abayer2dnr_v2.h: 43
if _libs["rkaiq"].has("rk_aiq_user_api2_abayer2dnrV2_GetInfo", "cdecl"):
    rk_aiq_user_api2_abayer2dnrV2_GetInfo = _libs["rkaiq"].get("rk_aiq_user_api2_abayer2dnrV2_GetInfo", "cdecl")
    rk_aiq_user_api2_abayer2dnrV2_GetInfo.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_bayer2dnr_info_v2_t)]
    rk_aiq_user_api2_abayer2dnrV2_GetInfo.restype = XCamReturn

enum_Abayernr_OPMode_e = c_int# /root/camera_engine_rkaiq/include/algos/arawnr2/rk_aiq_types_abayernr_algo_int_v2.h: 63

Abayernr_OPMode_t = enum_Abayernr_OPMode_e# /root/camera_engine_rkaiq/include/algos/arawnr2/rk_aiq_types_abayernr_algo_int_v2.h: 63

# /root/camera_engine_rkaiq/include/algos/arawnr2/rk_aiq_types_abayernr_algo_int_v2.h: 101
class struct_RK_Bayernr_2D_Params_V2_s(Structure):
    pass

struct_RK_Bayernr_2D_Params_V2_s.__slots__ = [
    'bayernrv2_2dnr_enable',
    'iso',
    'bayernrv2_edge_filter_lumapoint_r',
    'bayernrv2_edge_filter_wgt_r',
    'bayernrv2_filter_strength_r',
    'bayernrv2_filter_lumapoint_r',
    'bayernrv2_filter_sigma_r',
    'bayernrv2_filter_edgesofts_r',
    'bayernrv2_filter_soft_threshold_ratio_r',
    'bayernrv2_filter_out_wgt_r',
    'bayernrv2_gauss_guide_r',
]
struct_RK_Bayernr_2D_Params_V2_s._fields_ = [
    ('bayernrv2_2dnr_enable', c_int),
    ('iso', c_float * int(13)),
    ('bayernrv2_edge_filter_lumapoint_r', c_float * int(8)),
    ('bayernrv2_edge_filter_wgt_r', (c_float * int(8)) * int(13)),
    ('bayernrv2_filter_strength_r', c_float * int(13)),
    ('bayernrv2_filter_lumapoint_r', c_int * int(16)),
    ('bayernrv2_filter_sigma_r', (c_int * int(16)) * int(13)),
    ('bayernrv2_filter_edgesofts_r', c_float * int(13)),
    ('bayernrv2_filter_soft_threshold_ratio_r', c_float * int(13)),
    ('bayernrv2_filter_out_wgt_r', c_float * int(13)),
    ('bayernrv2_gauss_guide_r', c_int * int(13)),
]

RK_Bayernr_2D_Params_V2_t = struct_RK_Bayernr_2D_Params_V2_s# /root/camera_engine_rkaiq/include/algos/arawnr2/rk_aiq_types_abayernr_algo_int_v2.h: 101

# /root/camera_engine_rkaiq/include/algos/arawnr2/rk_aiq_types_abayernr_algo_int_v2.h: 125
class struct_RK_Bayernr_2D_Params_V2_Select_s(Structure):
    pass

struct_RK_Bayernr_2D_Params_V2_Select_s.__slots__ = [
    'bayernrv2_2dnr_enable',
    'bayernrv2_filter_strength',
    'bayernrv2_filter_soft_threshold_ratio',
    'bayernrv2_filter_out_wgt',
    'bayernrv2_filter_edgesofts',
    'bayernrv2_edge_filter_en',
    'bayernrv2_edge_filter_lumapoint',
    'bayernrv2_edge_filter_wgt',
    'bayernrv2_gauss_guide',
    'bayernrv2_filter_lumapoint',
    'bayernrv2_filter_sigma',
    'bayernrv2_bil_gauss_weight',
    'bayernrv2_gray_mode',
    'bayernrv2_dgains',
    'bayernrv2_thld_diff',
    'bayernrv2_pix_diff',
]
struct_RK_Bayernr_2D_Params_V2_Select_s._fields_ = [
    ('bayernrv2_2dnr_enable', c_int),
    ('bayernrv2_filter_strength', c_float),
    ('bayernrv2_filter_soft_threshold_ratio', c_float),
    ('bayernrv2_filter_out_wgt', c_float),
    ('bayernrv2_filter_edgesofts', c_float),
    ('bayernrv2_edge_filter_en', c_int),
    ('bayernrv2_edge_filter_lumapoint', c_int * int(8)),
    ('bayernrv2_edge_filter_wgt', c_int * int(8)),
    ('bayernrv2_gauss_guide', c_int),
    ('bayernrv2_filter_lumapoint', c_int * int(16)),
    ('bayernrv2_filter_sigma', c_int * int(16)),
    ('bayernrv2_bil_gauss_weight', c_int * int(16)),
    ('bayernrv2_gray_mode', c_int),
    ('bayernrv2_dgains', c_int * int(3)),
    ('bayernrv2_thld_diff', c_int),
    ('bayernrv2_pix_diff', c_int),
]

RK_Bayernr_2D_Params_V2_Select_t = struct_RK_Bayernr_2D_Params_V2_Select_s# /root/camera_engine_rkaiq/include/algos/arawnr2/rk_aiq_types_abayernr_algo_int_v2.h: 125

# /root/camera_engine_rkaiq/include/algos/arawnr2/rk_aiq_types_abayernr_algo_int_v2.h: 141
class struct_RK_Bayernr_3D_Params_V2_s(Structure):
    pass

struct_RK_Bayernr_3D_Params_V2_s.__slots__ = [
    'bayernrv2_tnr_enable',
    'iso',
    'bayernrv2_tnr_filter_strength_r',
    'bayernrv2_tnr_lo_clipwgt_r',
    'bayernrv2_tnr_hi_clipwgt_r',
    'bayernrv2_tnr_softwgt_r',
    'bayernrv2_lumapoint_r',
    'bayernrv2_sigma_r',
]
struct_RK_Bayernr_3D_Params_V2_s._fields_ = [
    ('bayernrv2_tnr_enable', c_int),
    ('iso', c_float * int(13)),
    ('bayernrv2_tnr_filter_strength_r', c_float * int(13)),
    ('bayernrv2_tnr_lo_clipwgt_r', c_float * int(13)),
    ('bayernrv2_tnr_hi_clipwgt_r', c_float * int(13)),
    ('bayernrv2_tnr_softwgt_r', c_float * int(13)),
    ('bayernrv2_lumapoint_r', c_int * int(16)),
    ('bayernrv2_sigma_r', (c_int * int(16)) * int(13)),
]

RK_Bayernr_3D_Params_V2_t = struct_RK_Bayernr_3D_Params_V2_s# /root/camera_engine_rkaiq/include/algos/arawnr2/rk_aiq_types_abayernr_algo_int_v2.h: 141

# /root/camera_engine_rkaiq/include/algos/arawnr2/rk_aiq_types_abayernr_algo_int_v2.h: 161
class struct_RK_Bayernr_3D_Params_V2_Select_s(Structure):
    pass

struct_RK_Bayernr_3D_Params_V2_Select_s.__slots__ = [
    'bayernrv2_tnr_enable',
    'bayernrv2_tnr_filter_strength',
    'bayernrv2_tnr_lo_clipwgt',
    'bayernrv2_tnr_hi_clipwgt',
    'bayernrv2_tnr_softwgt',
    'bayernrv2_tnr_sigratio',
    'bayernrv2_tnr_strength',
    'bayernrv2_tnr_global_pk_en',
    'bayernrv2_tnr_global_pksq',
    'bayernrv2_tnr_lumapoint',
    'bayernrv2_tnr_sigma',
]
struct_RK_Bayernr_3D_Params_V2_Select_s._fields_ = [
    ('bayernrv2_tnr_enable', c_int),
    ('bayernrv2_tnr_filter_strength', c_float),
    ('bayernrv2_tnr_lo_clipwgt', c_float),
    ('bayernrv2_tnr_hi_clipwgt', c_float),
    ('bayernrv2_tnr_softwgt', c_float),
    ('bayernrv2_tnr_sigratio', c_int),
    ('bayernrv2_tnr_strength', c_int),
    ('bayernrv2_tnr_global_pk_en', c_int),
    ('bayernrv2_tnr_global_pksq', c_int),
    ('bayernrv2_tnr_lumapoint', c_int * int(16)),
    ('bayernrv2_tnr_sigma', c_int * int(16)),
]

RK_Bayernr_3D_Params_V2_Select_t = struct_RK_Bayernr_3D_Params_V2_Select_s# /root/camera_engine_rkaiq/include/algos/arawnr2/rk_aiq_types_abayernr_algo_int_v2.h: 161

# /root/camera_engine_rkaiq/include/algos/arawnr2/rk_aiq_types_abayernr_algo_int_v2.h: 171
class struct_Abayernr_Manual_Attr_V2_s(Structure):
    pass

struct_Abayernr_Manual_Attr_V2_s.__slots__ = [
    'bayernr2DEn',
    'bayernr3DEn',
    'st2DSelect',
    'st3DSelect',
]
struct_Abayernr_Manual_Attr_V2_s._fields_ = [
    ('bayernr2DEn', c_int),
    ('bayernr3DEn', c_int),
    ('st2DSelect', RK_Bayernr_2D_Params_V2_Select_t),
    ('st3DSelect', RK_Bayernr_3D_Params_V2_Select_t),
]

Abayernr_Manual_Attr_V2_t = struct_Abayernr_Manual_Attr_V2_s# /root/camera_engine_rkaiq/include/algos/arawnr2/rk_aiq_types_abayernr_algo_int_v2.h: 171

# /root/camera_engine_rkaiq/include/algos/arawnr2/rk_aiq_types_abayernr_algo_int_v2.h: 184
class struct_Abayernr_Auto_Attr_V2_s(Structure):
    pass

struct_Abayernr_Auto_Attr_V2_s.__slots__ = [
    'bayernr2DEn',
    'bayernr3DEn',
    'st2DParams',
    'st3DParams',
    'st2DSelect',
    'st3DSelect',
]
struct_Abayernr_Auto_Attr_V2_s._fields_ = [
    ('bayernr2DEn', c_int),
    ('bayernr3DEn', c_int),
    ('st2DParams', RK_Bayernr_2D_Params_V2_t),
    ('st3DParams', RK_Bayernr_3D_Params_V2_t),
    ('st2DSelect', RK_Bayernr_2D_Params_V2_Select_t),
    ('st3DSelect', RK_Bayernr_3D_Params_V2_Select_t),
]

Abayernr_Auto_Attr_V2_t = struct_Abayernr_Auto_Attr_V2_s# /root/camera_engine_rkaiq/include/algos/arawnr2/rk_aiq_types_abayernr_algo_int_v2.h: 184

# /root/camera_engine_rkaiq/include/algos/arawnr2/rk_aiq_types_abayernr_algo_int_v2.h: 213
class struct_rk_aiq_bayernr_attrib_v2_s(Structure):
    pass

struct_rk_aiq_bayernr_attrib_v2_s.__slots__ = [
    'eMode',
    'stAuto',
    'stManual',
]
struct_rk_aiq_bayernr_attrib_v2_s._fields_ = [
    ('eMode', Abayernr_OPMode_t),
    ('stAuto', Abayernr_Auto_Attr_V2_t),
    ('stManual', Abayernr_Manual_Attr_V2_t),
]

rk_aiq_bayernr_attrib_v2_t = struct_rk_aiq_bayernr_attrib_v2_s# /root/camera_engine_rkaiq/include/algos/arawnr2/rk_aiq_types_abayernr_algo_int_v2.h: 213

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_abayernr_v2.h: 32
if _libs["rkaiq"].has("rk_aiq_user_api2_abayernrV2_SetAttrib", "cdecl"):
    rk_aiq_user_api2_abayernrV2_SetAttrib = _libs["rkaiq"].get("rk_aiq_user_api2_abayernrV2_SetAttrib", "cdecl")
    rk_aiq_user_api2_abayernrV2_SetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_bayernr_attrib_v2_t)]
    rk_aiq_user_api2_abayernrV2_SetAttrib.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_abayernr_v2.h: 35
if _libs["rkaiq"].has("rk_aiq_user_api2_abayernrV2_GetAttrib", "cdecl"):
    rk_aiq_user_api2_abayernrV2_GetAttrib = _libs["rkaiq"].get("rk_aiq_user_api2_abayernrV2_GetAttrib", "cdecl")
    rk_aiq_user_api2_abayernrV2_GetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_bayernr_attrib_v2_t)]
    rk_aiq_user_api2_abayernrV2_GetAttrib.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_abayernr_v2.h: 38
if _libs["rkaiq"].has("rk_aiq_user_api2_abayernrV2_SetSFStrength", "cdecl"):
    rk_aiq_user_api2_abayernrV2_SetSFStrength = _libs["rkaiq"].get("rk_aiq_user_api2_abayernrV2_SetSFStrength", "cdecl")
    rk_aiq_user_api2_abayernrV2_SetSFStrength.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_float]
    rk_aiq_user_api2_abayernrV2_SetSFStrength.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_abayernr_v2.h: 41
if _libs["rkaiq"].has("rk_aiq_user_api2_abayernrV2_SetTFStrength", "cdecl"):
    rk_aiq_user_api2_abayernrV2_SetTFStrength = _libs["rkaiq"].get("rk_aiq_user_api2_abayernrV2_SetTFStrength", "cdecl")
    rk_aiq_user_api2_abayernrV2_SetTFStrength.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_float]
    rk_aiq_user_api2_abayernrV2_SetTFStrength.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_abayernr_v2.h: 44
if _libs["rkaiq"].has("rk_aiq_user_api2_abayernrV2_GetSFStrength", "cdecl"):
    rk_aiq_user_api2_abayernrV2_GetSFStrength = _libs["rkaiq"].get("rk_aiq_user_api2_abayernrV2_GetSFStrength", "cdecl")
    rk_aiq_user_api2_abayernrV2_GetSFStrength.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(c_float)]
    rk_aiq_user_api2_abayernrV2_GetSFStrength.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_abayernr_v2.h: 47
if _libs["rkaiq"].has("rk_aiq_user_api2_abayernrV2_GetTFStrength", "cdecl"):
    rk_aiq_user_api2_abayernrV2_GetTFStrength = _libs["rkaiq"].get("rk_aiq_user_api2_abayernrV2_GetTFStrength", "cdecl")
    rk_aiq_user_api2_abayernrV2_GetTFStrength.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(c_float)]
    rk_aiq_user_api2_abayernrV2_GetTFStrength.restype = XCamReturn

# /root/camera_engine_rkaiq/include/algos/abayertnr2/rk_aiq_types_abayertnr_hw_v2.h: 88
class struct_RK_Bayertnr_Fix_V2_s(Structure):
    pass

struct_RK_Bayertnr_Fix_V2_s.__slots__ = [
    'bay3d_exp_sel',
    'bay3d_soft_st',
    'bay3d_soft_mode',
    'bay3d_bwsaving_en',
    'bay3d_loswitch_protect',
    'bay3d_glbpk_en',
    'bay3d_logaus3_bypass_en',
    'bay3d_logaus5_bypass_en',
    'bay3d_lomed_bypass_en',
    'bay3d_hichnsplit_en',
    'bay3d_hiabs_pssel',
    'bay3d_higaus_bypass_en',
    'bay3d_himed_bypass_en',
    'bay3d_lobypass_en',
    'bay3d_hibypass_en',
    'bay3d_bypass_en',
    'bay3d_en_i',
    'bay3d_softwgt',
    'bay3d_hidif_th',
    'bay3d_glbpk2',
    'bay3d_wgtlmt',
    'bay3d_wgtratio',
    'bay3d_sig0_x',
    'bay3d_sig0_y',
    'bay3d_sig1_x',
    'bay3d_sig1_y',
    'bay3d_sig2_y',
    'ro_sum_lodif',
    'ro_sum_hidif0',
    'sw_bay3dmi_st_linemode',
    'sw_bay3d_mi2cur_linecnt',
]
struct_RK_Bayertnr_Fix_V2_s._fields_ = [
    ('bay3d_exp_sel', uint8_t),
    ('bay3d_soft_st', uint8_t),
    ('bay3d_soft_mode', uint8_t),
    ('bay3d_bwsaving_en', uint8_t),
    ('bay3d_loswitch_protect', uint8_t),
    ('bay3d_glbpk_en', uint8_t),
    ('bay3d_logaus3_bypass_en', uint8_t),
    ('bay3d_logaus5_bypass_en', uint8_t),
    ('bay3d_lomed_bypass_en', uint8_t),
    ('bay3d_hichnsplit_en', uint8_t),
    ('bay3d_hiabs_pssel', uint8_t),
    ('bay3d_higaus_bypass_en', uint8_t),
    ('bay3d_himed_bypass_en', uint8_t),
    ('bay3d_lobypass_en', uint8_t),
    ('bay3d_hibypass_en', uint8_t),
    ('bay3d_bypass_en', uint8_t),
    ('bay3d_en_i', uint8_t),
    ('bay3d_softwgt', uint16_t),
    ('bay3d_hidif_th', uint16_t),
    ('bay3d_glbpk2', uint32_t),
    ('bay3d_wgtlmt', uint16_t),
    ('bay3d_wgtratio', uint16_t),
    ('bay3d_sig0_x', uint16_t * int(16)),
    ('bay3d_sig0_y', uint16_t * int(16)),
    ('bay3d_sig1_x', uint16_t * int(16)),
    ('bay3d_sig1_y', uint16_t * int(16)),
    ('bay3d_sig2_y', uint16_t * int(16)),
    ('ro_sum_lodif', uint64_t),
    ('ro_sum_hidif0', uint64_t),
    ('sw_bay3dmi_st_linemode', uint8_t),
    ('sw_bay3d_mi2cur_linecnt', uint8_t),
]

RK_Bayertnr_Fix_V2_t = struct_RK_Bayertnr_Fix_V2_s# /root/camera_engine_rkaiq/include/algos/abayertnr2/rk_aiq_types_abayertnr_hw_v2.h: 88

# /root/camera_engine_rkaiq/include/iq_parser_v2/bayertnr_uapi_head_v2.h: 81
class struct_RK_Bayertnr_Params_V2_Select_s(Structure):
    pass

struct_RK_Bayertnr_Params_V2_Select_s.__slots__ = [
    'enable',
    'lo_enable',
    'hi_enable',
    'lo_med_en',
    'lo_gsbay_en',
    'lo_gslum_en',
    'hi_med_en',
    'hi_gslum_en',
    'lumapoint',
    'sigma',
    'lumapoint2',
    'lo_sigma',
    'hi_sigma',
    'thumbds',
    'global_pk_en',
    'global_pksq',
    'lo_filter_strength',
    'hi_filter_strength',
    'soft_threshold_ratio',
    'clipwgt',
    'hi_wgt_comp',
    'hidif_th',
]
struct_RK_Bayertnr_Params_V2_Select_s._fields_ = [
    ('enable', c_int),
    ('lo_enable', c_int),
    ('hi_enable', c_int),
    ('lo_med_en', c_int),
    ('lo_gsbay_en', c_int),
    ('lo_gslum_en', c_int),
    ('hi_med_en', c_int),
    ('hi_gslum_en', c_int),
    ('lumapoint', c_int * int(16)),
    ('sigma', c_int * int(16)),
    ('lumapoint2', c_int * int(16)),
    ('lo_sigma', c_int * int(16)),
    ('hi_sigma', c_int * int(16)),
    ('thumbds', c_int),
    ('global_pk_en', c_int),
    ('global_pksq', c_int),
    ('lo_filter_strength', c_float),
    ('hi_filter_strength', c_float),
    ('soft_threshold_ratio', c_float),
    ('clipwgt', c_float),
    ('hi_wgt_comp', c_float),
    ('hidif_th', c_float),
]

RK_Bayertnr_Params_V2_Select_t = struct_RK_Bayertnr_Params_V2_Select_s# /root/camera_engine_rkaiq/include/iq_parser_v2/bayertnr_uapi_head_v2.h: 81

# /root/camera_engine_rkaiq/include/iq_parser_v2/bayertnr_uapi_head_v2.h: 106
class struct_Abayertnr_ExpInfo_V2_s(Structure):
    pass

struct_Abayertnr_ExpInfo_V2_s.__slots__ = [
    'hdr_mode',
    'snr_mode',
    'arTime',
    'arAGain',
    'arDGain',
    'arIso',
    'isoLow',
    'isoHigh',
]
struct_Abayertnr_ExpInfo_V2_s._fields_ = [
    ('hdr_mode', c_int),
    ('snr_mode', c_int),
    ('arTime', c_float * int(3)),
    ('arAGain', c_float * int(3)),
    ('arDGain', c_float * int(3)),
    ('arIso', c_int * int(3)),
    ('isoLow', c_int),
    ('isoHigh', c_int),
]

Abayertnr_ExpInfo_V2_t = struct_Abayertnr_ExpInfo_V2_s# /root/camera_engine_rkaiq/include/iq_parser_v2/bayertnr_uapi_head_v2.h: 106

# /root/camera_engine_rkaiq/include/iq_parser_v2/bayertnr_uapi_head_v2.h: 116
class struct_rk_aiq_bayertnr_info_v2_s(Structure):
    pass

struct_rk_aiq_bayertnr_info_v2_s.__slots__ = [
    'sync',
    'iso',
    'expo_info',
]
struct_rk_aiq_bayertnr_info_v2_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('iso', c_int),
    ('expo_info', Abayertnr_ExpInfo_V2_t),
]

rk_aiq_bayertnr_info_v2_t = struct_rk_aiq_bayertnr_info_v2_s# /root/camera_engine_rkaiq/include/iq_parser_v2/bayertnr_uapi_head_v2.h: 116

enum_Abayertnr_OPMode_V2_e = c_int# /root/camera_engine_rkaiq/include/algos/abayertnr2/rk_aiq_types_abayertnr_algo_int_v2.h: 66

Abayertnr_OPMode_V2_t = enum_Abayertnr_OPMode_V2_e# /root/camera_engine_rkaiq/include/algos/abayertnr2/rk_aiq_types_abayertnr_algo_int_v2.h: 66

# /root/camera_engine_rkaiq/include/algos/abayertnr2/rk_aiq_types_abayertnr_algo_int_v2.h: 111
class struct_RK_Bayertnr_Params_V2_s(Structure):
    pass

struct_RK_Bayertnr_Params_V2_s.__slots__ = [
    'enable',
    'iso',
    'lumapoint',
    'sigma',
    'lumapoint2',
    'lo_sigma',
    'hi_sigma',
    'thumbds',
    'lo_enable',
    'hi_enable',
    'lo_med_en',
    'lo_gsbay_en',
    'lo_gslum_en',
    'hi_med_en',
    'hi_gslum_en',
    'global_pk_en',
    'global_pksq',
    'lo_filter_strength',
    'hi_filter_strength',
    'soft_threshold_ratio',
    'hi_wgt_comp',
    'clipwgt',
    'hidif_th',
]
struct_RK_Bayertnr_Params_V2_s._fields_ = [
    ('enable', c_int),
    ('iso', c_float * int(13)),
    ('lumapoint', c_int * int(16)),
    ('sigma', (c_int * int(16)) * int(13)),
    ('lumapoint2', c_int * int(16)),
    ('lo_sigma', (c_int * int(16)) * int(13)),
    ('hi_sigma', (c_int * int(16)) * int(13)),
    ('thumbds', c_int * int(13)),
    ('lo_enable', c_int * int(13)),
    ('hi_enable', c_int * int(13)),
    ('lo_med_en', c_int * int(13)),
    ('lo_gsbay_en', c_int * int(13)),
    ('lo_gslum_en', c_int * int(13)),
    ('hi_med_en', c_int * int(13)),
    ('hi_gslum_en', c_int * int(13)),
    ('global_pk_en', c_int * int(13)),
    ('global_pksq', c_int * int(13)),
    ('lo_filter_strength', c_float * int(13)),
    ('hi_filter_strength', c_float * int(13)),
    ('soft_threshold_ratio', c_float * int(13)),
    ('hi_wgt_comp', c_float * int(13)),
    ('clipwgt', c_float * int(13)),
    ('hidif_th', c_float * int(13)),
]

RK_Bayertnr_Params_V2_t = struct_RK_Bayertnr_Params_V2_s# /root/camera_engine_rkaiq/include/algos/abayertnr2/rk_aiq_types_abayertnr_algo_int_v2.h: 111

# /root/camera_engine_rkaiq/include/algos/abayertnr2/rk_aiq_types_abayertnr_algo_int_v2.h: 152
class struct_Abayertnr_Manual_Attr_V2_s(Structure):
    pass

struct_Abayertnr_Manual_Attr_V2_s.__slots__ = [
    'st3DSelect',
    'st3DFix',
]
struct_Abayertnr_Manual_Attr_V2_s._fields_ = [
    ('st3DSelect', RK_Bayertnr_Params_V2_Select_t),
    ('st3DFix', RK_Bayertnr_Fix_V2_t),
]

Abayertnr_Manual_Attr_V2_t = struct_Abayertnr_Manual_Attr_V2_s# /root/camera_engine_rkaiq/include/algos/abayertnr2/rk_aiq_types_abayertnr_algo_int_v2.h: 152

# /root/camera_engine_rkaiq/include/algos/abayertnr2/rk_aiq_types_abayertnr_algo_int_v2.h: 161
class struct_Abayertnr_Auto_Attr_V2_s(Structure):
    pass

struct_Abayertnr_Auto_Attr_V2_s.__slots__ = [
    'st3DParams',
    'st3DSelect',
]
struct_Abayertnr_Auto_Attr_V2_s._fields_ = [
    ('st3DParams', RK_Bayertnr_Params_V2_t),
    ('st3DSelect', RK_Bayertnr_Params_V2_Select_t),
]

Abayertnr_Auto_Attr_V2_t = struct_Abayertnr_Auto_Attr_V2_s# /root/camera_engine_rkaiq/include/algos/abayertnr2/rk_aiq_types_abayertnr_algo_int_v2.h: 161

# /root/camera_engine_rkaiq/include/algos/abayertnr2/rk_aiq_types_abayertnr_algo_int_v2.h: 187
class struct_rk_aiq_bayertnr_attrib_v2_s(Structure):
    pass

struct_rk_aiq_bayertnr_attrib_v2_s.__slots__ = [
    'sync',
    'eMode',
    'stAuto',
    'stManual',
]
struct_rk_aiq_bayertnr_attrib_v2_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('eMode', Abayertnr_OPMode_V2_t),
    ('stAuto', Abayertnr_Auto_Attr_V2_t),
    ('stManual', Abayertnr_Manual_Attr_V2_t),
]

rk_aiq_bayertnr_attrib_v2_t = struct_rk_aiq_bayertnr_attrib_v2_s# /root/camera_engine_rkaiq/include/algos/abayertnr2/rk_aiq_types_abayertnr_algo_int_v2.h: 187

# /root/camera_engine_rkaiq/include/algos/abayertnr2/rk_aiq_types_abayertnr_algo_int_v2.h: 193
class struct_rk_aiq_bayertnr_strength_v2_s(Structure):
    pass

struct_rk_aiq_bayertnr_strength_v2_s.__slots__ = [
    'sync',
    'percent',
    'strength_enable',
]
struct_rk_aiq_bayertnr_strength_v2_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('percent', c_float),
    ('strength_enable', c_bool),
]

rk_aiq_bayertnr_strength_v2_t = struct_rk_aiq_bayertnr_strength_v2_s# /root/camera_engine_rkaiq/include/algos/abayertnr2/rk_aiq_types_abayertnr_algo_int_v2.h: 193

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_abayertnr_v2.h: 31
if _libs["rkaiq"].has("rk_aiq_user_api2_abayertnrV2_SetAttrib", "cdecl"):
    rk_aiq_user_api2_abayertnrV2_SetAttrib = _libs["rkaiq"].get("rk_aiq_user_api2_abayertnrV2_SetAttrib", "cdecl")
    rk_aiq_user_api2_abayertnrV2_SetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_bayertnr_attrib_v2_t)]
    rk_aiq_user_api2_abayertnrV2_SetAttrib.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_abayertnr_v2.h: 34
if _libs["rkaiq"].has("rk_aiq_user_api2_abayertnrV2_GetAttrib", "cdecl"):
    rk_aiq_user_api2_abayertnrV2_GetAttrib = _libs["rkaiq"].get("rk_aiq_user_api2_abayertnrV2_GetAttrib", "cdecl")
    rk_aiq_user_api2_abayertnrV2_GetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_bayertnr_attrib_v2_t)]
    rk_aiq_user_api2_abayertnrV2_GetAttrib.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_abayertnr_v2.h: 37
if _libs["rkaiq"].has("rk_aiq_user_api2_abayertnrV2_SetStrength", "cdecl"):
    rk_aiq_user_api2_abayertnrV2_SetStrength = _libs["rkaiq"].get("rk_aiq_user_api2_abayertnrV2_SetStrength", "cdecl")
    rk_aiq_user_api2_abayertnrV2_SetStrength.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_bayertnr_strength_v2_t)]
    rk_aiq_user_api2_abayertnrV2_SetStrength.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_abayertnr_v2.h: 40
if _libs["rkaiq"].has("rk_aiq_user_api2_abayertnrV2_GetStrength", "cdecl"):
    rk_aiq_user_api2_abayertnrV2_GetStrength = _libs["rkaiq"].get("rk_aiq_user_api2_abayertnrV2_GetStrength", "cdecl")
    rk_aiq_user_api2_abayertnrV2_GetStrength.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_bayertnr_strength_v2_t)]
    rk_aiq_user_api2_abayertnrV2_GetStrength.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_abayertnr_v2.h: 43
if _libs["rkaiq"].has("rk_aiq_user_api2_abayertnrV2_GetInfo", "cdecl"):
    rk_aiq_user_api2_abayertnrV2_GetInfo = _libs["rkaiq"].get("rk_aiq_user_api2_abayertnrV2_GetInfo", "cdecl")
    rk_aiq_user_api2_abayertnrV2_GetInfo.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_bayertnr_info_v2_t)]
    rk_aiq_user_api2_abayertnrV2_GetInfo.restype = XCamReturn

# /root/camera_engine_rkaiq/include/iq_parser_v2/ablc_uapi_head.h: 40
class struct_AblcSelect_s(Structure):
    pass

struct_AblcSelect_s.__slots__ = [
    'enable',
    'blc_r',
    'blc_gr',
    'blc_gb',
    'blc_b',
]
struct_AblcSelect_s._fields_ = [
    ('enable', c_bool),
    ('blc_r', c_float),
    ('blc_gr', c_float),
    ('blc_gb', c_float),
    ('blc_b', c_float),
]

AblcSelect_t = struct_AblcSelect_s# /root/camera_engine_rkaiq/include/iq_parser_v2/ablc_uapi_head.h: 40

AblcManualAttr_t = AblcSelect_t# /root/camera_engine_rkaiq/include/iq_parser_v2/ablc_uapi_head.h: 42

# /root/camera_engine_rkaiq/include/iq_parser_v2/ablc_uapi_head.h: 61
class struct_AblcExpInfo_s(Structure):
    pass

struct_AblcExpInfo_s.__slots__ = [
    'hdr_mode',
    'arTime',
    'arAGain',
    'arDGain',
    'arIso',
    'isoLow',
    'isoHigh',
]
struct_AblcExpInfo_s._fields_ = [
    ('hdr_mode', c_int),
    ('arTime', c_float * int(3)),
    ('arAGain', c_float * int(3)),
    ('arDGain', c_float * int(3)),
    ('arIso', c_int * int(3)),
    ('isoLow', c_int),
    ('isoHigh', c_int),
]

AblcExpInfo_t = struct_AblcExpInfo_s# /root/camera_engine_rkaiq/include/iq_parser_v2/ablc_uapi_head.h: 61

# /root/camera_engine_rkaiq/include/iq_parser_v2/ablc_uapi_head.h: 70
class struct_rk_aiq_ablc_info_s(Structure):
    pass

struct_rk_aiq_ablc_info_s.__slots__ = [
    'sync',
    'iso',
    'expo_info',
]
struct_rk_aiq_ablc_info_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('iso', c_int),
    ('expo_info', AblcExpInfo_t),
]

rk_aiq_ablc_info_t = struct_rk_aiq_ablc_info_s# /root/camera_engine_rkaiq/include/iq_parser_v2/ablc_uapi_head.h: 70

enum_AblcOPMode_e = c_int# /root/camera_engine_rkaiq/include/algos/ablc/rk_aiq_types_ablc_algo_int.h: 59

AblcOPMode_t = enum_AblcOPMode_e# /root/camera_engine_rkaiq/include/algos/ablc/rk_aiq_types_ablc_algo_int.h: 59

# /root/camera_engine_rkaiq/include/algos/ablc/rk_aiq_types_ablc_algo_int.h: 76
class struct_AblcParams_s(Structure):
    pass

struct_AblcParams_s.__slots__ = [
    'enable',
    'len',
    'iso',
    'blc_r',
    'blc_gr',
    'blc_gb',
    'blc_b',
]
struct_AblcParams_s._fields_ = [
    ('enable', c_bool),
    ('len', c_int),
    ('iso', POINTER(c_float)),
    ('blc_r', POINTER(c_float)),
    ('blc_gr', POINTER(c_float)),
    ('blc_gb', POINTER(c_float)),
    ('blc_b', POINTER(c_float)),
]

AblcParams_t = struct_AblcParams_s# /root/camera_engine_rkaiq/include/algos/ablc/rk_aiq_types_ablc_algo_int.h: 76

# /root/camera_engine_rkaiq/include/algos/ablc/rk_aiq_types_ablc_algo_int.h: 118
class struct_rk_aiq_blc_attrib_s(Structure):
    pass

struct_rk_aiq_blc_attrib_s.__slots__ = [
    'sync',
    'eMode',
    'stBlc0Auto',
    'stBlc1Auto',
    'stBlc0Manual',
    'stBlc1Manual',
]
struct_rk_aiq_blc_attrib_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('eMode', AblcOPMode_t),
    ('stBlc0Auto', AblcParams_t),
    ('stBlc1Auto', AblcParams_t),
    ('stBlc0Manual', AblcManualAttr_t),
    ('stBlc1Manual', AblcManualAttr_t),
]

rk_aiq_blc_attrib_t = struct_rk_aiq_blc_attrib_s# /root/camera_engine_rkaiq/include/algos/ablc/rk_aiq_types_ablc_algo_int.h: 118

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_ablc.h: 31
if _libs["rkaiq"].has("rk_aiq_user_api2_ablc_SetAttrib", "cdecl"):
    rk_aiq_user_api2_ablc_SetAttrib = _libs["rkaiq"].get("rk_aiq_user_api2_ablc_SetAttrib", "cdecl")
    rk_aiq_user_api2_ablc_SetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_blc_attrib_t)]
    rk_aiq_user_api2_ablc_SetAttrib.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_ablc.h: 33
if _libs["rkaiq"].has("rk_aiq_user_api2_ablc_GetAttrib", "cdecl"):
    rk_aiq_user_api2_ablc_GetAttrib = _libs["rkaiq"].get("rk_aiq_user_api2_ablc_GetAttrib", "cdecl")
    rk_aiq_user_api2_ablc_GetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_blc_attrib_t)]
    rk_aiq_user_api2_ablc_GetAttrib.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_ablc.h: 35
if _libs["rkaiq"].has("rk_aiq_user_api2_ablc_GetInfo", "cdecl"):
    rk_aiq_user_api2_ablc_GetInfo = _libs["rkaiq"].get("rk_aiq_user_api2_ablc_GetInfo", "cdecl")
    rk_aiq_user_api2_ablc_GetInfo.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_ablc_info_t)]
    rk_aiq_user_api2_ablc_GetInfo.restype = XCamReturn

# /root/camera_engine_rkaiq/include/algos/accm/rk_aiq_types_accm_algo.h: 32
class struct_rk_aiq_ccm_matrix_s(Structure):
    pass

struct_rk_aiq_ccm_matrix_s.__slots__ = [
    'ccMatrix',
    'ccOffsets',
]
struct_rk_aiq_ccm_matrix_s._fields_ = [
    ('ccMatrix', c_float * int(9)),
    ('ccOffsets', c_float * int(3)),
]

rk_aiq_ccm_matrix_t = struct_rk_aiq_ccm_matrix_s# /root/camera_engine_rkaiq/include/algos/accm/rk_aiq_types_accm_algo.h: 32

enum_rk_aiq_ccm_op_mode_s = c_int# /root/camera_engine_rkaiq/include/algos/accm/rk_aiq_types_accm_ext.h: 32

rk_aiq_ccm_op_mode_t = enum_rk_aiq_ccm_op_mode_s# /root/camera_engine_rkaiq/include/algos/accm/rk_aiq_types_accm_ext.h: 32

# /root/camera_engine_rkaiq/include/algos/accm/rk_aiq_types_accm_ext.h: 39
class struct_rk_aiq_ccm_color_inhibition_s(Structure):
    pass

struct_rk_aiq_ccm_color_inhibition_s.__slots__ = [
    'sensorGain',
    'level',
]
struct_rk_aiq_ccm_color_inhibition_s._fields_ = [
    ('sensorGain', c_float * int(4)),
    ('level', c_float * int(4)),
]

rk_aiq_ccm_color_inhibition_t = struct_rk_aiq_ccm_color_inhibition_s# /root/camera_engine_rkaiq/include/algos/accm/rk_aiq_types_accm_ext.h: 39

# /root/camera_engine_rkaiq/include/algos/accm/rk_aiq_types_accm_ext.h: 46
class struct_rk_aiq_ccm_color_saturation_s(Structure):
    pass

struct_rk_aiq_ccm_color_saturation_s.__slots__ = [
    'sensorGain',
    'level',
]
struct_rk_aiq_ccm_color_saturation_s._fields_ = [
    ('sensorGain', c_float * int(4)),
    ('level', c_float * int(4)),
]

rk_aiq_ccm_color_saturation_t = struct_rk_aiq_ccm_color_saturation_s# /root/camera_engine_rkaiq/include/algos/accm/rk_aiq_types_accm_ext.h: 46

# /root/camera_engine_rkaiq/include/algos/accm/rk_aiq_types_accm_ext.h: 53
class struct_rk_aiq_ccm_accm_attrib_s(Structure):
    pass

struct_rk_aiq_ccm_accm_attrib_s.__slots__ = [
    'color_inhibition',
    'color_saturation',
]
struct_rk_aiq_ccm_accm_attrib_s._fields_ = [
    ('color_inhibition', rk_aiq_ccm_color_inhibition_t),
    ('color_saturation', rk_aiq_ccm_color_saturation_t),
]

rk_aiq_ccm_accm_attrib_t = struct_rk_aiq_ccm_accm_attrib_s# /root/camera_engine_rkaiq/include/algos/accm/rk_aiq_types_accm_ext.h: 53

# /root/camera_engine_rkaiq/include/algos/accm/rk_aiq_types_accm_ext.h: 64
class struct_rk_aiq_ccm_mccm_attrib_s(Structure):
    pass

struct_rk_aiq_ccm_mccm_attrib_s.__slots__ = [
    'ccMatrix',
    'ccOffsets',
    'y_alpha_curve',
    'low_bound_pos_bit',
]
struct_rk_aiq_ccm_mccm_attrib_s._fields_ = [
    ('ccMatrix', c_float * int(9)),
    ('ccOffsets', c_float * int(3)),
    ('y_alpha_curve', c_float * int(17)),
    ('low_bound_pos_bit', c_float),
]

rk_aiq_ccm_mccm_attrib_t = struct_rk_aiq_ccm_mccm_attrib_s# /root/camera_engine_rkaiq/include/algos/accm/rk_aiq_types_accm_ext.h: 64

# /root/camera_engine_rkaiq/include/algos/accm/rk_aiq_types_accm_algo_int.h: 46
class struct_rk_aiq_ccm_attrib_s(Structure):
    pass

struct_rk_aiq_ccm_attrib_s.__slots__ = [
    'sync',
    'byPass',
    'mode',
    'stManual',
    'stAuto',
]
struct_rk_aiq_ccm_attrib_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('byPass', c_bool),
    ('mode', rk_aiq_ccm_op_mode_t),
    ('stManual', rk_aiq_ccm_mccm_attrib_t),
    ('stAuto', rk_aiq_ccm_accm_attrib_t),
]

rk_aiq_ccm_attrib_t = struct_rk_aiq_ccm_attrib_s# /root/camera_engine_rkaiq/include/algos/accm/rk_aiq_types_accm_algo_int.h: 46

# /root/camera_engine_rkaiq/include/algos/accm/rk_aiq_types_accm_algo_int.h: 66
class struct_rk_aiq_ccm_querry_info_s(Structure):
    pass

struct_rk_aiq_ccm_querry_info_s.__slots__ = [
    'ccm_en',
    'ccMatrix',
    'ccOffsets',
    'y_alpha_curve',
    'low_bound_pos_bit',
    'color_inhibition_level',
    'color_saturation_level',
    'finalSat',
    'ccmname1',
    'ccmname2',
]
struct_rk_aiq_ccm_querry_info_s._fields_ = [
    ('ccm_en', c_bool),
    ('ccMatrix', c_float * int(9)),
    ('ccOffsets', c_float * int(3)),
    ('y_alpha_curve', c_float * int(17)),
    ('low_bound_pos_bit', c_float),
    ('color_inhibition_level', c_float),
    ('color_saturation_level', c_float),
    ('finalSat', c_float),
    ('ccmname1', c_char * int(25)),
    ('ccmname2', c_char * int(25)),
]

rk_aiq_ccm_querry_info_t = struct_rk_aiq_ccm_querry_info_s# /root/camera_engine_rkaiq/include/algos/accm/rk_aiq_types_accm_algo_int.h: 66

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_accm.h: 30
if _libs["rkaiq"].has("rk_aiq_user_api2_accm_SetAttrib", "cdecl"):
    rk_aiq_user_api2_accm_SetAttrib = _libs["rkaiq"].get("rk_aiq_user_api2_accm_SetAttrib", "cdecl")
    rk_aiq_user_api2_accm_SetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), rk_aiq_ccm_attrib_t]
    rk_aiq_user_api2_accm_SetAttrib.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_accm.h: 32
if _libs["rkaiq"].has("rk_aiq_user_api2_accm_GetAttrib", "cdecl"):
    rk_aiq_user_api2_accm_GetAttrib = _libs["rkaiq"].get("rk_aiq_user_api2_accm_GetAttrib", "cdecl")
    rk_aiq_user_api2_accm_GetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_ccm_attrib_t)]
    rk_aiq_user_api2_accm_GetAttrib.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_accm.h: 34
if _libs["rkaiq"].has("rk_aiq_user_api2_accm_QueryCcmInfo", "cdecl"):
    rk_aiq_user_api2_accm_QueryCcmInfo = _libs["rkaiq"].get("rk_aiq_user_api2_accm_QueryCcmInfo", "cdecl")
    rk_aiq_user_api2_accm_QueryCcmInfo.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_ccm_querry_info_t)]
    rk_aiq_user_api2_accm_QueryCcmInfo.restype = XCamReturn

# /root/camera_engine_rkaiq/include/iq_parser_v2/cgc_head.h: 34
class struct___cgc_param(Structure):
    pass

struct___cgc_param.__slots__ = [
    'op_mode',
    'cgc_ratio_en',
    'cgc_yuv_limit',
]
struct___cgc_param._fields_ = [
    ('op_mode', RKAiqOPMode_t),
    ('cgc_ratio_en', c_bool),
    ('cgc_yuv_limit', c_bool),
]

Cgc_Param_t = struct___cgc_param# /root/camera_engine_rkaiq/include/iq_parser_v2/cgc_head.h: 34

rk_aiq_acgc_params_t = Cgc_Param_t# /root/camera_engine_rkaiq/include/algos/acgc/rk_aiq_types_acgc_algo.h: 25

# /root/camera_engine_rkaiq/include/algos/acgc/rk_aiq_uapi_acgc_int.h: 37
class struct_rk_aiq_uapi_acgc_attrib_s(Structure):
    pass

struct_rk_aiq_uapi_acgc_attrib_s.__slots__ = [
    'sync',
    'param',
]
struct_rk_aiq_uapi_acgc_attrib_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('param', rk_aiq_acgc_params_t),
]

rk_aiq_uapi_acgc_attrib_t = struct_rk_aiq_uapi_acgc_attrib_s# /root/camera_engine_rkaiq/include/algos/acgc/rk_aiq_uapi_acgc_int.h: 37

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_acgc.h: 27
if _libs["rkaiq"].has("rk_aiq_user_api2_acgc_SetAttrib", "cdecl"):
    rk_aiq_user_api2_acgc_SetAttrib = _libs["rkaiq"].get("rk_aiq_user_api2_acgc_SetAttrib", "cdecl")
    rk_aiq_user_api2_acgc_SetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), rk_aiq_uapi_acgc_attrib_t]
    rk_aiq_user_api2_acgc_SetAttrib.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_acgc.h: 29
if _libs["rkaiq"].has("rk_aiq_user_api2_acgc_GetAttrib", "cdecl"):
    rk_aiq_user_api2_acgc_GetAttrib = _libs["rkaiq"].get("rk_aiq_user_api2_acgc_GetAttrib", "cdecl")
    rk_aiq_user_api2_acgc_GetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_uapi_acgc_attrib_t)]
    rk_aiq_user_api2_acgc_GetAttrib.restype = XCamReturn

enum_Acnr_OPMode_e = c_int# /root/camera_engine_rkaiq/include/algos/acnr/rk_aiq_types_acnr_algo_int_v1.h: 90

Acnr_OPMode_t = enum_Acnr_OPMode_e# /root/camera_engine_rkaiq/include/algos/acnr/rk_aiq_types_acnr_algo_int_v1.h: 90

# /root/camera_engine_rkaiq/include/algos/acnr/rk_aiq_types_acnr_algo_int_v1.h: 153
class struct_RK_CNR_Params_V1_s(Structure):
    pass

struct_RK_CNR_Params_V1_s.__slots__ = [
    'enable',
    'iso',
    'rkcnr_hq_bila_bypass',
    'rkcnr_lq_bila_bypass',
    'rkcnr_exgain',
    'rkcnr_g_gain',
    'ratio',
    'offset',
    'medRatio1',
    'sigmaR1',
    'uvgain1',
    'bfRatio1',
    'hbf_wgt_clip',
    'medRatio2',
    'sigmaR2',
    'uvgain2',
    'sigmaR3',
    'uvgain3',
    'bfRatio3',
    'kernel_5x5_table',
]
struct_RK_CNR_Params_V1_s._fields_ = [
    ('enable', c_int),
    ('iso', c_float * int(13)),
    ('rkcnr_hq_bila_bypass', c_int * int(13)),
    ('rkcnr_lq_bila_bypass', c_int * int(13)),
    ('rkcnr_exgain', c_float * int(13)),
    ('rkcnr_g_gain', c_float * int(13)),
    ('ratio', c_float * int(13)),
    ('offset', c_float * int(13)),
    ('medRatio1', c_float * int(13)),
    ('sigmaR1', c_float * int(13)),
    ('uvgain1', c_float * int(13)),
    ('bfRatio1', c_float * int(13)),
    ('hbf_wgt_clip', c_int * int(13)),
    ('medRatio2', c_float * int(13)),
    ('sigmaR2', c_float * int(13)),
    ('uvgain2', c_float * int(13)),
    ('sigmaR3', c_float * int(13)),
    ('uvgain3', c_float * int(13)),
    ('bfRatio3', c_float * int(13)),
    ('kernel_5x5_table', c_float * int(5)),
]

RK_CNR_Params_V1_t = struct_RK_CNR_Params_V1_s# /root/camera_engine_rkaiq/include/algos/acnr/rk_aiq_types_acnr_algo_int_v1.h: 153

# /root/camera_engine_rkaiq/include/algos/acnr/rk_aiq_types_acnr_algo_int_v1.h: 199
class struct_RK_CNR_Params_V1_Select_s(Structure):
    pass

struct_RK_CNR_Params_V1_Select_s.__slots__ = [
    'enable',
    'rkcnr_hq_bila_bypass',
    'rkcnr_lq_bila_bypass',
    'rkcnr_exgain',
    'rkcnr_g_gain',
    'ratio',
    'offset',
    'medRatio1',
    'sigmaR1',
    'uvgain1',
    'bfRatio1',
    'hbf_wgt_clip',
    'medRatio2',
    'sigmaR2',
    'uvgain2',
    'sigmaR3',
    'uvgain3',
    'bfRatio3',
    'kernel_5x5_table',
]
struct_RK_CNR_Params_V1_Select_s._fields_ = [
    ('enable', c_int),
    ('rkcnr_hq_bila_bypass', c_int),
    ('rkcnr_lq_bila_bypass', c_int),
    ('rkcnr_exgain', c_float),
    ('rkcnr_g_gain', c_float),
    ('ratio', c_float),
    ('offset', c_float),
    ('medRatio1', c_float),
    ('sigmaR1', c_float),
    ('uvgain1', c_float),
    ('bfRatio1', c_float),
    ('hbf_wgt_clip', c_int),
    ('medRatio2', c_float),
    ('sigmaR2', c_float),
    ('uvgain2', c_float),
    ('sigmaR3', c_float),
    ('uvgain3', c_float),
    ('bfRatio3', c_float),
    ('kernel_5x5_table', c_float * int(5)),
]

RK_CNR_Params_V1_Select_t = struct_RK_CNR_Params_V1_Select_s# /root/camera_engine_rkaiq/include/algos/acnr/rk_aiq_types_acnr_algo_int_v1.h: 199

# /root/camera_engine_rkaiq/include/algos/acnr/rk_aiq_types_acnr_algo_int_v1.h: 207
class struct_Acnr_Manual_Attr_V1_s(Structure):
    pass

struct_Acnr_Manual_Attr_V1_s.__slots__ = [
    'cnrEn',
    'stSelect',
]
struct_Acnr_Manual_Attr_V1_s._fields_ = [
    ('cnrEn', c_int),
    ('stSelect', RK_CNR_Params_V1_Select_t),
]

Acnr_Manual_Attr_V1_t = struct_Acnr_Manual_Attr_V1_s# /root/camera_engine_rkaiq/include/algos/acnr/rk_aiq_types_acnr_algo_int_v1.h: 207

# /root/camera_engine_rkaiq/include/algos/acnr/rk_aiq_types_acnr_algo_int_v1.h: 217
class struct_Acnr_Auto_Attr_V1_s(Structure):
    pass

struct_Acnr_Auto_Attr_V1_s.__slots__ = [
    'cnrEn',
    'stParams',
    'stSelect',
]
struct_Acnr_Auto_Attr_V1_s._fields_ = [
    ('cnrEn', c_int),
    ('stParams', RK_CNR_Params_V1_t),
    ('stSelect', RK_CNR_Params_V1_Select_t),
]

Acnr_Auto_Attr_V1_t = struct_Acnr_Auto_Attr_V1_s# /root/camera_engine_rkaiq/include/algos/acnr/rk_aiq_types_acnr_algo_int_v1.h: 217

# /root/camera_engine_rkaiq/include/algos/acnr/rk_aiq_types_acnr_algo_int_v1.h: 245
class struct_rk_aiq_cnr_attrib_v1_s(Structure):
    pass

struct_rk_aiq_cnr_attrib_v1_s.__slots__ = [
    'eMode',
    'stAuto',
    'stManual',
]
struct_rk_aiq_cnr_attrib_v1_s._fields_ = [
    ('eMode', Acnr_OPMode_t),
    ('stAuto', Acnr_Auto_Attr_V1_t),
    ('stManual', Acnr_Manual_Attr_V1_t),
]

rk_aiq_cnr_attrib_v1_t = struct_rk_aiq_cnr_attrib_v1_s# /root/camera_engine_rkaiq/include/algos/acnr/rk_aiq_types_acnr_algo_int_v1.h: 245

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_acnr_v1.h: 31
if _libs["rkaiq"].has("rk_aiq_user_api2_acnrV1_SetAttrib", "cdecl"):
    rk_aiq_user_api2_acnrV1_SetAttrib = _libs["rkaiq"].get("rk_aiq_user_api2_acnrV1_SetAttrib", "cdecl")
    rk_aiq_user_api2_acnrV1_SetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_cnr_attrib_v1_t)]
    rk_aiq_user_api2_acnrV1_SetAttrib.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_acnr_v1.h: 34
if _libs["rkaiq"].has("rk_aiq_user_api2_acnrV1_GetAttrib", "cdecl"):
    rk_aiq_user_api2_acnrV1_GetAttrib = _libs["rkaiq"].get("rk_aiq_user_api2_acnrV1_GetAttrib", "cdecl")
    rk_aiq_user_api2_acnrV1_GetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_cnr_attrib_v1_t)]
    rk_aiq_user_api2_acnrV1_GetAttrib.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_acnr_v1.h: 37
if _libs["rkaiq"].has("rk_aiq_user_api2_acnrV1_SetStrength", "cdecl"):
    rk_aiq_user_api2_acnrV1_SetStrength = _libs["rkaiq"].get("rk_aiq_user_api2_acnrV1_SetStrength", "cdecl")
    rk_aiq_user_api2_acnrV1_SetStrength.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_float]
    rk_aiq_user_api2_acnrV1_SetStrength.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_acnr_v1.h: 40
if _libs["rkaiq"].has("rk_aiq_user_api2_acnrV1_GetStrength", "cdecl"):
    rk_aiq_user_api2_acnrV1_GetStrength = _libs["rkaiq"].get("rk_aiq_user_api2_acnrV1_GetStrength", "cdecl")
    rk_aiq_user_api2_acnrV1_GetStrength.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(c_float)]
    rk_aiq_user_api2_acnrV1_GetStrength.restype = XCamReturn

# /root/camera_engine_rkaiq/include/algos/acnr2/rk_aiq_types_acnr_hw_v2.h: 70
class struct_RK_CNR_Fix_V2_s(Structure):
    pass

struct_RK_CNR_Fix_V2_s.__slots__ = [
    'cnr_thumb_mix_cur_en',
    'cnr_lq_bila_bypass',
    'cnr_hq_bila_bypass',
    'cnr_exgain_bypass',
    'cnr_en_i',
    'cnr_global_gain_alpha',
    'cnr_global_gain',
    'cnr_gain_iso',
    'cnr_gain_offset',
    'cnr_gain_1sigma',
    'cnr_gain_uvgain1',
    'cnr_gain_uvgain0',
    'cnr_lmed3_alpha',
    'cnr_lbf5_gain_y',
    'cnr_lbf5_gain_c',
    'cnr_lbf5_weit_d',
    'cnr_hmed3_alpha',
    'cnr_hbf5_weit_src',
    'cnr_hbf5_min_wgt',
    'cnr_hbf5_sigma',
    'cnr_lbf5_weit_src',
    'cnr_lbf3_sigma',
    'cnr_sigma_y',
]
struct_RK_CNR_Fix_V2_s._fields_ = [
    ('cnr_thumb_mix_cur_en', uint8_t),
    ('cnr_lq_bila_bypass', uint8_t),
    ('cnr_hq_bila_bypass', uint8_t),
    ('cnr_exgain_bypass', uint8_t),
    ('cnr_en_i', uint8_t),
    ('cnr_global_gain_alpha', uint8_t),
    ('cnr_global_gain', uint16_t),
    ('cnr_gain_iso', uint8_t),
    ('cnr_gain_offset', uint8_t),
    ('cnr_gain_1sigma', uint8_t),
    ('cnr_gain_uvgain1', uint8_t),
    ('cnr_gain_uvgain0', uint8_t),
    ('cnr_lmed3_alpha', uint8_t),
    ('cnr_lbf5_gain_y', uint8_t),
    ('cnr_lbf5_gain_c', uint8_t),
    ('cnr_lbf5_weit_d', uint8_t * int(5)),
    ('cnr_hmed3_alpha', uint8_t),
    ('cnr_hbf5_weit_src', uint8_t),
    ('cnr_hbf5_min_wgt', uint8_t),
    ('cnr_hbf5_sigma', uint16_t),
    ('cnr_lbf5_weit_src', uint8_t),
    ('cnr_lbf3_sigma', uint16_t),
    ('cnr_sigma_y', uint8_t * int(13)),
]

RK_CNR_Fix_V2_t = struct_RK_CNR_Fix_V2_s# /root/camera_engine_rkaiq/include/algos/acnr2/rk_aiq_types_acnr_hw_v2.h: 70

# /root/camera_engine_rkaiq/include/iq_parser_v2/cnr_uapi_head_v2.h: 88
class struct_RK_CNR_Params_V2_Select_s(Structure):
    pass

struct_RK_CNR_Params_V2_Select_s.__slots__ = [
    'enable',
    'hf_bypass',
    'lf_bypass',
    'global_gain',
    'global_gain_alpha',
    'local_gain_scale',
    'gain_adj_strength_ratio',
    'color_sat_adj',
    'color_sat_adj_alpha',
    'hf_spikes_reducion_strength',
    'hf_denoise_strength',
    'hf_color_sat',
    'hf_denoise_alpha',
    'hf_bf_wgt_clip',
    'thumb_spikes_reducion_strength',
    'thumb_denoise_strength',
    'thumb_color_sat',
    'lf_denoise_strength',
    'lf_color_sat',
    'lf_denoise_alpha',
    'kernel_5x5',
]
struct_RK_CNR_Params_V2_Select_s._fields_ = [
    ('enable', c_int),
    ('hf_bypass', c_int),
    ('lf_bypass', c_int),
    ('global_gain', c_float),
    ('global_gain_alpha', c_float),
    ('local_gain_scale', c_float),
    ('gain_adj_strength_ratio', c_int * int(13)),
    ('color_sat_adj', c_float),
    ('color_sat_adj_alpha', c_float),
    ('hf_spikes_reducion_strength', c_float),
    ('hf_denoise_strength', c_float),
    ('hf_color_sat', c_float),
    ('hf_denoise_alpha', c_float),
    ('hf_bf_wgt_clip', c_int),
    ('thumb_spikes_reducion_strength', c_float),
    ('thumb_denoise_strength', c_float),
    ('thumb_color_sat', c_float),
    ('lf_denoise_strength', c_float),
    ('lf_color_sat', c_float),
    ('lf_denoise_alpha', c_float),
    ('kernel_5x5', c_float * int(5)),
]

RK_CNR_Params_V2_Select_t = struct_RK_CNR_Params_V2_Select_s# /root/camera_engine_rkaiq/include/iq_parser_v2/cnr_uapi_head_v2.h: 88

# /root/camera_engine_rkaiq/include/iq_parser_v2/cnr_uapi_head_v2.h: 116
class struct_AcnrV2_ExpInfo_s(Structure):
    pass

struct_AcnrV2_ExpInfo_s.__slots__ = [
    'hdr_mode',
    'snr_mode',
    'arTime',
    'arAGain',
    'arDGain',
    'arIso',
    'isoLow',
    'isoHigh',
    'rawWidth',
    'rawHeight',
]
struct_AcnrV2_ExpInfo_s._fields_ = [
    ('hdr_mode', c_int),
    ('snr_mode', c_int),
    ('arTime', c_float * int(3)),
    ('arAGain', c_float * int(3)),
    ('arDGain', c_float * int(3)),
    ('arIso', c_int * int(3)),
    ('isoLow', c_int),
    ('isoHigh', c_int),
    ('rawWidth', c_int),
    ('rawHeight', c_int),
]

AcnrV2_ExpInfo_t = struct_AcnrV2_ExpInfo_s# /root/camera_engine_rkaiq/include/iq_parser_v2/cnr_uapi_head_v2.h: 116

# /root/camera_engine_rkaiq/include/iq_parser_v2/cnr_uapi_head_v2.h: 125
class struct_rk_aiq_cnr_info_v2_s(Structure):
    pass

struct_rk_aiq_cnr_info_v2_s.__slots__ = [
    'sync',
    'iso',
    'expo_info',
]
struct_rk_aiq_cnr_info_v2_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('iso', c_int),
    ('expo_info', AcnrV2_ExpInfo_t),
]

rk_aiq_cnr_info_v2_t = struct_rk_aiq_cnr_info_v2_s# /root/camera_engine_rkaiq/include/iq_parser_v2/cnr_uapi_head_v2.h: 125

enum_AcnrV2_OPMode_e = c_int# /root/camera_engine_rkaiq/include/algos/acnr2/rk_aiq_types_acnr_algo_int_v2.h: 100

AcnrV2_OPMode_t = enum_AcnrV2_OPMode_e# /root/camera_engine_rkaiq/include/algos/acnr2/rk_aiq_types_acnr_algo_int_v2.h: 100

# /root/camera_engine_rkaiq/include/algos/acnr2/rk_aiq_types_acnr_algo_int_v2.h: 158
class struct_RK_CNR_Params_V2_s(Structure):
    pass

struct_RK_CNR_Params_V2_s.__slots__ = [
    'enable',
    'iso',
    'hf_bypass',
    'lf_bypass',
    'global_gain',
    'global_gain_alpha',
    'local_gain_scale',
    'gain_adj_strength_ratio',
    'color_sat_adj',
    'color_sat_adj_alpha',
    'hf_spikes_reducion_strength',
    'hf_denoise_strength',
    'hf_color_sat',
    'hf_denoise_alpha',
    'hf_bf_wgt_clip',
    'thumb_spikes_reducion_strength',
    'thumb_denoise_strength',
    'thumb_color_sat',
    'lf_denoise_strength',
    'lf_color_sat',
    'lf_denoise_alpha',
    'kernel_5x5',
]
struct_RK_CNR_Params_V2_s._fields_ = [
    ('enable', c_int),
    ('iso', c_float * int(13)),
    ('hf_bypass', c_int * int(13)),
    ('lf_bypass', c_int * int(13)),
    ('global_gain', c_float * int(13)),
    ('global_gain_alpha', c_float * int(13)),
    ('local_gain_scale', c_float * int(13)),
    ('gain_adj_strength_ratio', (c_int * int(13)) * int(13)),
    ('color_sat_adj', c_float * int(13)),
    ('color_sat_adj_alpha', c_float * int(13)),
    ('hf_spikes_reducion_strength', c_float * int(13)),
    ('hf_denoise_strength', c_float * int(13)),
    ('hf_color_sat', c_float * int(13)),
    ('hf_denoise_alpha', c_float * int(13)),
    ('hf_bf_wgt_clip', c_int * int(13)),
    ('thumb_spikes_reducion_strength', c_float * int(13)),
    ('thumb_denoise_strength', c_float * int(13)),
    ('thumb_color_sat', c_float * int(13)),
    ('lf_denoise_strength', c_float * int(13)),
    ('lf_color_sat', c_float * int(13)),
    ('lf_denoise_alpha', c_float * int(13)),
    ('kernel_5x5', c_float * int(5)),
]

RK_CNR_Params_V2_t = struct_RK_CNR_Params_V2_s# /root/camera_engine_rkaiq/include/algos/acnr2/rk_aiq_types_acnr_algo_int_v2.h: 158

# /root/camera_engine_rkaiq/include/algos/acnr2/rk_aiq_types_acnr_algo_int_v2.h: 220
class struct_Acnr_Manual_Attr_V2_s(Structure):
    pass

struct_Acnr_Manual_Attr_V2_s.__slots__ = [
    'stSelect',
    'stFix',
]
struct_Acnr_Manual_Attr_V2_s._fields_ = [
    ('stSelect', RK_CNR_Params_V2_Select_t),
    ('stFix', RK_CNR_Fix_V2_t),
]

Acnr_Manual_Attr_V2_t = struct_Acnr_Manual_Attr_V2_s# /root/camera_engine_rkaiq/include/algos/acnr2/rk_aiq_types_acnr_algo_int_v2.h: 220

# /root/camera_engine_rkaiq/include/algos/acnr2/rk_aiq_types_acnr_algo_int_v2.h: 229
class struct_Acnr_Auto_Attr_V2_s(Structure):
    pass

struct_Acnr_Auto_Attr_V2_s.__slots__ = [
    'stParams',
    'stSelect',
]
struct_Acnr_Auto_Attr_V2_s._fields_ = [
    ('stParams', RK_CNR_Params_V2_t),
    ('stSelect', RK_CNR_Params_V2_Select_t),
]

Acnr_Auto_Attr_V2_t = struct_Acnr_Auto_Attr_V2_s# /root/camera_engine_rkaiq/include/algos/acnr2/rk_aiq_types_acnr_algo_int_v2.h: 229

# /root/camera_engine_rkaiq/include/algos/acnr2/rk_aiq_types_acnr_algo_int_v2.h: 257
class struct_rk_aiq_cnr_attrib_v2_s(Structure):
    pass

struct_rk_aiq_cnr_attrib_v2_s.__slots__ = [
    'sync',
    'eMode',
    'stAuto',
    'stManual',
]
struct_rk_aiq_cnr_attrib_v2_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('eMode', AcnrV2_OPMode_t),
    ('stAuto', Acnr_Auto_Attr_V2_t),
    ('stManual', Acnr_Manual_Attr_V2_t),
]

rk_aiq_cnr_attrib_v2_t = struct_rk_aiq_cnr_attrib_v2_s# /root/camera_engine_rkaiq/include/algos/acnr2/rk_aiq_types_acnr_algo_int_v2.h: 257

# /root/camera_engine_rkaiq/include/algos/acnr2/rk_aiq_types_acnr_algo_int_v2.h: 264
class struct_rk_aiq_cnr_strength_v2_s(Structure):
    pass

struct_rk_aiq_cnr_strength_v2_s.__slots__ = [
    'sync',
    'percent',
    'strength_enable',
]
struct_rk_aiq_cnr_strength_v2_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('percent', c_float),
    ('strength_enable', c_bool),
]

rk_aiq_cnr_strength_v2_t = struct_rk_aiq_cnr_strength_v2_s# /root/camera_engine_rkaiq/include/algos/acnr2/rk_aiq_types_acnr_algo_int_v2.h: 264

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_acnr_v2.h: 31
if _libs["rkaiq"].has("rk_aiq_user_api2_acnrV2_SetAttrib", "cdecl"):
    rk_aiq_user_api2_acnrV2_SetAttrib = _libs["rkaiq"].get("rk_aiq_user_api2_acnrV2_SetAttrib", "cdecl")
    rk_aiq_user_api2_acnrV2_SetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_cnr_attrib_v2_t)]
    rk_aiq_user_api2_acnrV2_SetAttrib.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_acnr_v2.h: 34
if _libs["rkaiq"].has("rk_aiq_user_api2_acnrV2_GetAttrib", "cdecl"):
    rk_aiq_user_api2_acnrV2_GetAttrib = _libs["rkaiq"].get("rk_aiq_user_api2_acnrV2_GetAttrib", "cdecl")
    rk_aiq_user_api2_acnrV2_GetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_cnr_attrib_v2_t)]
    rk_aiq_user_api2_acnrV2_GetAttrib.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_acnr_v2.h: 37
if _libs["rkaiq"].has("rk_aiq_user_api2_acnrV2_SetStrength", "cdecl"):
    rk_aiq_user_api2_acnrV2_SetStrength = _libs["rkaiq"].get("rk_aiq_user_api2_acnrV2_SetStrength", "cdecl")
    rk_aiq_user_api2_acnrV2_SetStrength.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_cnr_strength_v2_t)]
    rk_aiq_user_api2_acnrV2_SetStrength.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_acnr_v2.h: 40
if _libs["rkaiq"].has("rk_aiq_user_api2_acnrV2_GetStrength", "cdecl"):
    rk_aiq_user_api2_acnrV2_GetStrength = _libs["rkaiq"].get("rk_aiq_user_api2_acnrV2_GetStrength", "cdecl")
    rk_aiq_user_api2_acnrV2_GetStrength.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_cnr_strength_v2_t)]
    rk_aiq_user_api2_acnrV2_GetStrength.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_acnr_v2.h: 43
if _libs["rkaiq"].has("rk_aiq_user_api2_acnrV2_GetInfo", "cdecl"):
    rk_aiq_user_api2_acnrV2_GetInfo = _libs["rkaiq"].get("rk_aiq_user_api2_acnrV2_GetInfo", "cdecl")
    rk_aiq_user_api2_acnrV2_GetInfo.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_cnr_info_v2_t)]
    rk_aiq_user_api2_acnrV2_GetInfo.restype = XCamReturn

# /root/camera_engine_rkaiq/include/iq_parser_v2/acp_uapi_head.h: 35
class struct_acp_attrib_s(Structure):
    pass

struct_acp_attrib_s.__slots__ = [
    'sync',
    'brightness',
    'contrast',
    'saturation',
    'hue',
]
struct_acp_attrib_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('brightness', uint8_t),
    ('contrast', uint8_t),
    ('saturation', uint8_t),
    ('hue', uint8_t),
]

acp_attrib_t = struct_acp_attrib_s# /root/camera_engine_rkaiq/include/iq_parser_v2/acp_uapi_head.h: 35

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_acp.h: 31
if _libs["rkaiq"].has("rk_aiq_user_api2_acp_SetAttrib", "cdecl"):
    rk_aiq_user_api2_acp_SetAttrib = _libs["rkaiq"].get("rk_aiq_user_api2_acp_SetAttrib", "cdecl")
    rk_aiq_user_api2_acp_SetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), acp_attrib_t]
    rk_aiq_user_api2_acp_SetAttrib.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_acp.h: 33
if _libs["rkaiq"].has("rk_aiq_user_api2_acp_GetAttrib", "cdecl"):
    rk_aiq_user_api2_acp_GetAttrib = _libs["rkaiq"].get("rk_aiq_user_api2_acp_GetAttrib", "cdecl")
    rk_aiq_user_api2_acp_GetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(acp_attrib_t)]
    rk_aiq_user_api2_acp_GetAttrib.restype = XCamReturn

# /root/camera_engine_rkaiq/include/iq_parser_v2/csm_head.h: 40
class struct___csm_param(Structure):
    pass

struct___csm_param.__slots__ = [
    'op_mode',
    'full_range',
    'y_offset',
    'c_offset',
    'coeff',
]
struct___csm_param._fields_ = [
    ('op_mode', RKAiqOPMode_t),
    ('full_range', c_bool),
    ('y_offset', uint8_t),
    ('c_offset', uint8_t),
    ('coeff', c_float * int(9)),
]

Csm_Param_t = struct___csm_param# /root/camera_engine_rkaiq/include/iq_parser_v2/csm_head.h: 40

rk_aiq_acsm_params_t = Csm_Param_t# /root/camera_engine_rkaiq/include/algos/acsm/rk_aiq_types_acsm_algo.h: 25

# /root/camera_engine_rkaiq/include/algos/acsm/rk_aiq_uapi_acsm.h: 19
class struct_rk_aiq_uapi_acsm_attrib_s(Structure):
    pass

struct_rk_aiq_uapi_acsm_attrib_s.__slots__ = [
    'sync',
    'param',
]
struct_rk_aiq_uapi_acsm_attrib_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('param', rk_aiq_acsm_params_t),
]

rk_aiq_uapi_acsm_attrib_t = struct_rk_aiq_uapi_acsm_attrib_s# /root/camera_engine_rkaiq/include/algos/acsm/rk_aiq_uapi_acsm.h: 19

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_acsm.h: 31
if _libs["rkaiq"].has("rk_aiq_user_api2_acsm_SetAttrib", "cdecl"):
    rk_aiq_user_api2_acsm_SetAttrib = _libs["rkaiq"].get("rk_aiq_user_api2_acsm_SetAttrib", "cdecl")
    rk_aiq_user_api2_acsm_SetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), rk_aiq_uapi_acsm_attrib_t]
    rk_aiq_user_api2_acsm_SetAttrib.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_acsm.h: 33
if _libs["rkaiq"].has("rk_aiq_user_api2_acsm_GetAttrib", "cdecl"):
    rk_aiq_user_api2_acsm_GetAttrib = _libs["rkaiq"].get("rk_aiq_user_api2_acsm_GetAttrib", "cdecl")
    rk_aiq_user_api2_acsm_GetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_uapi_acsm_attrib_t)]
    rk_aiq_user_api2_acsm_GetAttrib.restype = XCamReturn

enum_rk_aiq_debayer_op_mode_s = c_int# /root/camera_engine_rkaiq/include/algos/adebayer/rk_aiq_types_adebayer_ext.h: 32

rk_aiq_debayer_op_mode_t = enum_rk_aiq_debayer_op_mode_s# /root/camera_engine_rkaiq/include/algos/adebayer/rk_aiq_types_adebayer_ext.h: 32

# /root/camera_engine_rkaiq/include/algos/adebayer/rk_aiq_types_adebayer_ext.h: 80
class struct_adebayer_attrib_auto_s(Structure):
    pass

struct_adebayer_attrib_auto_s.__slots__ = [
    'debayer_filter1',
    'debayer_filter2',
    'ISO',
    'debayer_gain_offset',
    'debayer_offset',
    'debayer_clip_en',
    'debayer_filter_g_en',
    'debayer_filter_c_en',
    'debayer_thed0',
    'debayer_thed1',
    'debayer_dist_scale',
    'debayer_cnr_strength',
    'debayer_shift_num',
    'sharp_strength',
    'debayer_hf_offset',
]
struct_adebayer_attrib_auto_s._fields_ = [
    ('debayer_filter1', c_int * int(5)),
    ('debayer_filter2', c_int * int(5)),
    ('ISO', c_int * int(13)),
    ('debayer_gain_offset', c_ubyte * int(13)),
    ('debayer_offset', c_ubyte * int(13)),
    ('debayer_clip_en', c_ubyte * int(13)),
    ('debayer_filter_g_en', c_ubyte * int(13)),
    ('debayer_filter_c_en', c_ubyte * int(13)),
    ('debayer_thed0', c_ubyte * int(13)),
    ('debayer_thed1', c_ubyte * int(13)),
    ('debayer_dist_scale', c_ubyte * int(13)),
    ('debayer_cnr_strength', c_ubyte * int(13)),
    ('debayer_shift_num', c_ubyte * int(13)),
    ('sharp_strength', c_ubyte * int(13)),
    ('debayer_hf_offset', c_ushort * int(13)),
]

adebayer_attrib_auto_t = struct_adebayer_attrib_auto_s# /root/camera_engine_rkaiq/include/algos/adebayer/rk_aiq_types_adebayer_ext.h: 80

# /root/camera_engine_rkaiq/include/algos/adebayer/rk_aiq_types_adebayer_ext.h: 125
class struct_adebayer_attrib_manual_s(Structure):
    pass

struct_adebayer_attrib_manual_s.__slots__ = [
    'filter1',
    'filter2',
    'gain_offset',
    'sharp_strength',
    'hf_offset',
    'offset',
    'clip_en',
    'filter_g_en',
    'filter_c_en',
    'thed0',
    'thed1',
    'dist_scale',
    'cnr_strength',
    'shift_num',
]
struct_adebayer_attrib_manual_s._fields_ = [
    ('filter1', c_int8 * int(5)),
    ('filter2', c_int8 * int(5)),
    ('gain_offset', uint8_t),
    ('sharp_strength', uint8_t),
    ('hf_offset', uint16_t),
    ('offset', uint8_t),
    ('clip_en', uint8_t),
    ('filter_g_en', uint8_t),
    ('filter_c_en', uint8_t),
    ('thed0', uint8_t),
    ('thed1', uint8_t),
    ('dist_scale', uint8_t),
    ('cnr_strength', uint8_t),
    ('shift_num', uint8_t),
]

adebayer_attrib_manual_t = struct_adebayer_attrib_manual_s# /root/camera_engine_rkaiq/include/algos/adebayer/rk_aiq_types_adebayer_ext.h: 125

# /root/camera_engine_rkaiq/include/algos/adebayer/rk_aiq_types_adebayer_ext.h: 141
class struct_adebayer_attrib_s(Structure):
    pass

struct_adebayer_attrib_s.__slots__ = [
    'sync',
    'enable',
    'mode',
    'stManual',
    'stAuto',
]
struct_adebayer_attrib_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('enable', uint8_t),
    ('mode', rk_aiq_debayer_op_mode_t),
    ('stManual', adebayer_attrib_manual_t),
    ('stAuto', adebayer_attrib_auto_t),
]

adebayer_attrib_t = struct_adebayer_attrib_s# /root/camera_engine_rkaiq/include/algos/adebayer/rk_aiq_types_adebayer_ext.h: 141

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_adebayer.h: 31
if _libs["rkaiq"].has("rk_aiq_user_api2_adebayer_SetAttrib", "cdecl"):
    rk_aiq_user_api2_adebayer_SetAttrib = _libs["rkaiq"].get("rk_aiq_user_api2_adebayer_SetAttrib", "cdecl")
    rk_aiq_user_api2_adebayer_SetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), adebayer_attrib_t]
    rk_aiq_user_api2_adebayer_SetAttrib.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_adebayer.h: 33
if _libs["rkaiq"].has("rk_aiq_user_api2_adebayer_GetAttrib", "cdecl"):
    rk_aiq_user_api2_adebayer_GetAttrib = _libs["rkaiq"].get("rk_aiq_user_api2_adebayer_GetAttrib", "cdecl")
    rk_aiq_user_api2_adebayer_GetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(adebayer_attrib_t)]
    rk_aiq_user_api2_adebayer_GetAttrib.restype = XCamReturn

# /root/camera_engine_rkaiq/include/iq_parser_v2/adegamma_head.h: 46
class struct_AdegmmaParaV2_s(Structure):
    pass

struct_AdegmmaParaV2_s.__slots__ = [
    'degamma_en',
    'X_axis',
    'curve_R',
    'curve_G',
    'curve_B',
]
struct_AdegmmaParaV2_s._fields_ = [
    ('degamma_en', c_bool),
    ('X_axis', c_int * int(17)),
    ('curve_R', c_int * int(17)),
    ('curve_G', c_int * int(17)),
    ('curve_B', c_int * int(17)),
]

AdegmmaParaV2_t = struct_AdegmmaParaV2_s# /root/camera_engine_rkaiq/include/iq_parser_v2/adegamma_head.h: 46

# /root/camera_engine_rkaiq/include/iq_parser_v2/adegamma_head.h: 51
class struct_CalibDbV2_Adegmma_s(Structure):
    pass

struct_CalibDbV2_Adegmma_s.__slots__ = [
    'DegammaTuningPara',
]
struct_CalibDbV2_Adegmma_s._fields_ = [
    ('DegammaTuningPara', AdegmmaParaV2_t),
]

CalibDbV2_Adegmma_t = struct_CalibDbV2_Adegmma_s# /root/camera_engine_rkaiq/include/iq_parser_v2/adegamma_head.h: 51

enum_rk_aiq_degamma_op_mode_s = c_int# /root/camera_engine_rkaiq/include/algos/adegamma/rk_aiq_types_adegamma_algo_int.h: 46

rk_aiq_degamma_op_mode_t = enum_rk_aiq_degamma_op_mode_s# /root/camera_engine_rkaiq/include/algos/adegamma/rk_aiq_types_adegamma_algo_int.h: 46

# /root/camera_engine_rkaiq/include/algos/adegamma/rk_aiq_types_adegamma_algo_int.h: 54
class struct_Adegamma_api_manual_s(Structure):
    pass

struct_Adegamma_api_manual_s.__slots__ = [
    'en',
    'X_axis',
    'curve_R',
    'curve_G',
    'curve_B',
]
struct_Adegamma_api_manual_s._fields_ = [
    ('en', c_bool),
    ('X_axis', c_int * int(17)),
    ('curve_R', c_int * int(17)),
    ('curve_G', c_int * int(17)),
    ('curve_B', c_int * int(17)),
]

Adegamma_api_manual_t = struct_Adegamma_api_manual_s# /root/camera_engine_rkaiq/include/algos/adegamma/rk_aiq_types_adegamma_algo_int.h: 54

# /root/camera_engine_rkaiq/include/algos/adegamma/rk_aiq_types_adegamma_algo_int.h: 69
class struct_rk_aiq_degamma_attr_s(Structure):
    pass

struct_rk_aiq_degamma_attr_s.__slots__ = [
    'mode',
    'stManual',
    'stTool',
    'Scene_mode',
]
struct_rk_aiq_degamma_attr_s._fields_ = [
    ('mode', rk_aiq_degamma_op_mode_t),
    ('stManual', Adegamma_api_manual_t),
    ('stTool', CalibDbV2_Adegmma_t),
    ('Scene_mode', c_int),
]

rk_aiq_degamma_attr_t = struct_rk_aiq_degamma_attr_s# /root/camera_engine_rkaiq/include/algos/adegamma/rk_aiq_types_adegamma_algo_int.h: 69

rk_aiq_degamma_attrib_t = rk_aiq_degamma_attr_t# /root/camera_engine_rkaiq/include/algos/adegamma/rk_aiq_uapi_adegamma_int.h: 15

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_adegamma.h: 31
if _libs["rkaiq"].has("rk_aiq_user_api2_adegamma_SetAttrib", "cdecl"):
    rk_aiq_user_api2_adegamma_SetAttrib = _libs["rkaiq"].get("rk_aiq_user_api2_adegamma_SetAttrib", "cdecl")
    rk_aiq_user_api2_adegamma_SetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), rk_aiq_degamma_attrib_t]
    rk_aiq_user_api2_adegamma_SetAttrib.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_adegamma.h: 33
if _libs["rkaiq"].has("rk_aiq_user_api2_adegamma_GetAttrib", "cdecl"):
    rk_aiq_user_api2_adegamma_GetAttrib = _libs["rkaiq"].get("rk_aiq_user_api2_adegamma_GetAttrib", "cdecl")
    rk_aiq_user_api2_adegamma_GetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_degamma_attrib_t)]
    rk_aiq_user_api2_adegamma_GetAttrib.restype = XCamReturn

enum_CtrlDataType_e = c_int# /root/camera_engine_rkaiq/include/iq_parser_v2/adehaze_head.h: 35

CtrlDataType_t = enum_CtrlDataType_e# /root/camera_engine_rkaiq/include/iq_parser_v2/adehaze_head.h: 35

# /root/camera_engine_rkaiq/include/iq_parser_v2/adehaze_uapi_head.h: 66
class struct_mDehazeDataV21_s(Structure):
    pass

struct_mDehazeDataV21_s.__slots__ = [
    'dc_min_th',
    'dc_max_th',
    'yhist_th',
    'yblk_th',
    'dark_th',
    'bright_min',
    'bright_max',
    'wt_max',
    'air_min',
    'air_max',
    'tmax_base',
    'tmax_off',
    'tmax_max',
    'cfg_wt',
    'cfg_air',
    'cfg_tmax',
    'dc_weitcur',
    'bf_weight',
    'range_sigma',
    'space_sigma_pre',
    'space_sigma_cur',
]
struct_mDehazeDataV21_s._fields_ = [
    ('dc_min_th', c_float),
    ('dc_max_th', c_float),
    ('yhist_th', c_float),
    ('yblk_th', c_float),
    ('dark_th', c_float),
    ('bright_min', c_float),
    ('bright_max', c_float),
    ('wt_max', c_float),
    ('air_min', c_float),
    ('air_max', c_float),
    ('tmax_base', c_float),
    ('tmax_off', c_float),
    ('tmax_max', c_float),
    ('cfg_wt', c_float),
    ('cfg_air', c_float),
    ('cfg_tmax', c_float),
    ('dc_weitcur', c_float),
    ('bf_weight', c_float),
    ('range_sigma', c_float),
    ('space_sigma_pre', c_float),
    ('space_sigma_cur', c_float),
]

mDehazeDataV21_t = struct_mDehazeDataV21_s# /root/camera_engine_rkaiq/include/iq_parser_v2/adehaze_uapi_head.h: 66

# /root/camera_engine_rkaiq/include/iq_parser_v2/adehaze_uapi_head.h: 87
class struct_mDehaze_Setting_V21_s(Structure):
    pass

struct_mDehaze_Setting_V21_s.__slots__ = [
    'en',
    'air_lc_en',
    'stab_fnum',
    'sigma',
    'wt_sigma',
    'air_sigma',
    'tmax_sigma',
    'pre_wet',
    'DehazeData',
]
struct_mDehaze_Setting_V21_s._fields_ = [
    ('en', c_bool),
    ('air_lc_en', c_bool),
    ('stab_fnum', c_float),
    ('sigma', c_float),
    ('wt_sigma', c_float),
    ('air_sigma', c_float),
    ('tmax_sigma', c_float),
    ('pre_wet', c_float),
    ('DehazeData', mDehazeDataV21_t),
]

mDehaze_Setting_V21_t = struct_mDehaze_Setting_V21_s# /root/camera_engine_rkaiq/include/iq_parser_v2/adehaze_uapi_head.h: 87

# /root/camera_engine_rkaiq/include/iq_parser_v2/adehaze_uapi_head.h: 94
class struct_mEnhanceDataV21_s(Structure):
    pass

struct_mEnhanceDataV21_s.__slots__ = [
    'enhance_value',
    'enhance_chroma',
]
struct_mEnhanceDataV21_s._fields_ = [
    ('enhance_value', c_float),
    ('enhance_chroma', c_float),
]

mEnhanceDataV21_t = struct_mEnhanceDataV21_s# /root/camera_engine_rkaiq/include/iq_parser_v2/adehaze_uapi_head.h: 94

# /root/camera_engine_rkaiq/include/iq_parser_v2/adehaze_uapi_head.h: 103
class struct_mEnhance_Setting_V21_s(Structure):
    pass

struct_mEnhance_Setting_V21_s.__slots__ = [
    'en',
    'enhance_curve',
    'EnhanceData',
]
struct_mEnhance_Setting_V21_s._fields_ = [
    ('en', c_bool),
    ('enhance_curve', c_float * int(17)),
    ('EnhanceData', mEnhanceDataV21_t),
]

mEnhance_Setting_V21_t = struct_mEnhance_Setting_V21_s# /root/camera_engine_rkaiq/include/iq_parser_v2/adehaze_uapi_head.h: 103

# /root/camera_engine_rkaiq/include/iq_parser_v2/adehaze_uapi_head.h: 118
class struct_mHistDataV21_s(Structure):
    pass

struct_mHistDataV21_s.__slots__ = [
    'hist_gratio',
    'hist_th_off',
    'hist_k',
    'hist_min',
    'hist_scale',
    'cfg_gratio',
]
struct_mHistDataV21_s._fields_ = [
    ('hist_gratio', c_float),
    ('hist_th_off', c_float),
    ('hist_k', c_float),
    ('hist_min', c_float),
    ('hist_scale', c_float),
    ('cfg_gratio', c_float),
]

mHistDataV21_t = struct_mHistDataV21_s# /root/camera_engine_rkaiq/include/iq_parser_v2/adehaze_uapi_head.h: 118

# /root/camera_engine_rkaiq/include/iq_parser_v2/adehaze_uapi_head.h: 127
class struct_mHist_setting_V21_s(Structure):
    pass

struct_mHist_setting_V21_s.__slots__ = [
    'en',
    'hist_para_en',
    'HistData',
]
struct_mHist_setting_V21_s._fields_ = [
    ('en', c_bool),
    ('hist_para_en', c_bool),
    ('HistData', mHistDataV21_t),
]

mHist_setting_V21_t = struct_mHist_setting_V21_s# /root/camera_engine_rkaiq/include/iq_parser_v2/adehaze_uapi_head.h: 127

# /root/camera_engine_rkaiq/include/iq_parser_v2/adehaze_uapi_head.h: 140
class struct_mDehazeAttr_s(Structure):
    pass

struct_mDehazeAttr_s.__slots__ = [
    'Enable',
    'cfg_alpha',
    'dehaze_setting',
    'enhance_setting',
    'hist_setting',
]
struct_mDehazeAttr_s._fields_ = [
    ('Enable', c_bool),
    ('cfg_alpha', c_float),
    ('dehaze_setting', mDehaze_Setting_V21_t),
    ('enhance_setting', mEnhance_Setting_V21_t),
    ('hist_setting', mHist_setting_V21_t),
]

mDehazeAttr_t = struct_mDehazeAttr_s# /root/camera_engine_rkaiq/include/iq_parser_v2/adehaze_uapi_head.h: 140

# /root/camera_engine_rkaiq/include/iq_parser_v2/adehaze_uapi_head.h: 187
class struct_aDehazeDataV21_s(Structure):
    pass

struct_aDehazeDataV21_s.__slots__ = [
    'CtrlData',
    'dc_min_th',
    'dc_max_th',
    'yhist_th',
    'yblk_th',
    'dark_th',
    'bright_min',
    'bright_max',
    'wt_max',
    'air_min',
    'air_max',
    'tmax_base',
    'tmax_off',
    'tmax_max',
    'cfg_wt',
    'cfg_air',
    'cfg_tmax',
    'dc_weitcur',
    'bf_weight',
    'range_sigma',
    'space_sigma_pre',
    'space_sigma_cur',
]
struct_aDehazeDataV21_s._fields_ = [
    ('CtrlData', c_float * int(13)),
    ('dc_min_th', c_float * int(13)),
    ('dc_max_th', c_float * int(13)),
    ('yhist_th', c_float * int(13)),
    ('yblk_th', c_float * int(13)),
    ('dark_th', c_float * int(13)),
    ('bright_min', c_float * int(13)),
    ('bright_max', c_float * int(13)),
    ('wt_max', c_float * int(13)),
    ('air_min', c_float * int(13)),
    ('air_max', c_float * int(13)),
    ('tmax_base', c_float * int(13)),
    ('tmax_off', c_float * int(13)),
    ('tmax_max', c_float * int(13)),
    ('cfg_wt', c_float * int(13)),
    ('cfg_air', c_float * int(13)),
    ('cfg_tmax', c_float * int(13)),
    ('dc_weitcur', c_float * int(13)),
    ('bf_weight', c_float * int(13)),
    ('range_sigma', c_float * int(13)),
    ('space_sigma_pre', c_float * int(13)),
    ('space_sigma_cur', c_float * int(13)),
]

aDehazeDataV21_t = struct_aDehazeDataV21_s# /root/camera_engine_rkaiq/include/iq_parser_v2/adehaze_uapi_head.h: 187

# /root/camera_engine_rkaiq/include/iq_parser_v2/adehaze_uapi_head.h: 208
class struct_aDehaze_Setting_V21_s(Structure):
    pass

struct_aDehaze_Setting_V21_s.__slots__ = [
    'en',
    'air_lc_en',
    'stab_fnum',
    'sigma',
    'wt_sigma',
    'air_sigma',
    'tmax_sigma',
    'pre_wet',
    'DehazeData',
]
struct_aDehaze_Setting_V21_s._fields_ = [
    ('en', c_bool),
    ('air_lc_en', c_bool),
    ('stab_fnum', c_float),
    ('sigma', c_float),
    ('wt_sigma', c_float),
    ('air_sigma', c_float),
    ('tmax_sigma', c_float),
    ('pre_wet', c_float),
    ('DehazeData', aDehazeDataV21_t),
]

aDehaze_Setting_V21_t = struct_aDehaze_Setting_V21_s# /root/camera_engine_rkaiq/include/iq_parser_v2/adehaze_uapi_head.h: 208

# /root/camera_engine_rkaiq/include/iq_parser_v2/adehaze_uapi_head.h: 217
class struct_aEnhanceDataV21_s(Structure):
    pass

struct_aEnhanceDataV21_s.__slots__ = [
    'CtrlData',
    'enhance_value',
    'enhance_chroma',
]
struct_aEnhanceDataV21_s._fields_ = [
    ('CtrlData', c_float * int(13)),
    ('enhance_value', c_float * int(13)),
    ('enhance_chroma', c_float * int(13)),
]

aEnhanceDataV21_t = struct_aEnhanceDataV21_s# /root/camera_engine_rkaiq/include/iq_parser_v2/adehaze_uapi_head.h: 217

# /root/camera_engine_rkaiq/include/iq_parser_v2/adehaze_uapi_head.h: 226
class struct_aEnhance_Setting_V21_s(Structure):
    pass

struct_aEnhance_Setting_V21_s.__slots__ = [
    'en',
    'enhance_curve',
    'EnhanceData',
]
struct_aEnhance_Setting_V21_s._fields_ = [
    ('en', c_bool),
    ('enhance_curve', c_float * int(17)),
    ('EnhanceData', aEnhanceDataV21_t),
]

aEnhance_Setting_V21_t = struct_aEnhance_Setting_V21_s# /root/camera_engine_rkaiq/include/iq_parser_v2/adehaze_uapi_head.h: 226

# /root/camera_engine_rkaiq/include/iq_parser_v2/adehaze_uapi_head.h: 243
class struct_aHistDataV21_s(Structure):
    pass

struct_aHistDataV21_s.__slots__ = [
    'CtrlData',
    'hist_gratio',
    'hist_th_off',
    'hist_k',
    'hist_min',
    'hist_scale',
    'cfg_gratio',
]
struct_aHistDataV21_s._fields_ = [
    ('CtrlData', c_float * int(13)),
    ('hist_gratio', c_float * int(13)),
    ('hist_th_off', c_float * int(13)),
    ('hist_k', c_float * int(13)),
    ('hist_min', c_float * int(13)),
    ('hist_scale', c_float * int(13)),
    ('cfg_gratio', c_float * int(13)),
]

aHistDataV21_t = struct_aHistDataV21_s# /root/camera_engine_rkaiq/include/iq_parser_v2/adehaze_uapi_head.h: 243

# /root/camera_engine_rkaiq/include/iq_parser_v2/adehaze_uapi_head.h: 252
class struct_aHist_setting_V21_s(Structure):
    pass

struct_aHist_setting_V21_s.__slots__ = [
    'en',
    'hist_para_en',
    'HistData',
]
struct_aHist_setting_V21_s._fields_ = [
    ('en', c_bool),
    ('hist_para_en', c_bool),
    ('HistData', aHistDataV21_t),
]

aHist_setting_V21_t = struct_aHist_setting_V21_s# /root/camera_engine_rkaiq/include/iq_parser_v2/adehaze_uapi_head.h: 252

# /root/camera_engine_rkaiq/include/iq_parser_v2/adehaze_uapi_head.h: 269
class struct_aDehazeAttrData_s(Structure):
    pass

struct_aDehazeAttrData_s.__slots__ = [
    'Enable',
    'CtrlDataType',
    'cfg_alpha',
    'ByPassThr',
    'dehaze_setting',
    'enhance_setting',
    'hist_setting',
]
struct_aDehazeAttrData_s._fields_ = [
    ('Enable', c_bool),
    ('CtrlDataType', CtrlDataType_t),
    ('cfg_alpha', c_float),
    ('ByPassThr', c_float),
    ('dehaze_setting', aDehaze_Setting_V21_t),
    ('enhance_setting', aEnhance_Setting_V21_t),
    ('hist_setting', aHist_setting_V21_t),
]

aDehazeAttrData_t = struct_aDehazeAttrData_s# /root/camera_engine_rkaiq/include/iq_parser_v2/adehaze_uapi_head.h: 269

# /root/camera_engine_rkaiq/include/iq_parser_v2/adehaze_uapi_head.h: 274
class struct_aDehazeAttr_s(Structure):
    pass

struct_aDehazeAttr_s.__slots__ = [
    'DehazeTuningPara',
]
struct_aDehazeAttr_s._fields_ = [
    ('DehazeTuningPara', aDehazeAttrData_t),
]

aDehazeAttr_t = struct_aDehazeAttr_s# /root/camera_engine_rkaiq/include/iq_parser_v2/adehaze_uapi_head.h: 274

enum_dehaze_api_mode_s = c_int# /root/camera_engine_rkaiq/include/algos/adehaze/rk_aiq_types_adehaze_algo_int.h: 37

dehaze_api_mode_t = enum_dehaze_api_mode_s# /root/camera_engine_rkaiq/include/algos/adehaze/rk_aiq_types_adehaze_algo_int.h: 37

# /root/camera_engine_rkaiq/include/algos/adehaze/rk_aiq_types_adehaze_algo_int.h: 42
class struct_DehazeManuAttr_s(Structure):
    pass

struct_DehazeManuAttr_s.__slots__ = [
    'update',
    'level',
]
struct_DehazeManuAttr_s._fields_ = [
    ('update', c_bool),
    ('level', c_int),
]

DehazeManuAttr_t = struct_DehazeManuAttr_s# /root/camera_engine_rkaiq/include/algos/adehaze/rk_aiq_types_adehaze_algo_int.h: 42

# /root/camera_engine_rkaiq/include/algos/adehaze/rk_aiq_types_adehaze_algo_int.h: 47
class struct_EnhanceManuAttr_s(Structure):
    pass

struct_EnhanceManuAttr_s.__slots__ = [
    'update',
    'level',
]
struct_EnhanceManuAttr_s._fields_ = [
    ('update', c_bool),
    ('level', c_int),
]

EnhanceManuAttr_t = struct_EnhanceManuAttr_s# /root/camera_engine_rkaiq/include/algos/adehaze/rk_aiq_types_adehaze_algo_int.h: 47

# /root/camera_engine_rkaiq/include/algos/adehaze/rk_aiq_types_adehaze_algo_int.h: 57
class struct_adehaze_sw_V2_s(Structure):
    pass

struct_adehaze_sw_V2_s.__slots__ = [
    'sync',
    'mode',
    'stAuto',
    'stManual',
    'stDehazeManu',
    'stEnhanceManu',
]
struct_adehaze_sw_V2_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('mode', dehaze_api_mode_t),
    ('stAuto', aDehazeAttr_t),
    ('stManual', mDehazeAttr_t),
    ('stDehazeManu', DehazeManuAttr_t),
    ('stEnhanceManu', EnhanceManuAttr_t),
]

adehaze_sw_V2_t = struct_adehaze_sw_V2_s# /root/camera_engine_rkaiq/include/algos/adehaze/rk_aiq_types_adehaze_algo_int.h: 57

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_adehaze.h: 30
if _libs["rkaiq"].has("rk_aiq_user_api2_adehaze_setSwAttrib", "cdecl"):
    rk_aiq_user_api2_adehaze_setSwAttrib = _libs["rkaiq"].get("rk_aiq_user_api2_adehaze_setSwAttrib", "cdecl")
    rk_aiq_user_api2_adehaze_setSwAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), adehaze_sw_V2_t]
    rk_aiq_user_api2_adehaze_setSwAttrib.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_adehaze.h: 31
if _libs["rkaiq"].has("rk_aiq_user_api2_adehaze_getSwAttrib", "cdecl"):
    rk_aiq_user_api2_adehaze_getSwAttrib = _libs["rkaiq"].get("rk_aiq_user_api2_adehaze_getSwAttrib", "cdecl")
    rk_aiq_user_api2_adehaze_getSwAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(adehaze_sw_V2_t)]
    rk_aiq_user_api2_adehaze_getSwAttrib.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_adpcc.h: 31
if _libs["rkaiq"].has("rk_aiq_user_api2_adpcc_SetAttrib", "cdecl"):
    rk_aiq_user_api2_adpcc_SetAttrib = _libs["rkaiq"].get("rk_aiq_user_api2_adpcc_SetAttrib", "cdecl")
    rk_aiq_user_api2_adpcc_SetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_dpcc_attrib_V20_t)]
    rk_aiq_user_api2_adpcc_SetAttrib.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_adpcc.h: 33
if _libs["rkaiq"].has("rk_aiq_user_api2_adpcc_GetAttrib", "cdecl"):
    rk_aiq_user_api2_adpcc_GetAttrib = _libs["rkaiq"].get("rk_aiq_user_api2_adpcc_GetAttrib", "cdecl")
    rk_aiq_user_api2_adpcc_GetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_dpcc_attrib_V20_t)]
    rk_aiq_user_api2_adpcc_GetAttrib.restype = XCamReturn

enum_CompressMode_e = c_int# /root/camera_engine_rkaiq/include/iq_parser_v2/adrc_head.h: 91

CompressMode_t = enum_CompressMode_e# /root/camera_engine_rkaiq/include/iq_parser_v2/adrc_head.h: 91

# /root/camera_engine_rkaiq/include/iq_parser_v2/adrc_head.h: 98
class struct_Compress_s(Structure):
    pass

struct_Compress_s.__slots__ = [
    'Mode',
    'Manual_curve',
]
struct_Compress_s._fields_ = [
    ('Mode', CompressMode_t),
    ('Manual_curve', uint16_t * int(17)),
]

Compress_t = struct_Compress_s# /root/camera_engine_rkaiq/include/iq_parser_v2/adrc_head.h: 98

# /root/camera_engine_rkaiq/include/iq_parser_v2/adrc_uapi_head.h: 30
class struct_mDrcGain_t(Structure):
    pass

struct_mDrcGain_t.__slots__ = [
    'DrcGain',
    'Alpha',
    'Clip',
]
struct_mDrcGain_t._fields_ = [
    ('DrcGain', c_float),
    ('Alpha', c_float),
    ('Clip', c_float),
]

mDrcGain_t = struct_mDrcGain_t# /root/camera_engine_rkaiq/include/iq_parser_v2/adrc_uapi_head.h: 30

# /root/camera_engine_rkaiq/include/iq_parser_v2/adrc_uapi_head.h: 35
class struct_mDrcHiLit_s(Structure):
    pass

struct_mDrcHiLit_s.__slots__ = [
    'Strength',
]
struct_mDrcHiLit_s._fields_ = [
    ('Strength', c_float),
]

mDrcHiLit_t = struct_mDrcHiLit_s# /root/camera_engine_rkaiq/include/iq_parser_v2/adrc_uapi_head.h: 35

# /root/camera_engine_rkaiq/include/iq_parser_v2/adrc_uapi_head.h: 44
class struct_mLocalDataV21_s(Structure):
    pass

struct_mLocalDataV21_s.__slots__ = [
    'LocalWeit',
    'GlobalContrast',
    'LoLitContrast',
]
struct_mLocalDataV21_s._fields_ = [
    ('LocalWeit', c_float),
    ('GlobalContrast', c_float),
    ('LoLitContrast', c_float),
]

mLocalDataV21_t = struct_mLocalDataV21_s# /root/camera_engine_rkaiq/include/iq_parser_v2/adrc_uapi_head.h: 44

# /root/camera_engine_rkaiq/include/iq_parser_v2/adrc_uapi_head.h: 63
class struct_mDrcLocalV21_s(Structure):
    pass

struct_mDrcLocalV21_s.__slots__ = [
    'LocalData',
    'curPixWeit',
    'preFrameWeit',
    'Range_force_sgm',
    'Range_sgm_cur',
    'Range_sgm_pre',
    'Space_sgm_cur',
    'Space_sgm_pre',
]
struct_mDrcLocalV21_s._fields_ = [
    ('LocalData', mLocalDataV21_t),
    ('curPixWeit', c_float),
    ('preFrameWeit', c_float),
    ('Range_force_sgm', c_float),
    ('Range_sgm_cur', c_float),
    ('Range_sgm_pre', c_float),
    ('Space_sgm_cur', c_int),
    ('Space_sgm_pre', c_int),
]

mDrcLocalV21_t = struct_mDrcLocalV21_s# /root/camera_engine_rkaiq/include/iq_parser_v2/adrc_uapi_head.h: 63

# /root/camera_engine_rkaiq/include/iq_parser_v2/adrc_uapi_head.h: 70
class struct_mDrcCompress_s(Structure):
    pass

struct_mDrcCompress_s.__slots__ = [
    'Mode',
    'Manual_curve',
]
struct_mDrcCompress_s._fields_ = [
    ('Mode', CompressMode_t),
    ('Manual_curve', uint16_t * int(17)),
]

mDrcCompress_t = struct_mDrcCompress_s# /root/camera_engine_rkaiq/include/iq_parser_v2/adrc_uapi_head.h: 70

# /root/camera_engine_rkaiq/include/iq_parser_v2/adrc_uapi_head.h: 91
class struct_mdrcAttr_V21_s(Structure):
    pass

struct_mdrcAttr_V21_s.__slots__ = [
    'Enable',
    'DrcGain',
    'HiLit',
    'LocalSetting',
    'Compress',
    'Scale_y',
    'Edge_Weit',
    'OutPutLongFrame',
    'IIR_frame',
]
struct_mdrcAttr_V21_s._fields_ = [
    ('Enable', c_bool),
    ('DrcGain', mDrcGain_t),
    ('HiLit', mDrcHiLit_t),
    ('LocalSetting', mDrcLocalV21_t),
    ('Compress', mDrcCompress_t),
    ('Scale_y', c_int * int(17)),
    ('Edge_Weit', c_float),
    ('OutPutLongFrame', c_bool),
    ('IIR_frame', c_int),
]

mdrcAttr_V21_t = struct_mdrcAttr_V21_s# /root/camera_engine_rkaiq/include/iq_parser_v2/adrc_uapi_head.h: 91

# /root/camera_engine_rkaiq/include/iq_parser_v2/adrc_uapi_head.h: 104
class struct_mLocalDataV30_s(Structure):
    pass

struct_mLocalDataV30_s.__slots__ = [
    'LocalWeit',
    'LocalAutoEnable',
    'LocalAutoWeit',
    'GlobalContrast',
    'LoLitContrast',
]
struct_mLocalDataV30_s._fields_ = [
    ('LocalWeit', c_float),
    ('LocalAutoEnable', c_int),
    ('LocalAutoWeit', c_float),
    ('GlobalContrast', c_float),
    ('LoLitContrast', c_float),
]

mLocalDataV30_t = struct_mLocalDataV30_s# /root/camera_engine_rkaiq/include/iq_parser_v2/adrc_uapi_head.h: 104

# /root/camera_engine_rkaiq/include/iq_parser_v2/adrc_uapi_head.h: 123
class struct_mDrcLocalV30_s(Structure):
    pass

struct_mDrcLocalV30_s.__slots__ = [
    'LocalData',
    'curPixWeit',
    'preFrameWeit',
    'Range_force_sgm',
    'Range_sgm_cur',
    'Range_sgm_pre',
    'Space_sgm_cur',
    'Space_sgm_pre',
]
struct_mDrcLocalV30_s._fields_ = [
    ('LocalData', mLocalDataV30_t),
    ('curPixWeit', c_float),
    ('preFrameWeit', c_float),
    ('Range_force_sgm', c_float),
    ('Range_sgm_cur', c_float),
    ('Range_sgm_pre', c_float),
    ('Space_sgm_cur', c_int),
    ('Space_sgm_pre', c_int),
]

mDrcLocalV30_t = struct_mDrcLocalV30_s# /root/camera_engine_rkaiq/include/iq_parser_v2/adrc_uapi_head.h: 123

# /root/camera_engine_rkaiq/include/iq_parser_v2/adrc_uapi_head.h: 144
class struct_mdrcAttr_V30_s(Structure):
    pass

struct_mdrcAttr_V30_s.__slots__ = [
    'Enable',
    'DrcGain',
    'HiLight',
    'LocalSetting',
    'CompressSetting',
    'Scale_y',
    'Edge_Weit',
    'OutPutLongFrame',
    'IIR_frame',
]
struct_mdrcAttr_V30_s._fields_ = [
    ('Enable', c_bool),
    ('DrcGain', mDrcGain_t),
    ('HiLight', mDrcHiLit_t),
    ('LocalSetting', mDrcLocalV30_t),
    ('CompressSetting', mDrcCompress_t),
    ('Scale_y', c_int * int(17)),
    ('Edge_Weit', c_float),
    ('OutPutLongFrame', c_bool),
    ('IIR_frame', c_int),
]

mdrcAttr_V30_t = struct_mdrcAttr_V30_s# /root/camera_engine_rkaiq/include/iq_parser_v2/adrc_uapi_head.h: 144

# /root/camera_engine_rkaiq/include/iq_parser_v2/adrc_uapi_head.h: 155
class struct_stAutoDrcGain_s(Structure):
    pass

struct_stAutoDrcGain_s.__slots__ = [
    'CtrlData',
    'DrcGain',
    'Alpha',
    'Clip',
]
struct_stAutoDrcGain_s._fields_ = [
    ('CtrlData', c_float * int(13)),
    ('DrcGain', c_float * int(13)),
    ('Alpha', c_float * int(13)),
    ('Clip', c_float * int(13)),
]

stAutoDrcGain_t = struct_stAutoDrcGain_s# /root/camera_engine_rkaiq/include/iq_parser_v2/adrc_uapi_head.h: 155

# /root/camera_engine_rkaiq/include/iq_parser_v2/adrc_uapi_head.h: 162
class struct_stAutoDrcHiLit_s(Structure):
    pass

struct_stAutoDrcHiLit_s.__slots__ = [
    'CtrlData',
    'Strength',
]
struct_stAutoDrcHiLit_s._fields_ = [
    ('CtrlData', c_float * int(13)),
    ('Strength', c_float * int(13)),
]

stAutoDrcHiLit_t = struct_stAutoDrcHiLit_s# /root/camera_engine_rkaiq/include/iq_parser_v2/adrc_uapi_head.h: 162

# /root/camera_engine_rkaiq/include/iq_parser_v2/adrc_uapi_head.h: 177
class struct_stAutoLocalDataV30_s(Structure):
    pass

struct_stAutoLocalDataV30_s.__slots__ = [
    'CtrlData',
    'LocalWeit',
    'LocalAutoEnable',
    'LocalAutoWeit',
    'GlobalContrast',
    'LoLitContrast',
]
struct_stAutoLocalDataV30_s._fields_ = [
    ('CtrlData', c_float * int(13)),
    ('LocalWeit', c_float * int(13)),
    ('LocalAutoEnable', c_int * int(13)),
    ('LocalAutoWeit', c_float * int(13)),
    ('GlobalContrast', c_float * int(13)),
    ('LoLitContrast', c_float * int(13)),
]

stAutoLocalDataV30_t = struct_stAutoLocalDataV30_s# /root/camera_engine_rkaiq/include/iq_parser_v2/adrc_uapi_head.h: 177

# /root/camera_engine_rkaiq/include/iq_parser_v2/adrc_uapi_head.h: 196
class struct_stAutoDrcLocalV30_s(Structure):
    pass

struct_stAutoDrcLocalV30_s.__slots__ = [
    'LocalData',
    'curPixWeit',
    'preFrameWeit',
    'Range_force_sgm',
    'Range_sgm_cur',
    'Range_sgm_pre',
    'Space_sgm_cur',
    'Space_sgm_pre',
]
struct_stAutoDrcLocalV30_s._fields_ = [
    ('LocalData', stAutoLocalDataV30_t),
    ('curPixWeit', c_float),
    ('preFrameWeit', c_float),
    ('Range_force_sgm', c_float),
    ('Range_sgm_cur', c_float),
    ('Range_sgm_pre', c_float),
    ('Space_sgm_cur', c_int),
    ('Space_sgm_pre', c_int),
]

stAutoDrcLocalV30_t = struct_stAutoDrcLocalV30_s# /root/camera_engine_rkaiq/include/iq_parser_v2/adrc_uapi_head.h: 196

# /root/camera_engine_rkaiq/include/iq_parser_v2/adrc_uapi_head.h: 225
class struct_adrcAttrData_V30_s(Structure):
    pass

struct_adrcAttrData_V30_s.__slots__ = [
    'Enable',
    'CtrlDataType',
    'DrcGain',
    'HiLight',
    'LocalSetting',
    'CompressSetting',
    'Scale_y',
    'ByPassThr',
    'Edge_Weit',
    'OutPutLongFrame',
    'IIR_frame',
    'Tolerance',
    'damp',
]
struct_adrcAttrData_V30_s._fields_ = [
    ('Enable', c_bool),
    ('CtrlDataType', CtrlDataType_t),
    ('DrcGain', stAutoDrcGain_t),
    ('HiLight', stAutoDrcHiLit_t),
    ('LocalSetting', stAutoDrcLocalV30_t),
    ('CompressSetting', Compress_t),
    ('Scale_y', c_int * int(17)),
    ('ByPassThr', c_float),
    ('Edge_Weit', c_float),
    ('OutPutLongFrame', c_bool),
    ('IIR_frame', c_int),
    ('Tolerance', c_float),
    ('damp', c_float),
]

adrcAttrData_V30_t = struct_adrcAttrData_V30_s# /root/camera_engine_rkaiq/include/iq_parser_v2/adrc_uapi_head.h: 225

# /root/camera_engine_rkaiq/include/iq_parser_v2/adrc_uapi_head.h: 230
class struct_adrcAttr_V30_s(Structure):
    pass

struct_adrcAttr_V30_s.__slots__ = [
    'DrcTuningPara',
]
struct_adrcAttr_V30_s._fields_ = [
    ('DrcTuningPara', adrcAttrData_V30_t),
]

adrcAttr_V30_t = struct_adrcAttr_V30_s# /root/camera_engine_rkaiq/include/iq_parser_v2/adrc_uapi_head.h: 230

# /root/camera_engine_rkaiq/include/iq_parser_v2/adrc_uapi_head.h: 241
class struct_stAutoLocalDataV21_s(Structure):
    pass

struct_stAutoLocalDataV21_s.__slots__ = [
    'CtrlData',
    'LocalWeit',
    'GlobalContrast',
    'LoLitContrast',
]
struct_stAutoLocalDataV21_s._fields_ = [
    ('CtrlData', c_float * int(13)),
    ('LocalWeit', c_float * int(13)),
    ('GlobalContrast', c_float * int(13)),
    ('LoLitContrast', c_float * int(13)),
]

stAutoLocalDataV21_t = struct_stAutoLocalDataV21_s# /root/camera_engine_rkaiq/include/iq_parser_v2/adrc_uapi_head.h: 241

# /root/camera_engine_rkaiq/include/iq_parser_v2/adrc_uapi_head.h: 260
class struct_stAutoDrcLocalV21_s(Structure):
    pass

struct_stAutoDrcLocalV21_s.__slots__ = [
    'LocalTMOData',
    'curPixWeit',
    'preFrameWeit',
    'Range_force_sgm',
    'Range_sgm_cur',
    'Range_sgm_pre',
    'Space_sgm_cur',
    'Space_sgm_pre',
]
struct_stAutoDrcLocalV21_s._fields_ = [
    ('LocalTMOData', stAutoLocalDataV21_t),
    ('curPixWeit', c_float),
    ('preFrameWeit', c_float),
    ('Range_force_sgm', c_float),
    ('Range_sgm_cur', c_float),
    ('Range_sgm_pre', c_float),
    ('Space_sgm_cur', c_int),
    ('Space_sgm_pre', c_int),
]

stAutoDrcLocalV21_t = struct_stAutoDrcLocalV21_s# /root/camera_engine_rkaiq/include/iq_parser_v2/adrc_uapi_head.h: 260

# /root/camera_engine_rkaiq/include/iq_parser_v2/adrc_uapi_head.h: 289
class struct_adrcAttrData_V21_s(Structure):
    pass

struct_adrcAttrData_V21_s.__slots__ = [
    'Enable',
    'CtrlDataType',
    'DrcGain',
    'HiLight',
    'LocalTMOSetting',
    'CompressSetting',
    'Scale_y',
    'ByPassThr',
    'Edge_Weit',
    'OutPutLongFrame',
    'IIR_frame',
    'Tolerance',
    'damp',
]
struct_adrcAttrData_V21_s._fields_ = [
    ('Enable', c_bool),
    ('CtrlDataType', CtrlDataType_t),
    ('DrcGain', stAutoDrcGain_t),
    ('HiLight', stAutoDrcHiLit_t),
    ('LocalTMOSetting', stAutoDrcLocalV21_t),
    ('CompressSetting', Compress_t),
    ('Scale_y', c_int * int(17)),
    ('ByPassThr', c_float),
    ('Edge_Weit', c_float),
    ('OutPutLongFrame', c_bool),
    ('IIR_frame', c_int),
    ('Tolerance', c_float),
    ('damp', c_float),
]

adrcAttrData_V21_t = struct_adrcAttrData_V21_s# /root/camera_engine_rkaiq/include/iq_parser_v2/adrc_uapi_head.h: 289

# /root/camera_engine_rkaiq/include/iq_parser_v2/adrc_uapi_head.h: 294
class struct_adrcAttr_V21_s(Structure):
    pass

struct_adrcAttr_V21_s.__slots__ = [
    'DrcTuningPara',
]
struct_adrcAttr_V21_s._fields_ = [
    ('DrcTuningPara', adrcAttrData_V21_t),
]

adrcAttr_V21_t = struct_adrcAttr_V21_s# /root/camera_engine_rkaiq/include/iq_parser_v2/adrc_uapi_head.h: 294

# /root/camera_engine_rkaiq/include/iq_parser_v2/adrc_uapi_head.h: 301
class struct_DrcCtrlInfo_s(Structure):
    pass

struct_DrcCtrlInfo_s.__slots__ = [
    'EnvLv',
    'ISO',
]
struct_DrcCtrlInfo_s._fields_ = [
    ('EnvLv', c_float),
    ('ISO', c_float),
]

DrcCtrlInfo_t = struct_DrcCtrlInfo_s# /root/camera_engine_rkaiq/include/iq_parser_v2/adrc_uapi_head.h: 301

# /root/camera_engine_rkaiq/include/iq_parser_v2/adrc_uapi_head.h: 310
class struct_DrcInfo_s(Structure):
    pass

struct_DrcInfo_s.__slots__ = [
    'CtrlInfo',
    'ValidParamsV21',
    'ValidParamsV30',
]
struct_DrcInfo_s._fields_ = [
    ('CtrlInfo', DrcCtrlInfo_t),
    ('ValidParamsV21', mdrcAttr_V21_t),
    ('ValidParamsV30', mdrcAttr_V30_t),
]

DrcInfo_t = struct_DrcInfo_s# /root/camera_engine_rkaiq/include/iq_parser_v2/adrc_uapi_head.h: 310

enum_AdrcVersion_e = c_int# /root/camera_engine_rkaiq/include/algos/adrc/rk_aiq_types_adrc_algo_int.h: 97

AdrcVersion_t = enum_AdrcVersion_e# /root/camera_engine_rkaiq/include/algos/adrc/rk_aiq_types_adrc_algo_int.h: 97

enum_drc_OpMode_s = c_int# /root/camera_engine_rkaiq/include/algos/adrc/rk_aiq_types_adrc_algo_int.h: 102

drc_OpMode_t = enum_drc_OpMode_s# /root/camera_engine_rkaiq/include/algos/adrc/rk_aiq_types_adrc_algo_int.h: 102

# /root/camera_engine_rkaiq/include/algos/adrc/rk_aiq_types_adrc_algo_int.h: 114
class struct_drcAttr_s(Structure):
    pass

struct_drcAttr_s.__slots__ = [
    'sync',
    'Version',
    'opMode',
    'stAutoV21',
    'stAutoV30',
    'stManualV21',
    'stManualV30',
    'Info',
]
struct_drcAttr_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('Version', AdrcVersion_t),
    ('opMode', drc_OpMode_t),
    ('stAutoV21', adrcAttr_V21_t),
    ('stAutoV30', adrcAttr_V30_t),
    ('stManualV21', mdrcAttr_V21_t),
    ('stManualV30', mdrcAttr_V30_t),
    ('Info', DrcInfo_t),
]

drcAttr_t = struct_drcAttr_s# /root/camera_engine_rkaiq/include/algos/adrc/rk_aiq_types_adrc_algo_int.h: 114

drc_attrib_t = drcAttr_t# /root/camera_engine_rkaiq/include/algos/adrc/rk_aiq_uapi_adrc_int.h: 9

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_adrc.h: 31
if _libs["rkaiq"].has("rk_aiq_user_api2_adrc_SetAttrib", "cdecl"):
    rk_aiq_user_api2_adrc_SetAttrib = _libs["rkaiq"].get("rk_aiq_user_api2_adrc_SetAttrib", "cdecl")
    rk_aiq_user_api2_adrc_SetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), drc_attrib_t]
    rk_aiq_user_api2_adrc_SetAttrib.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_adrc.h: 33
if _libs["rkaiq"].has("rk_aiq_user_api2_adrc_GetAttrib", "cdecl"):
    rk_aiq_user_api2_adrc_GetAttrib = _libs["rkaiq"].get("rk_aiq_user_api2_adrc_GetAttrib", "cdecl")
    rk_aiq_user_api2_adrc_GetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(drc_attrib_t)]
    rk_aiq_user_api2_adrc_GetAttrib.restype = XCamReturn

enum__CalibDb_HdrAeRatioTypeV2_e = c_int# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_head.h: 46

CalibDb_HdrAeRatioTypeV2_t = enum__CalibDb_HdrAeRatioTypeV2_e# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_head.h: 46

enum__CalibDb_AeStrategyModeV2_e = c_int# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_head.h: 51

CalibDb_AeStrategyModeV2_t = enum__CalibDb_AeStrategyModeV2_e# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_head.h: 51

enum__CalibDb_AeHdrLongFrmModeV2_e = c_int# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_head.h: 57

CalibDb_AeHdrLongFrmModeV2_t = enum__CalibDb_AeHdrLongFrmModeV2_e# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_head.h: 57

enum__CalibDb_AecMeasAreaModeV2_e = c_int# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_head.h: 66

CalibDb_AecMeasAreaModeV2_t = enum__CalibDb_AecMeasAreaModeV2_e# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_head.h: 66

enum__CalibDb_FlickerFreqV2_e = c_int# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_head.h: 72

CalibDb_FlickerFreqV2_t = enum__CalibDb_FlickerFreqV2_e# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_head.h: 72

enum__CalibDb_AntiFlickerModeV2_e = c_int# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_head.h: 77

CalibDb_AntiFlickerModeV2_t = enum__CalibDb_AntiFlickerModeV2_e# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_head.h: 77

enum__CalibDb_IrisTypeV2_e = c_int# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_head.h: 82

CalibDb_IrisTypeV2_t = enum__CalibDb_IrisTypeV2_e# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_head.h: 82

enum__CalibDb_CamYRangeModeV2_e = c_int# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_head.h: 89

CalibDb_CamYRangeModeV2_t = enum__CalibDb_CamYRangeModeV2_e# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_head.h: 89

enum__CalibDb_CamRawStatsModeV2_e = c_int# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_head.h: 98

CalibDb_CamRawStatsModeV2_t = enum__CalibDb_CamRawStatsModeV2_e# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_head.h: 98

enum__CalibDb_CamHistStatsModeV2_e = c_int# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_head.h: 108

CalibDb_CamHistStatsModeV2_t = enum__CalibDb_CamHistStatsModeV2_e# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_head.h: 108

# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_head.h: 139
class struct_CalibDb_AeSpeedV2_s(Structure):
    pass

struct_CalibDb_AeSpeedV2_s.__slots__ = [
    'SmoothEn',
    'DyDampEn',
    'DampOver',
    'DampUnder',
    'DampDark2Bright',
    'DampBright2Dark',
]
struct_CalibDb_AeSpeedV2_s._fields_ = [
    ('SmoothEn', c_bool),
    ('DyDampEn', c_bool),
    ('DampOver', c_float),
    ('DampUnder', c_float),
    ('DampDark2Bright', c_float),
    ('DampBright2Dark', c_float),
]

CalibDb_AeSpeedV2_t = struct_CalibDb_AeSpeedV2_s# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_head.h: 139

# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_head.h: 147
class struct_CalibDb_AeFrmRateAttrV2_s(Structure):
    pass

struct_CalibDb_AeFrmRateAttrV2_s.__slots__ = [
    'isFpsFix',
    'FpsValue',
]
struct_CalibDb_AeFrmRateAttrV2_s._fields_ = [
    ('isFpsFix', c_bool),
    ('FpsValue', c_float),
]

CalibDb_AeFrmRateAttrV2_t = struct_CalibDb_AeFrmRateAttrV2_s# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_head.h: 147

# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_head.h: 158
class struct_CalibDb_AntiFlickerAttrV2_s(Structure):
    pass

struct_CalibDb_AntiFlickerAttrV2_s.__slots__ = [
    'enable',
    'Frequency',
    'Mode',
]
struct_CalibDb_AntiFlickerAttrV2_s._fields_ = [
    ('enable', c_bool),
    ('Frequency', CalibDb_FlickerFreqV2_t),
    ('Mode', CalibDb_AntiFlickerModeV2_t),
]

CalibDb_AntiFlickerAttrV2_t = struct_CalibDb_AntiFlickerAttrV2_s# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_head.h: 158

# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_head.h: 308
class struct_CalibDb_LinExpInitExpV2_s(Structure):
    pass

struct_CalibDb_LinExpInitExpV2_s.__slots__ = [
    'InitTimeValue',
    'InitGainValue',
    'InitIspDGainValue',
    'InitPIrisGainValue',
    'InitDCIrisDutyValue',
]
struct_CalibDb_LinExpInitExpV2_s._fields_ = [
    ('InitTimeValue', c_float),
    ('InitGainValue', c_float),
    ('InitIspDGainValue', c_float),
    ('InitPIrisGainValue', c_int),
    ('InitDCIrisDutyValue', c_int),
]

CalibDb_LinExpInitExpV2_t = struct_CalibDb_LinExpInitExpV2_s# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_head.h: 308

# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_head.h: 323
class struct_CalibDb_LinAeRoute_AttrV2_s(Structure):
    pass

struct_CalibDb_LinAeRoute_AttrV2_s.__slots__ = [
    'TimeDot',
    'TimeDot_len',
    'GainDot',
    'GainDot_len',
    'IspDGainDot',
    'IspDGainDot_len',
    'PIrisDot',
    'PIrisDot_len',
]
struct_CalibDb_LinAeRoute_AttrV2_s._fields_ = [
    ('TimeDot', POINTER(c_float)),
    ('TimeDot_len', c_int),
    ('GainDot', POINTER(c_float)),
    ('GainDot_len', c_int),
    ('IspDGainDot', POINTER(c_float)),
    ('IspDGainDot_len', c_int),
    ('PIrisDot', POINTER(c_int)),
    ('PIrisDot_len', c_int),
]

CalibDb_LinAeRoute_AttrV2_t = struct_CalibDb_LinAeRoute_AttrV2_s# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_head.h: 323

# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_head.h: 332
class struct_CalibDb_AecDynamicSetpointV2_s(Structure):
    pass

struct_CalibDb_AecDynamicSetpointV2_s.__slots__ = [
    'ExpLevel',
    'ExpLevel_len',
    'DySetpoint',
    'DySetpoint_len',
]
struct_CalibDb_AecDynamicSetpointV2_s._fields_ = [
    ('ExpLevel', POINTER(c_float)),
    ('ExpLevel_len', c_int),
    ('DySetpoint', POINTER(c_float)),
    ('DySetpoint_len', c_int),
]

CalibDb_AecDynamicSetpointV2_t = struct_CalibDb_AecDynamicSetpointV2_s# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_head.h: 332

# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_head.h: 347
class struct_CalibDb_BacklitSetPointV2_s(Structure):
    pass

struct_CalibDb_BacklitSetPointV2_s.__slots__ = [
    'ExpLevel',
    'ExpLevel_len',
    'NonOEPdfTh',
    'NonOEPdfTh_len',
    'LowLightPdfTh',
    'LowLightPdfTh_len',
    'TargetLLLuma',
    'TargetLLLuma_len',
]
struct_CalibDb_BacklitSetPointV2_s._fields_ = [
    ('ExpLevel', POINTER(c_float)),
    ('ExpLevel_len', c_int),
    ('NonOEPdfTh', POINTER(c_float)),
    ('NonOEPdfTh_len', c_int),
    ('LowLightPdfTh', POINTER(c_float)),
    ('LowLightPdfTh_len', c_int),
    ('TargetLLLuma', POINTER(c_float)),
    ('TargetLLLuma_len', c_int),
]

CalibDb_BacklitSetPointV2_t = struct_CalibDb_BacklitSetPointV2_s# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_head.h: 347

# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_head.h: 373
class struct_CalibDb_AecBacklightV2_s(Structure):
    pass

struct_CalibDb_AecBacklightV2_s.__slots__ = [
    'Enable',
    'StrBias',
    'MeasArea',
    'OEROILowTh',
    'LumaDistTh',
    'LvLowTh',
    'LvHighTh',
    'BacklitSetPoint',
]
struct_CalibDb_AecBacklightV2_s._fields_ = [
    ('Enable', c_bool),
    ('StrBias', c_float),
    ('MeasArea', CalibDb_AecMeasAreaModeV2_t),
    ('OEROILowTh', c_float),
    ('LumaDistTh', c_float),
    ('LvLowTh', c_float),
    ('LvHighTh', c_float),
    ('BacklitSetPoint', CalibDb_BacklitSetPointV2_t),
]

CalibDb_AecBacklightV2_t = struct_CalibDb_AecBacklightV2_s# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_head.h: 373

# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_head.h: 385
class struct_CalibDb_OverExpSetPointV2_s(Structure):
    pass

struct_CalibDb_OverExpSetPointV2_s.__slots__ = [
    'OEpdf',
    'OEpdf_len',
    'LowLightWeight',
    'LowLightWeight_len',
    'HighLightWeight',
    'HighLightWeight_len',
]
struct_CalibDb_OverExpSetPointV2_s._fields_ = [
    ('OEpdf', POINTER(c_float)),
    ('OEpdf_len', c_int),
    ('LowLightWeight', POINTER(c_float)),
    ('LowLightWeight_len', c_int),
    ('HighLightWeight', POINTER(c_float)),
    ('HighLightWeight_len', c_int),
]

CalibDb_OverExpSetPointV2_t = struct_CalibDb_OverExpSetPointV2_s# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_head.h: 385

# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_head.h: 405
class struct_CalibDb_AecOverExpCtrlV2_s(Structure):
    pass

struct_CalibDb_AecOverExpCtrlV2_s.__slots__ = [
    'Enable',
    'StrBias',
    'MaxWeight',
    'HighLightTh',
    'LowLightTh',
    'OverExpSetPoint',
]
struct_CalibDb_AecOverExpCtrlV2_s._fields_ = [
    ('Enable', c_bool),
    ('StrBias', c_float),
    ('MaxWeight', c_float),
    ('HighLightTh', c_float),
    ('LowLightTh', c_float),
    ('OverExpSetPoint', CalibDb_OverExpSetPointV2_t),
]

CalibDb_AecOverExpCtrlV2_t = struct_CalibDb_AecOverExpCtrlV2_s# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_head.h: 405

# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_head.h: 437
class struct_CalibDb_LinearAE_AttrV2_s(Structure):
    pass

struct_CalibDb_LinearAE_AttrV2_s.__slots__ = [
    'RawStatsEn',
    'ToleranceIn',
    'ToleranceOut',
    'Evbias',
    'StrategyMode',
    'InitExp',
    'Route',
    'DySetpoint',
    'BackLightCtrl',
    'OverExpCtrl',
]
struct_CalibDb_LinearAE_AttrV2_s._fields_ = [
    ('RawStatsEn', c_bool),
    ('ToleranceIn', c_float),
    ('ToleranceOut', c_float),
    ('Evbias', c_float),
    ('StrategyMode', CalibDb_AeStrategyModeV2_t),
    ('InitExp', CalibDb_LinExpInitExpV2_t),
    ('Route', CalibDb_LinAeRoute_AttrV2_t),
    ('DySetpoint', CalibDb_AecDynamicSetpointV2_t),
    ('BackLightCtrl', CalibDb_AecBacklightV2_t),
    ('OverExpCtrl', CalibDb_AecOverExpCtrlV2_t),
]

CalibDb_LinearAE_AttrV2_t = struct_CalibDb_LinearAE_AttrV2_s# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_head.h: 437

# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_head.h: 459
class struct_CalibDb_HdrExpInitExpV2_s(Structure):
    pass

struct_CalibDb_HdrExpInitExpV2_s.__slots__ = [
    'InitTimeValue',
    'InitGainValue',
    'InitIspDGainValue',
    'InitPIrisGainValue',
    'InitDCIrisDutyValue',
]
struct_CalibDb_HdrExpInitExpV2_s._fields_ = [
    ('InitTimeValue', c_float * int(3)),
    ('InitGainValue', c_float * int(3)),
    ('InitIspDGainValue', c_float * int(3)),
    ('InitPIrisGainValue', c_int),
    ('InitDCIrisDutyValue', c_int),
]

CalibDb_HdrExpInitExpV2_t = struct_CalibDb_HdrExpInitExpV2_s# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_head.h: 459

# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_head.h: 477
class struct_CalibDb_ExpRatioV2_s(Structure):
    pass

struct_CalibDb_ExpRatioV2_s.__slots__ = [
    'RatioExpDot',
    'RatioExpDot_len',
    'M2SRatioFix',
    'M2SRatioFix_len',
    'L2MRatioFix',
    'L2MRatioFix_len',
    'M2SRatioMax',
    'M2SRatioMax_len',
    'L2MRatioMax',
    'L2MRatioMax_len',
]
struct_CalibDb_ExpRatioV2_s._fields_ = [
    ('RatioExpDot', POINTER(c_float)),
    ('RatioExpDot_len', c_int),
    ('M2SRatioFix', POINTER(c_float)),
    ('M2SRatioFix_len', c_int),
    ('L2MRatioFix', POINTER(c_float)),
    ('L2MRatioFix_len', c_int),
    ('M2SRatioMax', POINTER(c_float)),
    ('M2SRatioMax_len', c_int),
    ('L2MRatioMax', POINTER(c_float)),
    ('L2MRatioMax_len', c_int),
]

CalibDb_ExpRatioV2_t = struct_CalibDb_ExpRatioV2_s# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_head.h: 477

# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_head.h: 485
class struct_CalibDb_ExpRatioCtrlV2_s(Structure):
    pass

struct_CalibDb_ExpRatioCtrlV2_s.__slots__ = [
    'ExpRatioType',
    'ExpRatio',
]
struct_CalibDb_ExpRatioCtrlV2_s._fields_ = [
    ('ExpRatioType', CalibDb_HdrAeRatioTypeV2_t),
    ('ExpRatio', CalibDb_ExpRatioV2_t),
]

CalibDb_ExpRatioCtrlV2_t = struct_CalibDb_ExpRatioCtrlV2_s# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_head.h: 485

# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_head.h: 518
class struct_CalibDb_HdrAeRoute_AttrV2_s(Structure):
    pass

struct_CalibDb_HdrAeRoute_AttrV2_s.__slots__ = [
    'Frm0TimeDot',
    'Frm0TimeDot_len',
    'Frm0GainDot',
    'Frm0GainDot_len',
    'Frm0IspDGainDot',
    'Frm0IspDGainDot_len',
    'Frm1TimeDot',
    'Frm1TimeDot_len',
    'Frm1GainDot',
    'Frm1GainDot_len',
    'Frm1IspDGainDot',
    'Frm1IspDGainDot_len',
    'Frm2TimeDot',
    'Frm2TimeDot_len',
    'Frm2GainDot',
    'Frm2GainDot_len',
    'Frm2IspDGainDot',
    'Frm2IspDGainDot_len',
    'PIrisDot',
    'PIrisDot_len',
]
struct_CalibDb_HdrAeRoute_AttrV2_s._fields_ = [
    ('Frm0TimeDot', POINTER(c_float)),
    ('Frm0TimeDot_len', c_int),
    ('Frm0GainDot', POINTER(c_float)),
    ('Frm0GainDot_len', c_int),
    ('Frm0IspDGainDot', POINTER(c_float)),
    ('Frm0IspDGainDot_len', c_int),
    ('Frm1TimeDot', POINTER(c_float)),
    ('Frm1TimeDot_len', c_int),
    ('Frm1GainDot', POINTER(c_float)),
    ('Frm1GainDot_len', c_int),
    ('Frm1IspDGainDot', POINTER(c_float)),
    ('Frm1IspDGainDot_len', c_int),
    ('Frm2TimeDot', POINTER(c_float)),
    ('Frm2TimeDot_len', c_int),
    ('Frm2GainDot', POINTER(c_float)),
    ('Frm2GainDot_len', c_int),
    ('Frm2IspDGainDot', POINTER(c_float)),
    ('Frm2IspDGainDot_len', c_int),
    ('PIrisDot', POINTER(c_int)),
    ('PIrisDot_len', c_int),
]

CalibDb_HdrAeRoute_AttrV2_t = struct_CalibDb_HdrAeRoute_AttrV2_s# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_head.h: 518

# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_head.h: 537
class struct_CalibDb_LfrmSetPointV2_s(Structure):
    pass

struct_CalibDb_LfrmSetPointV2_s.__slots__ = [
    'LExpLevel',
    'LExpLevel_len',
    'NonOEPdfTh',
    'NonOEPdfTh_len',
    'LowLightPdfTh',
    'LowLightPdfTh_len',
    'LSetPoint',
    'LSetPoint_len',
    'TargetLLLuma',
    'TargetLLLuma_len',
]
struct_CalibDb_LfrmSetPointV2_s._fields_ = [
    ('LExpLevel', POINTER(c_float)),
    ('LExpLevel_len', c_int),
    ('NonOEPdfTh', POINTER(c_float)),
    ('NonOEPdfTh_len', c_int),
    ('LowLightPdfTh', POINTER(c_float)),
    ('LowLightPdfTh_len', c_int),
    ('LSetPoint', POINTER(c_float)),
    ('LSetPoint_len', c_int),
    ('TargetLLLuma', POINTER(c_float)),
    ('TargetLLLuma_len', c_int),
]

CalibDb_LfrmSetPointV2_t = struct_CalibDb_LfrmSetPointV2_s# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_head.h: 537

# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_head.h: 552
class struct_CalibDb_LfrmCtrlV2_s(Structure):
    pass

struct_CalibDb_LfrmCtrlV2_s.__slots__ = [
    'OEROILowTh',
    'LvLowTh',
    'LvHighTh',
    'LfrmSetPoint',
]
struct_CalibDb_LfrmCtrlV2_s._fields_ = [
    ('OEROILowTh', c_float),
    ('LvLowTh', c_float),
    ('LvHighTh', c_float),
    ('LfrmSetPoint', CalibDb_LfrmSetPointV2_t),
]

CalibDb_LfrmCtrlV2_t = struct_CalibDb_LfrmCtrlV2_s# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_head.h: 552

# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_head.h: 562
class struct_CalibDb_MfrmCtrlV2_s(Structure):
    pass

struct_CalibDb_MfrmCtrlV2_s.__slots__ = [
    'MExpLevel',
    'MExpLevel_len',
    'MSetPoint',
    'MSetPoint_len',
]
struct_CalibDb_MfrmCtrlV2_s._fields_ = [
    ('MExpLevel', POINTER(c_float)),
    ('MExpLevel_len', c_int),
    ('MSetPoint', POINTER(c_float)),
    ('MSetPoint_len', c_int),
]

CalibDb_MfrmCtrlV2_t = struct_CalibDb_MfrmCtrlV2_s# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_head.h: 562

# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_head.h: 575
class struct_CalibDb_SfrmSetPointV2_s(Structure):
    pass

struct_CalibDb_SfrmSetPointV2_s.__slots__ = [
    'SExpLevel',
    'SExpLevel_len',
    'SSetPoint',
    'SSetPoint_len',
    'TargetHLLuma',
    'TargetHLLuma_len',
]
struct_CalibDb_SfrmSetPointV2_s._fields_ = [
    ('SExpLevel', POINTER(c_float)),
    ('SExpLevel_len', c_int),
    ('SSetPoint', POINTER(c_float)),
    ('SSetPoint_len', c_int),
    ('TargetHLLuma', POINTER(c_float)),
    ('TargetHLLuma_len', c_int),
]

CalibDb_SfrmSetPointV2_t = struct_CalibDb_SfrmSetPointV2_s# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_head.h: 575

# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_head.h: 587
class struct_CalibDb_SfrmCtrlV2_s(Structure):
    pass

struct_CalibDb_SfrmCtrlV2_s.__slots__ = [
    'HLROIExpandEn',
    'HLLumaTolerance',
    'SfrmSetPoint',
]
struct_CalibDb_SfrmCtrlV2_s._fields_ = [
    ('HLROIExpandEn', c_bool),
    ('HLLumaTolerance', c_float),
    ('SfrmSetPoint', CalibDb_SfrmSetPointV2_t),
]

CalibDb_SfrmCtrlV2_t = struct_CalibDb_SfrmCtrlV2_s# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_head.h: 587

# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_head.h: 598
class struct_CalibDb_LongFrmCtrlV2_s(Structure):
    pass

struct_CalibDb_LongFrmCtrlV2_s.__slots__ = [
    'mode',
    'SfrmMinLine',
    'LfrmModeExpTh',
]
struct_CalibDb_LongFrmCtrlV2_s._fields_ = [
    ('mode', CalibDb_AeHdrLongFrmModeV2_t),
    ('SfrmMinLine', uint16_t),
    ('LfrmModeExpTh', c_float),
]

CalibDb_LongFrmCtrlV2_t = struct_CalibDb_LongFrmCtrlV2_s# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_head.h: 598

# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_head.h: 636
class struct_CalibDb_HdrAE_AttrV2_s(Structure):
    pass

struct_CalibDb_HdrAE_AttrV2_s.__slots__ = [
    'ToleranceIn',
    'ToleranceOut',
    'Evbias',
    'StrategyMode',
    'LumaDistTh',
    'InitExp',
    'Route',
    'ExpRatioCtrl',
    'LongFrmMode',
    'LframeCtrl',
    'MframeCtrl',
    'SframeCtrl',
]
struct_CalibDb_HdrAE_AttrV2_s._fields_ = [
    ('ToleranceIn', c_float),
    ('ToleranceOut', c_float),
    ('Evbias', c_float),
    ('StrategyMode', CalibDb_AeStrategyModeV2_t),
    ('LumaDistTh', c_float),
    ('InitExp', CalibDb_HdrExpInitExpV2_t),
    ('Route', CalibDb_HdrAeRoute_AttrV2_t),
    ('ExpRatioCtrl', CalibDb_ExpRatioCtrlV2_t),
    ('LongFrmMode', CalibDb_LongFrmCtrlV2_t),
    ('LframeCtrl', CalibDb_LfrmCtrlV2_t),
    ('MframeCtrl', CalibDb_MfrmCtrlV2_t),
    ('SframeCtrl', CalibDb_SfrmCtrlV2_t),
]

CalibDb_HdrAE_AttrV2_t = struct_CalibDb_HdrAE_AttrV2_s# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_head.h: 636

# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_head.h: 658
class struct_CalibDb_LinAlterExpV2_s(Structure):
    pass

struct_CalibDb_LinAlterExpV2_s.__slots__ = [
    'TimeValue',
    'GainValue',
    'IspDGainValue',
    'PIrisGainValue',
    'DcgMode',
]
struct_CalibDb_LinAlterExpV2_s._fields_ = [
    ('TimeValue', c_float),
    ('GainValue', c_float),
    ('IspDGainValue', c_float),
    ('PIrisGainValue', c_int),
    ('DcgMode', c_int),
]

CalibDb_LinAlterExpV2_t = struct_CalibDb_LinAlterExpV2_s# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_head.h: 658

# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_head.h: 675
class struct_CalibDb_HdrAlterExpV2_s(Structure):
    pass

struct_CalibDb_HdrAlterExpV2_s.__slots__ = [
    'TimeValue',
    'GainValue',
    'IspDGainValue',
    'PIrisGainValue',
    'DcgMode',
]
struct_CalibDb_HdrAlterExpV2_s._fields_ = [
    ('TimeValue', c_float * int(3)),
    ('GainValue', c_float * int(3)),
    ('IspDGainValue', c_float * int(3)),
    ('PIrisGainValue', c_int),
    ('DcgMode', c_int * int(3)),
]

CalibDb_HdrAlterExpV2_t = struct_CalibDb_HdrAlterExpV2_s# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_head.h: 675

# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_head.h: 685
class struct_CalibDb_AlterExpV2_s(Structure):
    pass

struct_CalibDb_AlterExpV2_s.__slots__ = [
    'LinearAE',
    'LinearAE_len',
    'HdrAE',
    'HdrAE_len',
]
struct_CalibDb_AlterExpV2_s._fields_ = [
    ('LinearAE', POINTER(CalibDb_LinAlterExpV2_t)),
    ('LinearAE_len', c_int),
    ('HdrAE', POINTER(CalibDb_HdrAlterExpV2_t)),
    ('HdrAE_len', c_int),
]

CalibDb_AlterExpV2_t = struct_CalibDb_AlterExpV2_s# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_head.h: 685

# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_head.h: 696
class struct_CalibDb_AeSyncTestV2_s(Structure):
    pass

struct_CalibDb_AeSyncTestV2_s.__slots__ = [
    'Enable',
    'IntervalFrm',
    'AlterExp',
]
struct_CalibDb_AeSyncTestV2_s._fields_ = [
    ('Enable', c_bool),
    ('IntervalFrm', c_int),
    ('AlterExp', CalibDb_AlterExpV2_t),
]

CalibDb_AeSyncTestV2_t = struct_CalibDb_AeSyncTestV2_s# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_head.h: 696

# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_head.h: 709
class struct_CalibDb_MIris_AttrV2_s(Structure):
    pass

struct_CalibDb_MIris_AttrV2_s.__slots__ = [
    'PIrisGainValue',
    'DCIrisHoldValue',
]
struct_CalibDb_MIris_AttrV2_s._fields_ = [
    ('PIrisGainValue', c_int),
    ('DCIrisHoldValue', c_int),
]

CalibDb_MIris_AttrV2_t = struct_CalibDb_MIris_AttrV2_s# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_head.h: 709

# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_head.h: 723
class struct_CalibDb_PIris_AttrV2_s(Structure):
    pass

struct_CalibDb_PIris_AttrV2_s.__slots__ = [
    'TotalStep',
    'EffcStep',
    'ZeroIsMax',
    'StepTable',
]
struct_CalibDb_PIris_AttrV2_s._fields_ = [
    ('TotalStep', uint16_t),
    ('EffcStep', uint16_t),
    ('ZeroIsMax', c_bool),
    ('StepTable', uint16_t * int(1024)),
]

CalibDb_PIris_AttrV2_t = struct_CalibDb_PIris_AttrV2_s# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_head.h: 723

# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_head.h: 740
class struct_CalibDb_DCIris_AttrV2_s(Structure):
    pass

struct_CalibDb_DCIris_AttrV2_s.__slots__ = [
    'Kp',
    'Ki',
    'Kd',
    'MinPwmDuty',
    'MaxPwmDuty',
    'OpenPwmDuty',
    'ClosePwmDuty',
]
struct_CalibDb_DCIris_AttrV2_s._fields_ = [
    ('Kp', c_float),
    ('Ki', c_float),
    ('Kd', c_float),
    ('MinPwmDuty', c_int),
    ('MaxPwmDuty', c_int),
    ('OpenPwmDuty', c_int),
    ('ClosePwmDuty', c_int),
]

CalibDb_DCIris_AttrV2_t = struct_CalibDb_DCIris_AttrV2_s# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_head.h: 740

# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_head.h: 763
class struct_CalibDb_AecIrisCtrlV2_s(Structure):
    pass

struct_CalibDb_AecIrisCtrlV2_s.__slots__ = [
    'Enable',
    'IrisType',
    'ManualEn',
    'ManualAttr',
    'InitAttr',
    'PIrisAttr',
    'DCIrisAttr',
]
struct_CalibDb_AecIrisCtrlV2_s._fields_ = [
    ('Enable', c_bool),
    ('IrisType', CalibDb_IrisTypeV2_t),
    ('ManualEn', c_bool),
    ('ManualAttr', CalibDb_MIris_AttrV2_t),
    ('InitAttr', CalibDb_MIris_AttrV2_t),
    ('PIrisAttr', CalibDb_PIris_AttrV2_t),
    ('DCIrisAttr', CalibDb_DCIris_AttrV2_t),
]

CalibDb_AecIrisCtrlV2_t = struct_CalibDb_AecIrisCtrlV2_s# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_head.h: 763

# /root/camera_engine_rkaiq/include/algos/ae/rk_aiq_types_ae_hw.h: 55
class struct_window(Structure):
    pass

struct_window._pack_ = 1
struct_window.__slots__ = [
    'h_offs',
    'v_offs',
    'h_size',
    'v_size',
]
struct_window._fields_ = [
    ('h_offs', uint16_t),
    ('v_offs', uint16_t),
    ('h_size', uint16_t),
    ('v_size', uint16_t),
]

window_t = struct_window# /root/camera_engine_rkaiq/include/algos/ae/rk_aiq_types_ae_hw.h: 55

# /root/camera_engine_rkaiq/include/algos/ae/rk_aiq_types_ae_hw.h: 173
class struct_rawhist_stat(Structure):
    pass

struct_rawhist_stat.__slots__ = [
    'bins',
]
struct_rawhist_stat._fields_ = [
    ('bins', c_uint * int(256)),
]

rawhist_stat_t = struct_rawhist_stat# /root/camera_engine_rkaiq/include/algos/ae/rk_aiq_types_ae_hw.h: 173

# /root/camera_engine_rkaiq/include/algos/ae/rk_aiq_types_ae_hw.h: 177
class struct_sihist_stat_t(Structure):
    pass

struct_sihist_stat_t.__slots__ = [
    'bins',
]
struct_sihist_stat_t._fields_ = [
    ('bins', c_uint * int(32)),
]

sihist_stat_t = struct_sihist_stat_t# /root/camera_engine_rkaiq/include/algos/ae/rk_aiq_types_ae_hw.h: 177

# /root/camera_engine_rkaiq/include/algos/ae/rk_aiq_types_ae_hw.h: 191
class struct_rawaebig_stat(Structure):
    pass

struct_rawaebig_stat.__slots__ = [
    'channelr_xy',
    'channelg_xy',
    'channelb_xy',
    'channely_xy',
    'wndx_sumr',
    'wndx_sumg',
    'wndx_sumb',
    'wndx_channelr',
    'wndx_channelg',
    'wndx_channelb',
    'wndx_channely',
]
struct_rawaebig_stat._fields_ = [
    ('channelr_xy', uint16_t * int(225)),
    ('channelg_xy', uint16_t * int(225)),
    ('channelb_xy', uint16_t * int(225)),
    ('channely_xy', uint16_t * int(225)),
    ('wndx_sumr', uint64_t * int(4)),
    ('wndx_sumg', uint64_t * int(4)),
    ('wndx_sumb', uint64_t * int(4)),
    ('wndx_channelr', uint16_t * int(4)),
    ('wndx_channelg', uint16_t * int(4)),
    ('wndx_channelb', uint16_t * int(4)),
    ('wndx_channely', uint16_t * int(4)),
]

rawaebig_stat_t = struct_rawaebig_stat# /root/camera_engine_rkaiq/include/algos/ae/rk_aiq_types_ae_hw.h: 191

# /root/camera_engine_rkaiq/include/algos/ae/rk_aiq_types_ae_hw.h: 198
class struct_rawaelite_stat(Structure):
    pass

struct_rawaelite_stat.__slots__ = [
    'channelr_xy',
    'channelg_xy',
    'channelb_xy',
    'channely_xy',
]
struct_rawaelite_stat._fields_ = [
    ('channelr_xy', uint16_t * int(25)),
    ('channelg_xy', uint16_t * int(25)),
    ('channelb_xy', uint16_t * int(25)),
    ('channely_xy', uint16_t * int(25)),
]

rawaelite_stat_t = struct_rawaelite_stat# /root/camera_engine_rkaiq/include/algos/ae/rk_aiq_types_ae_hw.h: 198

# /root/camera_engine_rkaiq/include/algos/ae/rk_aiq_types_ae_hw.h: 203
class struct_yuvae_stat(Structure):
    pass

struct_yuvae_stat.__slots__ = [
    'ro_yuvae_sumy',
    'mean',
]
struct_yuvae_stat._fields_ = [
    ('ro_yuvae_sumy', uint64_t * int(4)),
    ('mean', c_ubyte * int(225)),
]

yuvae_stat_t = struct_yuvae_stat# /root/camera_engine_rkaiq/include/algos/ae/rk_aiq_types_ae_hw.h: 203

# /root/camera_engine_rkaiq/include/algos/ae/rk_aiq_types_ae_hw.h: 212
class struct_Aec_Stat_Res_s(Structure):
    pass

struct_Aec_Stat_Res_s.__slots__ = [
    'rawae_big',
    'rawae_lite',
    'rawhist_big',
    'rawhist_lite',
]
struct_Aec_Stat_Res_s._fields_ = [
    ('rawae_big', rawaebig_stat_t),
    ('rawae_lite', rawaelite_stat_t),
    ('rawhist_big', rawhist_stat_t),
    ('rawhist_lite', rawhist_stat_t),
]

Aec_Stat_Res_t = struct_Aec_Stat_Res_s# /root/camera_engine_rkaiq/include/algos/ae/rk_aiq_types_ae_hw.h: 212

# /root/camera_engine_rkaiq/include/algos/ae/rk_aiq_types_ae_hw.h: 226
class struct_RkAiqAecHwStatsRes_s(Structure):
    pass

struct_RkAiqAecHwStatsRes_s.__slots__ = [
    'chn',
    'extra',
    'yuvae',
    'sihist',
]
struct_RkAiqAecHwStatsRes_s._fields_ = [
    ('chn', Aec_Stat_Res_t * int(3)),
    ('extra', Aec_Stat_Res_t),
    ('yuvae', yuvae_stat_t),
    ('sihist', sihist_stat_t),
]

RkAiqAecHwStatsRes_t = struct_RkAiqAecHwStatsRes_s# /root/camera_engine_rkaiq/include/algos/ae/rk_aiq_types_ae_hw.h: 226

# /root/camera_engine_rkaiq/include/algos/ae/rk_aiq_types_ae_hw.h: 267
class struct_RkAiqExpRealParam_s(Structure):
    pass

struct_RkAiqExpRealParam_s.__slots__ = [
    'integration_time',
    'analog_gain',
    'digital_gain',
    'isp_dgain',
    'iso',
    'dcg_mode',
    'longfrm_mode',
]
struct_RkAiqExpRealParam_s._fields_ = [
    ('integration_time', c_float),
    ('analog_gain', c_float),
    ('digital_gain', c_float),
    ('isp_dgain', c_float),
    ('iso', c_int),
    ('dcg_mode', c_int),
    ('longfrm_mode', c_int),
]

RkAiqExpRealParam_t = struct_RkAiqExpRealParam_s# /root/camera_engine_rkaiq/include/algos/ae/rk_aiq_types_ae_hw.h: 267

# /root/camera_engine_rkaiq/include/algos/ae/rk_aiq_types_ae_hw.h: 285
class struct_RkAiqExpSensorParam_s(Structure):
    pass

struct_RkAiqExpSensorParam_s.__slots__ = [
    'fine_integration_time',
    'coarse_integration_time',
    'analog_gain_code_global',
    'digital_gain_global',
    'isp_digital_gain',
]
struct_RkAiqExpSensorParam_s._fields_ = [
    ('fine_integration_time', c_uint),
    ('coarse_integration_time', c_uint),
    ('analog_gain_code_global', c_uint),
    ('digital_gain_global', c_uint),
    ('isp_digital_gain', c_uint),
]

RkAiqExpSensorParam_t = struct_RkAiqExpSensorParam_s# /root/camera_engine_rkaiq/include/algos/ae/rk_aiq_types_ae_hw.h: 285

# /root/camera_engine_rkaiq/include/algos/ae/rk_aiq_types_ae_hw.h: 318
class struct_anon_68(Structure):
    pass

struct_anon_68.__slots__ = [
    'exp_real_params',
    'exp_sensor_params',
]
struct_anon_68._fields_ = [
    ('exp_real_params', RkAiqExpRealParam_t),
    ('exp_sensor_params', RkAiqExpSensorParam_t),
]

RkAiqExpParamComb_t = struct_anon_68# /root/camera_engine_rkaiq/include/algos/ae/rk_aiq_types_ae_hw.h: 318

# /root/camera_engine_rkaiq/include/algos/ae/rk_aiq_types_ae_hw.h: 327
class struct_anon_69(Structure):
    pass

struct_anon_69.__slots__ = [
    'step',
    'gain',
    'update',
]
struct_anon_69._fields_ = [
    ('step', c_int),
    ('gain', c_int),
    ('update', c_bool),
]

RkAiqPIrisParam_t = struct_anon_69# /root/camera_engine_rkaiq/include/algos/ae/rk_aiq_types_ae_hw.h: 327

# /root/camera_engine_rkaiq/include/algos/ae/rk_aiq_types_ae_hw.h: 334
class struct_anon_70(Structure):
    pass

struct_anon_70.__slots__ = [
    'pwmDuty',
    'update',
]
struct_anon_70._fields_ = [
    ('pwmDuty', c_int),
    ('update', c_bool),
]

RkAiqDCIrisParam_t = struct_anon_70# /root/camera_engine_rkaiq/include/algos/ae/rk_aiq_types_ae_hw.h: 334

# /root/camera_engine_rkaiq/include/algos/ae/rk_aiq_types_ae_hw.h: 341
class struct_anon_71(Structure):
    pass

struct_anon_71.__slots__ = [
    'PIris',
    'DCIris',
]
struct_anon_71._fields_ = [
    ('PIris', RkAiqPIrisParam_t),
    ('DCIris', RkAiqDCIrisParam_t),
]

RkAiqIrisParamComb_t = struct_anon_71# /root/camera_engine_rkaiq/include/algos/ae/rk_aiq_types_ae_hw.h: 341

# /root/camera_engine_rkaiq/include/algos/ae/rk_aiq_types_ae_hw.h: 386
class struct_RKAiqAecStats_s(Structure):
    pass

struct_RKAiqAecStats_s.__slots__ = [
    'ae_data',
    'ae_exp',
]
struct_RKAiqAecStats_s._fields_ = [
    ('ae_data', RkAiqAecHwStatsRes_t),
    ('ae_exp', RKAiqAecExpInfo_t),
]

RKAiqAecStats_t = struct_RKAiqAecStats_s# /root/camera_engine_rkaiq/include/algos/ae/rk_aiq_types_ae_hw.h: 386

# /root/camera_engine_rkaiq/include/algos/ae/rk_aiq_types_ae_algo_int.h: 367
class struct_Aec_AeRange_s(Structure):
    pass

struct_Aec_AeRange_s.__slots__ = [
    'Min',
    'Max',
]
struct_Aec_AeRange_s._fields_ = [
    ('Min', c_float),
    ('Max', c_float),
]

Aec_AeRange_t = struct_Aec_AeRange_s# /root/camera_engine_rkaiq/include/algos/ae/rk_aiq_types_ae_algo_int.h: 367

# /root/camera_engine_rkaiq/include/algos/ae/rk_aiq_types_ae_algo_int.h: 374
class struct_Aec_LinAeRange_s(Structure):
    pass

struct_Aec_LinAeRange_s.__slots__ = [
    'stExpTimeRange',
    'stGainRange',
    'stIspDGainRange',
    'stPIrisRange',
]
struct_Aec_LinAeRange_s._fields_ = [
    ('stExpTimeRange', Aec_AeRange_t),
    ('stGainRange', Aec_AeRange_t),
    ('stIspDGainRange', Aec_AeRange_t),
    ('stPIrisRange', Aec_AeRange_t),
]

Aec_LinAeRange_t = struct_Aec_LinAeRange_s# /root/camera_engine_rkaiq/include/algos/ae/rk_aiq_types_ae_algo_int.h: 374

# /root/camera_engine_rkaiq/include/algos/ae/rk_aiq_types_ae_algo_int.h: 381
class struct_Aec_HdrAeRange_s(Structure):
    pass

struct_Aec_HdrAeRange_s.__slots__ = [
    'stExpTimeRange',
    'stGainRange',
    'stIspDGainRange',
    'stPIrisRange',
]
struct_Aec_HdrAeRange_s._fields_ = [
    ('stExpTimeRange', Aec_AeRange_t * int(3)),
    ('stGainRange', Aec_AeRange_t * int(3)),
    ('stIspDGainRange', Aec_AeRange_t * int(3)),
    ('stPIrisRange', Aec_AeRange_t),
]

Aec_HdrAeRange_t = struct_Aec_HdrAeRange_s# /root/camera_engine_rkaiq/include/algos/ae/rk_aiq_types_ae_algo_int.h: 381

# /root/camera_engine_rkaiq/include/algos/ae/rk_aiq_types_ae_algo_int.h: 391
class struct_Aec_uapi_advanced_attr_s(Structure):
    pass

struct_Aec_uapi_advanced_attr_s.__slots__ = [
    'enable',
    'GridWeights',
    'DayGridWeights',
    'NightGridWeights',
    'SetAeRangeEn',
    'SetLinAeRange',
    'SetHdrAeRange',
]
struct_Aec_uapi_advanced_attr_s._fields_ = [
    ('enable', c_bool),
    ('GridWeights', uint8_t * int((15 * 15))),
    ('DayGridWeights', uint8_t * int(225)),
    ('NightGridWeights', uint8_t * int(225)),
    ('SetAeRangeEn', c_bool),
    ('SetLinAeRange', Aec_LinAeRange_t),
    ('SetHdrAeRange', Aec_HdrAeRange_t),
]

Aec_uapi_advanced_attr_t = struct_Aec_uapi_advanced_attr_s# /root/camera_engine_rkaiq/include/algos/ae/rk_aiq_types_ae_algo_int.h: 391

Uapi_AeSpeedV2_t = CalibDb_AeSpeedV2_t# /root/camera_engine_rkaiq/include/algos/ae/rk_aiq_uapi_ae_int_types_v2.h: 18

Uapi_AeFpsAttrV2_t = CalibDb_AeFrmRateAttrV2_t# /root/camera_engine_rkaiq/include/algos/ae/rk_aiq_uapi_ae_int_types_v2.h: 26

Uapi_AntiFlickerV2_t = CalibDb_AntiFlickerAttrV2_t# /root/camera_engine_rkaiq/include/algos/ae/rk_aiq_uapi_ae_int_types_v2.h: 28

# /root/camera_engine_rkaiq/include/algos/ae/rk_aiq_uapi_ae_int_types_v2.h: 42
class struct_Uapi_AeAttrV2_s(Structure):
    pass

struct_Uapi_AeAttrV2_s.__slots__ = [
    'stAeSpeed',
    'BlackDelayFrame',
    'WhiteDelayFrame',
    'stFrmRate',
    'stAntiFlicker',
    'LinAeRange',
    'HdrAeRange',
]
struct_Uapi_AeAttrV2_s._fields_ = [
    ('stAeSpeed', Uapi_AeSpeedV2_t),
    ('BlackDelayFrame', uint8_t),
    ('WhiteDelayFrame', uint8_t),
    ('stFrmRate', Uapi_AeFpsAttrV2_t),
    ('stAntiFlicker', Uapi_AntiFlickerV2_t),
    ('LinAeRange', Aec_LinAeRange_t),
    ('HdrAeRange', Aec_HdrAeRange_t),
]

Uapi_AeAttrV2_t = struct_Uapi_AeAttrV2_s# /root/camera_engine_rkaiq/include/algos/ae/rk_aiq_uapi_ae_int_types_v2.h: 42

# /root/camera_engine_rkaiq/include/algos/ae/rk_aiq_uapi_ae_int_types_v2.h: 63
class struct_Uapi_LinMeAttrV2_s(Structure):
    pass

struct_Uapi_LinMeAttrV2_s.__slots__ = [
    'ManualTimeEn',
    'ManualGainEn',
    'ManualIspDgainEn',
    'TimeValue',
    'GainValue',
    'IspDGainValue',
]
struct_Uapi_LinMeAttrV2_s._fields_ = [
    ('ManualTimeEn', c_bool),
    ('ManualGainEn', c_bool),
    ('ManualIspDgainEn', c_bool),
    ('TimeValue', c_float),
    ('GainValue', c_float),
    ('IspDGainValue', c_float),
]

Uapi_LinMeAttrV2_t = struct_Uapi_LinMeAttrV2_s# /root/camera_engine_rkaiq/include/algos/ae/rk_aiq_uapi_ae_int_types_v2.h: 63

# /root/camera_engine_rkaiq/include/algos/ae/rk_aiq_uapi_ae_int_types_v2.h: 83
class struct_Uapi_HdrMeAttrV2_s(Structure):
    pass

struct_Uapi_HdrMeAttrV2_s.__slots__ = [
    'ManualTimeEn',
    'ManualGainEn',
    'ManualIspDgainEn',
    'TimeValue',
    'GainValue',
    'IspDGainValue',
]
struct_Uapi_HdrMeAttrV2_s._fields_ = [
    ('ManualTimeEn', c_bool),
    ('ManualGainEn', c_bool),
    ('ManualIspDgainEn', c_bool),
    ('TimeValue', c_float * int(3)),
    ('GainValue', c_float * int(3)),
    ('IspDGainValue', c_float * int(3)),
]

Uapi_HdrMeAttrV2_t = struct_Uapi_HdrMeAttrV2_s# /root/camera_engine_rkaiq/include/algos/ae/rk_aiq_uapi_ae_int_types_v2.h: 83

# /root/camera_engine_rkaiq/include/algos/ae/rk_aiq_uapi_ae_int_types_v2.h: 91
class struct_Uapi_MeAttrV2_s(Structure):
    pass

struct_Uapi_MeAttrV2_s.__slots__ = [
    'LinearAE',
    'HdrAE',
]
struct_Uapi_MeAttrV2_s._fields_ = [
    ('LinearAE', Uapi_LinMeAttrV2_t),
    ('HdrAE', Uapi_HdrMeAttrV2_t),
]

Uapi_MeAttrV2_t = struct_Uapi_MeAttrV2_s# /root/camera_engine_rkaiq/include/algos/ae/rk_aiq_uapi_ae_int_types_v2.h: 91

Uapi_ExpSwAttr_AdvancedV2_t = Aec_uapi_advanced_attr_t# /root/camera_engine_rkaiq/include/algos/ae/rk_aiq_uapi_ae_int_types_v2.h: 93

# /root/camera_engine_rkaiq/include/algos/ae/rk_aiq_uapi_ae_int_types_v2.h: 112
class struct_Uapi_ExpSwAttrV2_s(Structure):
    pass

struct_Uapi_ExpSwAttrV2_s.__slots__ = [
    'sync',
    'Enable',
    'RawStatsMode',
    'HistStatsMode',
    'YRangeMode',
    'AecRunInterval',
    'AecOpType',
    'GridWeights',
    'stAuto',
    'stManual',
    'stAdvanced',
]
struct_Uapi_ExpSwAttrV2_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('Enable', uint8_t),
    ('RawStatsMode', CalibDb_CamRawStatsModeV2_t),
    ('HistStatsMode', CalibDb_CamHistStatsModeV2_t),
    ('YRangeMode', CalibDb_CamYRangeModeV2_t),
    ('AecRunInterval', uint8_t),
    ('AecOpType', RKAiqOPMode_t),
    ('GridWeights', Cam15x15UCharMatrix_t),
    ('stAuto', Uapi_AeAttrV2_t),
    ('stManual', Uapi_MeAttrV2_t),
    ('stAdvanced', Uapi_ExpSwAttr_AdvancedV2_t),
]

Uapi_ExpSwAttrV2_t = struct_Uapi_ExpSwAttrV2_s# /root/camera_engine_rkaiq/include/algos/ae/rk_aiq_uapi_ae_int_types_v2.h: 112

# /root/camera_engine_rkaiq/include/algos/ae/rk_aiq_uapi_ae_int_types_v2.h: 122
class struct_Uapi_LinAeRouteAttr_s(Structure):
    pass

struct_Uapi_LinAeRouteAttr_s.__slots__ = [
    'sync',
    'Params',
]
struct_Uapi_LinAeRouteAttr_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('Params', CalibDb_LinAeRoute_AttrV2_t),
]

Uapi_LinAeRouteAttr_t = struct_Uapi_LinAeRouteAttr_s# /root/camera_engine_rkaiq/include/algos/ae/rk_aiq_uapi_ae_int_types_v2.h: 122

# /root/camera_engine_rkaiq/include/algos/ae/rk_aiq_uapi_ae_int_types_v2.h: 127
class struct_Uapi_HdrAeRouteAttr_s(Structure):
    pass

struct_Uapi_HdrAeRouteAttr_s.__slots__ = [
    'sync',
    'Params',
]
struct_Uapi_HdrAeRouteAttr_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('Params', CalibDb_HdrAeRoute_AttrV2_t),
]

Uapi_HdrAeRouteAttr_t = struct_Uapi_HdrAeRouteAttr_s# /root/camera_engine_rkaiq/include/algos/ae/rk_aiq_uapi_ae_int_types_v2.h: 127

# /root/camera_engine_rkaiq/include/algos/ae/rk_aiq_uapi_ae_int_types_v2.h: 137
class struct_Uapi_IrisAttrV2_s(Structure):
    pass

struct_Uapi_IrisAttrV2_s.__slots__ = [
    'sync',
    'Params',
]
struct_Uapi_IrisAttrV2_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('Params', CalibDb_AecIrisCtrlV2_t),
]

Uapi_IrisAttrV2_t = struct_Uapi_IrisAttrV2_s# /root/camera_engine_rkaiq/include/algos/ae/rk_aiq_uapi_ae_int_types_v2.h: 137

# /root/camera_engine_rkaiq/include/algos/ae/rk_aiq_uapi_ae_int_types_v2.h: 147
class struct_Uapi_AecSyncTest_s(Structure):
    pass

struct_Uapi_AecSyncTest_s.__slots__ = [
    'sync',
    'Params',
]
struct_Uapi_AecSyncTest_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('Params', CalibDb_AeSyncTestV2_t),
]

Uapi_AecSyncTest_t = struct_Uapi_AecSyncTest_s# /root/camera_engine_rkaiq/include/algos/ae/rk_aiq_uapi_ae_int_types_v2.h: 147

# /root/camera_engine_rkaiq/include/algos/ae/rk_aiq_uapi_ae_int_types_v2.h: 157
class struct_Uapi_LinExpAttrV2_s(Structure):
    pass

struct_Uapi_LinExpAttrV2_s.__slots__ = [
    'sync',
    'Params',
]
struct_Uapi_LinExpAttrV2_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('Params', CalibDb_LinearAE_AttrV2_t),
]

Uapi_LinExpAttrV2_t = struct_Uapi_LinExpAttrV2_s# /root/camera_engine_rkaiq/include/algos/ae/rk_aiq_uapi_ae_int_types_v2.h: 157

# /root/camera_engine_rkaiq/include/algos/ae/rk_aiq_uapi_ae_int_types_v2.h: 162
class struct_Uapi_HdrExpAttrV2_s(Structure):
    pass

struct_Uapi_HdrExpAttrV2_s.__slots__ = [
    'sync',
    'Params',
]
struct_Uapi_HdrExpAttrV2_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('Params', CalibDb_HdrAE_AttrV2_t),
]

Uapi_HdrExpAttrV2_t = struct_Uapi_HdrExpAttrV2_s# /root/camera_engine_rkaiq/include/algos/ae/rk_aiq_uapi_ae_int_types_v2.h: 162

# /root/camera_engine_rkaiq/include/algos/ae/rk_aiq_uapi_ae_int_types_v2.h: 172
class struct_Uapi_ExpWin_s(Structure):
    pass

struct_Uapi_ExpWin_s.__slots__ = [
    'sync',
    'Params',
]
struct_Uapi_ExpWin_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('Params', window_t),
]

Uapi_ExpWin_t = struct_Uapi_ExpWin_s# /root/camera_engine_rkaiq/include/algos/ae/rk_aiq_uapi_ae_int_types_v2.h: 172

# /root/camera_engine_rkaiq/include/algos/ae/rk_aiq_uapi_ae_int_types_v2.h: 211
class struct_Uapi_ExpQueryInfo_s(Structure):
    pass

struct_Uapi_ExpQueryInfo_s.__slots__ = [
    'IsConverged',
    'IsExpMax',
    'LumaDeviation',
    'HdrLumaDeviation',
    'MeanLuma',
    'HdrMeanLuma',
    'GlobalEnvLux',
    'BlockEnvLux',
    'CurExpInfo',
    'Piris',
    'LinePeriodsPerField',
    'PixelPeriodsPerLine',
    'PixelClockFreqMHZ',
]
struct_Uapi_ExpQueryInfo_s._fields_ = [
    ('IsConverged', c_bool),
    ('IsExpMax', c_bool),
    ('LumaDeviation', c_float),
    ('HdrLumaDeviation', c_float * int(3)),
    ('MeanLuma', c_float),
    ('HdrMeanLuma', c_float * int(3)),
    ('GlobalEnvLux', c_float),
    ('BlockEnvLux', c_float * int((25 > 225) and 25 or 225)),
    ('CurExpInfo', RKAiqAecExpInfo_t),
    ('Piris', c_ushort),
    ('LinePeriodsPerField', c_float),
    ('PixelPeriodsPerLine', c_float),
    ('PixelClockFreqMHZ', c_float),
]

Uapi_ExpQueryInfo_t = struct_Uapi_ExpQueryInfo_s# /root/camera_engine_rkaiq/include/algos/ae/rk_aiq_uapi_ae_int_types_v2.h: 211

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_ae.h: 30
if _libs["rkaiq"].has("rk_aiq_user_api2_ae_setExpSwAttr", "cdecl"):
    rk_aiq_user_api2_ae_setExpSwAttr = _libs["rkaiq"].get("rk_aiq_user_api2_ae_setExpSwAttr", "cdecl")
    rk_aiq_user_api2_ae_setExpSwAttr.argtypes = [POINTER(rk_aiq_sys_ctx_t), Uapi_ExpSwAttrV2_t]
    rk_aiq_user_api2_ae_setExpSwAttr.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_ae.h: 31
if _libs["rkaiq"].has("rk_aiq_user_api2_ae_getExpSwAttr", "cdecl"):
    rk_aiq_user_api2_ae_getExpSwAttr = _libs["rkaiq"].get("rk_aiq_user_api2_ae_getExpSwAttr", "cdecl")
    rk_aiq_user_api2_ae_getExpSwAttr.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(Uapi_ExpSwAttrV2_t)]
    rk_aiq_user_api2_ae_getExpSwAttr.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_ae.h: 32
if _libs["rkaiq"].has("rk_aiq_user_api2_ae_setLinExpAttr", "cdecl"):
    rk_aiq_user_api2_ae_setLinExpAttr = _libs["rkaiq"].get("rk_aiq_user_api2_ae_setLinExpAttr", "cdecl")
    rk_aiq_user_api2_ae_setLinExpAttr.argtypes = [POINTER(rk_aiq_sys_ctx_t), Uapi_LinExpAttrV2_t]
    rk_aiq_user_api2_ae_setLinExpAttr.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_ae.h: 33
if _libs["rkaiq"].has("rk_aiq_user_api2_ae_getLinExpAttr", "cdecl"):
    rk_aiq_user_api2_ae_getLinExpAttr = _libs["rkaiq"].get("rk_aiq_user_api2_ae_getLinExpAttr", "cdecl")
    rk_aiq_user_api2_ae_getLinExpAttr.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(Uapi_LinExpAttrV2_t)]
    rk_aiq_user_api2_ae_getLinExpAttr.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_ae.h: 34
if _libs["rkaiq"].has("rk_aiq_user_api2_ae_setHdrExpAttr", "cdecl"):
    rk_aiq_user_api2_ae_setHdrExpAttr = _libs["rkaiq"].get("rk_aiq_user_api2_ae_setHdrExpAttr", "cdecl")
    rk_aiq_user_api2_ae_setHdrExpAttr.argtypes = [POINTER(rk_aiq_sys_ctx_t), Uapi_HdrExpAttrV2_t]
    rk_aiq_user_api2_ae_setHdrExpAttr.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_ae.h: 35
if _libs["rkaiq"].has("rk_aiq_user_api2_ae_getHdrExpAttr", "cdecl"):
    rk_aiq_user_api2_ae_getHdrExpAttr = _libs["rkaiq"].get("rk_aiq_user_api2_ae_getHdrExpAttr", "cdecl")
    rk_aiq_user_api2_ae_getHdrExpAttr.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(Uapi_HdrExpAttrV2_t)]
    rk_aiq_user_api2_ae_getHdrExpAttr.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_ae.h: 37
if _libs["rkaiq"].has("rk_aiq_user_api2_ae_setLinAeRouteAttr", "cdecl"):
    rk_aiq_user_api2_ae_setLinAeRouteAttr = _libs["rkaiq"].get("rk_aiq_user_api2_ae_setLinAeRouteAttr", "cdecl")
    rk_aiq_user_api2_ae_setLinAeRouteAttr.argtypes = [POINTER(rk_aiq_sys_ctx_t), Uapi_LinAeRouteAttr_t]
    rk_aiq_user_api2_ae_setLinAeRouteAttr.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_ae.h: 38
if _libs["rkaiq"].has("rk_aiq_user_api2_ae_getLinAeRouteAttr", "cdecl"):
    rk_aiq_user_api2_ae_getLinAeRouteAttr = _libs["rkaiq"].get("rk_aiq_user_api2_ae_getLinAeRouteAttr", "cdecl")
    rk_aiq_user_api2_ae_getLinAeRouteAttr.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(Uapi_LinAeRouteAttr_t)]
    rk_aiq_user_api2_ae_getLinAeRouteAttr.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_ae.h: 39
if _libs["rkaiq"].has("rk_aiq_user_api2_ae_setHdrAeRouteAttr", "cdecl"):
    rk_aiq_user_api2_ae_setHdrAeRouteAttr = _libs["rkaiq"].get("rk_aiq_user_api2_ae_setHdrAeRouteAttr", "cdecl")
    rk_aiq_user_api2_ae_setHdrAeRouteAttr.argtypes = [POINTER(rk_aiq_sys_ctx_t), Uapi_HdrAeRouteAttr_t]
    rk_aiq_user_api2_ae_setHdrAeRouteAttr.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_ae.h: 40
if _libs["rkaiq"].has("rk_aiq_user_api2_ae_getHdrAeRouteAttr", "cdecl"):
    rk_aiq_user_api2_ae_getHdrAeRouteAttr = _libs["rkaiq"].get("rk_aiq_user_api2_ae_getHdrAeRouteAttr", "cdecl")
    rk_aiq_user_api2_ae_getHdrAeRouteAttr.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(Uapi_HdrAeRouteAttr_t)]
    rk_aiq_user_api2_ae_getHdrAeRouteAttr.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_ae.h: 42
if _libs["rkaiq"].has("rk_aiq_user_api2_ae_setIrisAttr", "cdecl"):
    rk_aiq_user_api2_ae_setIrisAttr = _libs["rkaiq"].get("rk_aiq_user_api2_ae_setIrisAttr", "cdecl")
    rk_aiq_user_api2_ae_setIrisAttr.argtypes = [POINTER(rk_aiq_sys_ctx_t), Uapi_IrisAttrV2_t]
    rk_aiq_user_api2_ae_setIrisAttr.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_ae.h: 43
if _libs["rkaiq"].has("rk_aiq_user_api2_ae_getIrisAttr", "cdecl"):
    rk_aiq_user_api2_ae_getIrisAttr = _libs["rkaiq"].get("rk_aiq_user_api2_ae_getIrisAttr", "cdecl")
    rk_aiq_user_api2_ae_getIrisAttr.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(Uapi_IrisAttrV2_t)]
    rk_aiq_user_api2_ae_getIrisAttr.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_ae.h: 44
if _libs["rkaiq"].has("rk_aiq_user_api2_ae_setSyncTestAttr", "cdecl"):
    rk_aiq_user_api2_ae_setSyncTestAttr = _libs["rkaiq"].get("rk_aiq_user_api2_ae_setSyncTestAttr", "cdecl")
    rk_aiq_user_api2_ae_setSyncTestAttr.argtypes = [POINTER(rk_aiq_sys_ctx_t), Uapi_AecSyncTest_t]
    rk_aiq_user_api2_ae_setSyncTestAttr.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_ae.h: 45
if _libs["rkaiq"].has("rk_aiq_user_api2_ae_getSyncTestAttr", "cdecl"):
    rk_aiq_user_api2_ae_getSyncTestAttr = _libs["rkaiq"].get("rk_aiq_user_api2_ae_getSyncTestAttr", "cdecl")
    rk_aiq_user_api2_ae_getSyncTestAttr.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(Uapi_AecSyncTest_t)]
    rk_aiq_user_api2_ae_getSyncTestAttr.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_ae.h: 47
if _libs["rkaiq"].has("rk_aiq_user_api2_ae_queryExpResInfo", "cdecl"):
    rk_aiq_user_api2_ae_queryExpResInfo = _libs["rkaiq"].get("rk_aiq_user_api2_ae_queryExpResInfo", "cdecl")
    rk_aiq_user_api2_ae_queryExpResInfo.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(Uapi_ExpQueryInfo_t)]
    rk_aiq_user_api2_ae_queryExpResInfo.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_ae.h: 48
if _libs["rkaiq"].has("rk_aiq_user_api2_ae_setExpWinAttr", "cdecl"):
    rk_aiq_user_api2_ae_setExpWinAttr = _libs["rkaiq"].get("rk_aiq_user_api2_ae_setExpWinAttr", "cdecl")
    rk_aiq_user_api2_ae_setExpWinAttr.argtypes = [POINTER(rk_aiq_sys_ctx_t), Uapi_ExpWin_t]
    rk_aiq_user_api2_ae_setExpWinAttr.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_ae.h: 49
if _libs["rkaiq"].has("rk_aiq_user_api2_ae_getExpWinAttr", "cdecl"):
    rk_aiq_user_api2_ae_getExpWinAttr = _libs["rkaiq"].get("rk_aiq_user_api2_ae_getExpWinAttr", "cdecl")
    rk_aiq_user_api2_ae_getExpWinAttr.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(Uapi_ExpWin_t)]
    rk_aiq_user_api2_ae_getExpWinAttr.restype = XCamReturn

enum_fec_correct_direction_e = c_int# /root/camera_engine_rkaiq/include/algos/afec/rk_aiq_types_afec_algo.h: 26

fec_correct_direction_t = enum_fec_correct_direction_e# /root/camera_engine_rkaiq/include/algos/afec/rk_aiq_types_afec_algo.h: 26

enum_fec_correct_mode_e = c_int# /root/camera_engine_rkaiq/include/algos/afec/rk_aiq_types_afec_algo.h: 32

fec_correct_mode_t = enum_fec_correct_mode_e# /root/camera_engine_rkaiq/include/algos/afec/rk_aiq_types_afec_algo.h: 32

# /root/camera_engine_rkaiq/include/algos/afec/rk_aiq_types_afec_algo_int.h: 12
class struct_rk_aiq_fec_cfg_s(Structure):
    pass

struct_rk_aiq_fec_cfg_s.__slots__ = [
    'en',
    'mode',
    'bypass',
    'correct_level',
    'direction',
]
struct_rk_aiq_fec_cfg_s._fields_ = [
    ('en', c_uint),
    ('mode', fec_correct_mode_t),
    ('bypass', c_int),
    ('correct_level', c_int),
    ('direction', fec_correct_direction_t),
]

rk_aiq_fec_cfg_t = struct_rk_aiq_fec_cfg_s# /root/camera_engine_rkaiq/include/algos/afec/rk_aiq_types_afec_algo_int.h: 12

rk_aiq_fec_attrib_t = rk_aiq_fec_cfg_t# /root/camera_engine_rkaiq/include/algos/afec/rk_aiq_uapi_afec_int.h: 8

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_afec.h: 25
if _libs["rkaiq"].has("rk_aiq_user_api2_afec_SetAttrib", "cdecl"):
    rk_aiq_user_api2_afec_SetAttrib = _libs["rkaiq"].get("rk_aiq_user_api2_afec_SetAttrib", "cdecl")
    rk_aiq_user_api2_afec_SetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), rk_aiq_fec_attrib_t]
    rk_aiq_user_api2_afec_SetAttrib.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_afec.h: 27
if _libs["rkaiq"].has("rk_aiq_user_api2_afec_GetAttrib", "cdecl"):
    rk_aiq_user_api2_afec_GetAttrib = _libs["rkaiq"].get("rk_aiq_user_api2_afec_GetAttrib", "cdecl")
    rk_aiq_user_api2_afec_GetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_fec_attrib_t)]
    rk_aiq_user_api2_afec_GetAttrib.restype = XCamReturn

enum_mems_sensor_type_e = c_int# /root/camera_engine_rkaiq/include/common/rk_aiq_mems_sensor.h: 35

mems_sensor_type_t = enum_mems_sensor_type_e# /root/camera_engine_rkaiq/include/common/rk_aiq_mems_sensor.h: 35

enum_mems_sensor_return_e = c_int# /root/camera_engine_rkaiq/include/common/rk_aiq_mems_sensor.h: 46

mems_sensor_return_t = enum_mems_sensor_return_e# /root/camera_engine_rkaiq/include/common/rk_aiq_mems_sensor.h: 46

# /root/camera_engine_rkaiq/include/common/rk_aiq_mems_sensor.h: 57
class struct_mems_sensor_capabilities_s(Structure):
    pass

struct_mems_sensor_capabilities_s.__slots__ = [
    'type',
    'resolutions',
    'num_resolutions',
    'scale',
    'num_scale',
    'sample_rates',
    'num_sample_rates',
    'is_data_valid',
]
struct_mems_sensor_capabilities_s._fields_ = [
    ('type', mems_sensor_type_t),
    ('resolutions', POINTER(c_double)),
    ('num_resolutions', uint8_t),
    ('scale', POINTER(c_double)),
    ('num_scale', uint8_t),
    ('sample_rates', POINTER(c_double)),
    ('num_sample_rates', uint8_t),
    ('is_data_valid', c_bool),
]

mems_sensor_capabilities_t = struct_mems_sensor_capabilities_s# /root/camera_engine_rkaiq/include/common/rk_aiq_mems_sensor.h: 57

# /root/camera_engine_rkaiq/include/common/rk_aiq_mems_sensor.h: 65
class struct_mems_sensor_config_s(Structure):
    pass

struct_mems_sensor_config_s.__slots__ = [
    'resolution',
    'scale',
    'sample_rate',
    'max_data_count',
    'buf_count',
]
struct_mems_sensor_config_s._fields_ = [
    ('resolution', c_double),
    ('scale', c_double),
    ('sample_rate', c_double),
    ('max_data_count', uint32_t),
    ('buf_count', uint32_t),
]

mems_sensor_config_t = struct_mems_sensor_config_s# /root/camera_engine_rkaiq/include/common/rk_aiq_mems_sensor.h: 65

# /root/camera_engine_rkaiq/include/common/rk_aiq_mems_sensor.h: 126
class struct_mems_sensor_list_s(Structure):
    pass

struct_mems_sensor_list_s.__slots__ = [
    'count',
    'key_list',
]
struct_mems_sensor_list_s._fields_ = [
    ('count', c_int),
    ('key_list', POINTER(POINTER(c_char))),
]

mems_sensor_list_t = struct_mems_sensor_list_s# /root/camera_engine_rkaiq/include/common/rk_aiq_mems_sensor.h: 126

mems_sensor_ctx_t = POINTER(None)# /root/camera_engine_rkaiq/include/common/rk_aiq_mems_sensor.h: 128

mems_sensor_handle_t = POINTER(None)# /root/camera_engine_rkaiq/include/common/rk_aiq_mems_sensor.h: 129

mems_sensor_data_t = POINTER(None)# /root/camera_engine_rkaiq/include/common/rk_aiq_mems_sensor.h: 130

rk_aiq_mems_sensor_createContext = CFUNCTYPE(UNCHECKED(mems_sensor_ctx_t), )# /root/camera_engine_rkaiq/include/common/rk_aiq_mems_sensor.h: 132

rk_aiq_mems_sensor_destroyContext = CFUNCTYPE(UNCHECKED(mems_sensor_return_t), mems_sensor_ctx_t)# /root/camera_engine_rkaiq/include/common/rk_aiq_mems_sensor.h: 133

rk_aiq_mems_sensor_getSensorList = CFUNCTYPE(UNCHECKED(mems_sensor_return_t), mems_sensor_ctx_t, mems_sensor_type_t, POINTER(mems_sensor_list_t))# /root/camera_engine_rkaiq/include/common/rk_aiq_mems_sensor.h: 134

rk_aiq_mems_sensor_releaseSensorList = CFUNCTYPE(UNCHECKED(mems_sensor_return_t), POINTER(mems_sensor_list_t))# /root/camera_engine_rkaiq/include/common/rk_aiq_mems_sensor.h: 137

rk_aiq_mems_sensor_getSensorCapabilities = CFUNCTYPE(UNCHECKED(mems_sensor_return_t), mems_sensor_ctx_t, mems_sensor_type_t, String, POINTER(mems_sensor_capabilities_t))# /root/camera_engine_rkaiq/include/common/rk_aiq_mems_sensor.h: 139

rk_aiq_mems_sensor_releaseSensorCapabilities = CFUNCTYPE(UNCHECKED(mems_sensor_return_t), POINTER(mems_sensor_capabilities_t))# /root/camera_engine_rkaiq/include/common/rk_aiq_mems_sensor.h: 142

rk_aiq_mems_sensor_getConfig = CFUNCTYPE(UNCHECKED(mems_sensor_return_t), mems_sensor_ctx_t, mems_sensor_type_t, String, POINTER(mems_sensor_config_t))# /root/camera_engine_rkaiq/include/common/rk_aiq_mems_sensor.h: 144

rk_aiq_mems_sensor_setConfig = CFUNCTYPE(UNCHECKED(mems_sensor_return_t), mems_sensor_ctx_t, mems_sensor_type_t, String, mems_sensor_config_t)# /root/camera_engine_rkaiq/include/common/rk_aiq_mems_sensor.h: 148

rk_aiq_mems_sensor_createHandle = CFUNCTYPE(UNCHECKED(mems_sensor_handle_t), mems_sensor_ctx_t, mems_sensor_type_t, String, uint32_t, uint32_t)# /root/camera_engine_rkaiq/include/common/rk_aiq_mems_sensor.h: 152

rk_aiq_mems_sensor_destroyHandle = CFUNCTYPE(UNCHECKED(mems_sensor_return_t), mems_sensor_handle_t)# /root/camera_engine_rkaiq/include/common/rk_aiq_mems_sensor.h: 157

rk_aiq_mems_sensor_getData = CFUNCTYPE(UNCHECKED(mems_sensor_data_t), mems_sensor_handle_t, POINTER(c_size_t))# /root/camera_engine_rkaiq/include/common/rk_aiq_mems_sensor.h: 158

rk_aiq_mems_sensor_getLastNSamples = CFUNCTYPE(UNCHECKED(mems_sensor_data_t), mems_sensor_handle_t, c_size_t)# /root/camera_engine_rkaiq/include/common/rk_aiq_mems_sensor.h: 160

rk_aiq_mems_sensor_releaseSamplesData = CFUNCTYPE(UNCHECKED(mems_sensor_return_t), mems_sensor_handle_t, mems_sensor_data_t)# /root/camera_engine_rkaiq/include/common/rk_aiq_mems_sensor.h: 162

# /root/camera_engine_rkaiq/include/common/rk_aiq_mems_sensor.h: 179
class struct_rk_aiq_mems_sensor_intf_s(Structure):
    pass

struct_rk_aiq_mems_sensor_intf_s.__slots__ = [
    'createContext',
    'destroyContext',
    'getSensorList',
    'releaseSensorList',
    'getSensorCapabilities',
    'releaseSensorCapabilities',
    'getConfig',
    'setConfig',
    'createHandle',
    'destroyHandle',
    'getData',
    'getLastNSamples',
    'releaseSamplesData',
]
struct_rk_aiq_mems_sensor_intf_s._fields_ = [
    ('createContext', rk_aiq_mems_sensor_createContext),
    ('destroyContext', rk_aiq_mems_sensor_destroyContext),
    ('getSensorList', rk_aiq_mems_sensor_getSensorList),
    ('releaseSensorList', rk_aiq_mems_sensor_releaseSensorList),
    ('getSensorCapabilities', rk_aiq_mems_sensor_getSensorCapabilities),
    ('releaseSensorCapabilities', rk_aiq_mems_sensor_releaseSensorCapabilities),
    ('getConfig', rk_aiq_mems_sensor_getConfig),
    ('setConfig', rk_aiq_mems_sensor_setConfig),
    ('createHandle', rk_aiq_mems_sensor_createHandle),
    ('destroyHandle', rk_aiq_mems_sensor_destroyHandle),
    ('getData', rk_aiq_mems_sensor_getData),
    ('getLastNSamples', rk_aiq_mems_sensor_getLastNSamples),
    ('releaseSamplesData', rk_aiq_mems_sensor_releaseSamplesData),
]

rk_aiq_mems_sensor_intf_t = struct_rk_aiq_mems_sensor_intf_s# /root/camera_engine_rkaiq/include/common/rk_aiq_mems_sensor.h: 179

enum_rk_aiq_down_scale_mode_e = c_int# /root/camera_engine_rkaiq/include/algos/awb/rk_aiq_types_awb_stat_v2xx.h: 44

rk_aiq_down_scale_mode_t = enum_rk_aiq_down_scale_mode_e# /root/camera_engine_rkaiq/include/algos/awb/rk_aiq_types_awb_stat_v2xx.h: 44

# /root/camera_engine_rkaiq/include/algos/awb/rk_aiq_types_awb_stat_v2xx.h: 49
class struct_rk_aiq_rgb2xy_para_s(Structure):
    pass

struct_rk_aiq_rgb2xy_para_s.__slots__ = [
    'pseudoLuminanceWeight',
    'rotationMat',
]
struct_rk_aiq_rgb2xy_para_s._fields_ = [
    ('pseudoLuminanceWeight', c_ushort * int(3)),
    ('rotationMat', c_short * int(9)),
]

rk_aiq_rgb2xy_para_t = struct_rk_aiq_rgb2xy_para_s# /root/camera_engine_rkaiq/include/algos/awb/rk_aiq_types_awb_stat_v2xx.h: 49

# /root/camera_engine_rkaiq/include/algos/awb/rk_aiq_types_awb_stat_v2xx.h: 57
class struct_rk_aiq_awb_xy_range_para_s(Structure):
    pass

struct_rk_aiq_awb_xy_range_para_s.__slots__ = [
    'NorrangeX',
    'NorrangeY',
    'SperangeX',
    'SperangeY',
    'SmalrangeX',
    'SmalrangeY',
]
struct_rk_aiq_awb_xy_range_para_s._fields_ = [
    ('NorrangeX', c_int * int(2)),
    ('NorrangeY', c_int * int(2)),
    ('SperangeX', c_int * int(2)),
    ('SperangeY', c_int * int(2)),
    ('SmalrangeX', c_int * int(2)),
    ('SmalrangeY', c_int * int(2)),
]

rk_aiq_awb_xy_range_para_t = struct_rk_aiq_awb_xy_range_para_s# /root/camera_engine_rkaiq/include/algos/awb/rk_aiq_types_awb_stat_v2xx.h: 57

# /root/camera_engine_rkaiq/include/algos/awb/rk_aiq_types_awb_stat_v2xx.h: 63
class struct_rk_aiq_awb_uv_range_para_s(Structure):
    pass

struct_rk_aiq_awb_uv_range_para_s.__slots__ = [
    'pu_region',
    'pv_region',
    'slope_inv',
]
struct_rk_aiq_awb_uv_range_para_s._fields_ = [
    ('pu_region', c_ushort * int(5)),
    ('pv_region', c_ushort * int(5)),
    ('slope_inv', c_int * int(4)),
]

rk_aiq_awb_uv_range_para_t = struct_rk_aiq_awb_uv_range_para_s# /root/camera_engine_rkaiq/include/algos/awb/rk_aiq_types_awb_stat_v2xx.h: 63

# /root/camera_engine_rkaiq/include/algos/awb/rk_aiq_types_awb_stat_v2xx.h: 75
class struct_rk_aiq_awb_3dyuv_range_para_s(Structure):
    pass

struct_rk_aiq_awb_3dyuv_range_para_s.__slots__ = [
    'b_uv',
    'slope_inv_neg_uv',
    'slope_factor_uv',
    'slope_ydis',
    'b_ydis',
    'ref_u',
    'ref_v',
    'dis',
    'th',
]
struct_rk_aiq_awb_3dyuv_range_para_s._fields_ = [
    ('b_uv', c_int),
    ('slope_inv_neg_uv', c_int),
    ('slope_factor_uv', c_int),
    ('slope_ydis', c_int),
    ('b_ydis', c_int),
    ('ref_u', c_ubyte),
    ('ref_v', c_ubyte),
    ('dis', c_ushort * int(6)),
    ('th', c_ubyte * int(6)),
]

rk_aiq_awb_3dyuv_range_para_t = struct_rk_aiq_awb_3dyuv_range_para_s# /root/camera_engine_rkaiq/include/algos/awb/rk_aiq_types_awb_stat_v2xx.h: 75

# /root/camera_engine_rkaiq/include/algos/awb/rk_aiq_types_awb_stat_v2xx.h: 83
class struct_rk_aiq_awb_rt3dyuv_range_para_s(Structure):
    pass

struct_rk_aiq_awb_rt3dyuv_range_para_s.__slots__ = [
    'thcurve_u',
    'thcure_th',
    'lineP1',
    'vP1P2',
    'disP1P2',
]
struct_rk_aiq_awb_rt3dyuv_range_para_s._fields_ = [
    ('thcurve_u', c_ubyte * int(6)),
    ('thcure_th', c_ushort * int(6)),
    ('lineP1', c_ushort * int(3)),
    ('vP1P2', c_short * int(3)),
    ('disP1P2', c_ubyte),
]

rk_aiq_awb_rt3dyuv_range_para_t = struct_rk_aiq_awb_rt3dyuv_range_para_s# /root/camera_engine_rkaiq/include/algos/awb/rk_aiq_types_awb_stat_v2xx.h: 83

enum_rk_aiq_awb_exc_range_domain_e = c_int# /root/camera_engine_rkaiq/include/algos/awb/rk_aiq_types_awb_stat_v2xx.h: 89

rk_aiq_awb_exc_range_domain_t = enum_rk_aiq_awb_exc_range_domain_e# /root/camera_engine_rkaiq/include/algos/awb/rk_aiq_types_awb_stat_v2xx.h: 89

RK_AIQ_AWB_XY_TYPE_SMALL_V200 = 2# /root/camera_engine_rkaiq/include/algos/awb/rk_aiq_types_awb_stat_v200.h: 36

RK_AIQ_AWB_XY_TYPE_MAX_V200 = (RK_AIQ_AWB_XY_TYPE_SMALL_V200 + 1)# /root/camera_engine_rkaiq/include/algos/awb/rk_aiq_types_awb_stat_v200.h: 36

enum_rk_aiq_blk_stat_mode_v200_e = c_int# /root/camera_engine_rkaiq/include/algos/awb/rk_aiq_types_awb_stat_v200.h: 44

rk_aiq_blk_stat_mode_v200_t = enum_rk_aiq_blk_stat_mode_v200_e# /root/camera_engine_rkaiq/include/algos/awb/rk_aiq_types_awb_stat_v200.h: 44

# /root/camera_engine_rkaiq/include/algos/awb/rk_aiq_types_awb_stat_v200.h: 51
class struct_rk_aiq_awb_exc_range_s(Structure):
    pass

struct_rk_aiq_awb_exc_range_s.__slots__ = [
    'domain',
    'excludeEnable',
    'measureEnable',
    'xu',
    'yv',
]
struct_rk_aiq_awb_exc_range_s._fields_ = [
    ('domain', rk_aiq_awb_exc_range_domain_t),
    ('excludeEnable', c_bool),
    ('measureEnable', c_bool),
    ('xu', c_int * int(2)),
    ('yv', c_int * int(2)),
]

rk_aiq_awb_exc_range_t = struct_rk_aiq_awb_exc_range_s# /root/camera_engine_rkaiq/include/algos/awb/rk_aiq_types_awb_stat_v200.h: 51

# /root/camera_engine_rkaiq/include/algos/awb/rk_aiq_types_awb_stat_v200.h: 91
class struct_rk_aiq_awb_stat_cfg_v200_s(Structure):
    pass

struct_rk_aiq_awb_stat_cfg_v200_s.__slots__ = [
    'awbEnable',
    'lscBypEnable',
    'uvDetectionEnable',
    'xyDetectionEnable',
    'storeWpFlagIllu',
    'threeDyuvIllu',
    'dsMode',
    'blkMeasureMode',
    'blkMeasWpTh',
    'multiwindow_en',
    'frameChoose',
    'rgb2yuv_c_range',
    'rgb2yuv_y_range',
    'rgb2yuv_matrix',
    'windowSet',
    'lightNum',
    'maxR',
    'minR',
    'maxG',
    'minG',
    'maxB',
    'minB',
    'maxY',
    'minY',
    'uvRange_param',
    'yuvRange_param',
    'rgb2xy_param',
    'xyRange_param',
    'multiwindow',
    'excludeWpRange',
    'groupIllIndxCurrent',
    'IllIndxSetCurrent',
    'timeSign',
]
struct_rk_aiq_awb_stat_cfg_v200_s._fields_ = [
    ('awbEnable', c_bool),
    ('lscBypEnable', c_bool),
    ('uvDetectionEnable', c_bool),
    ('xyDetectionEnable', c_bool),
    ('storeWpFlagIllu', c_ushort * int(3)),
    ('threeDyuvIllu', c_ushort * int(4)),
    ('dsMode', rk_aiq_down_scale_mode_t),
    ('blkMeasureMode', rk_aiq_blk_stat_mode_v200_t),
    ('blkMeasWpTh', c_ushort * int(3)),
    ('multiwindow_en', c_bool),
    ('frameChoose', uint8_t),
    ('rgb2yuv_c_range', uint8_t),
    ('rgb2yuv_y_range', uint8_t),
    ('rgb2yuv_matrix', c_short * int(9)),
    ('windowSet', c_ushort * int(4)),
    ('lightNum', c_ubyte),
    ('maxR', c_ushort),
    ('minR', c_ushort),
    ('maxG', c_ushort),
    ('minG', c_ushort),
    ('maxB', c_ushort),
    ('minB', c_ushort),
    ('maxY', c_ushort),
    ('minY', c_ushort),
    ('uvRange_param', rk_aiq_awb_uv_range_para_t * int(7)),
    ('yuvRange_param', rk_aiq_awb_3dyuv_range_para_t * int(4)),
    ('rgb2xy_param', rk_aiq_rgb2xy_para_t),
    ('xyRange_param', rk_aiq_awb_xy_range_para_t * int(7)),
    ('multiwindow', (c_ushort * int(4)) * int(8)),
    ('excludeWpRange', rk_aiq_awb_exc_range_t * int(7)),
    ('groupIllIndxCurrent', c_int),
    ('IllIndxSetCurrent', c_int * int(7)),
    ('timeSign', c_char * int(64)),
]

rk_aiq_awb_stat_cfg_v200_t = struct_rk_aiq_awb_stat_cfg_v200_s# /root/camera_engine_rkaiq/include/algos/awb/rk_aiq_types_awb_stat_v200.h: 91

# /root/camera_engine_rkaiq/include/algos/awb/rk_aiq_types_awb_stat_v200.h: 98
class struct_rk_aiq_awb_stat_wp_res_v200_s(Structure):
    pass

struct_rk_aiq_awb_stat_wp_res_v200_s.__slots__ = [
    'WpNo',
    'Rvalue',
    'Gvalue',
    'Bvalue',
]
struct_rk_aiq_awb_stat_wp_res_v200_s._fields_ = [
    ('WpNo', c_uint),
    ('Rvalue', c_uint),
    ('Gvalue', c_uint),
    ('Bvalue', c_uint),
]

rk_aiq_awb_stat_wp_res_v200_t = struct_rk_aiq_awb_stat_wp_res_v200_s# /root/camera_engine_rkaiq/include/algos/awb/rk_aiq_types_awb_stat_v200.h: 98

# /root/camera_engine_rkaiq/include/algos/awb/rk_aiq_types_awb_stat_v200.h: 105
class struct_rk_aiq_awb_stat_blk_res_v200_s(Structure):
    pass

struct_rk_aiq_awb_stat_blk_res_v200_s.__slots__ = [
    'Rvalue',
    'Gvalue',
    'Bvalue',
    'isWP',
]
struct_rk_aiq_awb_stat_blk_res_v200_s._fields_ = [
    ('Rvalue', c_uint),
    ('Gvalue', c_uint),
    ('Bvalue', c_uint),
    ('isWP', c_bool * int(3)),
]

rk_aiq_awb_stat_blk_res_v200_t = struct_rk_aiq_awb_stat_blk_res_v200_s# /root/camera_engine_rkaiq/include/algos/awb/rk_aiq_types_awb_stat_v200.h: 105

# /root/camera_engine_rkaiq/include/algos/awb/rk_aiq_types_awb_stat_v200.h: 109
class struct_rk_aiq_awb_stat_wp_res_light_v200_s(Structure):
    pass

struct_rk_aiq_awb_stat_wp_res_light_v200_s.__slots__ = [
    'xYType',
]
struct_rk_aiq_awb_stat_wp_res_light_v200_s._fields_ = [
    ('xYType', rk_aiq_awb_stat_wp_res_v200_t * int(RK_AIQ_AWB_XY_TYPE_MAX_V200)),
]

rk_aiq_awb_stat_wp_res_light_v200_t = struct_rk_aiq_awb_stat_wp_res_light_v200_s# /root/camera_engine_rkaiq/include/algos/awb/rk_aiq_types_awb_stat_v200.h: 109

# /root/camera_engine_rkaiq/include/algos/awb/rk_aiq_types_awb_stat_v200.h: 120
class struct_rk_aiq_awb_stat_res_v200_s(Structure):
    pass

struct_rk_aiq_awb_stat_res_v200_s.__slots__ = [
    'light',
    'blockResult',
    'multiwindowLightResult',
    'excWpRangeResult',
    'awb_cfg_effect_v200',
]
struct_rk_aiq_awb_stat_res_v200_s._fields_ = [
    ('light', rk_aiq_awb_stat_wp_res_light_v200_t * int(7)),
    ('blockResult', rk_aiq_awb_stat_blk_res_v200_t * int((15 * 15))),
    ('multiwindowLightResult', rk_aiq_awb_stat_wp_res_light_v200_t * int(7)),
    ('excWpRangeResult', rk_aiq_awb_stat_wp_res_v200_t * int(7)),
    ('awb_cfg_effect_v200', rk_aiq_awb_stat_cfg_v200_t),
]

rk_aiq_awb_stat_res_v200_t = struct_rk_aiq_awb_stat_res_v200_s# /root/camera_engine_rkaiq/include/algos/awb/rk_aiq_types_awb_stat_v200.h: 120

enum_rk_aiq_awb_xy_type_v201_e = c_int# /root/camera_engine_rkaiq/include/algos/awb/rk_aiq_types_awb_stat_v201.h: 58

RK_AIQ_AWB_XY_TYPE_BIG_V201 = 1# /root/camera_engine_rkaiq/include/algos/awb/rk_aiq_types_awb_stat_v201.h: 58

RK_AIQ_AWB_XY_TYPE_MAX_V201 = (RK_AIQ_AWB_XY_TYPE_BIG_V201 + 1)# /root/camera_engine_rkaiq/include/algos/awb/rk_aiq_types_awb_stat_v201.h: 58

rk_aiq_awb_xy_type_v201_t = enum_rk_aiq_awb_xy_type_v201_e# /root/camera_engine_rkaiq/include/algos/awb/rk_aiq_types_awb_stat_v201.h: 58

enum_rk_aiq_awb_blk_stat_mode_v201_e = c_int# /root/camera_engine_rkaiq/include/algos/awb/rk_aiq_types_awb_stat_v201.h: 65

rk_aiq_awb_blk_stat_mode_v201_t = enum_rk_aiq_awb_blk_stat_mode_v201_e# /root/camera_engine_rkaiq/include/algos/awb/rk_aiq_types_awb_stat_v201.h: 65

# /root/camera_engine_rkaiq/include/algos/awb/rk_aiq_types_awb_stat_v201.h: 73
class struct_rk_aiq_awb_exc_range_v201_s(Structure):
    pass

struct_rk_aiq_awb_exc_range_v201_s.__slots__ = [
    'domain',
    'excludeEnable',
    'measureEnable',
    'xu',
    'yv',
]
struct_rk_aiq_awb_exc_range_v201_s._fields_ = [
    ('domain', rk_aiq_awb_exc_range_domain_t),
    ('excludeEnable', c_bool * int(RK_AIQ_AWB_XY_TYPE_MAX_V201)),
    ('measureEnable', c_bool),
    ('xu', c_int * int(2)),
    ('yv', c_int * int(2)),
]

rk_aiq_awb_exc_range_v201_t = struct_rk_aiq_awb_exc_range_v201_s# /root/camera_engine_rkaiq/include/algos/awb/rk_aiq_types_awb_stat_v201.h: 73

enum_RK_AIQ_AWB_BLK_STAT_REALWP_ILL_S = c_int# /root/camera_engine_rkaiq/include/algos/awb/rk_aiq_types_awb_stat_v201.h: 85

rk_aiq_awb_blk_stat_realwp_ill_e = enum_RK_AIQ_AWB_BLK_STAT_REALWP_ILL_S# /root/camera_engine_rkaiq/include/algos/awb/rk_aiq_types_awb_stat_v201.h: 85

# /root/camera_engine_rkaiq/include/algos/awb/rk_aiq_types_awb_stat_v201.h: 152
class struct_rk_aiq_awb_stat_wp_res_v201_s(Structure):
    pass

struct_rk_aiq_awb_stat_wp_res_v201_s.__slots__ = [
    'WpNo',
    'RgainValue',
    'BgainValue',
]
struct_rk_aiq_awb_stat_wp_res_v201_s._fields_ = [
    ('WpNo', c_longlong),
    ('RgainValue', c_longlong),
    ('BgainValue', c_longlong),
]

rk_aiq_awb_stat_wp_res_v201_t = struct_rk_aiq_awb_stat_wp_res_v201_s# /root/camera_engine_rkaiq/include/algos/awb/rk_aiq_types_awb_stat_v201.h: 152

# /root/camera_engine_rkaiq/include/algos/awb/rk_aiq_types_awb_stat_v201.h: 159
class struct_rk_aiq_awb_stat_blk_res_v201_s(Structure):
    pass

struct_rk_aiq_awb_stat_blk_res_v201_s.__slots__ = [
    'WpNo',
    'Rvalue',
    'Gvalue',
    'Bvalue',
]
struct_rk_aiq_awb_stat_blk_res_v201_s._fields_ = [
    ('WpNo', c_longlong),
    ('Rvalue', c_longlong),
    ('Gvalue', c_longlong),
    ('Bvalue', c_longlong),
]

rk_aiq_awb_stat_blk_res_v201_t = struct_rk_aiq_awb_stat_blk_res_v201_s# /root/camera_engine_rkaiq/include/algos/awb/rk_aiq_types_awb_stat_v201.h: 159

# /root/camera_engine_rkaiq/include/algos/awb/rk_aiq_types_awb_stat_v201.h: 163
class struct_rk_aiq_awb_stat_wp_res_light_v201_s(Structure):
    pass

struct_rk_aiq_awb_stat_wp_res_light_v201_s.__slots__ = [
    'xYType',
]
struct_rk_aiq_awb_stat_wp_res_light_v201_s._fields_ = [
    ('xYType', rk_aiq_awb_stat_wp_res_v201_t * int(RK_AIQ_AWB_XY_TYPE_MAX_V201)),
]

rk_aiq_awb_stat_wp_res_light_v201_t = struct_rk_aiq_awb_stat_wp_res_light_v201_s# /root/camera_engine_rkaiq/include/algos/awb/rk_aiq_types_awb_stat_v201.h: 163

# /root/camera_engine_rkaiq/include/algos/awb/rk_aiq_types_awb_stat_v201.h: 195
class struct_rk_aiq_awb_stat_res2_v201_s(Structure):
    pass

struct_rk_aiq_awb_stat_res2_v201_s.__slots__ = [
    'light',
    'blockResult',
    'WpNoHist',
]
struct_rk_aiq_awb_stat_res2_v201_s._fields_ = [
    ('light', rk_aiq_awb_stat_wp_res_light_v201_t * int(7)),
    ('blockResult', rk_aiq_awb_stat_blk_res_v201_t * int((15 * 15))),
    ('WpNoHist', c_uint * int(8)),
]

rk_aiq_awb_stat_res2_v201_t = struct_rk_aiq_awb_stat_res2_v201_s# /root/camera_engine_rkaiq/include/algos/awb/rk_aiq_types_awb_stat_v201.h: 195

# /root/camera_engine_rkaiq/include/algos/awb/rk_aiq_types_awb_stat_v201.h: 210
class struct_rk_aiq_awb_stat_res2_v30_s(Structure):
    pass

struct_rk_aiq_awb_stat_res2_v30_s.__slots__ = [
    'light',
    'WpNo2',
    'blockResult',
    'multiwindowLightResult',
    'excWpRangeResult',
    'WpNoHist',
]
struct_rk_aiq_awb_stat_res2_v30_s._fields_ = [
    ('light', rk_aiq_awb_stat_wp_res_light_v201_t * int(7)),
    ('WpNo2', c_int * int(7)),
    ('blockResult', rk_aiq_awb_stat_blk_res_v201_t * int((15 * 15))),
    ('multiwindowLightResult', rk_aiq_awb_stat_wp_res_light_v201_t * int(4)),
    ('excWpRangeResult', rk_aiq_awb_stat_wp_res_v201_t * int(4)),
    ('WpNoHist', c_uint * int(8)),
]

rk_aiq_awb_stat_res2_v30_t = struct_rk_aiq_awb_stat_res2_v30_s# /root/camera_engine_rkaiq/include/algos/awb/rk_aiq_types_awb_stat_v201.h: 210

# /root/camera_engine_rkaiq/include/algos/awb/rk_aiq_types_awb_algo.h: 34
class struct_rk_aiq_wb_gain_s(Structure):
    pass

struct_rk_aiq_wb_gain_s.__slots__ = [
    'rgain',
    'grgain',
    'gbgain',
    'bgain',
]
struct_rk_aiq_wb_gain_s._fields_ = [
    ('rgain', c_float),
    ('grgain', c_float),
    ('gbgain', c_float),
    ('bgain', c_float),
]

rk_aiq_wb_gain_t = struct_rk_aiq_wb_gain_s# /root/camera_engine_rkaiq/include/algos/awb/rk_aiq_types_awb_algo.h: 34

enum_MergeBaseFrame_e = c_int# /root/camera_engine_rkaiq/include/iq_parser_v2/amerge_head.h: 82

MergeBaseFrame_t = enum_MergeBaseFrame_e# /root/camera_engine_rkaiq/include/iq_parser_v2/amerge_head.h: 82

# /root/camera_engine_rkaiq/include/iq_parser_v2/amerge_uapi_head.h: 16
class struct_mMergeOECurveV21_s(Structure):
    pass

struct_mMergeOECurveV21_s.__slots__ = [
    'Smooth',
    'Offset',
]
struct_mMergeOECurveV21_s._fields_ = [
    ('Smooth', c_float),
    ('Offset', c_float),
]

mMergeOECurveV21_t = struct_mMergeOECurveV21_s# /root/camera_engine_rkaiq/include/iq_parser_v2/amerge_uapi_head.h: 16

# /root/camera_engine_rkaiq/include/iq_parser_v2/amerge_uapi_head.h: 27
class struct_mMergeMDCurveV21_s(Structure):
    pass

struct_mMergeMDCurveV21_s.__slots__ = [
    'LM_smooth',
    'LM_offset',
    'MS_smooth',
    'MS_offset',
]
struct_mMergeMDCurveV21_s._fields_ = [
    ('LM_smooth', c_float),
    ('LM_offset', c_float),
    ('MS_smooth', c_float),
    ('MS_offset', c_float),
]

mMergeMDCurveV21_t = struct_mMergeMDCurveV21_s# /root/camera_engine_rkaiq/include/iq_parser_v2/amerge_uapi_head.h: 27

# /root/camera_engine_rkaiq/include/iq_parser_v2/amerge_uapi_head.h: 34
class struct_mmergeAttrV21_s(Structure):
    pass

struct_mmergeAttrV21_s.__slots__ = [
    'OECurve',
    'MDCurve',
]
struct_mmergeAttrV21_s._fields_ = [
    ('OECurve', mMergeOECurveV21_t),
    ('MDCurve', mMergeMDCurveV21_t),
]

mmergeAttrV21_t = struct_mmergeAttrV21_s# /root/camera_engine_rkaiq/include/iq_parser_v2/amerge_uapi_head.h: 34

# /root/camera_engine_rkaiq/include/iq_parser_v2/amerge_uapi_head.h: 41
class struct_mLongFrameModeData_s(Structure):
    pass

struct_mLongFrameModeData_s.__slots__ = [
    'OECurve',
    'MDCurve',
]
struct_mLongFrameModeData_s._fields_ = [
    ('OECurve', mMergeOECurveV21_t),
    ('MDCurve', mMergeMDCurveV21_t),
]

mLongFrameModeData_t = struct_mLongFrameModeData_s# /root/camera_engine_rkaiq/include/iq_parser_v2/amerge_uapi_head.h: 41

# /root/camera_engine_rkaiq/include/iq_parser_v2/amerge_uapi_head.h: 50
class struct_mMergeMDCurveV30Short_s(Structure):
    pass

struct_mMergeMDCurveV30Short_s.__slots__ = [
    'Coef',
    'ms_thd0',
    'lm_thd0',
]
struct_mMergeMDCurveV30Short_s._fields_ = [
    ('Coef', c_float),
    ('ms_thd0', c_float),
    ('lm_thd0', c_float),
]

mMergeMDCurveV30Short_t = struct_mMergeMDCurveV30Short_s# /root/camera_engine_rkaiq/include/iq_parser_v2/amerge_uapi_head.h: 50

# /root/camera_engine_rkaiq/include/iq_parser_v2/amerge_uapi_head.h: 57
class struct_mShortFrameModeData_s(Structure):
    pass

struct_mShortFrameModeData_s.__slots__ = [
    'OECurve',
    'MDCurve',
]
struct_mShortFrameModeData_s._fields_ = [
    ('OECurve', mMergeOECurveV21_t),
    ('MDCurve', mMergeMDCurveV30Short_t),
]

mShortFrameModeData_t = struct_mShortFrameModeData_s# /root/camera_engine_rkaiq/include/iq_parser_v2/amerge_uapi_head.h: 57

# /root/camera_engine_rkaiq/include/iq_parser_v2/amerge_uapi_head.h: 66
class struct_mMergeAttrV30_s(Structure):
    pass

struct_mMergeAttrV30_s.__slots__ = [
    'BaseFrm',
    'LongFrmModeData',
    'ShortFrmModeData',
]
struct_mMergeAttrV30_s._fields_ = [
    ('BaseFrm', MergeBaseFrame_t),
    ('LongFrmModeData', mLongFrameModeData_t),
    ('ShortFrmModeData', mShortFrameModeData_t),
]

mMergeAttrV30_t = struct_mMergeAttrV30_s# /root/camera_engine_rkaiq/include/iq_parser_v2/amerge_uapi_head.h: 66

# /root/camera_engine_rkaiq/include/iq_parser_v2/amerge_uapi_head.h: 75
class struct_uapiMergeCurrCtlData_s(Structure):
    pass

struct_uapiMergeCurrCtlData_s.__slots__ = [
    'Envlv',
    'ISO',
    'MoveCoef',
]
struct_uapiMergeCurrCtlData_s._fields_ = [
    ('Envlv', c_float),
    ('ISO', c_float),
    ('MoveCoef', c_float),
]

uapiMergeCurrCtlData_t = struct_uapiMergeCurrCtlData_s# /root/camera_engine_rkaiq/include/iq_parser_v2/amerge_uapi_head.h: 75

enum_merge_OpModeV21_e = c_int# /root/camera_engine_rkaiq/include/algos/amerge/rk_aiq_types_amerge_algo_int.h: 27

merge_OpModeV21_t = enum_merge_OpModeV21_e# /root/camera_engine_rkaiq/include/algos/amerge/rk_aiq_types_amerge_algo_int.h: 27

MergeCurrCtlData_t = uapiMergeCurrCtlData_t# /root/camera_engine_rkaiq/include/algos/amerge/rk_aiq_types_amerge_algo_int.h: 29

# /root/camera_engine_rkaiq/include/algos/amerge/rk_aiq_types_amerge_algo_int.h: 36
class struct_mergeAttrV21_s(Structure):
    pass

struct_mergeAttrV21_s.__slots__ = [
    'opMode',
    'stManual',
    'CtlInfo',
]
struct_mergeAttrV21_s._fields_ = [
    ('opMode', merge_OpModeV21_t),
    ('stManual', mmergeAttrV21_t),
    ('CtlInfo', MergeCurrCtlData_t),
]

mergeAttrV21_t = struct_mergeAttrV21_s# /root/camera_engine_rkaiq/include/algos/amerge/rk_aiq_types_amerge_algo_int.h: 36

# /root/camera_engine_rkaiq/include/algos/amerge/rk_aiq_types_amerge_algo_int.h: 43
class struct_mergeAttrV30_s(Structure):
    pass

struct_mergeAttrV30_s.__slots__ = [
    'opMode',
    'stManual',
    'CtlInfo',
]
struct_mergeAttrV30_s._fields_ = [
    ('opMode', merge_OpModeV21_t),
    ('stManual', mMergeAttrV30_t),
    ('CtlInfo', MergeCurrCtlData_t),
]

mergeAttrV30_t = struct_mergeAttrV30_s# /root/camera_engine_rkaiq/include/algos/amerge/rk_aiq_types_amerge_algo_int.h: 43

# /root/camera_engine_rkaiq/include/algos/amerge/rk_aiq_types_amerge_algo_int.h: 50
class struct_mergeAttr_s(Structure):
    pass

struct_mergeAttr_s.__slots__ = [
    'sync',
    'attrV21',
    'attrV30',
]
struct_mergeAttr_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('attrV21', mergeAttrV21_t),
    ('attrV30', mergeAttrV30_t),
]

mergeAttr_t = struct_mergeAttr_s# /root/camera_engine_rkaiq/include/algos/amerge/rk_aiq_types_amerge_algo_int.h: 50

enum_GlobalLumaMode_e = c_int# /root/camera_engine_rkaiq/include/iq_parser_v2/atmo_head.h: 30

GlobalLumaMode_t = enum_GlobalLumaMode_e# /root/camera_engine_rkaiq/include/iq_parser_v2/atmo_head.h: 30

# /root/camera_engine_rkaiq/include/iq_parser_v2/atmo_head.h: 43
class struct_GlobalLumaData_s(Structure):
    pass

struct_GlobalLumaData_s.__slots__ = [
    'EnvLv',
    'EnvLv_len',
    'ISO',
    'ISO_len',
    'Strength',
    'Strength_len',
]
struct_GlobalLumaData_s._fields_ = [
    ('EnvLv', POINTER(c_float)),
    ('EnvLv_len', c_int),
    ('ISO', POINTER(c_float)),
    ('ISO_len', c_int),
    ('Strength', POINTER(c_float)),
    ('Strength_len', c_int),
]

GlobalLumaData_t = struct_GlobalLumaData_s# /root/camera_engine_rkaiq/include/iq_parser_v2/atmo_head.h: 43

# /root/camera_engine_rkaiq/include/iq_parser_v2/atmo_head.h: 53
class struct_CalibDbGlobalLuma_s(Structure):
    pass

struct_CalibDbGlobalLuma_s.__slots__ = [
    'Mode',
    'GlobalLumaData',
    'Tolerance',
]
struct_CalibDbGlobalLuma_s._fields_ = [
    ('Mode', GlobalLumaMode_t),
    ('GlobalLumaData', GlobalLumaData_t),
    ('Tolerance', c_float),
]

CalibDbGlobalLuma_t = struct_CalibDbGlobalLuma_s# /root/camera_engine_rkaiq/include/iq_parser_v2/atmo_head.h: 53

enum_DetailsHighLightMode_e = c_int# /root/camera_engine_rkaiq/include/iq_parser_v2/atmo_head.h: 58

DetailsHighLightMode_t = enum_DetailsHighLightMode_e# /root/camera_engine_rkaiq/include/iq_parser_v2/atmo_head.h: 58

# /root/camera_engine_rkaiq/include/iq_parser_v2/atmo_head.h: 71
class struct_HighLightData_s(Structure):
    pass

struct_HighLightData_s.__slots__ = [
    'OEPdf',
    'OEPdf_len',
    'EnvLv',
    'EnvLv_len',
    'Strength',
    'Strength_len',
]
struct_HighLightData_s._fields_ = [
    ('OEPdf', POINTER(c_float)),
    ('OEPdf_len', c_int),
    ('EnvLv', POINTER(c_float)),
    ('EnvLv_len', c_int),
    ('Strength', POINTER(c_float)),
    ('Strength_len', c_int),
]

HighLightData_t = struct_HighLightData_s# /root/camera_engine_rkaiq/include/iq_parser_v2/atmo_head.h: 71

# /root/camera_engine_rkaiq/include/iq_parser_v2/atmo_head.h: 81
class struct_CalibDbDetailsHighLight_s(Structure):
    pass

struct_CalibDbDetailsHighLight_s.__slots__ = [
    'Mode',
    'HighLightData',
    'Tolerance',
]
struct_CalibDbDetailsHighLight_s._fields_ = [
    ('Mode', DetailsHighLightMode_t),
    ('HighLightData', HighLightData_t),
    ('Tolerance', c_float),
]

CalibDbDetailsHighLight_t = struct_CalibDbDetailsHighLight_s# /root/camera_engine_rkaiq/include/iq_parser_v2/atmo_head.h: 81

enum_DetailsLowLightMode_e = c_int# /root/camera_engine_rkaiq/include/iq_parser_v2/atmo_head.h: 87

DetailsLowLightMode_t = enum_DetailsLowLightMode_e# /root/camera_engine_rkaiq/include/iq_parser_v2/atmo_head.h: 87

# /root/camera_engine_rkaiq/include/iq_parser_v2/atmo_head.h: 103
class struct_LowLightData_s(Structure):
    pass

struct_LowLightData_s.__slots__ = [
    'FocusLuma',
    'FocusLuma_len',
    'DarkPdf',
    'DarkPdf_len',
    'ISO',
    'ISO_len',
    'Strength',
    'Strength_len',
]
struct_LowLightData_s._fields_ = [
    ('FocusLuma', POINTER(c_float)),
    ('FocusLuma_len', c_int),
    ('DarkPdf', POINTER(c_float)),
    ('DarkPdf_len', c_int),
    ('ISO', POINTER(c_float)),
    ('ISO_len', c_int),
    ('Strength', POINTER(c_float)),
    ('Strength_len', c_int),
]

LowLightData_t = struct_LowLightData_s# /root/camera_engine_rkaiq/include/iq_parser_v2/atmo_head.h: 103

# /root/camera_engine_rkaiq/include/iq_parser_v2/atmo_head.h: 113
class struct_CalibDbDetailsLowLight_s(Structure):
    pass

struct_CalibDbDetailsLowLight_s.__slots__ = [
    'Mode',
    'LowLightData',
    'Tolerance',
]
struct_CalibDbDetailsLowLight_s._fields_ = [
    ('Mode', DetailsLowLightMode_t),
    ('LowLightData', LowLightData_t),
    ('Tolerance', c_float),
]

CalibDbDetailsLowLight_t = struct_CalibDbDetailsLowLight_s# /root/camera_engine_rkaiq/include/iq_parser_v2/atmo_head.h: 113

enum_TmoTypeMode_e = c_int# /root/camera_engine_rkaiq/include/iq_parser_v2/atmo_head.h: 118

TmoTypeMode_t = enum_TmoTypeMode_e# /root/camera_engine_rkaiq/include/iq_parser_v2/atmo_head.h: 118

# /root/camera_engine_rkaiq/include/iq_parser_v2/atmo_head.h: 131
class struct_TmoData_s(Structure):
    pass

struct_TmoData_s.__slots__ = [
    'DynamicRange',
    'DynamicRange_len',
    'EnvLv',
    'EnvLv_len',
    'Strength',
    'Strength_len',
]
struct_TmoData_s._fields_ = [
    ('DynamicRange', POINTER(c_float)),
    ('DynamicRange_len', c_int),
    ('EnvLv', POINTER(c_float)),
    ('EnvLv_len', c_int),
    ('Strength', POINTER(c_float)),
    ('Strength_len', c_int),
]

TmoData_t = struct_TmoData_s# /root/camera_engine_rkaiq/include/iq_parser_v2/atmo_head.h: 131

# /root/camera_engine_rkaiq/include/iq_parser_v2/atmo_head.h: 141
class struct_CalibDbLocalTMO_s(Structure):
    pass

struct_CalibDbLocalTMO_s.__slots__ = [
    'Mode',
    'LocalTmoData',
    'Tolerance',
]
struct_CalibDbLocalTMO_s._fields_ = [
    ('Mode', TmoTypeMode_t),
    ('LocalTmoData', TmoData_t),
    ('Tolerance', c_float),
]

CalibDbLocalTMO_t = struct_CalibDbLocalTMO_s# /root/camera_engine_rkaiq/include/iq_parser_v2/atmo_head.h: 141

# /root/camera_engine_rkaiq/include/iq_parser_v2/atmo_head.h: 155
class struct_CalibDbGlobaTMO_s(Structure):
    pass

struct_CalibDbGlobaTMO_s.__slots__ = [
    'Enable',
    'IIR',
    'Mode',
    'GlobalTmoData',
    'Tolerance',
]
struct_CalibDbGlobaTMO_s._fields_ = [
    ('Enable', c_bool),
    ('IIR', c_float),
    ('Mode', TmoTypeMode_t),
    ('GlobalTmoData', TmoData_t),
    ('Tolerance', c_float),
]

CalibDbGlobaTMO_t = struct_CalibDbGlobaTMO_s# /root/camera_engine_rkaiq/include/iq_parser_v2/atmo_head.h: 155

# /root/camera_engine_rkaiq/include/iq_parser_v2/atmo_head.h: 173
class struct_CalibDbTmoV20_s(Structure):
    pass

struct_CalibDbTmoV20_s.__slots__ = [
    'Enable',
    'GlobalLuma',
    'DetailsHighLight',
    'DetailsLowLight',
    'LocalTMO',
    'GlobaTMO',
    'damp',
]
struct_CalibDbTmoV20_s._fields_ = [
    ('Enable', c_bool),
    ('GlobalLuma', CalibDbGlobalLuma_t),
    ('DetailsHighLight', CalibDbDetailsHighLight_t),
    ('DetailsLowLight', CalibDbDetailsLowLight_t),
    ('LocalTMO', CalibDbLocalTMO_t),
    ('GlobaTMO', CalibDbGlobaTMO_t),
    ('damp', c_float),
]

CalibDbTmoV20_t = struct_CalibDbTmoV20_s# /root/camera_engine_rkaiq/include/iq_parser_v2/atmo_head.h: 173

# /root/camera_engine_rkaiq/include/iq_parser_v2/atmo_head.h: 179
class struct_CalibDbV2_tmo_s(Structure):
    pass

struct_CalibDbV2_tmo_s.__slots__ = [
    'TmoTuningPara',
]
struct_CalibDbV2_tmo_s._fields_ = [
    ('TmoTuningPara', CalibDbTmoV20_t),
]

CalibDbV2_tmo_t = struct_CalibDbV2_tmo_s# /root/camera_engine_rkaiq/include/iq_parser_v2/atmo_head.h: 179

# /root/camera_engine_rkaiq/include/algos/atmo/rk_aiq_types_atmo_algo_int.h: 90
class struct_tmoCtrlData_s(Structure):
    pass

struct_tmoCtrlData_s.__slots__ = [
    'stCoef',
    'stCoefMax',
    'stCoefMin',
    'stMax',
    'stMin',
]
struct_tmoCtrlData_s._fields_ = [
    ('stCoef', c_float),
    ('stCoefMax', c_float),
    ('stCoefMin', c_float),
    ('stMax', c_int),
    ('stMin', c_int),
]

tmoCtrlData_t = struct_tmoCtrlData_s# /root/camera_engine_rkaiq/include/algos/atmo/rk_aiq_types_atmo_algo_int.h: 90

# /root/camera_engine_rkaiq/include/algos/atmo/rk_aiq_types_atmo_algo_int.h: 100
class struct_AGlobalTmoData_s(Structure):
    pass

struct_AGlobalTmoData_s.__slots__ = [
    'en',
    'stCoef',
    'stCoefMax',
    'stCoefMin',
    'stMax',
    'stMin',
]
struct_AGlobalTmoData_s._fields_ = [
    ('en', c_bool),
    ('stCoef', c_float),
    ('stCoefMax', c_float),
    ('stCoefMin', c_float),
    ('stMax', c_int),
    ('stMin', c_int),
]

AGlobalTmoData_t = struct_AGlobalTmoData_s# /root/camera_engine_rkaiq/include/algos/atmo/rk_aiq_types_atmo_algo_int.h: 100

# /root/camera_engine_rkaiq/include/algos/atmo/rk_aiq_types_atmo_algo_int.h: 109
class struct_atmoAttr_s(Structure):
    pass

struct_atmoAttr_s.__slots__ = [
    'stGlobeLuma',
    'stDtlsLL',
    'stDtlsHL',
    'stLocalTMO',
    'stGlobalTMO',
]
struct_atmoAttr_s._fields_ = [
    ('stGlobeLuma', tmoCtrlData_t),
    ('stDtlsLL', tmoCtrlData_t),
    ('stDtlsHL', tmoCtrlData_t),
    ('stLocalTMO', tmoCtrlData_t),
    ('stGlobalTMO', AGlobalTmoData_t),
]

atmoAttr_t = struct_atmoAttr_s# /root/camera_engine_rkaiq/include/algos/atmo/rk_aiq_types_atmo_algo_int.h: 109

# /root/camera_engine_rkaiq/include/algos/atmo/rk_aiq_types_atmo_algo_int.h: 120
class struct_mtmoAttr_s(Structure):
    pass

struct_mtmoAttr_s.__slots__ = [
    'Enable',
    'stGlobeLuma',
    'stDtlsHL',
    'stDtlsLL',
    'stLocalTMOStrength',
    'stGlobalTMOStrength',
    'damp',
]
struct_mtmoAttr_s._fields_ = [
    ('Enable', c_bool),
    ('stGlobeLuma', c_float),
    ('stDtlsHL', c_float),
    ('stDtlsLL', c_float),
    ('stLocalTMOStrength', c_float),
    ('stGlobalTMOStrength', c_float),
    ('damp', c_float),
]

mtmoAttr_t = struct_mtmoAttr_s# /root/camera_engine_rkaiq/include/algos/atmo/rk_aiq_types_atmo_algo_int.h: 120

# /root/camera_engine_rkaiq/include/algos/atmo/rk_aiq_types_atmo_algo_int.h: 126
class struct_atmoAttr_V2_s(Structure):
    pass

struct_atmoAttr_V2_s.__slots__ = [
    'bUpdateTmo',
    'stTmoAuto',
]
struct_atmoAttr_V2_s._fields_ = [
    ('bUpdateTmo', c_bool),
    ('stTmoAuto', atmoAttr_t),
]

atmoAttr_V2_t = struct_atmoAttr_V2_s# /root/camera_engine_rkaiq/include/algos/atmo/rk_aiq_types_atmo_algo_int.h: 126

# /root/camera_engine_rkaiq/include/algos/atmo/rk_aiq_types_atmo_algo_int.h: 132
class struct_mtmoAttr_V2_s(Structure):
    pass

struct_mtmoAttr_V2_s.__slots__ = [
    'bUpdateTmo',
    'stTmoManual',
]
struct_mtmoAttr_V2_s._fields_ = [
    ('bUpdateTmo', c_bool),
    ('stTmoManual', mtmoAttr_t),
]

mtmoAttr_V2_t = struct_mtmoAttr_V2_s# /root/camera_engine_rkaiq/include/algos/atmo/rk_aiq_types_atmo_algo_int.h: 132

enum_tmo_OpMode_s = c_int# /root/camera_engine_rkaiq/include/algos/atmo/rk_aiq_types_atmo_algo_int.h: 141

tmo_OpMode_t = enum_tmo_OpMode_s# /root/camera_engine_rkaiq/include/algos/atmo/rk_aiq_types_atmo_algo_int.h: 141

# /root/camera_engine_rkaiq/include/algos/atmo/rk_aiq_types_atmo_algo_int.h: 156
class struct_TmoCurrCtlData_s(Structure):
    pass

struct_TmoCurrCtlData_s.__slots__ = [
    'GlobalLumaMode',
    'DetailsHighLightMode',
    'DetailsLowLightMode',
    'GlobalTmoMode',
    'LocalTMOMode',
    'Envlv',
    'ISO',
    'OEPdf',
    'FocusLuma',
    'DarkPdf',
    'DynamicRange',
]
struct_TmoCurrCtlData_s._fields_ = [
    ('GlobalLumaMode', GlobalLumaMode_t),
    ('DetailsHighLightMode', DetailsHighLightMode_t),
    ('DetailsLowLightMode', DetailsLowLightMode_t),
    ('GlobalTmoMode', TmoTypeMode_t),
    ('LocalTMOMode', TmoTypeMode_t),
    ('Envlv', c_float),
    ('ISO', c_float),
    ('OEPdf', c_float),
    ('FocusLuma', c_float),
    ('DarkPdf', c_float),
    ('DynamicRange', c_float),
]

TmoCurrCtlData_t = struct_TmoCurrCtlData_s# /root/camera_engine_rkaiq/include/algos/atmo/rk_aiq_types_atmo_algo_int.h: 156

# /root/camera_engine_rkaiq/include/algos/atmo/rk_aiq_types_atmo_algo_int.h: 165
class struct_TmoCurrRegData_s(Structure):
    pass

struct_TmoCurrRegData_s.__slots__ = [
    'GlobalLuma',
    'DetailsLowlight',
    'DetailsHighlight',
    'LocalTmoStrength',
    'GlobaltmoStrength',
]
struct_TmoCurrRegData_s._fields_ = [
    ('GlobalLuma', c_float),
    ('DetailsLowlight', c_float),
    ('DetailsHighlight', c_float),
    ('LocalTmoStrength', c_float),
    ('GlobaltmoStrength', c_float),
]

TmoCurrRegData_t = struct_TmoCurrRegData_s# /root/camera_engine_rkaiq/include/algos/atmo/rk_aiq_types_atmo_algo_int.h: 165

# /root/camera_engine_rkaiq/include/algos/atmo/rk_aiq_types_atmo_algo_int.h: 170
class struct_DarkArea_s(Structure):
    pass

struct_DarkArea_s.__slots__ = [
    'level',
]
struct_DarkArea_s._fields_ = [
    ('level', c_int),
]

DarkArea_t = struct_DarkArea_s# /root/camera_engine_rkaiq/include/algos/atmo/rk_aiq_types_atmo_algo_int.h: 170

# /root/camera_engine_rkaiq/include/algos/atmo/rk_aiq_types_atmo_algo_int.h: 175
class struct_FastMode_s(Structure):
    pass

struct_FastMode_s.__slots__ = [
    'level',
]
struct_FastMode_s._fields_ = [
    ('level', c_int),
]

FastMode_t = struct_FastMode_s# /root/camera_engine_rkaiq/include/algos/atmo/rk_aiq_types_atmo_algo_int.h: 175

# /root/camera_engine_rkaiq/include/algos/atmo/rk_aiq_types_atmo_algo_int.h: 187
class struct_tmoAttr_s(Structure):
    pass

struct_tmoAttr_s.__slots__ = [
    'opMode',
    'stAuto',
    'stManual',
    'stSetLevel',
    'stDarkArea',
    'CtlInfo',
    'RegInfo',
    'stTool',
]
struct_tmoAttr_s._fields_ = [
    ('opMode', tmo_OpMode_t),
    ('stAuto', atmoAttr_V2_t),
    ('stManual', mtmoAttr_V2_t),
    ('stSetLevel', FastMode_t),
    ('stDarkArea', DarkArea_t),
    ('CtlInfo', TmoCurrCtlData_t),
    ('RegInfo', TmoCurrRegData_t),
    ('stTool', CalibDbV2_tmo_t),
]

tmoAttr_t = struct_tmoAttr_s# /root/camera_engine_rkaiq/include/algos/atmo/rk_aiq_types_atmo_algo_int.h: 187

enum_GammaType_e = c_int# /root/camera_engine_rkaiq/include/iq_parser_v2/agamma_head.h: 33

GammaType_t = enum_GammaType_e# /root/camera_engine_rkaiq/include/iq_parser_v2/agamma_head.h: 33

# /root/camera_engine_rkaiq/include/iq_parser_v2/agamma_uapi_head.h: 30
class struct_Agamma_api_Fast_s(Structure):
    pass

struct_Agamma_api_Fast_s.__slots__ = [
    'en',
    'GammaCoef',
    'SlopeAtZero',
]
struct_Agamma_api_Fast_s._fields_ = [
    ('en', c_bool),
    ('GammaCoef', c_float),
    ('SlopeAtZero', c_float),
]

Agamma_api_Fast_t = struct_Agamma_api_Fast_s# /root/camera_engine_rkaiq/include/iq_parser_v2/agamma_uapi_head.h: 30

# /root/camera_engine_rkaiq/include/iq_parser_v2/agamma_uapi_head.h: 41
class struct_Agamma_api_manualV21_s(Structure):
    pass

struct_Agamma_api_manualV21_s.__slots__ = [
    'Gamma_en',
    'Gamma_out_segnum',
    'Gamma_out_offset',
    'Gamma_curve',
]
struct_Agamma_api_manualV21_s._fields_ = [
    ('Gamma_en', c_bool),
    ('Gamma_out_segnum', GammaType_t),
    ('Gamma_out_offset', uint16_t),
    ('Gamma_curve', uint16_t * int(45)),
]

Agamma_api_manualV21_t = struct_Agamma_api_manualV21_s# /root/camera_engine_rkaiq/include/iq_parser_v2/agamma_uapi_head.h: 41

# /root/camera_engine_rkaiq/include/iq_parser_v2/agamma_uapi_head.h: 50
class struct_Agamma_api_manualV30_s(Structure):
    pass

struct_Agamma_api_manualV30_s.__slots__ = [
    'Gamma_en',
    'Gamma_out_offset',
    'Gamma_curve',
]
struct_Agamma_api_manualV30_s._fields_ = [
    ('Gamma_en', c_bool),
    ('Gamma_out_offset', uint16_t),
    ('Gamma_curve', uint16_t * int(49)),
]

Agamma_api_manualV30_t = struct_Agamma_api_manualV30_s# /root/camera_engine_rkaiq/include/iq_parser_v2/agamma_uapi_head.h: 50

enum_rk_aiq_gamma_op_mode_s = c_int# /root/camera_engine_rkaiq/include/algos/agamma/rk_aiq_types_agamma_algo_int.h: 31

rk_aiq_gamma_op_mode_t = enum_rk_aiq_gamma_op_mode_s# /root/camera_engine_rkaiq/include/algos/agamma/rk_aiq_types_agamma_algo_int.h: 31

# /root/camera_engine_rkaiq/include/algos/agamma/rk_aiq_types_agamma_algo_int.h: 37
class struct_rk_aiq_gamma_attrV21_s(Structure):
    pass

struct_rk_aiq_gamma_attrV21_s.__slots__ = [
    'mode',
    'stManual',
    'stFast',
]
struct_rk_aiq_gamma_attrV21_s._fields_ = [
    ('mode', rk_aiq_gamma_op_mode_t),
    ('stManual', Agamma_api_manualV21_t),
    ('stFast', Agamma_api_Fast_t),
]

rk_aiq_gamma_attrV21_t = struct_rk_aiq_gamma_attrV21_s# /root/camera_engine_rkaiq/include/algos/agamma/rk_aiq_types_agamma_algo_int.h: 37

# /root/camera_engine_rkaiq/include/algos/agamma/rk_aiq_types_agamma_algo_int.h: 43
class struct_rk_aiq_gamma_attrV30_s(Structure):
    pass

struct_rk_aiq_gamma_attrV30_s.__slots__ = [
    'mode',
    'stManual',
    'stFast',
]
struct_rk_aiq_gamma_attrV30_s._fields_ = [
    ('mode', rk_aiq_gamma_op_mode_t),
    ('stManual', Agamma_api_manualV30_t),
    ('stFast', Agamma_api_Fast_t),
]

rk_aiq_gamma_attrV30_t = struct_rk_aiq_gamma_attrV30_s# /root/camera_engine_rkaiq/include/algos/agamma/rk_aiq_types_agamma_algo_int.h: 43

# /root/camera_engine_rkaiq/include/algos/agamma/rk_aiq_types_agamma_algo_int.h: 50
class struct_rk_aiq_gamma_attr_s(Structure):
    pass

struct_rk_aiq_gamma_attr_s.__slots__ = [
    'sync',
    'atrrV21',
    'atrrV30',
]
struct_rk_aiq_gamma_attr_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('atrrV21', rk_aiq_gamma_attrV21_t),
    ('atrrV30', rk_aiq_gamma_attrV30_t),
]

rk_aiq_gamma_attr_t = struct_rk_aiq_gamma_attr_s# /root/camera_engine_rkaiq/include/algos/agamma/rk_aiq_types_agamma_algo_int.h: 50

enum_rk_aiq_ie_effect_e = c_int# /root/camera_engine_rkaiq/include/algos/aie/rk_aiq_types_aie_algo.h: 31

rk_aiq_ie_effect_t = enum_rk_aiq_ie_effect_e# /root/camera_engine_rkaiq/include/algos/aie/rk_aiq_types_aie_algo.h: 31

# /root/camera_engine_rkaiq/include/algos/anr/rk_aiq_types_anr_algo_int.h: 121
class struct_RKAnr_Bayernr_Params_s(Structure):
    pass

struct_RKAnr_Bayernr_Params_s.__slots__ = [
    'iso',
    'a',
    'b',
    'halfpatch',
    'halfblock',
    'filtpar',
    'ctrPit',
    'luLevel',
    'luRatio',
    'w',
    'peaknoisesigma',
    'sw_rawnr_gauss_en',
    'rgain_offs',
    'rgain_filp',
    'bgain_offs',
    'bgain_filp',
    'bayernr_ver_char',
    'bayernr_edgesoftness',
    'bayernr_gauss_weight0',
    'bayernr_gauss_weight1',
    'sw_bayernr_edge_filter_en',
    'sw_bayernr_edge_filter_lumapoint',
    'sw_bayernr_edge_filter_wgt',
    'sw_bayernr_filter_strength',
    'sw_bayernr_filter_lumapoint',
    'sw_bayernr_filter_sigma',
    'sw_bayernr_filter_edgesofts',
    'sw_bayernr_filter_soft_threshold_ratio',
    'sw_bayernr_filter_out_wgt',
]
struct_RKAnr_Bayernr_Params_s._fields_ = [
    ('iso', c_float * int(13)),
    ('a', c_float * int(13)),
    ('b', c_float * int(13)),
    ('halfpatch', c_int),
    ('halfblock', c_int),
    ('filtpar', c_float * int(13)),
    ('ctrPit', c_float * int(7)),
    ('luLevel', c_float * int(8)),
    ('luRatio', (c_float * int(8)) * int(13)),
    ('w', (c_float * int(4)) * int(13)),
    ('peaknoisesigma', c_int),
    ('sw_rawnr_gauss_en', c_int),
    ('rgain_offs', c_int),
    ('rgain_filp', c_int),
    ('bgain_offs', c_int),
    ('bgain_filp', c_int),
    ('bayernr_ver_char', c_char * int(64)),
    ('bayernr_edgesoftness', c_float),
    ('bayernr_gauss_weight0', c_float),
    ('bayernr_gauss_weight1', c_float),
    ('sw_bayernr_edge_filter_en', c_int),
    ('sw_bayernr_edge_filter_lumapoint', c_float * int(8)),
    ('sw_bayernr_edge_filter_wgt', (c_float * int(8)) * int(13)),
    ('sw_bayernr_filter_strength', c_float * int(13)),
    ('sw_bayernr_filter_lumapoint', c_int * int(16)),
    ('sw_bayernr_filter_sigma', (c_int * int(16)) * int(13)),
    ('sw_bayernr_filter_edgesofts', c_float * int(13)),
    ('sw_bayernr_filter_soft_threshold_ratio', c_float * int(13)),
    ('sw_bayernr_filter_out_wgt', c_float * int(13)),
]

RKAnr_Bayernr_Params_t = struct_RKAnr_Bayernr_Params_s# /root/camera_engine_rkaiq/include/algos/anr/rk_aiq_types_anr_algo_int.h: 121

# /root/camera_engine_rkaiq/include/algos/anr/rk_aiq_types_anr_algo_int.h: 171
class struct_RKAnr_Bayernr_Params_Select_s(Structure):
    pass

struct_RKAnr_Bayernr_Params_Select_s.__slots__ = [
    'a',
    'b',
    't0',
    'halfPatch',
    'halfBlock',
    'filtPar',
    'ctrPit',
    'luLevel',
    'luRatio',
    'w',
    'peaknoisesigma',
    'sw_rawnr_gauss_en',
    'rgain_offs',
    'rgain_filp',
    'bgain_offs',
    'bgain_filp',
    'bayernr_ver_char',
    'bayernr_edgesoftness',
    'bayernr_gauss_weight0',
    'bayernr_gauss_weight1',
    'sw_bayernr_edge_filter_en',
    'sw_bayernr_edge_filter_lumapoint',
    'sw_bayernr_edge_filter_wgt',
    'sw_bayernr_filter_strength',
    'sw_bayernr_filter_lumapoint',
    'sw_bayernr_filter_sigma',
    'sw_bayernr_filter_edgesofts',
    'sw_bayernr_filter_soft_threshold_ratio',
    'sw_bayernr_filter_out_wgt',
    'sw_dgain',
    'gausskparsq',
    'sigmaPar',
    'thld_diff',
    'thld_chanelw',
    'pix_diff',
    'log_bypass',
]
struct_RKAnr_Bayernr_Params_Select_s._fields_ = [
    ('a', c_float * int(3)),
    ('b', c_float * int(3)),
    ('t0', c_float * int(3)),
    ('halfPatch', c_int),
    ('halfBlock', c_int),
    ('filtPar', c_float * int(3)),
    ('ctrPit', c_float * int(7)),
    ('luLevel', c_float * int(8)),
    ('luRatio', c_float * int(8)),
    ('w', c_float * int(4)),
    ('peaknoisesigma', c_int),
    ('sw_rawnr_gauss_en', c_int),
    ('rgain_offs', c_int),
    ('rgain_filp', c_int),
    ('bgain_offs', c_int),
    ('bgain_filp', c_int),
    ('bayernr_ver_char', c_char * int(64)),
    ('bayernr_edgesoftness', c_float),
    ('bayernr_gauss_weight0', c_float),
    ('bayernr_gauss_weight1', c_float),
    ('sw_bayernr_edge_filter_en', c_int),
    ('sw_bayernr_edge_filter_lumapoint', c_float * int(8)),
    ('sw_bayernr_edge_filter_wgt', c_float * int(8)),
    ('sw_bayernr_filter_strength', c_float),
    ('sw_bayernr_filter_lumapoint', c_int * int(16)),
    ('sw_bayernr_filter_sigma', c_int * int(16)),
    ('sw_bayernr_filter_edgesofts', c_float),
    ('sw_bayernr_filter_soft_threshold_ratio', c_float),
    ('sw_bayernr_filter_out_wgt', c_float),
    ('sw_dgain', c_float * int(3)),
    ('gausskparsq', c_int),
    ('sigmaPar', c_int),
    ('thld_diff', c_int),
    ('thld_chanelw', c_int),
    ('pix_diff', c_int),
    ('log_bypass', c_int),
]

RKAnr_Bayernr_Params_Select_t = struct_RKAnr_Bayernr_Params_Select_s# /root/camera_engine_rkaiq/include/algos/anr/rk_aiq_types_anr_algo_int.h: 171

# /root/camera_engine_rkaiq/include/algos/anr/rk_aiq_types_anr_algo_int.h: 212
class struct_RKAnr_Mfnr_Params_s(Structure):
    pass

struct_RKAnr_Mfnr_Params_s.__slots__ = [
    'iso',
    'back_ref_num',
    'weight_limit_y',
    'weight_limit_uv',
    'ratio_frq',
    'luma_w_in_chroma',
    'awb_uv_ratio',
    'curve',
    'curve_x0',
    'ci',
    'dnweight',
    'scale',
    'lumanrpoint',
    'lumanrcurve',
    'dnstr',
    'gfdelta',
    'ci_uv',
    'dnweight_uv',
    'scale_uv',
    'lumanrpoint_uv',
    'lumanrcurve_uv',
    'dnstr_uv',
    'gfdelta_uv',
    'gfsigma',
    'noise_sigma',
    'mfnr_sigma_scale',
    'motion_detection_enable',
    'mfnr_ver_char',
]
struct_RKAnr_Mfnr_Params_s._fields_ = [
    ('iso', c_float * int(13)),
    ('back_ref_num', c_int),
    ('weight_limit_y', (c_int * int(((3 + 1) > 4) and (3 + 1) or 4)) * int(13)),
    ('weight_limit_uv', (c_int * int(3)) * int(13)),
    ('ratio_frq', (c_double * int(4)) * int(13)),
    ('luma_w_in_chroma', (c_double * int(3)) * int(13)),
    ('awb_uv_ratio', (c_double * int(2)) * int(4)),
    ('curve', (c_double * int((4 + 1))) * int(13)),
    ('curve_x0', c_double * int(13)),
    ('ci', ((c_double * int(((3 + 1) > 4) and (3 + 1) or 4)) * int(2)) * int(13)),
    ('dnweight', ((c_double * int(((3 + 1) > 4) and (3 + 1) or 4)) * int(2)) * int(13)),
    ('scale', ((c_double * int(((3 + 1) > 4) and (3 + 1) or 4)) * int(2)) * int(13)),
    ('lumanrpoint', ((c_double * int(6)) * int(2)) * int(13)),
    ('lumanrcurve', ((c_double * int(6)) * int(2)) * int(13)),
    ('dnstr', (c_double * int(2)) * int(13)),
    ('gfdelta', (((c_double * int(10)) * int(((3 + 1) > 4) and (3 + 1) or 4)) * int(2)) * int(13)),
    ('ci_uv', ((c_double * int(3)) * int(2)) * int(13)),
    ('dnweight_uv', ((c_double * int(3)) * int(2)) * int(13)),
    ('scale_uv', ((c_double * int(3)) * int(2)) * int(13)),
    ('lumanrpoint_uv', ((c_double * int(6)) * int(2)) * int(13)),
    ('lumanrcurve_uv', ((c_double * int(6)) * int(2)) * int(13)),
    ('dnstr_uv', (c_double * int(2)) * int(13)),
    ('gfdelta_uv', (((c_double * int(10)) * int(3)) * int(2)) * int(13)),
    ('gfsigma', ((c_double * int(10)) * int(4)) * int(13)),
    ('noise_sigma', (c_double * int((1 << 12))) * int(13)),
    ('mfnr_sigma_scale', c_float * int(13)),
    ('motion_detection_enable', c_int),
    ('mfnr_ver_char', c_char),
]

RKAnr_Mfnr_Params_t = struct_RKAnr_Mfnr_Params_s# /root/camera_engine_rkaiq/include/algos/anr/rk_aiq_types_anr_algo_int.h: 212

# /root/camera_engine_rkaiq/include/algos/anr/rk_aiq_types_anr_algo_int.h: 251
class struct_RKAnr_Mfnr_Params_Select_s(Structure):
    pass

struct_RKAnr_Mfnr_Params_Select_s.__slots__ = [
    'back_ref_num',
    'weight_limit_y',
    'weight_limit_uv',
    'ratio_frq',
    'luma_w_in_chroma',
    'awb_uv_ratio',
    'ci',
    'dnweight',
    'scale',
    'lumanrpoint',
    'lumanrcurve',
    'dnstr',
    'gfdelta',
    'ci_uv',
    'dnweight_uv',
    'scale_uv',
    'lumanrpoint_uv',
    'lumanrcurve_uv',
    'dnstr_uv',
    'gfdelta_uv',
    'gfsigma',
    'noise_sigma',
    'noise_sigma_sample',
    'noise_sigma_dehaze',
    'fix_x_pos',
    'fix_x_pos_dehaze',
    'mfnr_sigma_scale',
]
struct_RKAnr_Mfnr_Params_Select_s._fields_ = [
    ('back_ref_num', c_int),
    ('weight_limit_y', c_int * int(((3 + 1) > 4) and (3 + 1) or 4)),
    ('weight_limit_uv', c_int * int(3)),
    ('ratio_frq', c_double * int(4)),
    ('luma_w_in_chroma', c_double * int(3)),
    ('awb_uv_ratio', c_double * int(2)),
    ('ci', (c_double * int(((3 + 1) > 4) and (3 + 1) or 4)) * int(2)),
    ('dnweight', (c_double * int(((3 + 1) > 4) and (3 + 1) or 4)) * int(2)),
    ('scale', (c_double * int(((3 + 1) > 4) and (3 + 1) or 4)) * int(2)),
    ('lumanrpoint', (c_double * int(6)) * int(2)),
    ('lumanrcurve', (c_double * int(6)) * int(2)),
    ('dnstr', c_double * int(2)),
    ('gfdelta', ((c_double * int(10)) * int(((3 + 1) > 4) and (3 + 1) or 4)) * int(2)),
    ('ci_uv', (c_double * int(3)) * int(2)),
    ('dnweight_uv', (c_double * int(3)) * int(2)),
    ('scale_uv', (c_double * int(3)) * int(2)),
    ('lumanrpoint_uv', (c_double * int(6)) * int(2)),
    ('lumanrcurve_uv', (c_double * int(6)) * int(2)),
    ('dnstr_uv', c_double * int(2)),
    ('gfdelta_uv', ((c_double * int(10)) * int(3)) * int(2)),
    ('gfsigma', (c_double * int(10)) * int(4)),
    ('noise_sigma', c_double * int((1 << 12))),
    ('noise_sigma_sample', c_double * int(17)),
    ('noise_sigma_dehaze', c_double * int(17)),
    ('fix_x_pos', c_ushort * int(17)),
    ('fix_x_pos_dehaze', c_ushort * int(17)),
    ('mfnr_sigma_scale', c_float),
]

RKAnr_Mfnr_Params_Select_t = struct_RKAnr_Mfnr_Params_Select_s# /root/camera_engine_rkaiq/include/algos/anr/rk_aiq_types_anr_algo_int.h: 251

# /root/camera_engine_rkaiq/include/algos/anr/rk_aiq_types_anr_algo_int.h: 329
class struct_RKAnr_Uvnr_Params_s(Structure):
    pass

struct_RKAnr_Uvnr_Params_s.__slots__ = [
    'iso',
    'rkuvnrISO',
    'ratio',
    'offset',
    'wStep1',
    'hStep1',
    'meanSize1',
    'nonMed1',
    'medSize1',
    'medRatio1',
    'isMedIIR1',
    'nonBf1',
    'bfSize1',
    'sigmaR1',
    'sigmaD1',
    'uvgain1',
    'bfRatio1',
    'isRowIIR1',
    'isYcopy1',
    'block2_ext',
    'wStep2',
    'hStep2',
    'meanSize2',
    'nonMed2',
    'medSize2',
    'medRatio2',
    'isMedIIR2',
    'nonBf2',
    'bfSize2',
    'sigmaR2',
    'sigmaD2',
    'uvgain2',
    'bfRatio2',
    'isRowIIR2',
    'isYcopy2',
    'nonBf3',
    'bfSize3',
    'sigmaR3',
    'sigmaD3',
    'uvgain3',
    'bfRatio3',
    'isRowIIR3',
    'isYcopy3',
    'kernel_3x3_table',
    'kernel_5x5_talbe',
    'kernel_9x9_table',
    'kernel_9x9_num',
    'sigmaAdj_x',
    'sigamAdj_y',
    'threAdj_x',
    'threAjd_y',
]
struct_RKAnr_Uvnr_Params_s._fields_ = [
    ('iso', c_float * int(13)),
    ('rkuvnrISO', c_char * int(256)),
    ('ratio', c_float * int(13)),
    ('offset', c_float * int(13)),
    ('wStep1', c_int * int(13)),
    ('hStep1', c_int * int(13)),
    ('meanSize1', c_int * int(13)),
    ('nonMed1', c_int * int(4)),
    ('medSize1', c_int * int(13)),
    ('medRatio1', c_float * int(13)),
    ('isMedIIR1', c_int * int(13)),
    ('nonBf1', c_int * int(4)),
    ('bfSize1', c_int * int(13)),
    ('sigmaR1', c_float * int(13)),
    ('sigmaD1', c_float * int(13)),
    ('uvgain1', c_float * int(13)),
    ('bfRatio1', c_float * int(13)),
    ('isRowIIR1', c_int * int(13)),
    ('isYcopy1', c_int * int(13)),
    ('block2_ext', c_int * int(4)),
    ('wStep2', c_int * int(13)),
    ('hStep2', c_int * int(13)),
    ('meanSize2', c_int * int(13)),
    ('nonMed2', c_int * int(4)),
    ('medSize2', c_int * int(13)),
    ('medRatio2', c_float * int(13)),
    ('isMedIIR2', c_int * int(13)),
    ('nonBf2', c_int * int(4)),
    ('bfSize2', c_int * int(13)),
    ('sigmaR2', c_float * int(13)),
    ('sigmaD2', c_float * int(13)),
    ('uvgain2', c_float * int(13)),
    ('bfRatio2', c_float * int(13)),
    ('isRowIIR2', c_int * int(13)),
    ('isYcopy2', c_int * int(13)),
    ('nonBf3', c_int * int(4)),
    ('bfSize3', c_int * int(13)),
    ('sigmaR3', c_float * int(13)),
    ('sigmaD3', c_float * int(13)),
    ('uvgain3', c_float * int(13)),
    ('bfRatio3', c_float * int(13)),
    ('isRowIIR3', c_int * int(13)),
    ('isYcopy3', c_int * int(13)),
    ('kernel_3x3_table', c_float * int(3)),
    ('kernel_5x5_talbe', c_float * int(5)),
    ('kernel_9x9_table', c_float * int(8)),
    ('kernel_9x9_num', c_int),
    ('sigmaAdj_x', c_int * int(9)),
    ('sigamAdj_y', c_float * int(9)),
    ('threAdj_x', c_int * int(9)),
    ('threAjd_y', c_int * int(9)),
]

RKAnr_Uvnr_Params_t = struct_RKAnr_Uvnr_Params_s# /root/camera_engine_rkaiq/include/algos/anr/rk_aiq_types_anr_algo_int.h: 329

# /root/camera_engine_rkaiq/include/algos/anr/rk_aiq_types_anr_algo_int.h: 401
class struct_RKAnr_Uvnr_Params_Select_s(Structure):
    pass

struct_RKAnr_Uvnr_Params_Select_s.__slots__ = [
    'select_iso',
    'ratio',
    'offset',
    'wStep1',
    'hStep1',
    'meanSize1',
    'nonMed1',
    'medSize1',
    'medRatio1',
    'isMedIIR1',
    'nonBf1',
    'bfSize1',
    'sigmaR1',
    'sigmaD1',
    'uvgain1',
    'bfRatio1',
    'isRowIIR1',
    'isYcopy1',
    'block2_ext',
    'wStep2',
    'hStep2',
    'meanSize2',
    'nonMed2',
    'medSize2',
    'medRatio2',
    'isMedIIR2',
    'nonBf2',
    'bfSize2',
    'sigmaR2',
    'sigmaD2',
    'uvgain2',
    'bfRatio2',
    'isRowIIR2',
    'isYcopy2',
    'nonBf3',
    'bfSize3',
    'sigmaR3',
    'sigmaD3',
    'uvgain3',
    'bfRatio3',
    'isRowIIR3',
    'isYcopy3',
    'kernel_3x3_table',
    'kernel_5x5_table',
    'kernel_9x9_table',
    'kernel_9x9_num',
    'sigmaAdj_x',
    'sigmaAdj_y',
    'threAdj_x',
    'threAdj_y',
]
struct_RKAnr_Uvnr_Params_Select_s._fields_ = [
    ('select_iso', c_char * int(256)),
    ('ratio', c_float),
    ('offset', c_float),
    ('wStep1', c_int),
    ('hStep1', c_int),
    ('meanSize1', c_int),
    ('nonMed1', c_int * int(4)),
    ('medSize1', c_int),
    ('medRatio1', c_float),
    ('isMedIIR1', c_int),
    ('nonBf1', c_int * int(4)),
    ('bfSize1', c_int),
    ('sigmaR1', c_float),
    ('sigmaD1', c_float),
    ('uvgain1', c_float),
    ('bfRatio1', c_float),
    ('isRowIIR1', c_int),
    ('isYcopy1', c_int),
    ('block2_ext', c_int * int(4)),
    ('wStep2', c_int),
    ('hStep2', c_int),
    ('meanSize2', c_int),
    ('nonMed2', c_int * int(4)),
    ('medSize2', c_int),
    ('medRatio2', c_float),
    ('isMedIIR2', c_int),
    ('nonBf2', c_int * int(4)),
    ('bfSize2', c_int),
    ('sigmaR2', c_float),
    ('sigmaD2', c_float),
    ('uvgain2', c_float),
    ('bfRatio2', c_float),
    ('isRowIIR2', c_int),
    ('isYcopy2', c_int),
    ('nonBf3', c_int * int(4)),
    ('bfSize3', c_int),
    ('sigmaR3', c_float),
    ('sigmaD3', c_float),
    ('uvgain3', c_float),
    ('bfRatio3', c_float),
    ('isRowIIR3', c_int),
    ('isYcopy3', c_int),
    ('kernel_3x3_table', c_float * int(3)),
    ('kernel_5x5_table', c_float * int(5)),
    ('kernel_9x9_table', c_float * int(8)),
    ('kernel_9x9_num', c_int),
    ('sigmaAdj_x', c_int * int(9)),
    ('sigmaAdj_y', c_float * int(9)),
    ('threAdj_x', c_int * int(9)),
    ('threAdj_y', c_int * int(9)),
]

RKAnr_Uvnr_Params_Select_t = struct_RKAnr_Uvnr_Params_Select_s# /root/camera_engine_rkaiq/include/algos/anr/rk_aiq_types_anr_algo_int.h: 401

# /root/camera_engine_rkaiq/include/algos/anr/rk_aiq_types_anr_algo_int.h: 449
class struct_RKAnr_Ynr_Params_Select_s(Structure):
    pass

struct_RKAnr_Ynr_Params_Select_s.__slots__ = [
    'iso',
    'ciISO',
    'noiseSigma',
    'lumaPoints',
    'loFreqNoiseCi',
    'loFreqDenoiseWeight',
    'loFreqBfScale',
    'loFreqLumaNrCurvePoint',
    'loFreqLumaNrCurveRatio',
    'loFreqDenoiseStrength',
    'loFreqDirectionStrength',
    'hiFreqDenoiseWeight',
    'hiFreqBfScale',
    'hiFreqEdgeSoftness',
    'hiFreqLumaNrCurvePoint',
    'hiFreqLumaNrCurveRatio',
    'hiFreqDenoiseStrength',
    'hiFreqSoftThresholdScale',
    'radialNoiseCtrPoint',
    'radialNoiseCtrRatio',
    'lscGainRatioAdjust',
    'detailThre',
    'detailThreRatioLevel',
    'detailMinAdjDnW',
    'detailThreLevel4',
    'detailThreRatioLevel4',
    'waveLetCoeffDeltaHi',
    'waveLetCoeffDeltaLo',
    'hiValueThre',
    'loValueThre',
    'ynr_level4_max_gain',
    'ynr_ver_char',
]
struct_RKAnr_Ynr_Params_Select_s._fields_ = [
    ('iso', c_float),
    ('ciISO', c_float * int(12)),
    ('noiseSigma', c_float * int(((1 << 4) + 1))),
    ('lumaPoints', c_short * int(((1 << 4) + 1))),
    ('loFreqNoiseCi', c_float * int(4)),
    ('loFreqDenoiseWeight', c_float * int(4)),
    ('loFreqBfScale', c_float * int(4)),
    ('loFreqLumaNrCurvePoint', c_float * int(6)),
    ('loFreqLumaNrCurveRatio', c_float * int(6)),
    ('loFreqDenoiseStrength', c_float * int(2)),
    ('loFreqDirectionStrength', c_float),
    ('hiFreqDenoiseWeight', c_float * int(4)),
    ('hiFreqBfScale', c_float * int(4)),
    ('hiFreqEdgeSoftness', c_float * int(4)),
    ('hiFreqLumaNrCurvePoint', c_float * int(6)),
    ('hiFreqLumaNrCurveRatio', c_float * int(6)),
    ('hiFreqDenoiseStrength', c_float),
    ('hiFreqSoftThresholdScale', c_float * int(4)),
    ('radialNoiseCtrPoint', c_short * int(7)),
    ('radialNoiseCtrRatio', c_float * int(7)),
    ('lscGainRatioAdjust', c_float * int(4)),
    ('detailThre', c_float * int(6)),
    ('detailThreRatioLevel', (c_float * int(6)) * int(3)),
    ('detailMinAdjDnW', c_float),
    ('detailThreLevel4', c_float * int(6)),
    ('detailThreRatioLevel4', c_float * int(6)),
    ('waveLetCoeffDeltaHi', c_short),
    ('waveLetCoeffDeltaLo', c_short),
    ('hiValueThre', c_short),
    ('loValueThre', c_short),
    ('ynr_level4_max_gain', c_int),
    ('ynr_ver_char', c_char * int(64)),
]

RKAnr_Ynr_Params_Select_t = struct_RKAnr_Ynr_Params_Select_s# /root/camera_engine_rkaiq/include/algos/anr/rk_aiq_types_anr_algo_int.h: 449

# /root/camera_engine_rkaiq/include/algos/anr/rk_aiq_types_anr_algo_int.h: 460
class struct_RKAnr_Ynr_Params_s(Structure):
    pass

struct_RKAnr_Ynr_Params_s.__slots__ = [
    'aYnrParamsISO',
    'rawBit',
    'isoValue',
    'ynr_ver_char',
]
struct_RKAnr_Ynr_Params_s._fields_ = [
    ('aYnrParamsISO', RKAnr_Ynr_Params_Select_t * int(13)),
    ('rawBit', c_short),
    ('isoValue', c_short),
    ('ynr_ver_char', c_char * int(64)),
]

RKAnr_Ynr_Params_t = struct_RKAnr_Ynr_Params_s# /root/camera_engine_rkaiq/include/algos/anr/rk_aiq_types_anr_algo_int.h: 460

enum_ANROPMode_e = c_int# /root/camera_engine_rkaiq/include/algos/anr/rk_aiq_types_anr_algo_int.h: 490

ANROPMode_t = enum_ANROPMode_e# /root/camera_engine_rkaiq/include/algos/anr/rk_aiq_types_anr_algo_int.h: 490

# /root/camera_engine_rkaiq/include/algos/anr/rk_aiq_types_anr_algo_int.h: 507
class struct_RKAnr_Mfnr_Dynamic_s(Structure):
    pass

struct_RKAnr_Mfnr_Dynamic_s.__slots__ = [
    'enable',
    'lowth_iso',
    'lowth_time',
    'highth_iso',
    'highth_time',
    'mfnr_enable_state',
]
struct_RKAnr_Mfnr_Dynamic_s._fields_ = [
    ('enable', c_int),
    ('lowth_iso', c_float),
    ('lowth_time', c_float),
    ('highth_iso', c_float),
    ('highth_time', c_float),
    ('mfnr_enable_state', c_int),
]

RKAnr_Mfnr_Dynamic_t = struct_RKAnr_Mfnr_Dynamic_s# /root/camera_engine_rkaiq/include/algos/anr/rk_aiq_types_anr_algo_int.h: 507

# /root/camera_engine_rkaiq/include/algos/anr/rk_aiq_types_anr_algo_int.h: 524
class struct_ANR_Manual_Attr_s(Structure):
    pass

struct_ANR_Manual_Attr_s.__slots__ = [
    'bayernrEn',
    'stBayernrParamSelect',
    'mfnrEn',
    'stMfnrParamSelect',
    'ynrEn',
    'stYnrParamSelect',
    'uvnrEn',
    'stUvnrParamSelect',
]
struct_ANR_Manual_Attr_s._fields_ = [
    ('bayernrEn', c_int),
    ('stBayernrParamSelect', RKAnr_Bayernr_Params_Select_t),
    ('mfnrEn', c_int),
    ('stMfnrParamSelect', RKAnr_Mfnr_Params_Select_t),
    ('ynrEn', c_int),
    ('stYnrParamSelect', RKAnr_Ynr_Params_Select_t),
    ('uvnrEn', c_int),
    ('stUvnrParamSelect', RKAnr_Uvnr_Params_Select_t),
]

ANR_Manual_Attr_t = struct_ANR_Manual_Attr_s# /root/camera_engine_rkaiq/include/algos/anr/rk_aiq_types_anr_algo_int.h: 524

# /root/camera_engine_rkaiq/include/algos/anr/rk_aiq_types_anr_algo_int.h: 551
class struct_ANR_Auto_Attr_s(Structure):
    pass

struct_ANR_Auto_Attr_s.__slots__ = [
    'bayernrEn',
    'stBayernrParams',
    'stBayernrParamSelect',
    'mfnrEn',
    'stMfnrParams',
    'stMfnrParamSelect',
    'ynrEn',
    'stYnrParams',
    'stYnrParamSelect',
    'uvnrEn',
    'stUvnrParams',
    'stUvnrParamSelect',
    'stMfnr_dynamic',
]
struct_ANR_Auto_Attr_s._fields_ = [
    ('bayernrEn', c_int),
    ('stBayernrParams', RKAnr_Bayernr_Params_t),
    ('stBayernrParamSelect', RKAnr_Bayernr_Params_Select_t),
    ('mfnrEn', c_int),
    ('stMfnrParams', RKAnr_Mfnr_Params_t),
    ('stMfnrParamSelect', RKAnr_Mfnr_Params_Select_t),
    ('ynrEn', c_int),
    ('stYnrParams', RKAnr_Ynr_Params_t),
    ('stYnrParamSelect', RKAnr_Ynr_Params_Select_t),
    ('uvnrEn', c_int),
    ('stUvnrParams', RKAnr_Uvnr_Params_t),
    ('stUvnrParamSelect', RKAnr_Uvnr_Params_Select_t),
    ('stMfnr_dynamic', RKAnr_Mfnr_Dynamic_t),
]

ANR_Auto_Attr_t = struct_ANR_Auto_Attr_s# /root/camera_engine_rkaiq/include/algos/anr/rk_aiq_types_anr_algo_int.h: 551

# /root/camera_engine_rkaiq/include/algos/anr/rk_aiq_types_anr_algo_int.h: 594
class struct_rk_aiq_nr_attrib_s(Structure):
    pass

struct_rk_aiq_nr_attrib_s.__slots__ = [
    'eMode',
    'stAuto',
    'stManual',
]
struct_rk_aiq_nr_attrib_s._fields_ = [
    ('eMode', ANROPMode_t),
    ('stAuto', ANR_Auto_Attr_t),
    ('stManual', ANR_Manual_Attr_t),
]

rk_aiq_nr_attrib_t = struct_rk_aiq_nr_attrib_s# /root/camera_engine_rkaiq/include/algos/anr/rk_aiq_types_anr_algo_int.h: 594

# /root/camera_engine_rkaiq/include/algos/anr/rk_aiq_types_anr_algo_int.h: 634
class struct_rk_aiq_nr_IQPara_s(Structure):
    pass

struct_rk_aiq_nr_IQPara_s.__slots__ = [
    'module_bits',
    'stBayernrPara',
    'stMfnrPara',
    'stUvnrPara',
    'stYnrPara',
]
struct_rk_aiq_nr_IQPara_s._fields_ = [
    ('module_bits', c_int),
    ('stBayernrPara', CalibDb_BayerNr_t),
    ('stMfnrPara', CalibDb_MFNR_t),
    ('stUvnrPara', CalibDb_UVNR_t),
    ('stYnrPara', CalibDb_YNR_t),
]

rk_aiq_nr_IQPara_t = struct_rk_aiq_nr_IQPara_s# /root/camera_engine_rkaiq/include/algos/anr/rk_aiq_types_anr_algo_int.h: 634

# /root/camera_engine_rkaiq/include/iq_parser_v2/agic_uapi_head.h: 77
class struct_rkaiq_gic_v1_param_selected_s(Structure):
    pass

struct_rkaiq_gic_v1_param_selected_s.__slots__ = [
    'iso',
    'bypass',
    'gr_ratio',
    'min_busy_thre',
    'min_grad_thr1',
    'min_grad_thr2',
    'k_grad1',
    'k_grad2',
    'gb_thre',
    'maxCorV',
    'maxCorVboth',
    'dark_thre',
    'dark_threHi',
    'k_grad1_dark',
    'k_grad2_dark',
    'min_grad_thr_dark1',
    'min_grad_thr_dark2',
    'noiseCurve_0',
    'noiseCurve_1',
    'GValueLimitLo',
    'GValueLimitHi',
    'textureStrength',
    'ScaleLo',
    'ScaleHi',
    'globalStrength',
    'diff_clip',
]
struct_rkaiq_gic_v1_param_selected_s._fields_ = [
    ('iso', uint32_t),
    ('bypass', uint8_t),
    ('gr_ratio', uint8_t),
    ('min_busy_thre', uint16_t),
    ('min_grad_thr1', uint16_t),
    ('min_grad_thr2', uint16_t),
    ('k_grad1', uint16_t),
    ('k_grad2', uint16_t),
    ('gb_thre', uint16_t),
    ('maxCorV', uint16_t),
    ('maxCorVboth', uint16_t),
    ('dark_thre', uint16_t),
    ('dark_threHi', uint16_t),
    ('k_grad1_dark', uint16_t),
    ('k_grad2_dark', uint16_t),
    ('min_grad_thr_dark1', uint16_t),
    ('min_grad_thr_dark2', uint16_t),
    ('noiseCurve_0', c_float),
    ('noiseCurve_1', c_float),
    ('GValueLimitLo', c_float),
    ('GValueLimitHi', c_float),
    ('textureStrength', c_float),
    ('ScaleLo', c_float),
    ('ScaleHi', c_float),
    ('globalStrength', c_float),
    ('diff_clip', uint16_t),
]

rkaiq_gic_v1_param_selected_t = struct_rkaiq_gic_v1_param_selected_s# /root/camera_engine_rkaiq/include/iq_parser_v2/agic_uapi_head.h: 77

# /root/camera_engine_rkaiq/include/iq_parser_v2/agic_uapi_head.h: 126
class struct_rkaiq_gic_v2_param_selected_s(Structure):
    pass

struct_rkaiq_gic_v2_param_selected_s.__slots__ = [
    'iso',
    'bypass',
    'gr_ratio',
    'min_busy_thre',
    'min_grad_thr1',
    'min_grad_thr2',
    'k_grad1',
    'k_grad2',
    'gb_thre',
    'maxCorV',
    'maxCorVboth',
    'dark_thre',
    'dark_threHi',
    'k_grad1_dark',
    'k_grad2_dark',
    'min_grad_thr_dark1',
    'min_grad_thr_dark2',
    'NoiseScale',
    'NoiseBase',
    'noiseCurve_0',
    'noiseCurve_1',
    'globalStrength',
    'diff_clip',
]
struct_rkaiq_gic_v2_param_selected_s._fields_ = [
    ('iso', uint32_t),
    ('bypass', uint8_t),
    ('gr_ratio', uint8_t),
    ('min_busy_thre', uint16_t),
    ('min_grad_thr1', uint16_t),
    ('min_grad_thr2', uint16_t),
    ('k_grad1', uint16_t),
    ('k_grad2', uint16_t),
    ('gb_thre', uint16_t),
    ('maxCorV', uint16_t),
    ('maxCorVboth', uint16_t),
    ('dark_thre', uint16_t),
    ('dark_threHi', uint16_t),
    ('k_grad1_dark', uint16_t),
    ('k_grad2_dark', uint16_t),
    ('min_grad_thr_dark1', uint16_t),
    ('min_grad_thr_dark2', uint16_t),
    ('NoiseScale', c_float),
    ('NoiseBase', c_float),
    ('noiseCurve_0', c_float),
    ('noiseCurve_1', c_float),
    ('globalStrength', c_float),
    ('diff_clip', uint16_t),
]

rkaiq_gic_v2_param_selected_t = struct_rkaiq_gic_v2_param_selected_s# /root/camera_engine_rkaiq/include/iq_parser_v2/agic_uapi_head.h: 126

enum_rkaiq_gic_api_op_mode_e = c_int# /root/camera_engine_rkaiq/include/iq_parser_v2/agic_uapi_head.h: 134

rkaiq_gic_api_op_mode_t = enum_rkaiq_gic_api_op_mode_e# /root/camera_engine_rkaiq/include/iq_parser_v2/agic_uapi_head.h: 134

# /root/camera_engine_rkaiq/include/iq_parser_v2/agic_uapi_head.h: 154
class struct_rkaiq_gic_v1_api_attr_s(Structure):
    pass

struct_rkaiq_gic_v1_api_attr_s.__slots__ = [
    'sync',
    'gic_en',
    'edge_open',
    'noise_cut_en',
    'op_mode',
    'iso_cnt',
    'auto_params',
    'manual_param',
]
struct_rkaiq_gic_v1_api_attr_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('gic_en', uint8_t),
    ('edge_open', uint8_t),
    ('noise_cut_en', uint8_t),
    ('op_mode', rkaiq_gic_api_op_mode_t),
    ('iso_cnt', uint32_t),
    ('auto_params', rkaiq_gic_v1_param_selected_t * int(16)),
    ('manual_param', rkaiq_gic_v1_param_selected_t),
]

rkaiq_gic_v1_api_attr_t = struct_rkaiq_gic_v1_api_attr_s# /root/camera_engine_rkaiq/include/iq_parser_v2/agic_uapi_head.h: 154

# /root/camera_engine_rkaiq/include/iq_parser_v2/agic_uapi_head.h: 168
class struct_rkaiq_gic_v2_api_attr_s(Structure):
    pass

struct_rkaiq_gic_v2_api_attr_s.__slots__ = [
    'sync',
    'gic_en',
    'op_mode',
    'iso_cnt',
    'auto_params',
    'manual_param',
]
struct_rkaiq_gic_v2_api_attr_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('gic_en', uint8_t),
    ('op_mode', rkaiq_gic_api_op_mode_t),
    ('iso_cnt', uint32_t),
    ('auto_params', rkaiq_gic_v2_param_selected_t * int(16)),
    ('manual_param', rkaiq_gic_v2_param_selected_t),
]

rkaiq_gic_v2_api_attr_t = struct_rkaiq_gic_v2_api_attr_s# /root/camera_engine_rkaiq/include/iq_parser_v2/agic_uapi_head.h: 168

# /root/camera_engine_rkaiq/include/algos/af/rk_aiq_types_af_algo.h: 66
class struct_anon_121(Structure):
    pass

struct_anon_121.__slots__ = [
    'roia_sharpness',
    'roia_luminance',
    'roib_sharpness',
    'roib_luminance',
    'global_sharpness',
    'lowpass_fv4_4',
    'lowpass_fv8_8',
    'lowpass_highlht',
    'lowpass_highlht2',
    'lowpass_id',
    'focus_starttim',
    'focus_endtim',
    'zoom_starttim',
    'zoom_endtim',
    'sof_tim',
    'focusCode',
    'zoomCode',
    'focusCorrection',
    'zoomCorrection',
    'angleZ',
]
struct_anon_121._fields_ = [
    ('roia_sharpness', c_ulonglong),
    ('roia_luminance', c_uint),
    ('roib_sharpness', c_uint),
    ('roib_luminance', c_uint),
    ('global_sharpness', c_uint * int(225)),
    ('lowpass_fv4_4', c_int * int(225)),
    ('lowpass_fv8_8', c_int * int(225)),
    ('lowpass_highlht', c_int * int(225)),
    ('lowpass_highlht2', c_int * int(225)),
    ('lowpass_id', c_int),
    ('focus_starttim', struct_timeval),
    ('focus_endtim', struct_timeval),
    ('zoom_starttim', struct_timeval),
    ('zoom_endtim', struct_timeval),
    ('sof_tim', c_int64),
    ('focusCode', c_int),
    ('zoomCode', c_int),
    ('focusCorrection', c_bool),
    ('zoomCorrection', c_bool),
    ('angleZ', c_float),
]

rk_aiq_af_algo_stat_v20_t = struct_anon_121# /root/camera_engine_rkaiq/include/algos/af/rk_aiq_types_af_algo.h: 66

# /root/camera_engine_rkaiq/include/algos/af/rk_aiq_types_af_algo.h: 78
class struct_anon_122(Structure):
    pass

struct_anon_122.__slots__ = [
    'enable',
    'ldg_xl',
    'ldg_yl',
    'ldg_kl',
    'ldg_xh',
    'ldg_yh',
    'ldg_kh',
    'highlight_th',
    'highlight2_th',
]
struct_anon_122._fields_ = [
    ('enable', c_bool),
    ('ldg_xl', c_int),
    ('ldg_yl', c_int),
    ('ldg_kl', c_int),
    ('ldg_xh', c_int),
    ('ldg_yh', c_int),
    ('ldg_kh', c_int),
    ('highlight_th', c_int),
    ('highlight2_th', c_int),
]

rk_aiq_af_algo_sp_meas_t = struct_anon_122# /root/camera_engine_rkaiq/include/algos/af/rk_aiq_types_af_algo.h: 78

# /root/camera_engine_rkaiq/include/algos/af/rk_aiq_types_af_algo.h: 112
class struct_anon_123(Structure):
    pass

struct_anon_123.__slots__ = [
    'contrast_af_en',
    'rawaf_sel',
    'window_num',
    'wina_h_offs',
    'wina_v_offs',
    'wina_h_size',
    'wina_v_size',
    'winb_h_offs',
    'winb_v_offs',
    'winb_h_size',
    'winb_v_size',
    'gamma_flt_en',
    'gamma_y',
    'gaus_flt_en',
    'gaus_h0',
    'gaus_h1',
    'gaus_h2',
    'line_en',
    'line_num',
    'afm_thres',
    'lum_var_shift',
    'afm_var_shift',
    'sp_meas',
]
struct_anon_123._fields_ = [
    ('contrast_af_en', c_ubyte),
    ('rawaf_sel', c_ubyte),
    ('window_num', c_ubyte),
    ('wina_h_offs', c_ushort),
    ('wina_v_offs', c_ushort),
    ('wina_h_size', c_ushort),
    ('wina_v_size', c_ushort),
    ('winb_h_offs', c_ushort),
    ('winb_v_offs', c_ushort),
    ('winb_h_size', c_ushort),
    ('winb_v_size', c_ushort),
    ('gamma_flt_en', c_ubyte),
    ('gamma_y', c_ushort * int(17)),
    ('gaus_flt_en', c_ubyte),
    ('gaus_h0', c_ubyte),
    ('gaus_h1', c_ubyte),
    ('gaus_h2', c_ubyte),
    ('line_en', c_ubyte * int(5)),
    ('line_num', c_ubyte * int(5)),
    ('afm_thres', c_ushort),
    ('lum_var_shift', c_ubyte * int(2)),
    ('afm_var_shift', c_ubyte * int(2)),
    ('sp_meas', rk_aiq_af_algo_sp_meas_t),
]

rk_aiq_af_algo_meas_v20_t = struct_anon_123# /root/camera_engine_rkaiq/include/algos/af/rk_aiq_types_af_algo.h: 112

# /root/camera_engine_rkaiq/include/algos/af/rk_aiq_types_af_algo.h: 136
class struct_anon_124(Structure):
    pass

struct_anon_124.__slots__ = [
    'wndb_luma',
    'wndb_sharpness',
    'winb_highlit_cnt',
    'wnda_luma',
    'wnda_fv_v1',
    'wnda_fv_v2',
    'wnda_fv_h1',
    'wnda_fv_h2',
    'wina_highlit_cnt',
    'int_state',
    'focus_starttim',
    'focus_endtim',
    'zoom_starttim',
    'zoom_endtim',
    'sof_tim',
    'focusCode',
    'zoomCode',
    'focusCorrection',
    'zoomCorrection',
    'angleZ',
]
struct_anon_124._fields_ = [
    ('wndb_luma', c_uint),
    ('wndb_sharpness', c_uint),
    ('winb_highlit_cnt', c_uint),
    ('wnda_luma', c_uint * int(225)),
    ('wnda_fv_v1', c_uint * int(225)),
    ('wnda_fv_v2', c_uint * int(225)),
    ('wnda_fv_h1', c_uint * int(225)),
    ('wnda_fv_h2', c_uint * int(225)),
    ('wina_highlit_cnt', c_uint * int(225)),
    ('int_state', c_uint),
    ('focus_starttim', struct_timeval),
    ('focus_endtim', struct_timeval),
    ('zoom_starttim', struct_timeval),
    ('zoom_endtim', struct_timeval),
    ('sof_tim', c_int64),
    ('focusCode', c_int),
    ('zoomCode', c_int),
    ('focusCorrection', c_bool),
    ('zoomCorrection', c_bool),
    ('angleZ', c_float),
]

rk_aiq_af_algo_stat_v30_t = struct_anon_124# /root/camera_engine_rkaiq/include/algos/af/rk_aiq_types_af_algo.h: 136

# /root/camera_engine_rkaiq/include/algos/af/rk_aiq_types_af_algo.h: 210
class struct_anon_125(Structure):
    pass

struct_anon_125.__slots__ = [
    'af_en',
    'rawaf_sel',
    'gamma_en',
    'gaus_en',
    'v1_fir_sel',
    'hiir_en',
    'viir_en',
    'v1_fv_outmode',
    'v2_fv_outmode',
    'h1_fv_outmode',
    'h2_fv_outmode',
    'ldg_en',
    'accu_8bit_mode',
    'ae_mode',
    'y_mode',
    'line_en',
    'line_num',
    'window_num',
    'wina_h_offs',
    'wina_v_offs',
    'wina_h_size',
    'wina_v_size',
    'winb_h_offs',
    'winb_v_offs',
    'winb_h_size',
    'winb_v_size',
    'gamma_y',
    'thres',
    'shift_sum_a',
    'shift_sum_b',
    'shift_y_a',
    'shift_y_b',
    'v1_iir_coe',
    'v1_fir_coe',
    'v2_iir_coe',
    'v2_fir_coe',
    'h1_iir1_coe',
    'h2_iir1_coe',
    'h1_iir2_coe',
    'h2_iir2_coe',
    'h_ldg_lumth',
    'h_ldg_gain',
    'h_ldg_gslp',
    'v_ldg_lumth',
    'v_ldg_gain',
    'v_ldg_gslp',
    'v_fv_thresh',
    'h_fv_thresh',
    'v1_fv_shift',
    'v2_fv_shift',
    'h1_fv_shift',
    'h2_fv_shift',
    'highlit_thresh',
]
struct_anon_125._fields_ = [
    ('af_en', c_ubyte),
    ('rawaf_sel', c_ubyte),
    ('gamma_en', c_ubyte),
    ('gaus_en', c_ubyte),
    ('v1_fir_sel', c_ubyte),
    ('hiir_en', c_ubyte),
    ('viir_en', c_ubyte),
    ('v1_fv_outmode', c_ubyte),
    ('v2_fv_outmode', c_ubyte),
    ('h1_fv_outmode', c_ubyte),
    ('h2_fv_outmode', c_ubyte),
    ('ldg_en', c_ubyte),
    ('accu_8bit_mode', c_ubyte),
    ('ae_mode', c_ubyte),
    ('y_mode', c_ubyte),
    ('line_en', c_ubyte * int(5)),
    ('line_num', c_ubyte * int(5)),
    ('window_num', c_ubyte),
    ('wina_h_offs', c_ushort),
    ('wina_v_offs', c_ushort),
    ('wina_h_size', c_ushort),
    ('wina_v_size', c_ushort),
    ('winb_h_offs', c_ushort),
    ('winb_v_offs', c_ushort),
    ('winb_h_size', c_ushort),
    ('winb_v_size', c_ushort),
    ('gamma_y', c_ushort * int(17)),
    ('thres', c_ushort),
    ('shift_sum_a', c_ubyte),
    ('shift_sum_b', c_ubyte),
    ('shift_y_a', c_ubyte),
    ('shift_y_b', c_ubyte),
    ('v1_iir_coe', c_short * int(9)),
    ('v1_fir_coe', c_short * int(3)),
    ('v2_iir_coe', c_short * int(3)),
    ('v2_fir_coe', c_short * int(3)),
    ('h1_iir1_coe', c_short * int(6)),
    ('h2_iir1_coe', c_short * int(6)),
    ('h1_iir2_coe', c_short * int(6)),
    ('h2_iir2_coe', c_short * int(6)),
    ('h_ldg_lumth', c_ubyte * int(2)),
    ('h_ldg_gain', c_ubyte * int(2)),
    ('h_ldg_gslp', c_ushort * int(2)),
    ('v_ldg_lumth', c_ubyte * int(2)),
    ('v_ldg_gain', c_ubyte * int(2)),
    ('v_ldg_gslp', c_ushort * int(2)),
    ('v_fv_thresh', c_ushort),
    ('h_fv_thresh', c_ushort),
    ('v1_fv_shift', c_ubyte),
    ('v2_fv_shift', c_ubyte),
    ('h1_fv_shift', c_ubyte),
    ('h2_fv_shift', c_ubyte),
    ('highlit_thresh', c_ushort),
]

rk_aiq_af_algo_meas_v30_t = struct_anon_125# /root/camera_engine_rkaiq/include/algos/af/rk_aiq_types_af_algo.h: 210

# /root/camera_engine_rkaiq/include/algos/asharp4/rk_aiq_types_asharp_hw_v4.h: 67
class struct_RK_SHARP_Fix_V4_s(Structure):
    pass

struct_RK_SHARP_Fix_V4_s.__slots__ = [
    'sharp_clk_dis',
    'sharp_exgain_bypass',
    'sharp_center_mode',
    'sharp_bypass',
    'sharp_en',
    'sharp_sharp_ratio',
    'sharp_bf_ratio',
    'sharp_gaus_ratio',
    'sharp_pbf_ratio',
    'sharp_luma_dx',
    'sharp_pbf_sigma_inv',
    'sharp_bf_sigma_inv',
    'sharp_bf_sigma_shift',
    'sharp_pbf_sigma_shift',
    'sharp_ehf_th',
    'sharp_clip_hf',
    'sharp_pbf_coef',
    'sharp_bf_coef',
    'sharp_gaus_coef',
]
struct_RK_SHARP_Fix_V4_s._fields_ = [
    ('sharp_clk_dis', uint8_t),
    ('sharp_exgain_bypass', uint8_t),
    ('sharp_center_mode', uint8_t),
    ('sharp_bypass', uint8_t),
    ('sharp_en', uint8_t),
    ('sharp_sharp_ratio', uint8_t),
    ('sharp_bf_ratio', uint8_t),
    ('sharp_gaus_ratio', uint8_t),
    ('sharp_pbf_ratio', uint8_t),
    ('sharp_luma_dx', uint8_t * int(7)),
    ('sharp_pbf_sigma_inv', uint16_t * int(8)),
    ('sharp_bf_sigma_inv', uint16_t * int(8)),
    ('sharp_bf_sigma_shift', uint8_t),
    ('sharp_pbf_sigma_shift', uint8_t),
    ('sharp_ehf_th', uint16_t * int(8)),
    ('sharp_clip_hf', uint16_t * int(8)),
    ('sharp_pbf_coef', uint8_t * int(3)),
    ('sharp_bf_coef', uint8_t * int(3)),
    ('sharp_gaus_coef', uint8_t * int(6)),
]

RK_SHARP_Fix_V4_t = struct_RK_SHARP_Fix_V4_s# /root/camera_engine_rkaiq/include/algos/asharp4/rk_aiq_types_asharp_hw_v4.h: 67

# /root/camera_engine_rkaiq/include/algos/aynr3/rk_aiq_types_aynr_hw_v3.h: 107
class struct_RK_YNR_Fix_V3_s(Structure):
    pass

struct_RK_YNR_Fix_V3_s.__slots__ = [
    'ynr_rnr_en',
    'ynr_gate_dis',
    'ynr_thumb_mix_cur_en',
    'ynr_global_gain_alpha',
    'ynr_global_gain',
    'ynr_flt1x1_bypass_sel',
    'ynr_sft5x5_bypass',
    'ynr_flt1x1_bypass',
    'ynr_lgft3x3_bypass',
    'ynr_lbft5x5_bypass',
    'ynr_bft3x3_bypass',
    'ynr_en',
    'ynr_local_gainscale',
    'ynr_rnr_max_r',
    'ynr_rnr_center_coorv',
    'ynr_rnr_center_coorh',
    'ynr_localgain_adj',
    'ynr_localgain_adj_thresh',
    'ynr_low_bf_inv',
    'ynr_low_peak_supress',
    'ynr_low_thred_adj',
    'ynr_low_dist_adj',
    'ynr_low_edge_adj_thresh',
    'ynr_low_bi_weight',
    'ynr_low_weight',
    'ynr_low_center_weight',
    'ynr_hi_min_adj',
    'ynr_high_thred_adj',
    'ynr_high_retain_weight',
    'ynr_hi_edge_thed',
    'ynr_base_filter_weight',
    'ynr_frame_full_size',
    'ynr_lbf_weight_thres',
    'ynr_low_gauss1_coeff',
    'ynr_low_gauss2_coeff',
    'ynr_direction_weight',
    'ynr_luma_points_x',
    'ynr_lsgm_y',
    'ynr_hsgm_y',
    'ynr_rnr_strength',
]
struct_RK_YNR_Fix_V3_s._fields_ = [
    ('ynr_rnr_en', uint8_t),
    ('ynr_gate_dis', uint8_t),
    ('ynr_thumb_mix_cur_en', uint8_t),
    ('ynr_global_gain_alpha', uint8_t),
    ('ynr_global_gain', uint16_t),
    ('ynr_flt1x1_bypass_sel', uint8_t),
    ('ynr_sft5x5_bypass', uint8_t),
    ('ynr_flt1x1_bypass', uint8_t),
    ('ynr_lgft3x3_bypass', uint8_t),
    ('ynr_lbft5x5_bypass', uint8_t),
    ('ynr_bft3x3_bypass', uint8_t),
    ('ynr_en', uint8_t),
    ('ynr_local_gainscale', uint8_t),
    ('ynr_rnr_max_r', uint16_t),
    ('ynr_rnr_center_coorv', uint16_t),
    ('ynr_rnr_center_coorh', uint16_t),
    ('ynr_localgain_adj', uint8_t),
    ('ynr_localgain_adj_thresh', uint16_t),
    ('ynr_low_bf_inv', uint16_t * int(2)),
    ('ynr_low_peak_supress', uint8_t),
    ('ynr_low_thred_adj', uint16_t),
    ('ynr_low_dist_adj', uint16_t),
    ('ynr_low_edge_adj_thresh', uint16_t),
    ('ynr_low_bi_weight', uint8_t),
    ('ynr_low_weight', uint8_t),
    ('ynr_low_center_weight', uint16_t),
    ('ynr_hi_min_adj', uint8_t),
    ('ynr_high_thred_adj', uint16_t),
    ('ynr_high_retain_weight', uint8_t),
    ('ynr_hi_edge_thed', uint8_t),
    ('ynr_base_filter_weight', uint8_t * int(3)),
    ('ynr_frame_full_size', uint32_t),
    ('ynr_lbf_weight_thres', uint16_t),
    ('ynr_low_gauss1_coeff', uint16_t * int(3)),
    ('ynr_low_gauss2_coeff', uint16_t * int(3)),
    ('ynr_direction_weight', uint8_t * int(8)),
    ('ynr_luma_points_x', uint16_t * int(17)),
    ('ynr_lsgm_y', uint16_t * int(17)),
    ('ynr_hsgm_y', uint16_t * int(17)),
    ('ynr_rnr_strength', uint16_t * int(17)),
]

RK_YNR_Fix_V3_t = struct_RK_YNR_Fix_V3_s# /root/camera_engine_rkaiq/include/algos/aynr3/rk_aiq_types_aynr_hw_v3.h: 107

# /root/camera_engine_rkaiq/include/algos/again2/rk_aiq_types_again_hw_v2.h: 41
class struct_RK_GAIN_Fix_V2_s(Structure):
    pass

struct_RK_GAIN_Fix_V2_s.__slots__ = [
    'sw_gain2ddr_mode',
    'sw_gain2ddr_wr_en',
    'sw_3dlut_gain_en',
    'sw_dhaz_gain_en',
    'sw_adrc_gain_en',
    'sw_lsc_gain_en',
    'sw_gain_module_free_mode',
    'sw_gain_dmard_mode_en',
    'sw_bayer3dnr_gain_en',
    'sw_gain_mp_pipe_dis',
    'sw_gain_gate_always_on',
    'sw_mge_gain_en',
    'sw_gain_en',
    'sw_gain',
]
struct_RK_GAIN_Fix_V2_s._fields_ = [
    ('sw_gain2ddr_mode', c_ubyte),
    ('sw_gain2ddr_wr_en', c_ubyte),
    ('sw_3dlut_gain_en', c_ubyte),
    ('sw_dhaz_gain_en', c_ubyte),
    ('sw_adrc_gain_en', c_ubyte),
    ('sw_lsc_gain_en', c_ubyte),
    ('sw_gain_module_free_mode', c_ubyte),
    ('sw_gain_dmard_mode_en', c_ubyte),
    ('sw_bayer3dnr_gain_en', c_ubyte),
    ('sw_gain_mp_pipe_dis', c_ubyte),
    ('sw_gain_gate_always_on', c_ubyte),
    ('sw_mge_gain_en', c_ubyte),
    ('sw_gain_en', c_ubyte),
    ('sw_gain', c_uint * int(3)),
]

RK_GAIN_Fix_V2_t = struct_RK_GAIN_Fix_V2_s# /root/camera_engine_rkaiq/include/algos/again2/rk_aiq_types_again_hw_v2.h: 41

rk_aiq_isp_awb_stats2_v3x_t = rk_aiq_awb_stat_res2_v30_t# /root/camera_engine_rkaiq/include/common/rk_aiq_types_v3x.h: 121

rk_aiq_isp_af_stats_v3x_t = rk_aiq_af_algo_stat_v30_t# /root/camera_engine_rkaiq/include/common/rk_aiq_types_v3x.h: 123

# /root/camera_engine_rkaiq/include/common/rk_aiq_types.h: 91
class struct_rk_aiq_range_s(Structure):
    pass

struct_rk_aiq_range_s.__slots__ = [
    'min',
    'max',
    'step',
]
struct_rk_aiq_range_s._fields_ = [
    ('min', c_float),
    ('max', c_float),
    ('step', c_float),
]

rk_aiq_range_t = struct_rk_aiq_range_s# /root/camera_engine_rkaiq/include/common/rk_aiq_types.h: 91

# /root/camera_engine_rkaiq/include/common/rk_aiq_types.h: 98
class struct_rk_aiq_rect_s(Structure):
    pass

struct_rk_aiq_rect_s.__slots__ = [
    'left',
    'top',
    'width',
    'height',
]
struct_rk_aiq_rect_s._fields_ = [
    ('left', c_int),
    ('top', c_int),
    ('width', c_int),
    ('height', c_int),
]

rk_aiq_rect_t = struct_rk_aiq_rect_s# /root/camera_engine_rkaiq/include/common/rk_aiq_types.h: 98

enum_rk_aiq_rotation_e = c_int# /root/camera_engine_rkaiq/include/common/rk_aiq_types.h: 104

rk_aiq_rotation_t = enum_rk_aiq_rotation_e# /root/camera_engine_rkaiq/include/common/rk_aiq_types.h: 104

enum_rk_aiq_af_sec_stat_e = c_int# /root/camera_engine_rkaiq/include/common/rk_aiq_types.h: 113

rk_aiq_af_sec_stat_t = enum_rk_aiq_af_sec_stat_e# /root/camera_engine_rkaiq/include/common/rk_aiq_types.h: 113

enum_anon_134 = c_int# /root/camera_engine_rkaiq/include/common/rk_aiq_types.h: 287

rk_aiq_format_t = enum_anon_134# /root/camera_engine_rkaiq/include/common/rk_aiq_types.h: 287

# /root/camera_engine_rkaiq/include/common/rk_aiq_types.h: 295
class struct_rk_frame_fmt_s(Structure):
    pass

struct_rk_frame_fmt_s.__slots__ = [
    'width',
    'height',
    'format',
    'fps',
    'hdr_mode',
]
struct_rk_frame_fmt_s._fields_ = [
    ('width', c_int32),
    ('height', c_int32),
    ('format', rk_aiq_format_t),
    ('fps', c_int32),
    ('hdr_mode', c_int32),
]

rk_frame_fmt_t = struct_rk_frame_fmt_s# /root/camera_engine_rkaiq/include/common/rk_aiq_types.h: 295

# /root/camera_engine_rkaiq/include/common/rk_aiq_types.h: 305
class struct_anon_135(Structure):
    pass

struct_anon_135.__slots__ = [
    'sensor_name',
    'support_fmt',
    'num',
    'binded_strm_media_idx',
    'phyId',
]
struct_anon_135._fields_ = [
    ('sensor_name', c_char * int(32)),
    ('support_fmt', rk_frame_fmt_t * int(10)),
    ('num', c_int32),
    ('binded_strm_media_idx', c_int8),
    ('phyId', c_int),
]

rk_aiq_sensor_info_t = struct_anon_135# /root/camera_engine_rkaiq/include/common/rk_aiq_types.h: 305

# /root/camera_engine_rkaiq/include/common/rk_aiq_types.h: 309
class struct_anon_136(Structure):
    pass

struct_anon_136.__slots__ = [
    'len_name',
]
struct_anon_136._fields_ = [
    ('len_name', c_char * int(32)),
]

rk_aiq_lens_info_t = struct_anon_136# /root/camera_engine_rkaiq/include/common/rk_aiq_types.h: 309

# /root/camera_engine_rkaiq/include/common/rk_aiq_types.h: 330
class struct_anon_137(Structure):
    pass

struct_anon_137.__slots__ = [
    'sensor_info',
    'lens_info',
    'isp_hw_ver',
    'has_lens_vcm',
    'has_fl',
    'fl_strth_adj_sup',
    'has_irc',
    'fl_ir_strth_adj_sup',
    '_is_1608_sensor',
    'is_multi_isp_mode',
    'multi_isp_extended_pixel',
    'reserved',
]
struct_anon_137._fields_ = [
    ('sensor_info', rk_aiq_sensor_info_t),
    ('lens_info', rk_aiq_lens_info_t),
    ('isp_hw_ver', c_int),
    ('has_lens_vcm', c_bool),
    ('has_fl', c_bool),
    ('fl_strth_adj_sup', c_bool),
    ('has_irc', c_bool),
    ('fl_ir_strth_adj_sup', c_bool),
    ('_is_1608_sensor', c_bool),
    ('is_multi_isp_mode', uint8_t),
    ('multi_isp_extended_pixel', uint16_t),
    ('reserved', uint8_t * int(13)),
]

rk_aiq_static_info_t = struct_anon_137# /root/camera_engine_rkaiq/include/common/rk_aiq_types.h: 330

# /root/camera_engine_rkaiq/include/common/rk_aiq_types.h: 360
class struct_anon_139(Structure):
    pass

struct_anon_139.__slots__ = [
    'start_ma',
    'rated_ma',
    'step_mode',
]
struct_anon_139._fields_ = [
    ('start_ma', c_int),
    ('rated_ma', c_int),
    ('step_mode', c_int),
]

rk_aiq_lens_vcmcfg = struct_anon_139# /root/camera_engine_rkaiq/include/common/rk_aiq_types.h: 360

# /root/camera_engine_rkaiq/include/common/rk_aiq_types.h: 367
class struct_anon_140(Structure):
    pass

struct_anon_140.__slots__ = [
    'stat',
    'search_num',
    'pos',
    'sharpness',
]
struct_anon_140._fields_ = [
    ('stat', rk_aiq_af_sec_stat_t),
    ('search_num', c_int32),
    ('pos', c_int32 * int(64)),
    ('sharpness', c_float * int(64)),
]

rk_aiq_af_sec_path_t = struct_anon_140# /root/camera_engine_rkaiq/include/common/rk_aiq_types.h: 367

# /root/camera_engine_rkaiq/include/common/rk_aiq_types.h: 372
class struct_anon_141(Structure):
    pass

struct_anon_141.__slots__ = [
    'stat',
    'final_pos',
]
struct_anon_141._fields_ = [
    ('stat', rk_aiq_af_sec_stat_t),
    ('final_pos', c_int32),
]

rk_aiq_af_result_t = struct_anon_141# /root/camera_engine_rkaiq/include/common/rk_aiq_types.h: 372

# /root/camera_engine_rkaiq/include/common/rk_aiq_types.h: 379
class struct_anon_142(Structure):
    pass

struct_anon_142.__slots__ = [
    'min_pos',
    'max_pos',
    'min_fl',
    'max_fl',
]
struct_anon_142._fields_ = [
    ('min_pos', c_int),
    ('max_pos', c_int),
    ('min_fl', c_float),
    ('max_fl', c_float),
]

rk_aiq_af_zoomrange = struct_anon_142# /root/camera_engine_rkaiq/include/common/rk_aiq_types.h: 379

# /root/camera_engine_rkaiq/include/common/rk_aiq_types.h: 384
class struct_anon_143(Structure):
    pass

struct_anon_143.__slots__ = [
    'min_pos',
    'max_pos',
]
struct_anon_143._fields_ = [
    ('min_pos', c_int),
    ('max_pos', c_int),
]

rk_aiq_af_focusrange = struct_anon_143# /root/camera_engine_rkaiq/include/common/rk_aiq_types.h: 384

rk_aiq_isp_aec_stats_t = RKAiqAecStats_t# /root/camera_engine_rkaiq/include/common/rk_aiq_types.h: 455

rk_aiq_isp_af_stats_t = rk_aiq_af_algo_stat_v20_t# /root/camera_engine_rkaiq/include/common/rk_aiq_types.h: 457

# /root/camera_engine_rkaiq/include/common/rk_aiq_types.h: 539
class union_anon_153(Union):
    pass

union_anon_153.__slots__ = [
    'awb_stats_v200',
    'awb_stats_v21',
    'awb_stats_v3x',
]
union_anon_153._fields_ = [
    ('awb_stats_v200', rk_aiq_awb_stat_res_v200_t),
    ('awb_stats_v21', rk_aiq_awb_stat_res2_v201_t),
    ('awb_stats_v3x', rk_aiq_isp_awb_stats2_v3x_t),
]

# /root/camera_engine_rkaiq/include/common/rk_aiq_types.h: 545
class union_anon_154(Union):
    pass

union_anon_154.__slots__ = [
    'af_stats',
    'af_stats_v3x',
]
union_anon_154._fields_ = [
    ('af_stats', rk_aiq_isp_af_stats_t),
    ('af_stats_v3x', rk_aiq_isp_af_stats_v3x_t),
]

# /root/camera_engine_rkaiq/include/common/rk_aiq_types.h: 549
class struct_anon_155(Structure):
    pass

struct_anon_155.__slots__ = [
    'frame_id',
    'aec_stats',
    'awb_hw_ver',
    'unnamed_1',
    'af_hw_ver',
    'unnamed_2',
]
struct_anon_155._anonymous_ = [
    'unnamed_1',
    'unnamed_2',
]
struct_anon_155._fields_ = [
    ('frame_id', sint32_t),
    ('aec_stats', rk_aiq_isp_aec_stats_t),
    ('awb_hw_ver', c_int),
    ('unnamed_1', union_anon_153),
    ('af_hw_ver', c_int),
    ('unnamed_2', union_anon_154),
]

rk_aiq_isp_stats_t = struct_anon_155# /root/camera_engine_rkaiq/include/common/rk_aiq_types.h: 549

enum_rk_aiq_gray_mode_e = c_int# /root/camera_engine_rkaiq/include/common/rk_aiq_types.h: 593

rk_aiq_gray_mode_t = enum_rk_aiq_gray_mode_e# /root/camera_engine_rkaiq/include/common/rk_aiq_types.h: 593

enum_rk_aiq_cpsls_e = c_int# /root/camera_engine_rkaiq/include/common/rk_aiq_types.h: 653

RK_AIQ_CPSLS_MIX = 3# /root/camera_engine_rkaiq/include/common/rk_aiq_types.h: 653

RK_AIQ_CPSLS_MAX = (RK_AIQ_CPSLS_MIX + 1)# /root/camera_engine_rkaiq/include/common/rk_aiq_types.h: 653

rk_aiq_cpsls_t = enum_rk_aiq_cpsls_e# /root/camera_engine_rkaiq/include/common/rk_aiq_types.h: 653

# /root/camera_engine_rkaiq/include/common/rk_aiq_types.h: 667
class struct_anon_156(Structure):
    pass

struct_anon_156.__slots__ = [
    'sensitivity',
    'sw_interval',
]
struct_anon_156._fields_ = [
    ('sensitivity', c_float),
    ('sw_interval', uint32_t),
]

# /root/camera_engine_rkaiq/include/common/rk_aiq_types.h: 671
class struct_anon_157(Structure):
    pass

struct_anon_157.__slots__ = [
    'on',
    'strength_led',
    'strength_ir',
]
struct_anon_157._fields_ = [
    ('on', uint8_t),
    ('strength_led', c_float),
    ('strength_ir', c_float),
]

# /root/camera_engine_rkaiq/include/common/rk_aiq_types.h: 666
class union_anon_158(Union):
    pass

union_anon_158.__slots__ = [
    'a',
    'm',
]
union_anon_158._fields_ = [
    ('a', struct_anon_156),
    ('m', struct_anon_157),
]

# /root/camera_engine_rkaiq/include/common/rk_aiq_types.h: 677
class struct_rk_aiq_cpsl_cfg_s(Structure):
    pass

struct_rk_aiq_cpsl_cfg_s.__slots__ = [
    'mode',
    'lght_src',
    'gray_on',
    'u',
]
struct_rk_aiq_cpsl_cfg_s._fields_ = [
    ('mode', RKAiqOPMode_t),
    ('lght_src', rk_aiq_cpsls_t),
    ('gray_on', c_bool),
    ('u', union_anon_158),
]

rk_aiq_cpsl_cfg_t = struct_rk_aiq_cpsl_cfg_s# /root/camera_engine_rkaiq/include/common/rk_aiq_types.h: 677

# /root/camera_engine_rkaiq/include/common/rk_aiq_types.h: 688
class struct_rk_aiq_cpsl_info_s(Structure):
    pass

struct_rk_aiq_cpsl_info_s.__slots__ = [
    'mode',
    'on',
    'gray',
    'strength_led',
    'strength_ir',
    'sensitivity',
    'sw_interval',
    'lght_src',
]
struct_rk_aiq_cpsl_info_s._fields_ = [
    ('mode', c_int32),
    ('on', uint8_t),
    ('gray', c_bool),
    ('strength_led', c_float),
    ('strength_ir', c_float),
    ('sensitivity', c_float),
    ('sw_interval', uint32_t),
    ('lght_src', c_int32),
]

rk_aiq_cpsl_info_t = struct_rk_aiq_cpsl_info_s# /root/camera_engine_rkaiq/include/common/rk_aiq_types.h: 688

# /root/camera_engine_rkaiq/include/common/rk_aiq_types.h: 698
class struct_rk_aiq_cpsl_cap_s(Structure):
    pass

struct_rk_aiq_cpsl_cap_s.__slots__ = [
    'supported_modes',
    'modes_num',
    'supported_lght_src',
    'lght_src_num',
    'strength_led',
    'sensitivity',
    'strength_ir',
]
struct_rk_aiq_cpsl_cap_s._fields_ = [
    ('supported_modes', c_int32 * int(RK_AIQ_OP_MODE_MAX)),
    ('modes_num', uint8_t),
    ('supported_lght_src', c_int32 * int(RK_AIQ_CPSLS_MAX)),
    ('lght_src_num', uint8_t),
    ('strength_led', rk_aiq_range_t),
    ('sensitivity', rk_aiq_range_t),
    ('strength_ir', rk_aiq_range_t),
]

rk_aiq_cpsl_cap_t = struct_rk_aiq_cpsl_cap_s# /root/camera_engine_rkaiq/include/common/rk_aiq_types.h: 698

enum_capture_raw_e = c_int# /root/camera_engine_rkaiq/include/common/rk_aiq_types.h: 786

capture_raw_t = enum_capture_raw_e# /root/camera_engine_rkaiq/include/common/rk_aiq_types.h: 786

enum_rk_aiq_rawbuf_type_s = c_int# /root/camera_engine_rkaiq/include/common/rk_aiq_types.h: 793

rk_aiq_rawbuf_type_t = enum_rk_aiq_rawbuf_type_s# /root/camera_engine_rkaiq/include/common/rk_aiq_types.h: 793

# /root/camera_engine_rkaiq/include/common/rk_aiq_types.h: 800
class struct_rk_aiq_raw_prop_s(Structure):
    pass

struct_rk_aiq_raw_prop_s.__slots__ = [
    'frame_width',
    'frame_height',
    'format',
    'rawbuf_type',
]
struct_rk_aiq_raw_prop_s._fields_ = [
    ('frame_width', uint32_t),
    ('frame_height', uint32_t),
    ('format', rk_aiq_format_t),
    ('rawbuf_type', rk_aiq_rawbuf_type_t),
]

rk_aiq_raw_prop_t = struct_rk_aiq_raw_prop_s# /root/camera_engine_rkaiq/include/common/rk_aiq_types.h: 800

enum_opMode_e = c_int# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api_common.h: 16

opMode_t = enum_opMode_e# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api_common.h: 16

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api_common.h: 33
class struct_paRange_s(Structure):
    pass

struct_paRange_s.__slots__ = [
    'max',
    'min',
]
struct_paRange_s._fields_ = [
    ('max', c_float),
    ('min', c_float),
]

paRange_t = struct_paRange_s# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api_common.h: 33

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api_common.h: 66
class struct_paRect_s(Structure):
    pass

struct_paRect_s.__slots__ = [
    'x',
    'y',
    'w',
    'h',
]
struct_paRect_s._fields_ = [
    ('x', c_int),
    ('y', c_int),
    ('w', c_uint),
    ('h', c_uint),
]

paRect_t = struct_paRect_s# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api_common.h: 66

enum_aeMeasAreaType_e = c_int# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api_common.h: 75

aeMeasAreaType_t = enum_aeMeasAreaType_e# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api_common.h: 75

enum_expPwrLineFreq_e = c_int# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api_common.h: 81

expPwrLineFreq_t = enum_expPwrLineFreq_e# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api_common.h: 81

enum_antiFlickerMode_e = c_int# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api_common.h: 86

antiFlickerMode_t = enum_antiFlickerMode_e# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api_common.h: 86

# /root/camera_engine_rkaiq/include/iq_parser_v2/af_uapi_head.h: 144
class struct_rk_tool_customAf_res_s(Structure):
    pass

struct_rk_tool_customAf_res_s.__slots__ = [
    'af_en',
    'rawaf_sel',
    'gamma_en',
    'gaus_en',
    'v1_fir_sel',
    'hiir_en',
    'viir_en',
    'v1_fv_outmode',
    'v2_fv_outmode',
    'h1_fv_outmode',
    'h2_fv_outmode',
    'ldg_en',
    'accu_8bit_mode',
    'ae_mode',
    'y_mode',
    'line_en',
    'line_num',
    'window_num',
    'wina_h_offs',
    'wina_v_offs',
    'wina_h_size',
    'wina_v_size',
    'winb_h_offs',
    'winb_v_offs',
    'winb_h_size',
    'winb_v_size',
    'gamma_y',
    'thres',
    'shift_sum_a',
    'shift_sum_b',
    'shift_y_a',
    'shift_y_b',
    'v1_iir_coe',
    'v1_fir_coe',
    'v2_iir_coe',
    'v2_fir_coe',
    'h1_iir1_coe',
    'h2_iir1_coe',
    'h1_iir2_coe',
    'h2_iir2_coe',
    'h_ldg_lumth',
    'h_ldg_gain',
    'h_ldg_gslp',
    'v_ldg_lumth',
    'v_ldg_gain',
    'v_ldg_gslp',
    'v_fv_thresh',
    'h_fv_thresh',
    'v1_fv_shift',
    'v2_fv_shift',
    'h1_fv_shift',
    'h2_fv_shift',
    'highlit_thresh',
]
struct_rk_tool_customAf_res_s._fields_ = [
    ('af_en', c_ubyte),
    ('rawaf_sel', c_ubyte),
    ('gamma_en', c_ubyte),
    ('gaus_en', c_ubyte),
    ('v1_fir_sel', c_ubyte),
    ('hiir_en', c_ubyte),
    ('viir_en', c_ubyte),
    ('v1_fv_outmode', c_ubyte),
    ('v2_fv_outmode', c_ubyte),
    ('h1_fv_outmode', c_ubyte),
    ('h2_fv_outmode', c_ubyte),
    ('ldg_en', c_ubyte),
    ('accu_8bit_mode', c_ubyte),
    ('ae_mode', c_ubyte),
    ('y_mode', c_ubyte),
    ('line_en', c_ubyte * int(5)),
    ('line_num', c_ubyte * int(5)),
    ('window_num', c_ubyte),
    ('wina_h_offs', c_ushort),
    ('wina_v_offs', c_ushort),
    ('wina_h_size', c_ushort),
    ('wina_v_size', c_ushort),
    ('winb_h_offs', c_ushort),
    ('winb_v_offs', c_ushort),
    ('winb_h_size', c_ushort),
    ('winb_v_size', c_ushort),
    ('gamma_y', c_ushort * int(17)),
    ('thres', c_ushort),
    ('shift_sum_a', c_ubyte),
    ('shift_sum_b', c_ubyte),
    ('shift_y_a', c_ubyte),
    ('shift_y_b', c_ubyte),
    ('v1_iir_coe', c_short * int(9)),
    ('v1_fir_coe', c_short * int(3)),
    ('v2_iir_coe', c_short * int(3)),
    ('v2_fir_coe', c_short * int(3)),
    ('h1_iir1_coe', c_short * int(6)),
    ('h2_iir1_coe', c_short * int(6)),
    ('h1_iir2_coe', c_short * int(6)),
    ('h2_iir2_coe', c_short * int(6)),
    ('h_ldg_lumth', c_ubyte * int(2)),
    ('h_ldg_gain', c_ubyte * int(2)),
    ('h_ldg_gslp', c_ushort * int(2)),
    ('v_ldg_lumth', c_ubyte * int(2)),
    ('v_ldg_gain', c_ubyte * int(2)),
    ('v_ldg_gslp', c_ushort * int(2)),
    ('v_fv_thresh', c_ushort),
    ('h_fv_thresh', c_ushort),
    ('v1_fv_shift', c_ubyte),
    ('v2_fv_shift', c_ubyte),
    ('h1_fv_shift', c_ubyte),
    ('h2_fv_shift', c_ubyte),
    ('highlit_thresh', c_ushort),
]

rk_tool_customAf_res_t = struct_rk_tool_customAf_res_s# /root/camera_engine_rkaiq/include/iq_parser_v2/af_uapi_head.h: 144

enum__RKAIQ_AF_MODE = c_int# /root/camera_engine_rkaiq/include/algos/af/rk_aiq_types_af_algo_int.h: 38

RKAIQ_AF_MODE = enum__RKAIQ_AF_MODE# /root/camera_engine_rkaiq/include/algos/af/rk_aiq_types_af_algo_int.h: 38

enum__RKAIQ_AF_HWVER = c_int# /root/camera_engine_rkaiq/include/algos/af/rk_aiq_types_af_algo_int.h: 45

RKAIQ_AF_HWVER = enum__RKAIQ_AF_HWVER# /root/camera_engine_rkaiq/include/algos/af/rk_aiq_types_af_algo_int.h: 45

# /root/camera_engine_rkaiq/include/algos/af/rk_aiq_types_af_algo_int.h: 66
class union_anon_163(Union):
    pass

union_anon_163.__slots__ = [
    'manual_meascfg',
    'manual_meascfg_v30',
]
union_anon_163._fields_ = [
    ('manual_meascfg', rk_aiq_af_algo_meas_v20_t),
    ('manual_meascfg_v30', rk_aiq_af_algo_meas_v30_t),
]

# /root/camera_engine_rkaiq/include/algos/af/rk_aiq_types_af_algo_int.h: 70
class struct_rk_aiq_af_attrib_s(Structure):
    pass

struct_rk_aiq_af_attrib_s.__slots__ = [
    'sync',
    'AfMode',
    'AfHwVer',
    'contrast_af',
    'laser_af',
    'pdaf',
    'h_offs',
    'v_offs',
    'h_size',
    'v_size',
    'fixedModeDefCode',
    'macroModeDefCode',
    'infinityModeDefCode',
    'unnamed_1',
]
struct_rk_aiq_af_attrib_s._anonymous_ = [
    'unnamed_1',
]
struct_rk_aiq_af_attrib_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('AfMode', RKAIQ_AF_MODE),
    ('AfHwVer', RKAIQ_AF_HWVER),
    ('contrast_af', c_bool),
    ('laser_af', c_bool),
    ('pdaf', c_bool),
    ('h_offs', c_int),
    ('v_offs', c_int),
    ('h_size', c_uint),
    ('v_size', c_uint),
    ('fixedModeDefCode', c_short),
    ('macroModeDefCode', c_short),
    ('infinityModeDefCode', c_short),
    ('unnamed_1', union_anon_163),
]

rk_aiq_af_attrib_t = struct_rk_aiq_af_attrib_s# /root/camera_engine_rkaiq/include/algos/af/rk_aiq_types_af_algo_int.h: 70

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_af.h: 30
if _libs["rkaiq"].has("rk_aiq_user_api2_af_SetAttrib", "cdecl"):
    rk_aiq_user_api2_af_SetAttrib = _libs["rkaiq"].get("rk_aiq_user_api2_af_SetAttrib", "cdecl")
    rk_aiq_user_api2_af_SetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_af_attrib_t)]
    rk_aiq_user_api2_af_SetAttrib.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_af.h: 32
if _libs["rkaiq"].has("rk_aiq_user_api2_af_GetAttrib", "cdecl"):
    rk_aiq_user_api2_af_GetAttrib = _libs["rkaiq"].get("rk_aiq_user_api2_af_GetAttrib", "cdecl")
    rk_aiq_user_api2_af_GetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_af_attrib_t)]
    rk_aiq_user_api2_af_GetAttrib.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_af.h: 34
if _libs["rkaiq"].has("rk_aiq_user_api2_af_Lock", "cdecl"):
    rk_aiq_user_api2_af_Lock = _libs["rkaiq"].get("rk_aiq_user_api2_af_Lock", "cdecl")
    rk_aiq_user_api2_af_Lock.argtypes = [POINTER(rk_aiq_sys_ctx_t)]
    rk_aiq_user_api2_af_Lock.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_af.h: 36
if _libs["rkaiq"].has("rk_aiq_user_api2_af_Unlock", "cdecl"):
    rk_aiq_user_api2_af_Unlock = _libs["rkaiq"].get("rk_aiq_user_api2_af_Unlock", "cdecl")
    rk_aiq_user_api2_af_Unlock.argtypes = [POINTER(rk_aiq_sys_ctx_t)]
    rk_aiq_user_api2_af_Unlock.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_af.h: 38
if _libs["rkaiq"].has("rk_aiq_user_api2_af_Oneshot", "cdecl"):
    rk_aiq_user_api2_af_Oneshot = _libs["rkaiq"].get("rk_aiq_user_api2_af_Oneshot", "cdecl")
    rk_aiq_user_api2_af_Oneshot.argtypes = [POINTER(rk_aiq_sys_ctx_t)]
    rk_aiq_user_api2_af_Oneshot.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_af.h: 40
if _libs["rkaiq"].has("rk_aiq_user_api2_af_ManualTriger", "cdecl"):
    rk_aiq_user_api2_af_ManualTriger = _libs["rkaiq"].get("rk_aiq_user_api2_af_ManualTriger", "cdecl")
    rk_aiq_user_api2_af_ManualTriger.argtypes = [POINTER(rk_aiq_sys_ctx_t)]
    rk_aiq_user_api2_af_ManualTriger.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_af.h: 42
if _libs["rkaiq"].has("rk_aiq_user_api2_af_Tracking", "cdecl"):
    rk_aiq_user_api2_af_Tracking = _libs["rkaiq"].get("rk_aiq_user_api2_af_Tracking", "cdecl")
    rk_aiq_user_api2_af_Tracking.argtypes = [POINTER(rk_aiq_sys_ctx_t)]
    rk_aiq_user_api2_af_Tracking.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_af.h: 44
if _libs["rkaiq"].has("rk_aiq_user_api2_af_SetZoomIndex", "cdecl"):
    rk_aiq_user_api2_af_SetZoomIndex = _libs["rkaiq"].get("rk_aiq_user_api2_af_SetZoomIndex", "cdecl")
    rk_aiq_user_api2_af_SetZoomIndex.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_int]
    rk_aiq_user_api2_af_SetZoomIndex.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_af.h: 46
if _libs["rkaiq"].has("rk_aiq_user_api2_af_GetZoomIndex", "cdecl"):
    rk_aiq_user_api2_af_GetZoomIndex = _libs["rkaiq"].get("rk_aiq_user_api2_af_GetZoomIndex", "cdecl")
    rk_aiq_user_api2_af_GetZoomIndex.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(c_int)]
    rk_aiq_user_api2_af_GetZoomIndex.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_af.h: 48
if _libs["rkaiq"].has("rk_aiq_user_api2_af_EndZoomChg", "cdecl"):
    rk_aiq_user_api2_af_EndZoomChg = _libs["rkaiq"].get("rk_aiq_user_api2_af_EndZoomChg", "cdecl")
    rk_aiq_user_api2_af_EndZoomChg.argtypes = [POINTER(rk_aiq_sys_ctx_t)]
    rk_aiq_user_api2_af_EndZoomChg.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_af.h: 50
if _libs["rkaiq"].has("rk_aiq_user_api2_af_StartZoomCalib", "cdecl"):
    rk_aiq_user_api2_af_StartZoomCalib = _libs["rkaiq"].get("rk_aiq_user_api2_af_StartZoomCalib", "cdecl")
    rk_aiq_user_api2_af_StartZoomCalib.argtypes = [POINTER(rk_aiq_sys_ctx_t)]
    rk_aiq_user_api2_af_StartZoomCalib.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_af.h: 52
if _libs["rkaiq"].has("rk_aiq_user_api2_af_resetZoom", "cdecl"):
    rk_aiq_user_api2_af_resetZoom = _libs["rkaiq"].get("rk_aiq_user_api2_af_resetZoom", "cdecl")
    rk_aiq_user_api2_af_resetZoom.argtypes = [POINTER(rk_aiq_sys_ctx_t)]
    rk_aiq_user_api2_af_resetZoom.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_af.h: 54
if _libs["rkaiq"].has("rk_aiq_user_api2_af_SetVcmCfg", "cdecl"):
    rk_aiq_user_api2_af_SetVcmCfg = _libs["rkaiq"].get("rk_aiq_user_api2_af_SetVcmCfg", "cdecl")
    rk_aiq_user_api2_af_SetVcmCfg.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_lens_vcmcfg)]
    rk_aiq_user_api2_af_SetVcmCfg.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_af.h: 56
if _libs["rkaiq"].has("rk_aiq_user_api2_af_GetVcmCfg", "cdecl"):
    rk_aiq_user_api2_af_GetVcmCfg = _libs["rkaiq"].get("rk_aiq_user_api2_af_GetVcmCfg", "cdecl")
    rk_aiq_user_api2_af_GetVcmCfg.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_lens_vcmcfg)]
    rk_aiq_user_api2_af_GetVcmCfg.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_af.h: 58
if _libs["rkaiq"].has("rk_aiq_user_api2_af_GetSearchPath", "cdecl"):
    rk_aiq_user_api2_af_GetSearchPath = _libs["rkaiq"].get("rk_aiq_user_api2_af_GetSearchPath", "cdecl")
    rk_aiq_user_api2_af_GetSearchPath.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_af_sec_path_t)]
    rk_aiq_user_api2_af_GetSearchPath.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_af.h: 60
if _libs["rkaiq"].has("rk_aiq_user_api2_af_GetSearchResult", "cdecl"):
    rk_aiq_user_api2_af_GetSearchResult = _libs["rkaiq"].get("rk_aiq_user_api2_af_GetSearchResult", "cdecl")
    rk_aiq_user_api2_af_GetSearchResult.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_af_result_t)]
    rk_aiq_user_api2_af_GetSearchResult.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_af.h: 62
if _libs["rkaiq"].has("rk_aiq_user_api2_af_GetZoomRange", "cdecl"):
    rk_aiq_user_api2_af_GetZoomRange = _libs["rkaiq"].get("rk_aiq_user_api2_af_GetZoomRange", "cdecl")
    rk_aiq_user_api2_af_GetZoomRange.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_af_zoomrange)]
    rk_aiq_user_api2_af_GetZoomRange.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_af.h: 64
if _libs["rkaiq"].has("rk_aiq_user_api2_af_GetFocusRange", "cdecl"):
    rk_aiq_user_api2_af_GetFocusRange = _libs["rkaiq"].get("rk_aiq_user_api2_af_GetFocusRange", "cdecl")
    rk_aiq_user_api2_af_GetFocusRange.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_af_focusrange)]
    rk_aiq_user_api2_af_GetFocusRange.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_af.h: 66
if _libs["rkaiq"].has("rk_aiq_user_api2_af_setAngleZ", "cdecl"):
    rk_aiq_user_api2_af_setAngleZ = _libs["rkaiq"].get("rk_aiq_user_api2_af_setAngleZ", "cdecl")
    rk_aiq_user_api2_af_setAngleZ.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_float]
    rk_aiq_user_api2_af_setAngleZ.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_af.h: 68
if _libs["rkaiq"].has("rk_aiq_user_api2_af_getCustomAfRes", "cdecl"):
    rk_aiq_user_api2_af_getCustomAfRes = _libs["rkaiq"].get("rk_aiq_user_api2_af_getCustomAfRes", "cdecl")
    rk_aiq_user_api2_af_getCustomAfRes.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_tool_customAf_res_t)]
    rk_aiq_user_api2_af_getCustomAfRes.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_af.h: 70
if _libs["rkaiq"].has("rk_aiq_user_api2_af_setCustomAfRes", "cdecl"):
    rk_aiq_user_api2_af_setCustomAfRes = _libs["rkaiq"].get("rk_aiq_user_api2_af_setCustomAfRes", "cdecl")
    rk_aiq_user_api2_af_setCustomAfRes.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_tool_customAf_res_t)]
    rk_aiq_user_api2_af_setCustomAfRes.restype = XCamReturn

# /root/camera_engine_rkaiq/include/iq_parser_v2/gain_uapi_head_v2.h: 37
class struct_RK_GAIN_Select_V2_s(Structure):
    pass

struct_RK_GAIN_Select_V2_s.__slots__ = [
    'hdrgain_ctrl_enable',
    'hdr_gain_scale_s',
    'hdr_gain_scale_m',
]
struct_RK_GAIN_Select_V2_s._fields_ = [
    ('hdrgain_ctrl_enable', c_bool),
    ('hdr_gain_scale_s', c_float),
    ('hdr_gain_scale_m', c_float),
]

RK_GAIN_Select_V2_t = struct_RK_GAIN_Select_V2_s# /root/camera_engine_rkaiq/include/iq_parser_v2/gain_uapi_head_v2.h: 37

# /root/camera_engine_rkaiq/include/iq_parser_v2/gain_uapi_head_v2.h: 59
class struct_Again_ExpInfo_V2_s(Structure):
    pass

struct_Again_ExpInfo_V2_s.__slots__ = [
    'hdr_mode',
    'snr_mode',
    'arTime',
    'arAGain',
    'arDGain',
    'arIso',
    'isoLow',
    'isoHigh',
]
struct_Again_ExpInfo_V2_s._fields_ = [
    ('hdr_mode', c_int),
    ('snr_mode', c_int),
    ('arTime', c_float * int(3)),
    ('arAGain', c_float * int(3)),
    ('arDGain', c_float * int(3)),
    ('arIso', c_int * int(3)),
    ('isoLow', c_int),
    ('isoHigh', c_int),
]

Again_ExpInfo_V2_t = struct_Again_ExpInfo_V2_s# /root/camera_engine_rkaiq/include/iq_parser_v2/gain_uapi_head_v2.h: 59

# /root/camera_engine_rkaiq/include/iq_parser_v2/gain_uapi_head_v2.h: 68
class struct_rk_aiq_gain_info_v2_s(Structure):
    pass

struct_rk_aiq_gain_info_v2_s.__slots__ = [
    'sync',
    'iso',
    'expo_info',
]
struct_rk_aiq_gain_info_v2_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('iso', c_int),
    ('expo_info', Again_ExpInfo_V2_t),
]

rk_aiq_gain_info_v2_t = struct_rk_aiq_gain_info_v2_s# /root/camera_engine_rkaiq/include/iq_parser_v2/gain_uapi_head_v2.h: 68

enum_Again_OPMode_V2_e = c_int# /root/camera_engine_rkaiq/include/algos/again2/rk_aiq_types_again_algo_int_v2.h: 75

Again_OPMode_V2_t = enum_Again_OPMode_V2_e# /root/camera_engine_rkaiq/include/algos/again2/rk_aiq_types_again_algo_int_v2.h: 75

# /root/camera_engine_rkaiq/include/algos/again2/rk_aiq_types_again_algo_int_v2.h: 101
class struct_RK_GAIN_Params_V2_s(Structure):
    pass

struct_RK_GAIN_Params_V2_s.__slots__ = [
    'hdrgain_ctrl_enable',
    'iso',
    'iso_params',
]
struct_RK_GAIN_Params_V2_s._fields_ = [
    ('hdrgain_ctrl_enable', c_bool),
    ('iso', c_int * int(13)),
    ('iso_params', RK_GAIN_Select_V2_t * int(13)),
]

RK_GAIN_Params_V2_t = struct_RK_GAIN_Params_V2_s# /root/camera_engine_rkaiq/include/algos/again2/rk_aiq_types_again_algo_int_v2.h: 101

# /root/camera_engine_rkaiq/include/algos/again2/rk_aiq_types_again_algo_int_v2.h: 108
class struct_Again_Manual_Attr_V2_s(Structure):
    pass

struct_Again_Manual_Attr_V2_s.__slots__ = [
    'stSelect',
    'stFix',
]
struct_Again_Manual_Attr_V2_s._fields_ = [
    ('stSelect', RK_GAIN_Select_V2_t),
    ('stFix', RK_GAIN_Fix_V2_t),
]

Again_Manual_Attr_V2_t = struct_Again_Manual_Attr_V2_s# /root/camera_engine_rkaiq/include/algos/again2/rk_aiq_types_again_algo_int_v2.h: 108

# /root/camera_engine_rkaiq/include/algos/again2/rk_aiq_types_again_algo_int_v2.h: 117
class struct_AgainV2_Auto_Attr_V2_s(Structure):
    pass

struct_AgainV2_Auto_Attr_V2_s.__slots__ = [
    'stParams',
    'stSelect',
]
struct_AgainV2_Auto_Attr_V2_s._fields_ = [
    ('stParams', RK_GAIN_Params_V2_t),
    ('stSelect', RK_GAIN_Select_V2_t),
]

Again_Auto_Attr_V2_t = struct_AgainV2_Auto_Attr_V2_s# /root/camera_engine_rkaiq/include/algos/again2/rk_aiq_types_again_algo_int_v2.h: 117

# /root/camera_engine_rkaiq/include/algos/again2/rk_aiq_types_again_algo_int_v2.h: 142
class struct_rk_aiq_gain_attrib_v2_s(Structure):
    pass

struct_rk_aiq_gain_attrib_v2_s.__slots__ = [
    'sync',
    'eMode',
    'stAuto',
    'stManual',
]
struct_rk_aiq_gain_attrib_v2_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('eMode', Again_OPMode_V2_t),
    ('stAuto', Again_Auto_Attr_V2_t),
    ('stManual', Again_Manual_Attr_V2_t),
]

rk_aiq_gain_attrib_v2_t = struct_rk_aiq_gain_attrib_v2_s# /root/camera_engine_rkaiq/include/algos/again2/rk_aiq_types_again_algo_int_v2.h: 142

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_again_v2.h: 31
if _libs["rkaiq"].has("rk_aiq_user_api2_againV2_SetAttrib", "cdecl"):
    rk_aiq_user_api2_againV2_SetAttrib = _libs["rkaiq"].get("rk_aiq_user_api2_againV2_SetAttrib", "cdecl")
    rk_aiq_user_api2_againV2_SetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_gain_attrib_v2_t)]
    rk_aiq_user_api2_againV2_SetAttrib.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_again_v2.h: 34
if _libs["rkaiq"].has("rk_aiq_user_api2_againV2_GetAttrib", "cdecl"):
    rk_aiq_user_api2_againV2_GetAttrib = _libs["rkaiq"].get("rk_aiq_user_api2_againV2_GetAttrib", "cdecl")
    rk_aiq_user_api2_againV2_GetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_gain_attrib_v2_t)]
    rk_aiq_user_api2_againV2_GetAttrib.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_again_v2.h: 37
if _libs["rkaiq"].has("rk_aiq_user_api2_againV2_GetInfo", "cdecl"):
    rk_aiq_user_api2_againV2_GetInfo = _libs["rkaiq"].get("rk_aiq_user_api2_againV2_GetInfo", "cdecl")
    rk_aiq_user_api2_againV2_GetInfo.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_gain_info_v2_t)]
    rk_aiq_user_api2_againV2_GetInfo.restype = XCamReturn

rk_aiq_gamma_attrib_V2_t = rk_aiq_gamma_attr_t# /root/camera_engine_rkaiq/include/algos/agamma/rk_aiq_uapi_agamma_int.h: 15

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_agamma.h: 31
if _libs["rkaiq"].has("rk_aiq_user_api2_agamma_SetAttrib", "cdecl"):
    rk_aiq_user_api2_agamma_SetAttrib = _libs["rkaiq"].get("rk_aiq_user_api2_agamma_SetAttrib", "cdecl")
    rk_aiq_user_api2_agamma_SetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), rk_aiq_gamma_attrib_V2_t]
    rk_aiq_user_api2_agamma_SetAttrib.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_agamma.h: 33
if _libs["rkaiq"].has("rk_aiq_user_api2_agamma_GetAttrib", "cdecl"):
    rk_aiq_user_api2_agamma_GetAttrib = _libs["rkaiq"].get("rk_aiq_user_api2_agamma_GetAttrib", "cdecl")
    rk_aiq_user_api2_agamma_GetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_gamma_attrib_V2_t)]
    rk_aiq_user_api2_agamma_GetAttrib.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_agic.h: 29
if _libs["rkaiq"].has("rk_aiq_user_api2_agic_v1_SetAttrib", "cdecl"):
    rk_aiq_user_api2_agic_v1_SetAttrib = _libs["rkaiq"].get("rk_aiq_user_api2_agic_v1_SetAttrib", "cdecl")
    rk_aiq_user_api2_agic_v1_SetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rkaiq_gic_v1_api_attr_t)]
    rk_aiq_user_api2_agic_v1_SetAttrib.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_agic.h: 30
if _libs["rkaiq"].has("rk_aiq_user_api2_agic_v1_GetAttrib", "cdecl"):
    rk_aiq_user_api2_agic_v1_GetAttrib = _libs["rkaiq"].get("rk_aiq_user_api2_agic_v1_GetAttrib", "cdecl")
    rk_aiq_user_api2_agic_v1_GetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rkaiq_gic_v1_api_attr_t)]
    rk_aiq_user_api2_agic_v1_GetAttrib.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_agic.h: 31
if _libs["rkaiq"].has("rk_aiq_user_api2_agic_v2_SetAttrib", "cdecl"):
    rk_aiq_user_api2_agic_v2_SetAttrib = _libs["rkaiq"].get("rk_aiq_user_api2_agic_v2_SetAttrib", "cdecl")
    rk_aiq_user_api2_agic_v2_SetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rkaiq_gic_v2_api_attr_t)]
    rk_aiq_user_api2_agic_v2_SetAttrib.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_agic.h: 32
if _libs["rkaiq"].has("rk_aiq_user_api2_agic_v2_GetAttrib", "cdecl"):
    rk_aiq_user_api2_agic_v2_GetAttrib = _libs["rkaiq"].get("rk_aiq_user_api2_agic_v2_GetAttrib", "cdecl")
    rk_aiq_user_api2_agic_v2_GetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rkaiq_gic_v2_api_attr_t)]
    rk_aiq_user_api2_agic_v2_GetAttrib.restype = XCamReturn

# /root/camera_engine_rkaiq/include/iq_parser_v2/aie_uapi_head.h: 30
class struct_aie_attrib_s(Structure):
    pass

struct_aie_attrib_s.__slots__ = [
    'sync',
    'mode',
]
struct_aie_attrib_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('mode', rk_aiq_ie_effect_t),
]

aie_attrib_t = struct_aie_attrib_s# /root/camera_engine_rkaiq/include/iq_parser_v2/aie_uapi_head.h: 30

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_aie.h: 31
if _libs["rkaiq"].has("rk_aiq_user_api2_aie_SetAttrib", "cdecl"):
    rk_aiq_user_api2_aie_SetAttrib = _libs["rkaiq"].get("rk_aiq_user_api2_aie_SetAttrib", "cdecl")
    rk_aiq_user_api2_aie_SetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), aie_attrib_t]
    rk_aiq_user_api2_aie_SetAttrib.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_aie.h: 33
if _libs["rkaiq"].has("rk_aiq_user_api2_aie_GetAttrib", "cdecl"):
    rk_aiq_user_api2_aie_GetAttrib = _libs["rkaiq"].get("rk_aiq_user_api2_aie_GetAttrib", "cdecl")
    rk_aiq_user_api2_aie_GetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(aie_attrib_t)]
    rk_aiq_user_api2_aie_GetAttrib.restype = XCamReturn

# /root/camera_engine_rkaiq/include/algos/aldch/rk_aiq_types_aldch_algo_int.h: 12
class struct_rk_aiq_ldch_cfg_s(Structure):
    pass

struct_rk_aiq_ldch_cfg_s.__slots__ = [
    'sync',
    'en',
    'correct_level',
]
struct_rk_aiq_ldch_cfg_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('en', c_uint),
    ('correct_level', c_int),
]

rk_aiq_ldch_cfg_t = struct_rk_aiq_ldch_cfg_s# /root/camera_engine_rkaiq/include/algos/aldch/rk_aiq_types_aldch_algo_int.h: 12

rk_aiq_ldch_attrib_t = rk_aiq_ldch_cfg_t# /root/camera_engine_rkaiq/include/algos/aldch/rk_aiq_uapi_aldch_int.h: 8

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_aldch.h: 26
if _libs["rkaiq"].has("rk_aiq_user_api2_aldch_SetAttrib", "cdecl"):
    rk_aiq_user_api2_aldch_SetAttrib = _libs["rkaiq"].get("rk_aiq_user_api2_aldch_SetAttrib", "cdecl")
    rk_aiq_user_api2_aldch_SetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), rk_aiq_ldch_attrib_t]
    rk_aiq_user_api2_aldch_SetAttrib.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_aldch.h: 28
if _libs["rkaiq"].has("rk_aiq_user_api2_aldch_GetAttrib", "cdecl"):
    rk_aiq_user_api2_aldch_GetAttrib = _libs["rkaiq"].get("rk_aiq_user_api2_aldch_GetAttrib", "cdecl")
    rk_aiq_user_api2_aldch_GetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_ldch_attrib_t)]
    rk_aiq_user_api2_aldch_GetAttrib.restype = XCamReturn

# /root/camera_engine_rkaiq/include/iq_parser_v2/alsc_uapi_head.h: 36
class struct_rk_aiq_lsc_table_s(Structure):
    pass

struct_rk_aiq_lsc_table_s.__slots__ = [
    'lsc_sect_size_x',
    'lsc_sect_size_y',
    'r_data_tbl',
    'gr_data_tbl',
    'gb_data_tbl',
    'b_data_tbl',
]
struct_rk_aiq_lsc_table_s._fields_ = [
    ('lsc_sect_size_x', uint16_t * int(8)),
    ('lsc_sect_size_y', uint16_t * int(8)),
    ('r_data_tbl', c_ushort * int(289)),
    ('gr_data_tbl', c_ushort * int(289)),
    ('gb_data_tbl', c_ushort * int(289)),
    ('b_data_tbl', c_ushort * int(289)),
]

rk_aiq_lsc_table_t = struct_rk_aiq_lsc_table_s# /root/camera_engine_rkaiq/include/iq_parser_v2/alsc_uapi_head.h: 36

# /root/camera_engine_rkaiq/include/algos/alsc/rk_aiq_types_alsc_common.h: 20
class struct_lsc_name_s(Structure):
    pass

struct_lsc_name_s.__slots__ = [
    'name',
]
struct_lsc_name_s._fields_ = [
    ('name', c_char * int(32)),
]

lsc_name_t = struct_lsc_name_s# /root/camera_engine_rkaiq/include/algos/alsc/rk_aiq_types_alsc_common.h: 20

# /root/camera_engine_rkaiq/include/algos/alsc/rk_aiq_types_alsc_common.h: 40
class struct_CalibDbV2_LscTableProfile_s(Structure):
    pass

struct_CalibDbV2_LscTableProfile_s.__slots__ = [
    'name',
    'resolution',
    'illumination',
    'vignetting',
    'lsc_samples_red',
    'lsc_samples_greenR',
    'lsc_samples_greenB',
    'lsc_samples_blue',
]
struct_CalibDbV2_LscTableProfile_s._fields_ = [
    ('name', c_char * int(32)),
    ('resolution', c_char * int(32)),
    ('illumination', c_char * int(32)),
    ('vignetting', c_float),
    ('lsc_samples_red', Cam17x17UShortMatrix_t),
    ('lsc_samples_greenR', Cam17x17UShortMatrix_t),
    ('lsc_samples_greenB', Cam17x17UShortMatrix_t),
    ('lsc_samples_blue', Cam17x17UShortMatrix_t),
]

CalibDbV2_LscTableProfile_t = struct_CalibDbV2_LscTableProfile_s# /root/camera_engine_rkaiq/include/algos/alsc/rk_aiq_types_alsc_common.h: 40

rk_aiq_lsc_mlsc_attrib_t = struct_rk_aiq_lsc_table_s# /root/camera_engine_rkaiq/include/algos/alsc/rk_aiq_types_alsc_algo_int.h: 61

enum_rk_aiq_lsc_op_mode_s = c_int# /root/camera_engine_rkaiq/include/algos/alsc/rk_aiq_types_alsc_algo_int.h: 68

rk_aiq_lsc_op_mode_t = enum_rk_aiq_lsc_op_mode_s# /root/camera_engine_rkaiq/include/algos/alsc/rk_aiq_types_alsc_algo_int.h: 68

# /root/camera_engine_rkaiq/include/algos/alsc/rk_aiq_types_alsc_algo_int.h: 74
class struct_Lsc_v2_Resolution_s(Structure):
    pass

struct_Lsc_v2_Resolution_s.__slots__ = [
    'name',
    'lsc_sect_size_x',
    'lsc_sect_size_y',
]
struct_Lsc_v2_Resolution_s._fields_ = [
    ('name', c_char * int(32)),
    ('lsc_sect_size_x', uint16_t * int(16)),
    ('lsc_sect_size_y', uint16_t * int(16)),
]

Lsc_v2_Resolution_t = struct_Lsc_v2_Resolution_s# /root/camera_engine_rkaiq/include/algos/alsc/rk_aiq_types_alsc_algo_int.h: 74

# /root/camera_engine_rkaiq/include/algos/alsc/rk_aiq_types_alsc_algo_int.h: 80
class struct_CalibDbV2_Lsc_Common_fixed_s(Structure):
    pass

struct_CalibDbV2_Lsc_Common_fixed_s.__slots__ = [
    'enable',
    'resolutionAll',
    'resolutionAll_len',
]
struct_CalibDbV2_Lsc_Common_fixed_s._fields_ = [
    ('enable', c_bool),
    ('resolutionAll', Lsc_v2_Resolution_t * int(2)),
    ('resolutionAll_len', c_int),
]

CalibDbV2_Lsc_Common_fixed_t = struct_CalibDbV2_Lsc_Common_fixed_s# /root/camera_engine_rkaiq/include/algos/alsc/rk_aiq_types_alsc_algo_int.h: 80

# /root/camera_engine_rkaiq/include/algos/alsc/rk_aiq_types_alsc_algo_int.h: 92
class struct_CalibDbV2_AlscCof_ill_fixed_s(Structure):
    pass

struct_CalibDbV2_AlscCof_ill_fixed_s.__slots__ = [
    'usedForCase',
    'name',
    'wbGain',
    'tableUsed',
    'tableUsed_len',
    'gains',
    'gains_len',
    'vig',
    'vig_len',
]
struct_CalibDbV2_AlscCof_ill_fixed_s._fields_ = [
    ('usedForCase', uint32_t),
    ('name', c_char * int(32)),
    ('wbGain', c_float * int(2)),
    ('tableUsed', lsc_name_t * int((7 * 2))),
    ('tableUsed_len', c_int),
    ('gains', c_float * int(100)),
    ('gains_len', c_int),
    ('vig', c_float * int(100)),
    ('vig_len', c_int),
]

CalibDbV2_AlscCof_ill_fixed_t = struct_CalibDbV2_AlscCof_ill_fixed_s# /root/camera_engine_rkaiq/include/algos/alsc/rk_aiq_types_alsc_algo_int.h: 92

# /root/camera_engine_rkaiq/include/algos/alsc/rk_aiq_types_alsc_algo_int.h: 98
class struct_CalibDbV2_AlscCof_fixed_s(Structure):
    pass

struct_CalibDbV2_AlscCof_fixed_s.__slots__ = [
    'damp_enable',
    'illAll',
    'illAll_len',
]
struct_CalibDbV2_AlscCof_fixed_s._fields_ = [
    ('damp_enable', c_bool),
    ('illAll', CalibDbV2_AlscCof_ill_fixed_t * int(7)),
    ('illAll_len', c_int),
]

CalibDbV2_AlscCof_fixed_t = struct_CalibDbV2_AlscCof_fixed_s# /root/camera_engine_rkaiq/include/algos/alsc/rk_aiq_types_alsc_algo_int.h: 98

# /root/camera_engine_rkaiq/include/algos/alsc/rk_aiq_types_alsc_algo_int.h: 103
class struct_CalibDbV2_LscTable_fixed_s(Structure):
    pass

struct_CalibDbV2_LscTable_fixed_s.__slots__ = [
    'tableAll',
    'tableAll_len',
]
struct_CalibDbV2_LscTable_fixed_s._fields_ = [
    ('tableAll', CalibDbV2_LscTableProfile_t * int((7 * 2))),
    ('tableAll_len', c_int),
]

CalibDbV2_LscTable_fixed_t = struct_CalibDbV2_LscTable_fixed_s# /root/camera_engine_rkaiq/include/algos/alsc/rk_aiq_types_alsc_algo_int.h: 103

# /root/camera_engine_rkaiq/include/algos/alsc/rk_aiq_types_alsc_algo_int.h: 109
class struct_rk_aiq_lsc_alsc_attrib_s(Structure):
    pass

struct_rk_aiq_lsc_alsc_attrib_s.__slots__ = [
    'common',
    'alscCoef',
    'tbl',
]
struct_rk_aiq_lsc_alsc_attrib_s._fields_ = [
    ('common', CalibDbV2_Lsc_Common_fixed_t),
    ('alscCoef', CalibDbV2_AlscCof_fixed_t),
    ('tbl', CalibDbV2_LscTable_fixed_t),
]

rk_aiq_lsc_alsc_attrib_t = struct_rk_aiq_lsc_alsc_attrib_s# /root/camera_engine_rkaiq/include/algos/alsc/rk_aiq_types_alsc_algo_int.h: 109

# /root/camera_engine_rkaiq/include/algos/alsc/rk_aiq_types_alsc_algo_int.h: 118
class struct_rk_aiq_lsc_attrib_s(Structure):
    pass

struct_rk_aiq_lsc_attrib_s.__slots__ = [
    'byPass',
    'mode',
    'stManual',
    'stAuto',
    'sync',
]
struct_rk_aiq_lsc_attrib_s._fields_ = [
    ('byPass', c_bool),
    ('mode', rk_aiq_lsc_op_mode_t),
    ('stManual', rk_aiq_lsc_mlsc_attrib_t),
    ('stAuto', rk_aiq_lsc_alsc_attrib_t),
    ('sync', rk_aiq_uapi_sync_t),
]

rk_aiq_lsc_attrib_t = struct_rk_aiq_lsc_attrib_s# /root/camera_engine_rkaiq/include/algos/alsc/rk_aiq_types_alsc_algo_int.h: 118

# /root/camera_engine_rkaiq/include/algos/alsc/rk_aiq_types_alsc_algo_int.h: 127
class struct_rk_aiq_lsc_querry_info_s(Structure):
    pass

struct_rk_aiq_lsc_querry_info_s.__slots__ = [
    'lsc_en',
    'r_data_tbl',
    'gr_data_tbl',
    'gb_data_tbl',
    'b_data_tbl',
]
struct_rk_aiq_lsc_querry_info_s._fields_ = [
    ('lsc_en', c_bool),
    ('r_data_tbl', c_ushort * int(289)),
    ('gr_data_tbl', c_ushort * int(289)),
    ('gb_data_tbl', c_ushort * int(289)),
    ('b_data_tbl', c_ushort * int(289)),
]

rk_aiq_lsc_querry_info_t = struct_rk_aiq_lsc_querry_info_s# /root/camera_engine_rkaiq/include/algos/alsc/rk_aiq_types_alsc_algo_int.h: 127

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_alsc.h: 30
if _libs["rkaiq"].has("rk_aiq_user_api2_alsc_SetAttrib", "cdecl"):
    rk_aiq_user_api2_alsc_SetAttrib = _libs["rkaiq"].get("rk_aiq_user_api2_alsc_SetAttrib", "cdecl")
    rk_aiq_user_api2_alsc_SetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), rk_aiq_lsc_attrib_t]
    rk_aiq_user_api2_alsc_SetAttrib.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_alsc.h: 32
if _libs["rkaiq"].has("rk_aiq_user_api2_alsc_GetAttrib", "cdecl"):
    rk_aiq_user_api2_alsc_GetAttrib = _libs["rkaiq"].get("rk_aiq_user_api2_alsc_GetAttrib", "cdecl")
    rk_aiq_user_api2_alsc_GetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_lsc_attrib_t)]
    rk_aiq_user_api2_alsc_GetAttrib.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_alsc.h: 35
if _libs["rkaiq"].has("rk_aiq_user_api2_alsc_QueryLscInfo", "cdecl"):
    rk_aiq_user_api2_alsc_QueryLscInfo = _libs["rkaiq"].get("rk_aiq_user_api2_alsc_QueryLscInfo", "cdecl")
    rk_aiq_user_api2_alsc_QueryLscInfo.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_lsc_querry_info_t)]
    rk_aiq_user_api2_alsc_QueryLscInfo.restype = XCamReturn

amerge_attrib_t = mergeAttr_t# /root/camera_engine_rkaiq/include/algos/amerge/rk_aiq_uapi_amerge_int.h: 13

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_amerge.h: 31
if _libs["rkaiq"].has("rk_aiq_user_api2_amerge_SetAttrib", "cdecl"):
    rk_aiq_user_api2_amerge_SetAttrib = _libs["rkaiq"].get("rk_aiq_user_api2_amerge_SetAttrib", "cdecl")
    rk_aiq_user_api2_amerge_SetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), amerge_attrib_t]
    rk_aiq_user_api2_amerge_SetAttrib.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_amerge.h: 33
if _libs["rkaiq"].has("rk_aiq_user_api2_amerge_GetAttrib", "cdecl"):
    rk_aiq_user_api2_amerge_GetAttrib = _libs["rkaiq"].get("rk_aiq_user_api2_amerge_GetAttrib", "cdecl")
    rk_aiq_user_api2_amerge_GetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(amerge_attrib_t)]
    rk_aiq_user_api2_amerge_GetAttrib.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_anr.h: 35
if _libs["rkaiq"].has("rk_aiq_user_api2_anr_SetAttrib", "cdecl"):
    rk_aiq_user_api2_anr_SetAttrib = _libs["rkaiq"].get("rk_aiq_user_api2_anr_SetAttrib", "cdecl")
    rk_aiq_user_api2_anr_SetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_nr_attrib_t)]
    rk_aiq_user_api2_anr_SetAttrib.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_anr.h: 37
if _libs["rkaiq"].has("rk_aiq_user_api2_anr_GetAttrib", "cdecl"):
    rk_aiq_user_api2_anr_GetAttrib = _libs["rkaiq"].get("rk_aiq_user_api2_anr_GetAttrib", "cdecl")
    rk_aiq_user_api2_anr_GetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_nr_attrib_t)]
    rk_aiq_user_api2_anr_GetAttrib.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_anr.h: 39
if _libs["rkaiq"].has("rk_aiq_user_api2_anr_SetIQPara", "cdecl"):
    rk_aiq_user_api2_anr_SetIQPara = _libs["rkaiq"].get("rk_aiq_user_api2_anr_SetIQPara", "cdecl")
    rk_aiq_user_api2_anr_SetIQPara.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_nr_IQPara_t)]
    rk_aiq_user_api2_anr_SetIQPara.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_anr.h: 41
if _libs["rkaiq"].has("rk_aiq_user_api2_anr_GetIQPara", "cdecl"):
    rk_aiq_user_api2_anr_GetIQPara = _libs["rkaiq"].get("rk_aiq_user_api2_anr_GetIQPara", "cdecl")
    rk_aiq_user_api2_anr_GetIQPara.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_nr_IQPara_t)]
    rk_aiq_user_api2_anr_GetIQPara.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_anr.h: 43
if _libs["rkaiq"].has("rk_aiq_user_api2_anr_SetLumaSFStrength", "cdecl"):
    rk_aiq_user_api2_anr_SetLumaSFStrength = _libs["rkaiq"].get("rk_aiq_user_api2_anr_SetLumaSFStrength", "cdecl")
    rk_aiq_user_api2_anr_SetLumaSFStrength.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_float]
    rk_aiq_user_api2_anr_SetLumaSFStrength.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_anr.h: 45
if _libs["rkaiq"].has("rk_aiq_user_api2_anr_SetLumaTFStrength", "cdecl"):
    rk_aiq_user_api2_anr_SetLumaTFStrength = _libs["rkaiq"].get("rk_aiq_user_api2_anr_SetLumaTFStrength", "cdecl")
    rk_aiq_user_api2_anr_SetLumaTFStrength.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_float]
    rk_aiq_user_api2_anr_SetLumaTFStrength.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_anr.h: 47
if _libs["rkaiq"].has("rk_aiq_user_api2_anr_GetLumaSFStrength", "cdecl"):
    rk_aiq_user_api2_anr_GetLumaSFStrength = _libs["rkaiq"].get("rk_aiq_user_api2_anr_GetLumaSFStrength", "cdecl")
    rk_aiq_user_api2_anr_GetLumaSFStrength.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(c_float)]
    rk_aiq_user_api2_anr_GetLumaSFStrength.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_anr.h: 49
if _libs["rkaiq"].has("rk_aiq_user_api2_anr_GetLumaTFStrength", "cdecl"):
    rk_aiq_user_api2_anr_GetLumaTFStrength = _libs["rkaiq"].get("rk_aiq_user_api2_anr_GetLumaTFStrength", "cdecl")
    rk_aiq_user_api2_anr_GetLumaTFStrength.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(c_float)]
    rk_aiq_user_api2_anr_GetLumaTFStrength.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_anr.h: 51
if _libs["rkaiq"].has("rk_aiq_user_api2_anr_SetChromaSFStrength", "cdecl"):
    rk_aiq_user_api2_anr_SetChromaSFStrength = _libs["rkaiq"].get("rk_aiq_user_api2_anr_SetChromaSFStrength", "cdecl")
    rk_aiq_user_api2_anr_SetChromaSFStrength.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_float]
    rk_aiq_user_api2_anr_SetChromaSFStrength.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_anr.h: 53
if _libs["rkaiq"].has("rk_aiq_user_api2_anr_SetChromaTFStrength", "cdecl"):
    rk_aiq_user_api2_anr_SetChromaTFStrength = _libs["rkaiq"].get("rk_aiq_user_api2_anr_SetChromaTFStrength", "cdecl")
    rk_aiq_user_api2_anr_SetChromaTFStrength.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_float]
    rk_aiq_user_api2_anr_SetChromaTFStrength.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_anr.h: 55
if _libs["rkaiq"].has("rk_aiq_user_api2_anr_GetChromaSFStrength", "cdecl"):
    rk_aiq_user_api2_anr_GetChromaSFStrength = _libs["rkaiq"].get("rk_aiq_user_api2_anr_GetChromaSFStrength", "cdecl")
    rk_aiq_user_api2_anr_GetChromaSFStrength.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(c_float)]
    rk_aiq_user_api2_anr_GetChromaSFStrength.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_anr.h: 57
if _libs["rkaiq"].has("rk_aiq_user_api2_anr_GetChromaTFStrength", "cdecl"):
    rk_aiq_user_api2_anr_GetChromaTFStrength = _libs["rkaiq"].get("rk_aiq_user_api2_anr_GetChromaTFStrength", "cdecl")
    rk_aiq_user_api2_anr_GetChromaTFStrength.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(c_float)]
    rk_aiq_user_api2_anr_GetChromaTFStrength.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_anr.h: 59
if _libs["rkaiq"].has("rk_aiq_user_api2_anr_SetRawnrSFStrength", "cdecl"):
    rk_aiq_user_api2_anr_SetRawnrSFStrength = _libs["rkaiq"].get("rk_aiq_user_api2_anr_SetRawnrSFStrength", "cdecl")
    rk_aiq_user_api2_anr_SetRawnrSFStrength.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_float]
    rk_aiq_user_api2_anr_SetRawnrSFStrength.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_anr.h: 61
if _libs["rkaiq"].has("rk_aiq_user_api2_anr_GetRawnrSFStrength", "cdecl"):
    rk_aiq_user_api2_anr_GetRawnrSFStrength = _libs["rkaiq"].get("rk_aiq_user_api2_anr_GetRawnrSFStrength", "cdecl")
    rk_aiq_user_api2_anr_GetRawnrSFStrength.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(c_float)]
    rk_aiq_user_api2_anr_GetRawnrSFStrength.restype = XCamReturn

enum_Asharp3_OPMode_e = c_int# /root/camera_engine_rkaiq/include/algos/asharp3/rk_aiq_types_asharp_algo_int_v3.h: 84

Asharp3_OPMode_t = enum_Asharp3_OPMode_e# /root/camera_engine_rkaiq/include/algos/asharp3/rk_aiq_types_asharp_algo_int_v3.h: 84

# /root/camera_engine_rkaiq/include/algos/asharp3/rk_aiq_types_asharp_algo_int_v3.h: 146
class struct_RK_SHARP_Params_V3_s(Structure):
    pass

struct_RK_SHARP_Params_V3_s.__slots__ = [
    'enable',
    'iso',
    'luma_point',
    'luma_sigma',
    'pbf_gain',
    'pbf_add',
    'pbf_ratio',
    'gaus_ratio',
    'sharp_ratio',
    'lum_clip_h',
    'bf_gain',
    'bf_add',
    'bf_ratio',
    'ehf_th',
    'kernel_pre_bila_filter',
    'kernel_range_filter',
    'kernel_bila_filter',
    'sharp_ratio_h',
    'sharp_ratio_m',
    'sharp_ratio_l',
    'clip_hf',
    'clip_mf',
    'clip_lf',
    'local_wgt',
    'kernel_hf_filter',
    'kernel_mf_filter',
    'kernel_lf_filter',
]
struct_RK_SHARP_Params_V3_s._fields_ = [
    ('enable', c_int),
    ('iso', c_int * int(13)),
    ('luma_point', c_short * int(8)),
    ('luma_sigma', (c_short * int(8)) * int(13)),
    ('pbf_gain', c_float * int(13)),
    ('pbf_add', c_float * int(13)),
    ('pbf_ratio', c_float * int(13)),
    ('gaus_ratio', c_float * int(13)),
    ('sharp_ratio', c_float * int(13)),
    ('lum_clip_h', (c_short * int(8)) * int(13)),
    ('bf_gain', c_float * int(13)),
    ('bf_add', c_float * int(13)),
    ('bf_ratio', c_float * int(13)),
    ('ehf_th', (c_short * int(8)) * int(13)),
    ('kernel_pre_bila_filter', (c_float * int((3 * 3))) * int(13)),
    ('kernel_range_filter', (c_float * int((3 * 3))) * int(13)),
    ('kernel_bila_filter', (c_float * int((3 * 3))) * int(13)),
    ('sharp_ratio_h', c_float * int(13)),
    ('sharp_ratio_m', c_float * int(13)),
    ('sharp_ratio_l', c_float * int(13)),
    ('clip_hf', (c_short * int(8)) * int(13)),
    ('clip_mf', (c_short * int(8)) * int(13)),
    ('clip_lf', (c_short * int(8)) * int(13)),
    ('local_wgt', (c_short * int(8)) * int(13)),
    ('kernel_hf_filter', (c_short * int((3 * 3))) * int(13)),
    ('kernel_mf_filter', (c_short * int((5 * 5))) * int(13)),
    ('kernel_lf_filter', (c_short * int((9 * 9))) * int(13)),
]

RK_SHARP_Params_V3_t = struct_RK_SHARP_Params_V3_s# /root/camera_engine_rkaiq/include/algos/asharp3/rk_aiq_types_asharp_algo_int_v3.h: 146

# /root/camera_engine_rkaiq/include/algos/asharp3/rk_aiq_types_asharp_algo_int_v3.h: 185
class struct_RK_SHARP_Params_V3_Select_s(Structure):
    pass

struct_RK_SHARP_Params_V3_Select_s.__slots__ = [
    'enable',
    'luma_point',
    'luma_sigma',
    'pbf_gain',
    'pbf_add',
    'pbf_ratio',
    'gaus_ratio',
    'sharp_ratio',
    'lum_clip_h',
    'bf_gain',
    'bf_add',
    'bf_ratio',
    'ehf_th',
    'kernel_pre_bila_filter',
    'kernel_range_filter',
    'kernel_bila_filter',
    'sharp_ratio_h',
    'sharp_ratio_m',
    'sharp_ratio_l',
    'clip_hf',
    'clip_mf',
    'clip_lf',
    'local_wgt',
    'kernel_hf_filter',
    'kernel_mf_filter',
    'kernel_lf_filter',
]
struct_RK_SHARP_Params_V3_Select_s._fields_ = [
    ('enable', c_int),
    ('luma_point', c_short * int(8)),
    ('luma_sigma', c_short * int(8)),
    ('pbf_gain', c_float),
    ('pbf_add', c_float),
    ('pbf_ratio', c_float),
    ('gaus_ratio', c_float),
    ('sharp_ratio', c_float),
    ('lum_clip_h', c_short * int(8)),
    ('bf_gain', c_float),
    ('bf_add', c_float),
    ('bf_ratio', c_float),
    ('ehf_th', c_short * int(8)),
    ('kernel_pre_bila_filter', c_float * int((3 * 3))),
    ('kernel_range_filter', c_float * int((3 * 3))),
    ('kernel_bila_filter', c_float * int((3 * 3))),
    ('sharp_ratio_h', c_float),
    ('sharp_ratio_m', c_float),
    ('sharp_ratio_l', c_float),
    ('clip_hf', c_short * int(8)),
    ('clip_mf', c_short * int(8)),
    ('clip_lf', c_short * int(8)),
    ('local_wgt', c_short * int(8)),
    ('kernel_hf_filter', c_short * int((3 * 3))),
    ('kernel_mf_filter', c_short * int((5 * 5))),
    ('kernel_lf_filter', c_short * int((9 * 9))),
]

RK_SHARP_Params_V3_Select_t = struct_RK_SHARP_Params_V3_Select_s# /root/camera_engine_rkaiq/include/algos/asharp3/rk_aiq_types_asharp_algo_int_v3.h: 185

# /root/camera_engine_rkaiq/include/algos/asharp3/rk_aiq_types_asharp_algo_int_v3.h: 192
class struct_Asharp_Manual_Attr_V3_s(Structure):
    pass

struct_Asharp_Manual_Attr_V3_s.__slots__ = [
    'stSelect',
]
struct_Asharp_Manual_Attr_V3_s._fields_ = [
    ('stSelect', RK_SHARP_Params_V3_Select_t),
]

Asharp_Manual_Attr_V3_t = struct_Asharp_Manual_Attr_V3_s# /root/camera_engine_rkaiq/include/algos/asharp3/rk_aiq_types_asharp_algo_int_v3.h: 192

# /root/camera_engine_rkaiq/include/algos/asharp3/rk_aiq_types_asharp_algo_int_v3.h: 201
class struct_Asharp_Auto_Attr_V3_s(Structure):
    pass

struct_Asharp_Auto_Attr_V3_s.__slots__ = [
    'stParams',
    'stSelect',
]
struct_Asharp_Auto_Attr_V3_s._fields_ = [
    ('stParams', RK_SHARP_Params_V3_t),
    ('stSelect', RK_SHARP_Params_V3_Select_t),
]

Asharp_Auto_Attr_V3_t = struct_Asharp_Auto_Attr_V3_s# /root/camera_engine_rkaiq/include/algos/asharp3/rk_aiq_types_asharp_algo_int_v3.h: 201

# /root/camera_engine_rkaiq/include/algos/asharp3/rk_aiq_types_asharp_algo_int_v3.h: 229
class struct_rk_aiq_sharp_attrib_v3_s(Structure):
    pass

struct_rk_aiq_sharp_attrib_v3_s.__slots__ = [
    'eMode',
    'stAuto',
    'stManual',
]
struct_rk_aiq_sharp_attrib_v3_s._fields_ = [
    ('eMode', Asharp3_OPMode_t),
    ('stAuto', Asharp_Auto_Attr_V3_t),
    ('stManual', Asharp_Manual_Attr_V3_t),
]

rk_aiq_sharp_attrib_v3_t = struct_rk_aiq_sharp_attrib_v3_s# /root/camera_engine_rkaiq/include/algos/asharp3/rk_aiq_types_asharp_algo_int_v3.h: 229

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_asharp_v3.h: 31
if _libs["rkaiq"].has("rk_aiq_user_api2_asharpV3_SetAttrib", "cdecl"):
    rk_aiq_user_api2_asharpV3_SetAttrib = _libs["rkaiq"].get("rk_aiq_user_api2_asharpV3_SetAttrib", "cdecl")
    rk_aiq_user_api2_asharpV3_SetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_sharp_attrib_v3_t)]
    rk_aiq_user_api2_asharpV3_SetAttrib.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_asharp_v3.h: 34
if _libs["rkaiq"].has("rk_aiq_user_api2_asharpV3_GetAttrib", "cdecl"):
    rk_aiq_user_api2_asharpV3_GetAttrib = _libs["rkaiq"].get("rk_aiq_user_api2_asharpV3_GetAttrib", "cdecl")
    rk_aiq_user_api2_asharpV3_GetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_sharp_attrib_v3_t)]
    rk_aiq_user_api2_asharpV3_GetAttrib.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_asharp_v3.h: 37
if _libs["rkaiq"].has("rk_aiq_user_api2_asharpV3_SetStrength", "cdecl"):
    rk_aiq_user_api2_asharpV3_SetStrength = _libs["rkaiq"].get("rk_aiq_user_api2_asharpV3_SetStrength", "cdecl")
    rk_aiq_user_api2_asharpV3_SetStrength.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_float]
    rk_aiq_user_api2_asharpV3_SetStrength.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_asharp_v3.h: 40
if _libs["rkaiq"].has("rk_aiq_user_api2_asharpV3_GetStrength", "cdecl"):
    rk_aiq_user_api2_asharpV3_GetStrength = _libs["rkaiq"].get("rk_aiq_user_api2_asharpV3_GetStrength", "cdecl")
    rk_aiq_user_api2_asharpV3_GetStrength.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(c_float)]
    rk_aiq_user_api2_asharpV3_GetStrength.restype = XCamReturn

# /root/camera_engine_rkaiq/include/iq_parser_v2/sharp_uapi_head_v4.h: 101
class struct_RK_SHARP_Params_V4_Select_s(Structure):
    pass

struct_RK_SHARP_Params_V4_Select_s.__slots__ = [
    'enable',
    'luma_point',
    'luma_sigma',
    'pbf_gain',
    'pbf_add',
    'pbf_ratio',
    'gaus_ratio',
    'sharp_ratio',
    'bf_gain',
    'bf_add',
    'bf_ratio',
    'hf_clip',
    'local_sharp_strength',
    'kernel_sigma_enable',
    'prefilter_sigma',
    'hfBilateralFilter_sigma',
    'GaussianFilter_sigma',
    'GaussianFilter_radius',
    'prefilter_coeff',
    'GaussianFilter_coeff',
    'hfBilateralFilter_coeff',
]
struct_RK_SHARP_Params_V4_Select_s._fields_ = [
    ('enable', c_int),
    ('luma_point', c_int16 * int(8)),
    ('luma_sigma', c_int16 * int(8)),
    ('pbf_gain', c_float),
    ('pbf_add', c_float),
    ('pbf_ratio', c_float),
    ('gaus_ratio', c_float),
    ('sharp_ratio', c_float),
    ('bf_gain', c_float),
    ('bf_add', c_float),
    ('bf_ratio', c_float),
    ('hf_clip', c_int16 * int(8)),
    ('local_sharp_strength', c_int16 * int(8)),
    ('kernel_sigma_enable', c_int),
    ('prefilter_sigma', c_float),
    ('hfBilateralFilter_sigma', c_float),
    ('GaussianFilter_sigma', c_float),
    ('GaussianFilter_radius', c_float),
    ('prefilter_coeff', c_float * int(3)),
    ('GaussianFilter_coeff', c_float * int(6)),
    ('hfBilateralFilter_coeff', c_float * int(3)),
]

RK_SHARP_Params_V4_Select_t = struct_RK_SHARP_Params_V4_Select_s# /root/camera_engine_rkaiq/include/iq_parser_v2/sharp_uapi_head_v4.h: 101

# /root/camera_engine_rkaiq/include/iq_parser_v2/sharp_uapi_head_v4.h: 130
class struct_Asharp4_ExpInfo_s(Structure):
    pass

struct_Asharp4_ExpInfo_s.__slots__ = [
    'hdr_mode',
    'snr_mode',
    'arTime',
    'arAGain',
    'arDGain',
    'arIso',
    'isoLow',
    'isoHigh',
    'rawWidth',
    'rawHeight',
]
struct_Asharp4_ExpInfo_s._fields_ = [
    ('hdr_mode', c_int),
    ('snr_mode', c_int),
    ('arTime', c_float * int(3)),
    ('arAGain', c_float * int(3)),
    ('arDGain', c_float * int(3)),
    ('arIso', c_int * int(3)),
    ('isoLow', c_int),
    ('isoHigh', c_int),
    ('rawWidth', c_int),
    ('rawHeight', c_int),
]

Asharp4_ExpInfo_t = struct_Asharp4_ExpInfo_s# /root/camera_engine_rkaiq/include/iq_parser_v2/sharp_uapi_head_v4.h: 130

# /root/camera_engine_rkaiq/include/iq_parser_v2/sharp_uapi_head_v4.h: 139
class struct_rk_aiq_sharp_info_v4_s(Structure):
    pass

struct_rk_aiq_sharp_info_v4_s.__slots__ = [
    'sync',
    'iso',
    'expo_info',
]
struct_rk_aiq_sharp_info_v4_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('iso', c_int),
    ('expo_info', Asharp4_ExpInfo_t),
]

rk_aiq_sharp_info_v4_t = struct_rk_aiq_sharp_info_v4_s# /root/camera_engine_rkaiq/include/iq_parser_v2/sharp_uapi_head_v4.h: 139

enum_Asharp4_OPMode_e = c_int# /root/camera_engine_rkaiq/include/algos/asharp4/rk_aiq_types_asharp_algo_int_v4.h: 87

Asharp4_OPMode_t = enum_Asharp4_OPMode_e# /root/camera_engine_rkaiq/include/algos/asharp4/rk_aiq_types_asharp_algo_int_v4.h: 87

# /root/camera_engine_rkaiq/include/algos/asharp4/rk_aiq_types_asharp_algo_int_v4.h: 130
class struct_RK_SHARP_Params_V4_s(Structure):
    pass

struct_RK_SHARP_Params_V4_s.__slots__ = [
    'enable',
    'kernel_sigma_enable',
    'iso',
    'luma_point',
    'luma_sigma',
    'pbf_gain',
    'pbf_add',
    'pbf_ratio',
    'gaus_ratio',
    'sharp_ratio',
    'hf_clip',
    'bf_gain',
    'bf_add',
    'bf_ratio',
    'local_sharp_strength',
    'prefilter_coeff',
    'GaussianFilter_coeff',
    'hfBilateralFilter_coeff',
    'prefilter_sigma',
    'GaussianFilter_sigma',
    'GaussianFilter_radius',
    'hfBilateralFilter_sigma',
]
struct_RK_SHARP_Params_V4_s._fields_ = [
    ('enable', c_int),
    ('kernel_sigma_enable', c_int),
    ('iso', c_int * int(13)),
    ('luma_point', c_short * int(8)),
    ('luma_sigma', (c_short * int(8)) * int(13)),
    ('pbf_gain', c_float * int(13)),
    ('pbf_add', c_float * int(13)),
    ('pbf_ratio', c_float * int(13)),
    ('gaus_ratio', c_float * int(13)),
    ('sharp_ratio', c_float * int(13)),
    ('hf_clip', (c_short * int(8)) * int(13)),
    ('bf_gain', c_float * int(13)),
    ('bf_add', c_float * int(13)),
    ('bf_ratio', c_float * int(13)),
    ('local_sharp_strength', (c_short * int(8)) * int(13)),
    ('prefilter_coeff', (c_float * int(3)) * int(13)),
    ('GaussianFilter_coeff', (c_float * int(6)) * int(13)),
    ('hfBilateralFilter_coeff', (c_float * int(3)) * int(13)),
    ('prefilter_sigma', c_float * int(13)),
    ('GaussianFilter_sigma', c_float * int(13)),
    ('GaussianFilter_radius', c_float * int(13)),
    ('hfBilateralFilter_sigma', c_float * int(13)),
]

RK_SHARP_Params_V4_t = struct_RK_SHARP_Params_V4_s# /root/camera_engine_rkaiq/include/algos/asharp4/rk_aiq_types_asharp_algo_int_v4.h: 130

# /root/camera_engine_rkaiq/include/algos/asharp4/rk_aiq_types_asharp_algo_int_v4.h: 169
class struct_Asharp_Manual_Attr_V4_s(Structure):
    pass

struct_Asharp_Manual_Attr_V4_s.__slots__ = [
    'stSelect',
    'stFix',
]
struct_Asharp_Manual_Attr_V4_s._fields_ = [
    ('stSelect', RK_SHARP_Params_V4_Select_t),
    ('stFix', RK_SHARP_Fix_V4_t),
]

Asharp_Manual_Attr_V4_t = struct_Asharp_Manual_Attr_V4_s# /root/camera_engine_rkaiq/include/algos/asharp4/rk_aiq_types_asharp_algo_int_v4.h: 169

# /root/camera_engine_rkaiq/include/algos/asharp4/rk_aiq_types_asharp_algo_int_v4.h: 178
class struct_Asharp_Auto_Attr_V4_s(Structure):
    pass

struct_Asharp_Auto_Attr_V4_s.__slots__ = [
    'stParams',
    'stSelect',
]
struct_Asharp_Auto_Attr_V4_s._fields_ = [
    ('stParams', RK_SHARP_Params_V4_t),
    ('stSelect', RK_SHARP_Params_V4_Select_t),
]

Asharp_Auto_Attr_V4_t = struct_Asharp_Auto_Attr_V4_s# /root/camera_engine_rkaiq/include/algos/asharp4/rk_aiq_types_asharp_algo_int_v4.h: 178

# /root/camera_engine_rkaiq/include/algos/asharp4/rk_aiq_types_asharp_algo_int_v4.h: 208
class struct_rk_aiq_sharp_attrib_v4_s(Structure):
    pass

struct_rk_aiq_sharp_attrib_v4_s.__slots__ = [
    'sync',
    'eMode',
    'stAuto',
    'stManual',
]
struct_rk_aiq_sharp_attrib_v4_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('eMode', Asharp4_OPMode_t),
    ('stAuto', Asharp_Auto_Attr_V4_t),
    ('stManual', Asharp_Manual_Attr_V4_t),
]

rk_aiq_sharp_attrib_v4_t = struct_rk_aiq_sharp_attrib_v4_s# /root/camera_engine_rkaiq/include/algos/asharp4/rk_aiq_types_asharp_algo_int_v4.h: 208

# /root/camera_engine_rkaiq/include/algos/asharp4/rk_aiq_types_asharp_algo_int_v4.h: 216
class struct_rk_aiq_sharp_strength_v4_s(Structure):
    pass

struct_rk_aiq_sharp_strength_v4_s.__slots__ = [
    'sync',
    'percent',
    'strength_enable',
]
struct_rk_aiq_sharp_strength_v4_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('percent', c_float),
    ('strength_enable', c_bool),
]

rk_aiq_sharp_strength_v4_t = struct_rk_aiq_sharp_strength_v4_s# /root/camera_engine_rkaiq/include/algos/asharp4/rk_aiq_types_asharp_algo_int_v4.h: 216

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_asharp_v4.h: 31
if _libs["rkaiq"].has("rk_aiq_user_api2_asharpV4_SetAttrib", "cdecl"):
    rk_aiq_user_api2_asharpV4_SetAttrib = _libs["rkaiq"].get("rk_aiq_user_api2_asharpV4_SetAttrib", "cdecl")
    rk_aiq_user_api2_asharpV4_SetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_sharp_attrib_v4_t)]
    rk_aiq_user_api2_asharpV4_SetAttrib.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_asharp_v4.h: 34
if _libs["rkaiq"].has("rk_aiq_user_api2_asharpV4_GetAttrib", "cdecl"):
    rk_aiq_user_api2_asharpV4_GetAttrib = _libs["rkaiq"].get("rk_aiq_user_api2_asharpV4_GetAttrib", "cdecl")
    rk_aiq_user_api2_asharpV4_GetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_sharp_attrib_v4_t)]
    rk_aiq_user_api2_asharpV4_GetAttrib.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_asharp_v4.h: 37
if _libs["rkaiq"].has("rk_aiq_user_api2_asharpV4_SetStrength", "cdecl"):
    rk_aiq_user_api2_asharpV4_SetStrength = _libs["rkaiq"].get("rk_aiq_user_api2_asharpV4_SetStrength", "cdecl")
    rk_aiq_user_api2_asharpV4_SetStrength.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_sharp_strength_v4_t)]
    rk_aiq_user_api2_asharpV4_SetStrength.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_asharp_v4.h: 40
if _libs["rkaiq"].has("rk_aiq_user_api2_asharpV4_GetStrength", "cdecl"):
    rk_aiq_user_api2_asharpV4_GetStrength = _libs["rkaiq"].get("rk_aiq_user_api2_asharpV4_GetStrength", "cdecl")
    rk_aiq_user_api2_asharpV4_GetStrength.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_sharp_strength_v4_t)]
    rk_aiq_user_api2_asharpV4_GetStrength.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_asharp_v4.h: 43
if _libs["rkaiq"].has("rk_aiq_user_api2_asharpV4_GetInfo", "cdecl"):
    rk_aiq_user_api2_asharpV4_GetInfo = _libs["rkaiq"].get("rk_aiq_user_api2_asharpV4_GetInfo", "cdecl")
    rk_aiq_user_api2_asharpV4_GetInfo.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_sharp_info_v4_t)]
    rk_aiq_user_api2_asharpV4_GetInfo.restype = XCamReturn

atmo_attrib_t = tmoAttr_t# /root/camera_engine_rkaiq/include/algos/atmo/rk_aiq_uapi_atmo_int.h: 13

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_atmo.h: 31
if _libs["rkaiq"].has("rk_aiq_user_api2_atmo_SetAttrib", "cdecl"):
    rk_aiq_user_api2_atmo_SetAttrib = _libs["rkaiq"].get("rk_aiq_user_api2_atmo_SetAttrib", "cdecl")
    rk_aiq_user_api2_atmo_SetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), atmo_attrib_t]
    rk_aiq_user_api2_atmo_SetAttrib.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_atmo.h: 33
if _libs["rkaiq"].has("rk_aiq_user_api2_atmo_GetAttrib", "cdecl"):
    rk_aiq_user_api2_atmo_GetAttrib = _libs["rkaiq"].get("rk_aiq_user_api2_atmo_GetAttrib", "cdecl")
    rk_aiq_user_api2_atmo_GetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(atmo_attrib_t)]
    rk_aiq_user_api2_atmo_GetAttrib.restype = XCamReturn

enum_CalibDbV2_Awb_Mul_Win_Mode_e = c_int# /root/camera_engine_rkaiq/include/iq_parser_v2/awb_head.h: 270

CalibDbV2_Awb_Mul_Win_Mode_t = enum_CalibDbV2_Awb_Mul_Win_Mode_e# /root/camera_engine_rkaiq/include/iq_parser_v2/awb_head.h: 270

# /root/camera_engine_rkaiq/include/iq_parser_v2/awb_head.h: 281
class struct_CalibDbV2_Awb_Mul_Win_s(Structure):
    pass

struct_CalibDbV2_Awb_Mul_Win_s.__slots__ = [
    'enable',
    'multiwindowMode',
    'window',
    'weight',
]
struct_CalibDbV2_Awb_Mul_Win_s._fields_ = [
    ('enable', c_bool),
    ('multiwindowMode', CalibDbV2_Awb_Mul_Win_Mode_t),
    ('window', (c_float * int(4)) * int(8)),
    ('weight', c_float),
]

CalibDbV2_Awb_Mul_Win_t = struct_CalibDbV2_Awb_Mul_Win_s# /root/camera_engine_rkaiq/include/iq_parser_v2/awb_head.h: 281

# /root/camera_engine_rkaiq/include/iq_parser_v2/awb_head.h: 440
class struct_CalibDbV2_Awb_gain_offset_cfg_s(Structure):
    pass

struct_CalibDbV2_Awb_gain_offset_cfg_s.__slots__ = [
    'enable',
    'offset',
]
struct_CalibDbV2_Awb_gain_offset_cfg_s._fields_ = [
    ('enable', c_bool),
    ('offset', c_float * int(4)),
]

CalibDbV2_Awb_gain_offset_cfg_t = struct_CalibDbV2_Awb_gain_offset_cfg_s# /root/camera_engine_rkaiq/include/iq_parser_v2/awb_head.h: 440

# /root/camera_engine_rkaiq/include/iq_parser_v2/awb_uapi_head.h: 31
class struct___uapi_wb_mode_t(Structure):
    pass

struct___uapi_wb_mode_t.__slots__ = [
    'mode',
]
struct___uapi_wb_mode_t._fields_ = [
    ('mode', opMode_t),
]

uapi_wb_mode_t = struct___uapi_wb_mode_t# /root/camera_engine_rkaiq/include/iq_parser_v2/awb_uapi_head.h: 31

# /root/camera_engine_rkaiq/include/iq_parser_v2/awb_uapi_head.h: 61
class struct_rk_tool_awb_stat_wp_res_v201_s(Structure):
    pass

struct_rk_tool_awb_stat_wp_res_v201_s.__slots__ = [
    'WpNo',
    'RgainValue',
    'BgainValue',
]
struct_rk_tool_awb_stat_wp_res_v201_s._fields_ = [
    ('WpNo', c_longlong),
    ('RgainValue', c_longlong),
    ('BgainValue', c_longlong),
]

rk_tool_awb_stat_wp_res_v201_t = struct_rk_tool_awb_stat_wp_res_v201_s# /root/camera_engine_rkaiq/include/iq_parser_v2/awb_uapi_head.h: 61

# /root/camera_engine_rkaiq/include/iq_parser_v2/awb_uapi_head.h: 72
class struct_rk_tool_awb_stat_blk_res_v201_s(Structure):
    pass

struct_rk_tool_awb_stat_blk_res_v201_s.__slots__ = [
    'WpNo',
    'Rvalue',
    'Gvalue',
    'Bvalue',
]
struct_rk_tool_awb_stat_blk_res_v201_s._fields_ = [
    ('WpNo', c_longlong),
    ('Rvalue', c_longlong),
    ('Gvalue', c_longlong),
    ('Bvalue', c_longlong),
]

rk_tool_awb_stat_blk_res_v201_t = struct_rk_tool_awb_stat_blk_res_v201_s# /root/camera_engine_rkaiq/include/iq_parser_v2/awb_uapi_head.h: 72

# /root/camera_engine_rkaiq/include/iq_parser_v2/awb_uapi_head.h: 77
class struct_rk_tool_awb_stat_wp_res_light_v201_s(Structure):
    pass

struct_rk_tool_awb_stat_wp_res_light_v201_s.__slots__ = [
    'xYType',
]
struct_rk_tool_awb_stat_wp_res_light_v201_s._fields_ = [
    ('xYType', rk_tool_awb_stat_wp_res_v201_t * int(2)),
]

rk_tool_awb_stat_wp_res_light_v201_t = struct_rk_tool_awb_stat_wp_res_light_v201_s# /root/camera_engine_rkaiq/include/iq_parser_v2/awb_uapi_head.h: 77

# /root/camera_engine_rkaiq/include/iq_parser_v2/awb_uapi_head.h: 92
class struct_rk_tool_awb_stat_res2_v30_s(Structure):
    pass

struct_rk_tool_awb_stat_res2_v30_s.__slots__ = [
    'light',
    'WpNo2',
    'blockResult',
    'multiwindowLightResult',
    'excWpRangeResult',
    'WpNoHist',
]
struct_rk_tool_awb_stat_res2_v30_s._fields_ = [
    ('light', rk_tool_awb_stat_wp_res_light_v201_t * int(7)),
    ('WpNo2', c_int * int(7)),
    ('blockResult', rk_tool_awb_stat_blk_res_v201_t * int(225)),
    ('multiwindowLightResult', rk_tool_awb_stat_wp_res_light_v201_t * int(4)),
    ('excWpRangeResult', rk_tool_awb_stat_wp_res_v201_t * int(4)),
    ('WpNoHist', c_uint * int(8)),
]

rk_tool_awb_stat_res2_v30_t = struct_rk_tool_awb_stat_res2_v30_s# /root/camera_engine_rkaiq/include/iq_parser_v2/awb_uapi_head.h: 92

# /root/camera_engine_rkaiq/include/iq_parser_v2/awb_uapi_head.h: 101
class struct_rk_tool_awb_measure_wp_res_fl_s(Structure):
    pass

struct_rk_tool_awb_measure_wp_res_fl_s.__slots__ = [
    'WpNo',
    'gain',
    'WpNoHist_2',
]
struct_rk_tool_awb_measure_wp_res_fl_s._fields_ = [
    ('WpNo', c_uint),
    ('gain', c_float * int(4)),
    ('WpNoHist_2', c_int * int(8)),
]

rk_tool_awb_measure_wp_res_fl_t = struct_rk_tool_awb_measure_wp_res_fl_s# /root/camera_engine_rkaiq/include/iq_parser_v2/awb_uapi_head.h: 101

# /root/camera_engine_rkaiq/include/iq_parser_v2/awb_uapi_head.h: 108
class struct_rk_tool_awb_measure_blk_res2_fl_s(Structure):
    pass

struct_rk_tool_awb_measure_blk_res2_fl_s.__slots__ = [
    'WpNo',
    'gain',
]
struct_rk_tool_awb_measure_blk_res2_fl_s._fields_ = [
    ('WpNo', c_uint),
    ('gain', c_float * int(4)),
]

rk_tool_awb_measure_blk_res2_fl_t = struct_rk_tool_awb_measure_blk_res2_fl_s# /root/camera_engine_rkaiq/include/iq_parser_v2/awb_uapi_head.h: 108

# /root/camera_engine_rkaiq/include/iq_parser_v2/awb_uapi_head.h: 113
class struct_rk_tool_awb_measure_wp_res_light_fl_s(Structure):
    pass

struct_rk_tool_awb_measure_wp_res_light_fl_s.__slots__ = [
    'xYType',
]
struct_rk_tool_awb_measure_wp_res_light_fl_s._fields_ = [
    ('xYType', rk_tool_awb_measure_wp_res_fl_t * int(2)),
]

rk_tool_awb_measure_wp_res_light_fl_t = struct_rk_tool_awb_measure_wp_res_light_fl_s# /root/camera_engine_rkaiq/include/iq_parser_v2/awb_uapi_head.h: 113

# /root/camera_engine_rkaiq/include/iq_parser_v2/awb_uapi_head.h: 122
class struct_rk_tool_awb_measure_blk_res_fl_s(Structure):
    pass

struct_rk_tool_awb_measure_blk_res_fl_s.__slots__ = [
    'R',
    'G',
    'B',
]
struct_rk_tool_awb_measure_blk_res_fl_s._fields_ = [
    ('R', c_float),
    ('G', c_float),
    ('B', c_float),
]

rk_tool_awb_measure_blk_res_fl_t = struct_rk_tool_awb_measure_blk_res_fl_s# /root/camera_engine_rkaiq/include/iq_parser_v2/awb_uapi_head.h: 122

# /root/camera_engine_rkaiq/include/iq_parser_v2/awb_uapi_head.h: 127
class struct_rk_tool_awb_effect_para1_s(Structure):
    pass

struct_rk_tool_awb_effect_para1_s.__slots__ = [
    'hdrFrameChoose',
]
struct_rk_tool_awb_effect_para1_s._fields_ = [
    ('hdrFrameChoose', c_int),
]

rk_tool_awb_effect_para1_t = struct_rk_tool_awb_effect_para1_s# /root/camera_engine_rkaiq/include/iq_parser_v2/awb_uapi_head.h: 127

# /root/camera_engine_rkaiq/include/iq_parser_v2/awb_uapi_head.h: 162
class struct_rk_tool_awb_stat_res_full_s(Structure):
    pass

struct_rk_tool_awb_stat_res_full_s.__slots__ = [
    'lightNum',
    'light',
    'lightWpResVaLidIll',
    'lightWpResVaLid',
    'WpNo',
    'WpNo2',
    'blkGwResValid',
    'blkSgcResVaLid',
    'blkSgcResult',
    'blkWpResVaLid',
    'blkWpResult',
    'excWpResValid',
    'excWpRangeResult',
    'extraLightResult',
    'WpNoHist',
    'effectHwPara',
]
struct_rk_tool_awb_stat_res_full_s._fields_ = [
    ('lightNum', c_int),
    ('light', rk_tool_awb_measure_wp_res_light_fl_t * int(14)),
    ('lightWpResVaLidIll', c_bool * int(14)),
    ('lightWpResVaLid', c_bool),
    ('WpNo', c_int * int(2)),
    ('WpNo2', c_int * int(14)),
    ('blkGwResValid', c_bool),
    ('blkSgcResVaLid', c_bool),
    ('blkSgcResult', rk_tool_awb_measure_blk_res_fl_t * int(225)),
    ('blkWpResVaLid', c_bool),
    ('blkWpResult', rk_tool_awb_measure_blk_res2_fl_t * int(225)),
    ('excWpResValid', c_bool),
    ('excWpRangeResult', rk_tool_awb_measure_wp_res_fl_t * int(4)),
    ('extraLightResult', rk_tool_awb_measure_wp_res_fl_t),
    ('WpNoHist', c_uint * int(8)),
    ('effectHwPara', rk_tool_awb_effect_para1_t),
]

rk_tool_awb_stat_res_full_t = struct_rk_tool_awb_stat_res_full_s# /root/camera_engine_rkaiq/include/iq_parser_v2/awb_uapi_head.h: 162

# /root/camera_engine_rkaiq/include/iq_parser_v2/awb_uapi_head.h: 183
class struct_rk_tool_awb_smart_run_res_s(Structure):
    pass

struct_rk_tool_awb_smart_run_res_s.__slots__ = [
    'blc1Stable',
    'lvStable',
    'wbgainStable',
    'wpDiffweiStable',
    'statisticsStable',
    'forceRunAwbFlag',
    'samrtRunAwbFlag2',
    'wbgainMean',
    'algMethodStable',
]
struct_rk_tool_awb_smart_run_res_s._fields_ = [
    ('blc1Stable', c_bool),
    ('lvStable', c_bool),
    ('wbgainStable', c_bool),
    ('wpDiffweiStable', c_bool),
    ('statisticsStable', c_bool),
    ('forceRunAwbFlag', c_bool),
    ('samrtRunAwbFlag2', c_bool),
    ('wbgainMean', c_float * int(4)),
    ('algMethodStable', c_bool),
]

rk_tool_awb_smart_run_res_t = struct_rk_tool_awb_smart_run_res_s# /root/camera_engine_rkaiq/include/iq_parser_v2/awb_uapi_head.h: 183

# /root/camera_engine_rkaiq/include/iq_parser_v2/awb_uapi_head.h: 204
class struct_rk_tool_awb_illInf_s(Structure):
    pass

struct_rk_tool_awb_illInf_s.__slots__ = [
    'illName',
    'gainValue',
    'prob_total',
    'prob_dis',
    'prob_LV',
    'spatialGainValue',
    'prob_WPNO',
    'staWeight',
    'xyType2Weight',
]
struct_rk_tool_awb_illInf_s._fields_ = [
    ('illName', c_char * int(100)),
    ('gainValue', c_float * int(4)),
    ('prob_total', c_float),
    ('prob_dis', c_float),
    ('prob_LV', c_float),
    ('spatialGainValue', c_float * int(4)),
    ('prob_WPNO', c_float),
    ('staWeight', c_float),
    ('xyType2Weight', c_float),
]

rk_tool_awb_illInf_t = struct_rk_tool_awb_illInf_s# /root/camera_engine_rkaiq/include/iq_parser_v2/awb_uapi_head.h: 204

# /root/camera_engine_rkaiq/include/iq_parser_v2/awb_uapi_head.h: 213
class struct_rk_tool_color_tempture_info_s(Structure):
    pass

struct_rk_tool_color_tempture_info_s.__slots__ = [
    'valid',
    'CCT',
    'CCRI',
]
struct_rk_tool_color_tempture_info_s._fields_ = [
    ('valid', c_bool),
    ('CCT', c_float),
    ('CCRI', c_float),
]

rk_tool_color_tempture_info_t = struct_rk_tool_color_tempture_info_s# /root/camera_engine_rkaiq/include/iq_parser_v2/awb_uapi_head.h: 213

# /root/camera_engine_rkaiq/include/iq_parser_v2/awb_uapi_head.h: 304
class struct_rk_tool_awb_strategy_result_s(Structure):
    pass

struct_rk_tool_awb_strategy_result_s.__slots__ = [
    'awbConverged',
    'cctGloabl',
    'lightNum',
    'smartAwbRunRes',
    'count',
    'runInterval',
    'tolerance',
    'dsRate',
    'width_ds',
    'height_ds',
    'WPmode',
    'WPTotalNUM',
    'WPType',
    'LVType',
    'LVValue',
    'fLVValue',
    'LVLevel',
    'illInf',
    'wbGainTepTp3',
    'wbWeiTepTp3',
    'xy_area_type',
    'spaGainEqu2Tem',
    'sgcGainEqu2Tem',
    'wbGainType3',
    'wbGainType1',
    'wbWeightType3',
    'wbGainTep',
    'wbGainSgc',
    'wbWeightSgc',
    'wbGainSpa',
    'wbWeightSpa',
    'varianceLuma',
    'wbGainDampFactor',
    'clipEnalbe',
    'updateFlag',
    'wbGainIntpStrategy',
    'wbGainClip',
    'wbGainCaga',
    'wbGainAdjust',
    'wbGainOffset',
    'wbGainSmooth',
    'stat3aAwbLastGainOut',
    'stat3aAwbGainOut',
    'algMethod',
]
struct_rk_tool_awb_strategy_result_s._fields_ = [
    ('awbConverged', c_bool),
    ('cctGloabl', rk_tool_color_tempture_info_t),
    ('lightNum', c_int),
    ('smartAwbRunRes', rk_tool_awb_smart_run_res_t),
    ('count', c_uint),
    ('runInterval', uint32_t),
    ('tolerance', c_float),
    ('dsRate', uint8_t),
    ('width_ds', uint32_t),
    ('height_ds', uint32_t),
    ('WPmode', c_int),
    ('WPTotalNUM', uint32_t),
    ('WPType', c_int),
    ('LVType', c_int),
    ('LVValue', c_int),
    ('fLVValue', c_float),
    ('LVLevel', c_int),
    ('illInf', rk_tool_awb_illInf_t * int(14)),
    ('wbGainTepTp3', c_float * int(4)),
    ('wbWeiTepTp3', c_float),
    ('xy_area_type', uint8_t),
    ('spaGainEqu2Tem', c_bool),
    ('sgcGainEqu2Tem', c_bool),
    ('wbGainType3', c_float * int(4)),
    ('wbGainType1', c_float * int(4)),
    ('wbWeightType3', c_float),
    ('wbGainTep', c_float * int(4)),
    ('wbGainSgc', c_float * int(4)),
    ('wbWeightSgc', c_float),
    ('wbGainSpa', c_float * int(4)),
    ('wbWeightSpa', c_float),
    ('varianceLuma', c_float),
    ('wbGainDampFactor', c_float),
    ('clipEnalbe', c_bool),
    ('updateFlag', c_bool),
    ('wbGainIntpStrategy', c_float * int(4)),
    ('wbGainClip', c_float * int(4)),
    ('wbGainCaga', c_float * int(4)),
    ('wbGainAdjust', c_float * int(4)),
    ('wbGainOffset', c_float * int(4)),
    ('wbGainSmooth', c_float * int(4)),
    ('stat3aAwbLastGainOut', c_float * int(4)),
    ('stat3aAwbGainOut', c_float * int(4)),
    ('algMethod', c_int),
]

rk_tool_awb_strategy_result_t = struct_rk_tool_awb_strategy_result_s# /root/camera_engine_rkaiq/include/iq_parser_v2/awb_uapi_head.h: 304

enum_rk_aiq_wb_scene_e = c_int# /root/camera_engine_rkaiq/include/algos/awb/rk_aiq_types_awb_algo_int.h: 39

rk_aiq_wb_scene_t = enum_rk_aiq_wb_scene_e# /root/camera_engine_rkaiq/include/algos/awb/rk_aiq_types_awb_algo_int.h: 39

# /root/camera_engine_rkaiq/include/algos/awb/rk_aiq_types_awb_algo_int.h: 44
class struct_rk_aiq_wb_cct_s(Structure):
    pass

struct_rk_aiq_wb_cct_s.__slots__ = [
    'CCT',
    'CCRI',
]
struct_rk_aiq_wb_cct_s._fields_ = [
    ('CCT', c_float),
    ('CCRI', c_float),
]

rk_aiq_wb_cct_t = struct_rk_aiq_wb_cct_s# /root/camera_engine_rkaiq/include/algos/awb/rk_aiq_types_awb_algo_int.h: 44

enum_rk_aiq_wb_mwb_mode_e = c_int# /root/camera_engine_rkaiq/include/algos/awb/rk_aiq_types_awb_algo_int.h: 63

rk_aiq_wb_mwb_mode_t = enum_rk_aiq_wb_mwb_mode_e# /root/camera_engine_rkaiq/include/algos/awb/rk_aiq_types_awb_algo_int.h: 63

# /root/camera_engine_rkaiq/include/algos/awb/rk_aiq_types_awb_algo_int.h: 69
class union_MWBPara_u(Union):
    pass

union_MWBPara_u.__slots__ = [
    'gain',
    'scene',
    'cct',
]
union_MWBPara_u._fields_ = [
    ('gain', rk_aiq_wb_gain_t),
    ('scene', rk_aiq_wb_scene_t),
    ('cct', rk_aiq_wb_cct_t),
]

# /root/camera_engine_rkaiq/include/algos/awb/rk_aiq_types_awb_algo_int.h: 74
class struct_rk_aiq_wb_mwb_attrib_s(Structure):
    pass

struct_rk_aiq_wb_mwb_attrib_s.__slots__ = [
    'sync',
    'mode',
    'para',
]
struct_rk_aiq_wb_mwb_attrib_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('mode', rk_aiq_wb_mwb_mode_t),
    ('para', union_MWBPara_u),
]

rk_aiq_wb_mwb_attrib_t = struct_rk_aiq_wb_mwb_attrib_s# /root/camera_engine_rkaiq/include/algos/awb/rk_aiq_types_awb_algo_int.h: 74

enum_rk_aiq_wb_op_mode_s = c_int# /root/camera_engine_rkaiq/include/algos/awb/rk_aiq_types_awb_algo_int.h: 119

rk_aiq_wb_op_mode_t = enum_rk_aiq_wb_op_mode_s# /root/camera_engine_rkaiq/include/algos/awb/rk_aiq_types_awb_algo_int.h: 119

# /root/camera_engine_rkaiq/include/algos/awb/rk_aiq_types_awb_algo_int.h: 125
class struct_rk_aiq_uapiV2_wb_opMode_s(Structure):
    pass

struct_rk_aiq_uapiV2_wb_opMode_s.__slots__ = [
    'sync',
    'mode',
]
struct_rk_aiq_uapiV2_wb_opMode_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('mode', rk_aiq_wb_op_mode_t),
]

rk_aiq_uapiV2_wb_opMode_t = struct_rk_aiq_uapiV2_wb_opMode_s# /root/camera_engine_rkaiq/include/algos/awb/rk_aiq_types_awb_algo_int.h: 125

# /root/camera_engine_rkaiq/include/algos/awb/rk_aiq_types_awb_algo_int.h: 139
class struct_rk_aiq_wb_querry_info_s(Structure):
    pass

struct_rk_aiq_wb_querry_info_s.__slots__ = [
    'gain',
    'cctGloabl',
    'awbConverged',
    'LVValue',
]
struct_rk_aiq_wb_querry_info_s._fields_ = [
    ('gain', rk_aiq_wb_gain_t),
    ('cctGloabl', rk_aiq_wb_cct_t),
    ('awbConverged', c_bool),
    ('LVValue', uint32_t),
]

rk_aiq_wb_querry_info_t = struct_rk_aiq_wb_querry_info_s# /root/camera_engine_rkaiq/include/algos/awb/rk_aiq_types_awb_algo_int.h: 139

# /root/camera_engine_rkaiq/include/algos/awb/rk_aiq_types_awb_algo_int.h: 171
class struct_rk_aiq_uapiV2_wb_awb_wbGainAdjustLut_s(Structure):
    pass

struct_rk_aiq_uapiV2_wb_awb_wbGainAdjustLut_s.__slots__ = [
    'lumaValue',
    'ct_grid_num',
    'cri_grid_num',
    'ct_in_range',
    'cri_in_range',
    'ct_lut_out',
    'cri_lut_out',
]
struct_rk_aiq_uapiV2_wb_awb_wbGainAdjustLut_s._fields_ = [
    ('lumaValue', c_float),
    ('ct_grid_num', c_int),
    ('cri_grid_num', c_int),
    ('ct_in_range', c_float * int(2)),
    ('cri_in_range', c_float * int(2)),
    ('ct_lut_out', POINTER(c_float)),
    ('cri_lut_out', POINTER(c_float)),
]

rk_aiq_uapiV2_wb_awb_wbGainAdjustLut_t = struct_rk_aiq_uapiV2_wb_awb_wbGainAdjustLut_s# /root/camera_engine_rkaiq/include/algos/awb/rk_aiq_types_awb_algo_int.h: 171

# /root/camera_engine_rkaiq/include/algos/awb/rk_aiq_types_awb_algo_int.h: 181
class struct_rk_aiq_uapiV2_wb_awb_wbGainAdjust_s(Structure):
    pass

struct_rk_aiq_uapiV2_wb_awb_wbGainAdjust_s.__slots__ = [
    'sync',
    'enable',
    'lutAll',
    'lutAll_len',
]
struct_rk_aiq_uapiV2_wb_awb_wbGainAdjust_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('enable', c_bool),
    ('lutAll', POINTER(rk_aiq_uapiV2_wb_awb_wbGainAdjustLut_t)),
    ('lutAll_len', c_int),
]

rk_aiq_uapiV2_wb_awb_wbGainAdjust_t = struct_rk_aiq_uapiV2_wb_awb_wbGainAdjust_s# /root/camera_engine_rkaiq/include/algos/awb/rk_aiq_types_awb_algo_int.h: 181

# /root/camera_engine_rkaiq/include/algos/awb/rk_aiq_types_awb_algo_int.h: 187
class struct_rk_aiq_uapiV2_wb_awb_wbGainOffset_s(Structure):
    pass

struct_rk_aiq_uapiV2_wb_awb_wbGainOffset_s.__slots__ = [
    'sync',
    'gainOffset',
]
struct_rk_aiq_uapiV2_wb_awb_wbGainOffset_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('gainOffset', CalibDbV2_Awb_gain_offset_cfg_t),
]

rk_aiq_uapiV2_wb_awb_wbGainOffset_t = struct_rk_aiq_uapiV2_wb_awb_wbGainOffset_s# /root/camera_engine_rkaiq/include/algos/awb/rk_aiq_types_awb_algo_int.h: 187

# /root/camera_engine_rkaiq/include/algos/awb/rk_aiq_types_awb_algo_int.h: 194
class struct_rk_aiq_uapiV2_wb_awb_mulWindow_s(Structure):
    pass

struct_rk_aiq_uapiV2_wb_awb_mulWindow_s.__slots__ = [
    'sync',
    'multiWindw',
]
struct_rk_aiq_uapiV2_wb_awb_mulWindow_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('multiWindw', CalibDbV2_Awb_Mul_Win_t),
]

rk_aiq_uapiV2_wb_awb_mulWindow_t = struct_rk_aiq_uapiV2_wb_awb_mulWindow_s# /root/camera_engine_rkaiq/include/algos/awb/rk_aiq_types_awb_algo_int.h: 194

# /root/camera_engine_rkaiq/include/algos/awb/rk_aiq_types_awb_algo_int.h: 200
class struct_rk_aiq_uapiV2_wbV21_awb_attrib_s(Structure):
    pass

struct_rk_aiq_uapiV2_wbV21_awb_attrib_s.__slots__ = [
    'wbGainAdjust',
    'wbGainOffset',
]
struct_rk_aiq_uapiV2_wbV21_awb_attrib_s._fields_ = [
    ('wbGainAdjust', rk_aiq_uapiV2_wb_awb_wbGainAdjust_t),
    ('wbGainOffset', CalibDbV2_Awb_gain_offset_cfg_t),
]

rk_aiq_uapiV2_wbV30_awb_attrib_t = struct_rk_aiq_uapiV2_wbV21_awb_attrib_s# /root/camera_engine_rkaiq/include/algos/awb/rk_aiq_types_awb_algo_int.h: 200

# /root/camera_engine_rkaiq/include/algos/awb/rk_aiq_types_awb_algo_int.h: 216
class struct_rk_aiq_uapiV2_wbV21_attrib_s(Structure):
    pass

struct_rk_aiq_uapiV2_wbV21_attrib_s.__slots__ = [
    'sync',
    'byPass',
    'mode',
    'stManual',
    'stAuto',
]
struct_rk_aiq_uapiV2_wbV21_attrib_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('byPass', c_bool),
    ('mode', rk_aiq_wb_op_mode_t),
    ('stManual', rk_aiq_wb_mwb_attrib_t),
    ('stAuto', rk_aiq_uapiV2_wbV30_awb_attrib_t),
]

rk_aiq_uapiV2_wbV21_attrib_t = struct_rk_aiq_uapiV2_wbV21_attrib_s# /root/camera_engine_rkaiq/include/algos/awb/rk_aiq_types_awb_algo_int.h: 216

# /root/camera_engine_rkaiq/include/algos/awb/rk_aiq_types_awb_algo_int.h: 232
class struct_rk_aiq_uapiV2_wbV30_attrib_s(Structure):
    pass

struct_rk_aiq_uapiV2_wbV30_attrib_s.__slots__ = [
    'sync',
    'byPass',
    'mode',
    'stManual',
    'stAuto',
]
struct_rk_aiq_uapiV2_wbV30_attrib_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('byPass', c_bool),
    ('mode', rk_aiq_wb_op_mode_t),
    ('stManual', rk_aiq_wb_mwb_attrib_t),
    ('stAuto', rk_aiq_uapiV2_wbV30_awb_attrib_t),
]

rk_aiq_uapiV2_wbV30_attrib_t = struct_rk_aiq_uapiV2_wbV30_attrib_s# /root/camera_engine_rkaiq/include/algos/awb/rk_aiq_types_awb_algo_int.h: 232

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_awb.h: 30
if _libs["rkaiq"].has("rk_aiq_user_api2_awbV21_SetAllAttrib", "cdecl"):
    rk_aiq_user_api2_awbV21_SetAllAttrib = _libs["rkaiq"].get("rk_aiq_user_api2_awbV21_SetAllAttrib", "cdecl")
    rk_aiq_user_api2_awbV21_SetAllAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), rk_aiq_uapiV2_wbV21_attrib_t]
    rk_aiq_user_api2_awbV21_SetAllAttrib.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_awb.h: 32
if _libs["rkaiq"].has("rk_aiq_user_api2_awbV21_GetAllAttrib", "cdecl"):
    rk_aiq_user_api2_awbV21_GetAllAttrib = _libs["rkaiq"].get("rk_aiq_user_api2_awbV21_GetAllAttrib", "cdecl")
    rk_aiq_user_api2_awbV21_GetAllAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_uapiV2_wbV21_attrib_t)]
    rk_aiq_user_api2_awbV21_GetAllAttrib.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_awb.h: 34
if _libs["rkaiq"].has("rk_aiq_user_api2_awbV30_SetAllAttrib", "cdecl"):
    rk_aiq_user_api2_awbV30_SetAllAttrib = _libs["rkaiq"].get("rk_aiq_user_api2_awbV30_SetAllAttrib", "cdecl")
    rk_aiq_user_api2_awbV30_SetAllAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), rk_aiq_uapiV2_wbV30_attrib_t]
    rk_aiq_user_api2_awbV30_SetAllAttrib.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_awb.h: 36
if _libs["rkaiq"].has("rk_aiq_user_api2_awbV30_GetAllAttrib", "cdecl"):
    rk_aiq_user_api2_awbV30_GetAllAttrib = _libs["rkaiq"].get("rk_aiq_user_api2_awbV30_GetAllAttrib", "cdecl")
    rk_aiq_user_api2_awbV30_GetAllAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_uapiV2_wbV30_attrib_t)]
    rk_aiq_user_api2_awbV30_GetAllAttrib.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_awb.h: 38
if _libs["rkaiq"].has("rk_aiq_user_api2_awb_GetCCT", "cdecl"):
    rk_aiq_user_api2_awb_GetCCT = _libs["rkaiq"].get("rk_aiq_user_api2_awb_GetCCT", "cdecl")
    rk_aiq_user_api2_awb_GetCCT.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_wb_cct_t)]
    rk_aiq_user_api2_awb_GetCCT.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_awb.h: 40
if _libs["rkaiq"].has("rk_aiq_user_api2_awb_QueryWBInfo", "cdecl"):
    rk_aiq_user_api2_awb_QueryWBInfo = _libs["rkaiq"].get("rk_aiq_user_api2_awb_QueryWBInfo", "cdecl")
    rk_aiq_user_api2_awb_QueryWBInfo.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_wb_querry_info_t)]
    rk_aiq_user_api2_awb_QueryWBInfo.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_awb.h: 42
if _libs["rkaiq"].has("rk_aiq_user_api2_awb_Lock", "cdecl"):
    rk_aiq_user_api2_awb_Lock = _libs["rkaiq"].get("rk_aiq_user_api2_awb_Lock", "cdecl")
    rk_aiq_user_api2_awb_Lock.argtypes = [POINTER(rk_aiq_sys_ctx_t)]
    rk_aiq_user_api2_awb_Lock.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_awb.h: 44
if _libs["rkaiq"].has("rk_aiq_user_api2_awb_Unlock", "cdecl"):
    rk_aiq_user_api2_awb_Unlock = _libs["rkaiq"].get("rk_aiq_user_api2_awb_Unlock", "cdecl")
    rk_aiq_user_api2_awb_Unlock.argtypes = [POINTER(rk_aiq_sys_ctx_t)]
    rk_aiq_user_api2_awb_Unlock.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_awb.h: 46
if _libs["rkaiq"].has("rk_aiq_user_api2_awb_SetWpModeAttrib", "cdecl"):
    rk_aiq_user_api2_awb_SetWpModeAttrib = _libs["rkaiq"].get("rk_aiq_user_api2_awb_SetWpModeAttrib", "cdecl")
    rk_aiq_user_api2_awb_SetWpModeAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), rk_aiq_uapiV2_wb_opMode_t]
    rk_aiq_user_api2_awb_SetWpModeAttrib.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_awb.h: 48
if _libs["rkaiq"].has("rk_aiq_user_api2_awb_GetWpModeAttrib", "cdecl"):
    rk_aiq_user_api2_awb_GetWpModeAttrib = _libs["rkaiq"].get("rk_aiq_user_api2_awb_GetWpModeAttrib", "cdecl")
    rk_aiq_user_api2_awb_GetWpModeAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_uapiV2_wb_opMode_t)]
    rk_aiq_user_api2_awb_GetWpModeAttrib.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_awb.h: 50
if _libs["rkaiq"].has("rk_aiq_user_api2_awb_SetMwbAttrib", "cdecl"):
    rk_aiq_user_api2_awb_SetMwbAttrib = _libs["rkaiq"].get("rk_aiq_user_api2_awb_SetMwbAttrib", "cdecl")
    rk_aiq_user_api2_awb_SetMwbAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), rk_aiq_wb_mwb_attrib_t]
    rk_aiq_user_api2_awb_SetMwbAttrib.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_awb.h: 52
if _libs["rkaiq"].has("rk_aiq_user_api2_awb_GetMwbAttrib", "cdecl"):
    rk_aiq_user_api2_awb_GetMwbAttrib = _libs["rkaiq"].get("rk_aiq_user_api2_awb_GetMwbAttrib", "cdecl")
    rk_aiq_user_api2_awb_GetMwbAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_wb_mwb_attrib_t)]
    rk_aiq_user_api2_awb_GetMwbAttrib.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_awb.h: 54
if _libs["rkaiq"].has("rk_aiq_user_api2_awb_SetWbGainAdjustAttrib", "cdecl"):
    rk_aiq_user_api2_awb_SetWbGainAdjustAttrib = _libs["rkaiq"].get("rk_aiq_user_api2_awb_SetWbGainAdjustAttrib", "cdecl")
    rk_aiq_user_api2_awb_SetWbGainAdjustAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), rk_aiq_uapiV2_wb_awb_wbGainAdjust_t]
    rk_aiq_user_api2_awb_SetWbGainAdjustAttrib.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_awb.h: 56
if _libs["rkaiq"].has("rk_aiq_user_api2_awb_GetWbGainAdjustAttrib", "cdecl"):
    rk_aiq_user_api2_awb_GetWbGainAdjustAttrib = _libs["rkaiq"].get("rk_aiq_user_api2_awb_GetWbGainAdjustAttrib", "cdecl")
    rk_aiq_user_api2_awb_GetWbGainAdjustAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_uapiV2_wb_awb_wbGainAdjust_t)]
    rk_aiq_user_api2_awb_GetWbGainAdjustAttrib.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_awb.h: 58
if _libs["rkaiq"].has("rk_aiq_user_api2_awb_SetWbGainOffsetAttrib", "cdecl"):
    rk_aiq_user_api2_awb_SetWbGainOffsetAttrib = _libs["rkaiq"].get("rk_aiq_user_api2_awb_SetWbGainOffsetAttrib", "cdecl")
    rk_aiq_user_api2_awb_SetWbGainOffsetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), rk_aiq_uapiV2_wb_awb_wbGainOffset_t]
    rk_aiq_user_api2_awb_SetWbGainOffsetAttrib.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_awb.h: 60
if _libs["rkaiq"].has("rk_aiq_user_api2_awb_GetWbGainOffsetAttrib", "cdecl"):
    rk_aiq_user_api2_awb_GetWbGainOffsetAttrib = _libs["rkaiq"].get("rk_aiq_user_api2_awb_GetWbGainOffsetAttrib", "cdecl")
    rk_aiq_user_api2_awb_GetWbGainOffsetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_uapiV2_wb_awb_wbGainOffset_t)]
    rk_aiq_user_api2_awb_GetWbGainOffsetAttrib.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_awb.h: 62
if _libs["rkaiq"].has("rk_aiq_user_api2_awb_SetMultiWindowAttrib", "cdecl"):
    rk_aiq_user_api2_awb_SetMultiWindowAttrib = _libs["rkaiq"].get("rk_aiq_user_api2_awb_SetMultiWindowAttrib", "cdecl")
    rk_aiq_user_api2_awb_SetMultiWindowAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), rk_aiq_uapiV2_wb_awb_mulWindow_t]
    rk_aiq_user_api2_awb_SetMultiWindowAttrib.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_awb.h: 64
if _libs["rkaiq"].has("rk_aiq_user_api2_awb_GetMultiWindowAttrib", "cdecl"):
    rk_aiq_user_api2_awb_GetMultiWindowAttrib = _libs["rkaiq"].get("rk_aiq_user_api2_awb_GetMultiWindowAttrib", "cdecl")
    rk_aiq_user_api2_awb_GetMultiWindowAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_uapiV2_wb_awb_mulWindow_t)]
    rk_aiq_user_api2_awb_GetMultiWindowAttrib.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_awb.h: 66
if _libs["rkaiq"].has("rk_aiq_user_api2_awbV30_getStrategyResult", "cdecl"):
    rk_aiq_user_api2_awbV30_getStrategyResult = _libs["rkaiq"].get("rk_aiq_user_api2_awbV30_getStrategyResult", "cdecl")
    rk_aiq_user_api2_awbV30_getStrategyResult.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_tool_awb_strategy_result_t)]
    rk_aiq_user_api2_awbV30_getStrategyResult.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_awb.h: 68
if _libs["rkaiq"].has("rk_aiq_user_api2_awbV30_getAlgoSta", "cdecl"):
    rk_aiq_user_api2_awbV30_getAlgoSta = _libs["rkaiq"].get("rk_aiq_user_api2_awbV30_getAlgoSta", "cdecl")
    rk_aiq_user_api2_awbV30_getAlgoSta.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_tool_awb_stat_res_full_t)]
    rk_aiq_user_api2_awbV30_getAlgoSta.restype = XCamReturn

enum_Aynr_OPMode_e = c_int# /root/camera_engine_rkaiq/include/algos/aynr2/rk_aiq_types_aynr_algo_int_v2.h: 69

Aynr_OPMode_t = enum_Aynr_OPMode_e# /root/camera_engine_rkaiq/include/algos/aynr2/rk_aiq_types_aynr_algo_int_v2.h: 69

# /root/camera_engine_rkaiq/include/algos/aynr2/rk_aiq_types_aynr_algo_int_v2.h: 126
class struct_RK_YNR_Params_V2_Select_s(Structure):
    pass

struct_RK_YNR_Params_V2_Select_s.__slots__ = [
    'enable',
    'ciISO_V2',
    'noiseSigma_V2',
    'lumaPoints_V2',
    'ynr_big_resolution_mode',
    'ynr_global_gain_V2',
    'ynr_rnr_strength_V2',
    'ynr_bft3x3_bypass_V2',
    'ynr_lbft5x5_bypass_V2',
    'ynr_lgft3x3_bypass_V2',
    'ynr_flt1x1_bypass_V2',
    'ynr_sft5x5_bypass_V2',
    'ynr_low_bf_V2',
    'ynr_low_thred_adj_V2',
    'ynr_low_peak_supress_V2',
    'ynr_low_edge_adj_thresh_V2',
    'ynr_low_center_weight_V2',
    'ynr_low_dist_adj_V2',
    'ynr_low_weight_V2',
    'ynr_low_filt1_strength_V2',
    'ynr_low_filt2_strength_V2',
    'ynr_low_bi_weight_V2',
    'ynr_base_filter_weight1_V2',
    'ynr_base_filter_weight2_V2',
    'ynr_base_filter_weight3_V2',
    'ynr_high_thred_adj_V2',
    'ynr_high_weight_V2',
    'ynr_direction_weight_V2',
    'ynr_hi_min_adj_V2',
    'ynr_hi_edge_thed_V2',
]
struct_RK_YNR_Params_V2_Select_s._fields_ = [
    ('enable', c_int),
    ('ciISO_V2', c_float * int(2)),
    ('noiseSigma_V2', c_float * int(((1 << 4) + 1))),
    ('lumaPoints_V2', c_short * int(((1 << 4) + 1))),
    ('ynr_big_resolution_mode', c_int),
    ('ynr_global_gain_V2', c_int),
    ('ynr_rnr_strength_V2', c_float * int(17)),
    ('ynr_bft3x3_bypass_V2', c_int),
    ('ynr_lbft5x5_bypass_V2', c_int),
    ('ynr_lgft3x3_bypass_V2', c_int),
    ('ynr_flt1x1_bypass_V2', c_int),
    ('ynr_sft5x5_bypass_V2', c_int),
    ('ynr_low_bf_V2', c_float * int(2)),
    ('ynr_low_thred_adj_V2', c_float),
    ('ynr_low_peak_supress_V2', c_float),
    ('ynr_low_edge_adj_thresh_V2', c_float),
    ('ynr_low_center_weight_V2', c_float),
    ('ynr_low_dist_adj_V2', c_float),
    ('ynr_low_weight_V2', c_float),
    ('ynr_low_filt1_strength_V2', c_float),
    ('ynr_low_filt2_strength_V2', c_float),
    ('ynr_low_bi_weight_V2', c_float),
    ('ynr_base_filter_weight1_V2', c_float),
    ('ynr_base_filter_weight2_V2', c_float),
    ('ynr_base_filter_weight3_V2', c_float),
    ('ynr_high_thred_adj_V2', c_float),
    ('ynr_high_weight_V2', c_float),
    ('ynr_direction_weight_V2', c_float * int(8)),
    ('ynr_hi_min_adj_V2', c_float),
    ('ynr_hi_edge_thed_V2', c_float),
]

RK_YNR_Params_V2_Select_t = struct_RK_YNR_Params_V2_Select_s# /root/camera_engine_rkaiq/include/algos/aynr2/rk_aiq_types_aynr_algo_int_v2.h: 126

# /root/camera_engine_rkaiq/include/algos/aynr2/rk_aiq_types_aynr_algo_int_v2.h: 137
class struct_RK_YNR_Params_V2_s(Structure):
    pass

struct_RK_YNR_Params_V2_s.__slots__ = [
    'enable',
    'version',
    'iso',
    'arYnrParamsISO',
]
struct_RK_YNR_Params_V2_s._fields_ = [
    ('enable', c_int),
    ('version', c_char * int(64)),
    ('iso', c_float * int(13)),
    ('arYnrParamsISO', RK_YNR_Params_V2_Select_t * int(13)),
]

RK_YNR_Params_V2_t = struct_RK_YNR_Params_V2_s# /root/camera_engine_rkaiq/include/algos/aynr2/rk_aiq_types_aynr_algo_int_v2.h: 137

# /root/camera_engine_rkaiq/include/algos/aynr2/rk_aiq_types_aynr_algo_int_v2.h: 145
class struct_Aynr_Manual_Attr_V2_s(Structure):
    pass

struct_Aynr_Manual_Attr_V2_s.__slots__ = [
    'ynrEn',
    'stSelect',
]
struct_Aynr_Manual_Attr_V2_s._fields_ = [
    ('ynrEn', c_int),
    ('stSelect', RK_YNR_Params_V2_Select_t),
]

Aynr_Manual_Attr_V2_t = struct_Aynr_Manual_Attr_V2_s# /root/camera_engine_rkaiq/include/algos/aynr2/rk_aiq_types_aynr_algo_int_v2.h: 145

# /root/camera_engine_rkaiq/include/algos/aynr2/rk_aiq_types_aynr_algo_int_v2.h: 155
class struct_Aynr_Auto_Attr_V2_s(Structure):
    pass

struct_Aynr_Auto_Attr_V2_s.__slots__ = [
    'ynrEn',
    'stParams',
    'stSelect',
]
struct_Aynr_Auto_Attr_V2_s._fields_ = [
    ('ynrEn', c_int),
    ('stParams', RK_YNR_Params_V2_t),
    ('stSelect', RK_YNR_Params_V2_Select_t),
]

Aynr_Auto_Attr_V2_t = struct_Aynr_Auto_Attr_V2_s# /root/camera_engine_rkaiq/include/algos/aynr2/rk_aiq_types_aynr_algo_int_v2.h: 155

# /root/camera_engine_rkaiq/include/algos/aynr2/rk_aiq_types_aynr_algo_int_v2.h: 183
class struct_rk_aiq_ynr_attrib_v2_s(Structure):
    pass

struct_rk_aiq_ynr_attrib_v2_s.__slots__ = [
    'eMode',
    'stAuto',
    'stManual',
]
struct_rk_aiq_ynr_attrib_v2_s._fields_ = [
    ('eMode', Aynr_OPMode_t),
    ('stAuto', Aynr_Auto_Attr_V2_t),
    ('stManual', Aynr_Manual_Attr_V2_t),
]

rk_aiq_ynr_attrib_v2_t = struct_rk_aiq_ynr_attrib_v2_s# /root/camera_engine_rkaiq/include/algos/aynr2/rk_aiq_types_aynr_algo_int_v2.h: 183

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_aynr_v2.h: 31
if _libs["rkaiq"].has("rk_aiq_user_api2_aynrV2_SetAttrib", "cdecl"):
    rk_aiq_user_api2_aynrV2_SetAttrib = _libs["rkaiq"].get("rk_aiq_user_api2_aynrV2_SetAttrib", "cdecl")
    rk_aiq_user_api2_aynrV2_SetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_ynr_attrib_v2_t)]
    rk_aiq_user_api2_aynrV2_SetAttrib.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_aynr_v2.h: 34
if _libs["rkaiq"].has("rk_aiq_user_api2_aynrV2_GetAttrib", "cdecl"):
    rk_aiq_user_api2_aynrV2_GetAttrib = _libs["rkaiq"].get("rk_aiq_user_api2_aynrV2_GetAttrib", "cdecl")
    rk_aiq_user_api2_aynrV2_GetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_ynr_attrib_v2_t)]
    rk_aiq_user_api2_aynrV2_GetAttrib.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_aynr_v2.h: 37
if _libs["rkaiq"].has("rk_aiq_user_api2_aynrV2_SetStrength", "cdecl"):
    rk_aiq_user_api2_aynrV2_SetStrength = _libs["rkaiq"].get("rk_aiq_user_api2_aynrV2_SetStrength", "cdecl")
    rk_aiq_user_api2_aynrV2_SetStrength.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_float]
    rk_aiq_user_api2_aynrV2_SetStrength.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_aynr_v2.h: 40
if _libs["rkaiq"].has("rk_aiq_user_api2_aynrV2_GetStrength", "cdecl"):
    rk_aiq_user_api2_aynrV2_GetStrength = _libs["rkaiq"].get("rk_aiq_user_api2_aynrV2_GetStrength", "cdecl")
    rk_aiq_user_api2_aynrV2_GetStrength.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(c_float)]
    rk_aiq_user_api2_aynrV2_GetStrength.restype = XCamReturn

# /root/camera_engine_rkaiq/include/iq_parser_v2/ynr_uapi_head_v3.h: 123
class struct_RK_YNR_Params_V3_Select_s(Structure):
    pass

struct_RK_YNR_Params_V3_Select_s.__slots__ = [
    'enable',
    'ynr_bft3x3_bypass',
    'ynr_lbft5x5_bypass',
    'ynr_lgft3x3_bypass',
    'ynr_flt1x1_bypass',
    'ynr_sft5x5_bypass',
    'lumaPoint',
    'sigma',
    'lo_lumaPoint',
    'lo_ratio',
    'hi_lumaPoint',
    'hi_ratio',
    'rnr_strength',
    'lci',
    'hci',
    'ynr_global_gain_alpha',
    'ynr_global_gain',
    'ynr_adjust_thresh',
    'ynr_adjust_scale',
    'low_bf1',
    'low_bf2',
    'low_thred_adj',
    'low_peak_supress',
    'low_edge_adj_thresh',
    'low_lbf_weight_thresh',
    'low_center_weight',
    'low_dist_adj',
    'low_weight',
    'low_filt1_strength',
    'low_filt2_strength',
    'low_bi_weight',
    'base_filter_weight1',
    'base_filter_weight2',
    'base_filter_weight3',
    'high_thred_adj',
    'high_weight',
    'hi_min_adj',
    'hi_edge_thed',
    'high_direction_weight',
]
struct_RK_YNR_Params_V3_Select_s._fields_ = [
    ('enable', c_int),
    ('ynr_bft3x3_bypass', c_int),
    ('ynr_lbft5x5_bypass', c_int),
    ('ynr_lgft3x3_bypass', c_int),
    ('ynr_flt1x1_bypass', c_int),
    ('ynr_sft5x5_bypass', c_int),
    ('lumaPoint', c_int16 * int(((1 << 4) + 1))),
    ('sigma', c_float * int(((1 << 4) + 1))),
    ('lo_lumaPoint', c_float * int(6)),
    ('lo_ratio', c_float * int(6)),
    ('hi_lumaPoint', c_float * int(6)),
    ('hi_ratio', c_float * int(6)),
    ('rnr_strength', c_float * int(17)),
    ('lci', c_float),
    ('hci', c_float),
    ('ynr_global_gain_alpha', c_float),
    ('ynr_global_gain', c_float),
    ('ynr_adjust_thresh', c_float),
    ('ynr_adjust_scale', c_float),
    ('low_bf1', c_float),
    ('low_bf2', c_float),
    ('low_thred_adj', c_float),
    ('low_peak_supress', c_float),
    ('low_edge_adj_thresh', c_float),
    ('low_lbf_weight_thresh', c_float),
    ('low_center_weight', c_float),
    ('low_dist_adj', c_float),
    ('low_weight', c_float),
    ('low_filt1_strength', c_float),
    ('low_filt2_strength', c_float),
    ('low_bi_weight', c_float),
    ('base_filter_weight1', c_float),
    ('base_filter_weight2', c_float),
    ('base_filter_weight3', c_float),
    ('high_thred_adj', c_float),
    ('high_weight', c_float),
    ('hi_min_adj', c_float),
    ('hi_edge_thed', c_float),
    ('high_direction_weight', c_float * int(8)),
]

RK_YNR_Params_V3_Select_t = struct_RK_YNR_Params_V3_Select_s# /root/camera_engine_rkaiq/include/iq_parser_v2/ynr_uapi_head_v3.h: 123

# /root/camera_engine_rkaiq/include/iq_parser_v2/ynr_uapi_head_v3.h: 150
class struct_Aynr_ExpInfo_V3_s(Structure):
    pass

struct_Aynr_ExpInfo_V3_s.__slots__ = [
    'hdr_mode',
    'snr_mode',
    'arTime',
    'arAGain',
    'arDGain',
    'arIso',
    'isoLow',
    'isoHigh',
    'rawWidth',
    'rawHeight',
]
struct_Aynr_ExpInfo_V3_s._fields_ = [
    ('hdr_mode', c_int),
    ('snr_mode', c_int),
    ('arTime', c_float * int(3)),
    ('arAGain', c_float * int(3)),
    ('arDGain', c_float * int(3)),
    ('arIso', c_int * int(3)),
    ('isoLow', c_int),
    ('isoHigh', c_int),
    ('rawWidth', c_int),
    ('rawHeight', c_int),
]

Aynr_ExpInfo_V3_t = struct_Aynr_ExpInfo_V3_s# /root/camera_engine_rkaiq/include/iq_parser_v2/ynr_uapi_head_v3.h: 150

# /root/camera_engine_rkaiq/include/iq_parser_v2/ynr_uapi_head_v3.h: 161
class struct_rk_aiq_ynr_info_v3_s(Structure):
    pass

struct_rk_aiq_ynr_info_v3_s.__slots__ = [
    'sync',
    'iso',
    'expo_info',
]
struct_rk_aiq_ynr_info_v3_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('iso', c_int),
    ('expo_info', Aynr_ExpInfo_V3_t),
]

rk_aiq_ynr_info_v3_t = struct_rk_aiq_ynr_info_v3_s# /root/camera_engine_rkaiq/include/iq_parser_v2/ynr_uapi_head_v3.h: 161

enum_Aynr_OPMode_V3_e = c_int# /root/camera_engine_rkaiq/include/algos/aynr3/rk_aiq_types_aynr_algo_int_v3.h: 72

Aynr_OPMode_V3_t = enum_Aynr_OPMode_V3_e# /root/camera_engine_rkaiq/include/algos/aynr3/rk_aiq_types_aynr_algo_int_v3.h: 72

# /root/camera_engine_rkaiq/include/algos/aynr3/rk_aiq_types_aynr_algo_int_v3.h: 139
class struct_RK_YNR_Sigma_formula_s(Structure):
    pass

struct_RK_YNR_Sigma_formula_s.__slots__ = [
    'sigma_curve',
]
struct_RK_YNR_Sigma_formula_s._fields_ = [
    ('sigma_curve', c_double * int(5)),
]

RK_YNR_Sigma_formula_t = struct_RK_YNR_Sigma_formula_s# /root/camera_engine_rkaiq/include/algos/aynr3/rk_aiq_types_aynr_algo_int_v3.h: 139

# /root/camera_engine_rkaiq/include/algos/aynr3/rk_aiq_types_aynr_algo_int_v3.h: 149
class struct_RK_YNR_Params_V3_s(Structure):
    pass

struct_RK_YNR_Params_V3_s.__slots__ = [
    'enable',
    'sigma_use_point',
    'version',
    'iso',
    'arYnrParamsISO',
    'arSigmaFormulaISO',
]
struct_RK_YNR_Params_V3_s._fields_ = [
    ('enable', c_int),
    ('sigma_use_point', c_bool),
    ('version', c_char * int(64)),
    ('iso', c_float * int(13)),
    ('arYnrParamsISO', RK_YNR_Params_V3_Select_t * int(13)),
    ('arSigmaFormulaISO', RK_YNR_Sigma_formula_t * int(13)),
]

RK_YNR_Params_V3_t = struct_RK_YNR_Params_V3_s# /root/camera_engine_rkaiq/include/algos/aynr3/rk_aiq_types_aynr_algo_int_v3.h: 149

# /root/camera_engine_rkaiq/include/algos/aynr3/rk_aiq_types_aynr_algo_int_v3.h: 158
class struct_Aynr_Manual_Attr_V3_s(Structure):
    pass

struct_Aynr_Manual_Attr_V3_s.__slots__ = [
    'stSelect',
    'stFix',
]
struct_Aynr_Manual_Attr_V3_s._fields_ = [
    ('stSelect', RK_YNR_Params_V3_Select_t),
    ('stFix', RK_YNR_Fix_V3_t),
]

Aynr_Manual_Attr_V3_t = struct_Aynr_Manual_Attr_V3_s# /root/camera_engine_rkaiq/include/algos/aynr3/rk_aiq_types_aynr_algo_int_v3.h: 158

# /root/camera_engine_rkaiq/include/algos/aynr3/rk_aiq_types_aynr_algo_int_v3.h: 167
class struct_Aynr_Auto_Attr_V3_s(Structure):
    pass

struct_Aynr_Auto_Attr_V3_s.__slots__ = [
    'stParams',
    'stSelect',
]
struct_Aynr_Auto_Attr_V3_s._fields_ = [
    ('stParams', RK_YNR_Params_V3_t),
    ('stSelect', RK_YNR_Params_V3_Select_t),
]

Aynr_Auto_Attr_V3_t = struct_Aynr_Auto_Attr_V3_s# /root/camera_engine_rkaiq/include/algos/aynr3/rk_aiq_types_aynr_algo_int_v3.h: 167

# /root/camera_engine_rkaiq/include/algos/aynr3/rk_aiq_types_aynr_algo_int_v3.h: 203
class struct_rk_aiq_ynr_attrib_v3_s(Structure):
    pass

struct_rk_aiq_ynr_attrib_v3_s.__slots__ = [
    'sync',
    'eMode',
    'stAuto',
    'stManual',
]
struct_rk_aiq_ynr_attrib_v3_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('eMode', Aynr_OPMode_V3_t),
    ('stAuto', Aynr_Auto_Attr_V3_t),
    ('stManual', Aynr_Manual_Attr_V3_t),
]

rk_aiq_ynr_attrib_v3_t = struct_rk_aiq_ynr_attrib_v3_s# /root/camera_engine_rkaiq/include/algos/aynr3/rk_aiq_types_aynr_algo_int_v3.h: 203

# /root/camera_engine_rkaiq/include/algos/aynr3/rk_aiq_types_aynr_algo_int_v3.h: 218
class struct_rk_aiq_ynr_strength_v3_s(Structure):
    pass

struct_rk_aiq_ynr_strength_v3_s.__slots__ = [
    'sync',
    'percent',
    'strength_enable',
]
struct_rk_aiq_ynr_strength_v3_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('percent', c_float),
    ('strength_enable', c_bool),
]

rk_aiq_ynr_strength_v3_t = struct_rk_aiq_ynr_strength_v3_s# /root/camera_engine_rkaiq/include/algos/aynr3/rk_aiq_types_aynr_algo_int_v3.h: 218

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_aynr_v3.h: 31
if _libs["rkaiq"].has("rk_aiq_user_api2_aynrV3_SetAttrib", "cdecl"):
    rk_aiq_user_api2_aynrV3_SetAttrib = _libs["rkaiq"].get("rk_aiq_user_api2_aynrV3_SetAttrib", "cdecl")
    rk_aiq_user_api2_aynrV3_SetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_ynr_attrib_v3_t)]
    rk_aiq_user_api2_aynrV3_SetAttrib.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_aynr_v3.h: 34
if _libs["rkaiq"].has("rk_aiq_user_api2_aynrV3_GetAttrib", "cdecl"):
    rk_aiq_user_api2_aynrV3_GetAttrib = _libs["rkaiq"].get("rk_aiq_user_api2_aynrV3_GetAttrib", "cdecl")
    rk_aiq_user_api2_aynrV3_GetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_ynr_attrib_v3_t)]
    rk_aiq_user_api2_aynrV3_GetAttrib.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_aynr_v3.h: 37
if _libs["rkaiq"].has("rk_aiq_user_api2_aynrV3_SetStrength", "cdecl"):
    rk_aiq_user_api2_aynrV3_SetStrength = _libs["rkaiq"].get("rk_aiq_user_api2_aynrV3_SetStrength", "cdecl")
    rk_aiq_user_api2_aynrV3_SetStrength.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_ynr_strength_v3_t)]
    rk_aiq_user_api2_aynrV3_SetStrength.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_aynr_v3.h: 40
if _libs["rkaiq"].has("rk_aiq_user_api2_aynrV3_GetStrength", "cdecl"):
    rk_aiq_user_api2_aynrV3_GetStrength = _libs["rkaiq"].get("rk_aiq_user_api2_aynrV3_GetStrength", "cdecl")
    rk_aiq_user_api2_aynrV3_GetStrength.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_ynr_strength_v3_t)]
    rk_aiq_user_api2_aynrV3_GetStrength.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_aynr_v3.h: 43
if _libs["rkaiq"].has("rk_aiq_user_api2_aynrV3_GetInfo", "cdecl"):
    rk_aiq_user_api2_aynrV3_GetInfo = _libs["rkaiq"].get("rk_aiq_user_api2_aynrV3_GetInfo", "cdecl")
    rk_aiq_user_api2_aynrV3_GetInfo.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_ynr_info_v3_t)]
    rk_aiq_user_api2_aynrV3_GetInfo.restype = XCamReturn

# /root/camera_engine_rkaiq/include/common/rk_aiq.h: 37
class struct_rk_aiq_metas_s(Structure):
    pass

struct_rk_aiq_metas_s.__slots__ = [
    'frame_id',
]
struct_rk_aiq_metas_s._fields_ = [
    ('frame_id', uint32_t),
]

rk_aiq_metas_t = struct_rk_aiq_metas_s# /root/camera_engine_rkaiq/include/common/rk_aiq.h: 37

# /root/camera_engine_rkaiq/include/common/rk_aiq.h: 42
class struct_rk_aiq_multi_cam_s(Structure):
    pass

struct_rk_aiq_multi_cam_s.__slots__ = [
    'multi_cam_id',
    'cam_count',
]
struct_rk_aiq_multi_cam_s._fields_ = [
    ('multi_cam_id', c_int * int(8)),
    ('cam_count', c_int),
]

rk_aiq_multi_cam_t = struct_rk_aiq_multi_cam_s# /root/camera_engine_rkaiq/include/common/rk_aiq.h: 42

# /root/camera_engine_rkaiq/include/common/rk_aiq.h: 49
class struct_rk_aiq_hwevt_s(Structure):
    pass

struct_rk_aiq_hwevt_s.__slots__ = [
    'cam_id',
    'aiq_status',
    'ctx',
    'multi_cam',
]
struct_rk_aiq_hwevt_s._fields_ = [
    ('cam_id', c_int),
    ('aiq_status', c_int),
    ('ctx', POINTER(None)),
    ('multi_cam', rk_aiq_multi_cam_t),
]

rk_aiq_hwevt_t = struct_rk_aiq_hwevt_s# /root/camera_engine_rkaiq/include/common/rk_aiq.h: 49

# /root/camera_engine_rkaiq/include/common/rk_aiq.h: 57
class struct_rk_aiq_err_msg_s(Structure):
    pass

struct_rk_aiq_err_msg_s.__slots__ = [
    'err_code',
]
struct_rk_aiq_err_msg_s._fields_ = [
    ('err_code', c_int),
]

rk_aiq_err_msg_t = struct_rk_aiq_err_msg_s# /root/camera_engine_rkaiq/include/common/rk_aiq.h: 57

# /root/camera_engine_rkaiq/include/common/rk_aiq.h: 67
class struct_rk_aiq_ver_info_s(Structure):
    pass

struct_rk_aiq_ver_info_s.__slots__ = [
    'aiq_ver',
    'iq_parser_ver',
    'iq_parser_magic_code',
    'awb_algo_ver',
    'ae_algo_ver',
    'af_algo_ver',
    'ahdr_algo_ver',
]
struct_rk_aiq_ver_info_s._fields_ = [
    ('aiq_ver', c_char * int(16)),
    ('iq_parser_ver', c_char * int(16)),
    ('iq_parser_magic_code', uint32_t),
    ('awb_algo_ver', c_char * int(16)),
    ('ae_algo_ver', c_char * int(16)),
    ('af_algo_ver', c_char * int(16)),
    ('ahdr_algo_ver', c_char * int(16)),
]

rk_aiq_ver_info_t = struct_rk_aiq_ver_info_s# /root/camera_engine_rkaiq/include/common/rk_aiq.h: 67

rk_aiq_error_cb = CFUNCTYPE(UNCHECKED(XCamReturn), POINTER(rk_aiq_err_msg_t))# /root/camera_engine_rkaiq/include/common/rk_aiq.h: 69

rk_aiq_metas_cb = CFUNCTYPE(UNCHECKED(XCamReturn), POINTER(rk_aiq_metas_t))# /root/camera_engine_rkaiq/include/common/rk_aiq.h: 70

rk_aiq_hwevt_cb = CFUNCTYPE(UNCHECKED(XCamReturn), POINTER(rk_aiq_hwevt_t))# /root/camera_engine_rkaiq/include/common/rk_aiq.h: 71

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_sysctl.h: 52
if _libs["rkaiq"].has("rk_aiq_uapi2_sysctl_preInit", "cdecl"):
    rk_aiq_uapi2_sysctl_preInit = _libs["rkaiq"].get("rk_aiq_uapi2_sysctl_preInit", "cdecl")
    rk_aiq_uapi2_sysctl_preInit.argtypes = [String, rk_aiq_working_mode_t, String]
    rk_aiq_uapi2_sysctl_preInit.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_sysctl.h: 57
if _libs["rkaiq"].has("rk_aiq_uapi2_sysctl_regHwEvtCb", "cdecl"):
    rk_aiq_uapi2_sysctl_regHwEvtCb = _libs["rkaiq"].get("rk_aiq_uapi2_sysctl_regHwEvtCb", "cdecl")
    rk_aiq_uapi2_sysctl_regHwEvtCb.argtypes = [String, rk_aiq_hwevt_cb, POINTER(None)]
    rk_aiq_uapi2_sysctl_regHwEvtCb.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_sysctl.h: 73
if _libs["rkaiq"].has("rk_aiq_uapi2_sysctl_init", "cdecl"):
    rk_aiq_uapi2_sysctl_init = _libs["rkaiq"].get("rk_aiq_uapi2_sysctl_init", "cdecl")
    rk_aiq_uapi2_sysctl_init.argtypes = [String, String, rk_aiq_error_cb, rk_aiq_metas_cb]
    rk_aiq_uapi2_sysctl_init.restype = POINTER(rk_aiq_sys_ctx_t)

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_sysctl.h: 86
if _libs["rkaiq"].has("rk_aiq_uapi2_sysctl_deinit", "cdecl"):
    rk_aiq_uapi2_sysctl_deinit = _libs["rkaiq"].get("rk_aiq_uapi2_sysctl_deinit", "cdecl")
    rk_aiq_uapi2_sysctl_deinit.argtypes = [POINTER(rk_aiq_sys_ctx_t)]
    rk_aiq_uapi2_sysctl_deinit.restype = None

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_sysctl.h: 101
if _libs["rkaiq"].has("rk_aiq_uapi2_sysctl_prepare", "cdecl"):
    rk_aiq_uapi2_sysctl_prepare = _libs["rkaiq"].get("rk_aiq_uapi2_sysctl_prepare", "cdecl")
    rk_aiq_uapi2_sysctl_prepare.argtypes = [POINTER(rk_aiq_sys_ctx_t), uint32_t, uint32_t, rk_aiq_working_mode_t]
    rk_aiq_uapi2_sysctl_prepare.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_sysctl.h: 115
if _libs["rkaiq"].has("rk_aiq_uapi2_sysctl_start", "cdecl"):
    rk_aiq_uapi2_sysctl_start = _libs["rkaiq"].get("rk_aiq_uapi2_sysctl_start", "cdecl")
    rk_aiq_uapi2_sysctl_start.argtypes = [POINTER(rk_aiq_sys_ctx_t)]
    rk_aiq_uapi2_sysctl_start.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_sysctl.h: 125
if _libs["rkaiq"].has("rk_aiq_uapi2_sysctl_stop", "cdecl"):
    rk_aiq_uapi2_sysctl_stop = _libs["rkaiq"].get("rk_aiq_uapi2_sysctl_stop", "cdecl")
    rk_aiq_uapi2_sysctl_stop.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_bool]
    rk_aiq_uapi2_sysctl_stop.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_sysctl.h: 133
if _libs["rkaiq"].has("rk_aiq_uapi2_get_version_info", "cdecl"):
    rk_aiq_uapi2_get_version_info = _libs["rkaiq"].get("rk_aiq_uapi2_get_version_info", "cdecl")
    rk_aiq_uapi2_get_version_info.argtypes = [POINTER(rk_aiq_ver_info_t)]
    rk_aiq_uapi2_get_version_info.restype = None

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_sysctl.h: 141
if _libs["rkaiq"].has("rk_aiq_uapi2_sysctl_updateIq", "cdecl"):
    rk_aiq_uapi2_sysctl_updateIq = _libs["rkaiq"].get("rk_aiq_uapi2_sysctl_updateIq", "cdecl")
    rk_aiq_uapi2_sysctl_updateIq.argtypes = [POINTER(rk_aiq_sys_ctx_t), String]
    rk_aiq_uapi2_sysctl_updateIq.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_sysctl.h: 145
if _libs["rkaiq"].has("rk_aiq_uapi2_sysctl_getModuleCtl", "cdecl"):
    rk_aiq_uapi2_sysctl_getModuleCtl = _libs["rkaiq"].get("rk_aiq_uapi2_sysctl_getModuleCtl", "cdecl")
    rk_aiq_uapi2_sysctl_getModuleCtl.argtypes = [POINTER(rk_aiq_sys_ctx_t), rk_aiq_module_id_t, POINTER(c_bool)]
    rk_aiq_uapi2_sysctl_getModuleCtl.restype = c_int32

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_sysctl.h: 149
if _libs["rkaiq"].has("rk_aiq_uapi2_sysctl_setModuleCtl", "cdecl"):
    rk_aiq_uapi2_sysctl_setModuleCtl = _libs["rkaiq"].get("rk_aiq_uapi2_sysctl_setModuleCtl", "cdecl")
    rk_aiq_uapi2_sysctl_setModuleCtl.argtypes = [POINTER(rk_aiq_sys_ctx_t), rk_aiq_module_id_t, c_bool]
    rk_aiq_uapi2_sysctl_setModuleCtl.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_sysctl.h: 162
if _libs["rkaiq"].has("rk_aiq_uapi2_sysctl_getAxlibStatus", "cdecl"):
    rk_aiq_uapi2_sysctl_getAxlibStatus = _libs["rkaiq"].get("rk_aiq_uapi2_sysctl_getAxlibStatus", "cdecl")
    rk_aiq_uapi2_sysctl_getAxlibStatus.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_int, c_int]
    rk_aiq_uapi2_sysctl_getAxlibStatus.restype = c_bool

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_sysctl.h: 184
if _libs["rkaiq"].has("rk_aiq_uapi2_sysctl_enableAxlib", "cdecl"):
    rk_aiq_uapi2_sysctl_enableAxlib = _libs["rkaiq"].get("rk_aiq_uapi2_sysctl_enableAxlib", "cdecl")
    rk_aiq_uapi2_sysctl_enableAxlib.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_int, c_int, c_bool]
    rk_aiq_uapi2_sysctl_enableAxlib.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_sysctl.h: 199
if _libs["rkaiq"].has("rk_aiq_uapi2_sysctl_getEnabledAxlibCtx", "cdecl"):
    rk_aiq_uapi2_sysctl_getEnabledAxlibCtx = _libs["rkaiq"].get("rk_aiq_uapi2_sysctl_getEnabledAxlibCtx", "cdecl")
    rk_aiq_uapi2_sysctl_getEnabledAxlibCtx.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_int]
    rk_aiq_uapi2_sysctl_getEnabledAxlibCtx.restype = POINTER(RkAiqAlgoContext)

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_sysctl.h: 205
if _libs["rkaiq"].has("rk_aiq_uapi2_sysctl_getStaticMetas", "cdecl"):
    rk_aiq_uapi2_sysctl_getStaticMetas = _libs["rkaiq"].get("rk_aiq_uapi2_sysctl_getStaticMetas", "cdecl")
    rk_aiq_uapi2_sysctl_getStaticMetas.argtypes = [String, POINTER(rk_aiq_static_info_t)]
    rk_aiq_uapi2_sysctl_getStaticMetas.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_sysctl.h: 215
if _libs["rkaiq"].has("rk_aiq_uapi2_sysctl_enumStaticMetas", "cdecl"):
    rk_aiq_uapi2_sysctl_enumStaticMetas = _libs["rkaiq"].get("rk_aiq_uapi2_sysctl_enumStaticMetas", "cdecl")
    rk_aiq_uapi2_sysctl_enumStaticMetas.argtypes = [c_int, POINTER(rk_aiq_static_info_t)]
    rk_aiq_uapi2_sysctl_enumStaticMetas.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_sysctl.h: 222
if _libs["rkaiq"].has("rk_aiq_uapi2_sysctl_getBindedSnsEntNmByVd", "cdecl"):
    rk_aiq_uapi2_sysctl_getBindedSnsEntNmByVd = _libs["rkaiq"].get("rk_aiq_uapi2_sysctl_getBindedSnsEntNmByVd", "cdecl")
    rk_aiq_uapi2_sysctl_getBindedSnsEntNmByVd.argtypes = [String]
    rk_aiq_uapi2_sysctl_getBindedSnsEntNmByVd.restype = c_char_p

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_sysctl.h: 231
if _libs["rkaiq"].has("rk_aiq_uapi2_sysctl_getCrop", "cdecl"):
    rk_aiq_uapi2_sysctl_getCrop = _libs["rkaiq"].get("rk_aiq_uapi2_sysctl_getCrop", "cdecl")
    rk_aiq_uapi2_sysctl_getCrop.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_rect_t)]
    rk_aiq_uapi2_sysctl_getCrop.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_sysctl.h: 242
if _libs["rkaiq"].has("rk_aiq_uapi2_sysctl_setCpsLtCfg", "cdecl"):
    rk_aiq_uapi2_sysctl_setCpsLtCfg = _libs["rkaiq"].get("rk_aiq_uapi2_sysctl_setCpsLtCfg", "cdecl")
    rk_aiq_uapi2_sysctl_setCpsLtCfg.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_cpsl_cfg_t)]
    rk_aiq_uapi2_sysctl_setCpsLtCfg.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_sysctl.h: 252
if _libs["rkaiq"].has("rk_aiq_uapi2_sysctl_getCpsLtInfo", "cdecl"):
    rk_aiq_uapi2_sysctl_getCpsLtInfo = _libs["rkaiq"].get("rk_aiq_uapi2_sysctl_getCpsLtInfo", "cdecl")
    rk_aiq_uapi2_sysctl_getCpsLtInfo.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_cpsl_info_t)]
    rk_aiq_uapi2_sysctl_getCpsLtInfo.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_sysctl.h: 262
if _libs["rkaiq"].has("rk_aiq_uapi2_sysctl_queryCpsLtCap", "cdecl"):
    rk_aiq_uapi2_sysctl_queryCpsLtCap = _libs["rkaiq"].get("rk_aiq_uapi2_sysctl_queryCpsLtCap", "cdecl")
    rk_aiq_uapi2_sysctl_queryCpsLtCap.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_cpsl_cap_t)]
    rk_aiq_uapi2_sysctl_queryCpsLtCap.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_sysctl.h: 273
if _libs["rkaiq"].has("rk_aiq_uapi2_sysctl_setSharpFbcRotation", "cdecl"):
    rk_aiq_uapi2_sysctl_setSharpFbcRotation = _libs["rkaiq"].get("rk_aiq_uapi2_sysctl_setSharpFbcRotation", "cdecl")
    rk_aiq_uapi2_sysctl_setSharpFbcRotation.argtypes = [POINTER(rk_aiq_sys_ctx_t), rk_aiq_rotation_t]
    rk_aiq_uapi2_sysctl_setSharpFbcRotation.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_sysctl.h: 283
if _libs["rkaiq"].has("rk_aiq_uapi2_sysctl_setMulCamConc", "cdecl"):
    rk_aiq_uapi2_sysctl_setMulCamConc = _libs["rkaiq"].get("rk_aiq_uapi2_sysctl_setMulCamConc", "cdecl")
    rk_aiq_uapi2_sysctl_setMulCamConc.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_bool]
    rk_aiq_uapi2_sysctl_setMulCamConc.restype = None

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_sysctl.h: 291
if _libs["rkaiq"].has("rk_aiq_uapi2_sysctl_regMemsSensorIntf", "cdecl"):
    rk_aiq_uapi2_sysctl_regMemsSensorIntf = _libs["rkaiq"].get("rk_aiq_uapi2_sysctl_regMemsSensorIntf", "cdecl")
    rk_aiq_uapi2_sysctl_regMemsSensorIntf.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_mems_sensor_intf_t)]
    rk_aiq_uapi2_sysctl_regMemsSensorIntf.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_sysctl.h: 304
if _libs["rkaiq"].has("rk_aiq_uapi2_sysctl_switch_scene", "cdecl"):
    rk_aiq_uapi2_sysctl_switch_scene = _libs["rkaiq"].get("rk_aiq_uapi2_sysctl_switch_scene", "cdecl")
    rk_aiq_uapi2_sysctl_switch_scene.argtypes = [POINTER(rk_aiq_sys_ctx_t), String, String]
    rk_aiq_uapi2_sysctl_switch_scene.restype = c_int

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_sysctl.h: 309
if _libs["rkaiq"].has("rk_aiq_uapi2_sysctl_tuning", "cdecl"):
    rk_aiq_uapi2_sysctl_tuning = _libs["rkaiq"].get("rk_aiq_uapi2_sysctl_tuning", "cdecl")
    rk_aiq_uapi2_sysctl_tuning.argtypes = [POINTER(rk_aiq_sys_ctx_t), String]
    rk_aiq_uapi2_sysctl_tuning.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_sysctl.h: 311
if _libs["rkaiq"].has("rk_aiq_uapi2_sysctl_readiq", "cdecl"):
    rk_aiq_uapi2_sysctl_readiq = _libs["rkaiq"].get("rk_aiq_uapi2_sysctl_readiq", "cdecl")
    rk_aiq_uapi2_sysctl_readiq.argtypes = [POINTER(rk_aiq_sys_ctx_t), String]
    if sizeof(c_int) == sizeof(c_void_p):
        rk_aiq_uapi2_sysctl_readiq.restype = ReturnString
    else:
        rk_aiq_uapi2_sysctl_readiq.restype = String
        rk_aiq_uapi2_sysctl_readiq.errcheck = ReturnString

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_sysctl.h: 314
if _libs["rkaiq"].has("rk_aiq_uapi2_sysctl_preInit_scene", "cdecl"):
    rk_aiq_uapi2_sysctl_preInit_scene = _libs["rkaiq"].get("rk_aiq_uapi2_sysctl_preInit_scene", "cdecl")
    rk_aiq_uapi2_sysctl_preInit_scene.argtypes = [String, String, String]
    rk_aiq_uapi2_sysctl_preInit_scene.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_sysctl.h: 327
if _libs["rkaiq"].has("rk_aiq_uapi2_sysctl_preInit_iq_addr", "cdecl"):
    rk_aiq_uapi2_sysctl_preInit_iq_addr = _libs["rkaiq"].get("rk_aiq_uapi2_sysctl_preInit_iq_addr", "cdecl")
    rk_aiq_uapi2_sysctl_preInit_iq_addr.argtypes = [String, POINTER(None), c_size_t]
    rk_aiq_uapi2_sysctl_preInit_iq_addr.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_sysctl.h: 332
class struct_rk_aiq_ctx_camInfo_s(Structure):
    pass

struct_rk_aiq_ctx_camInfo_s.__slots__ = [
    'sns_ent_nm',
    'sns_camPhyId',
]
struct_rk_aiq_ctx_camInfo_s._fields_ = [
    ('sns_ent_nm', String),
    ('sns_camPhyId', c_int),
]

rk_aiq_ctx_camInfo_t = struct_rk_aiq_ctx_camInfo_s# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_sysctl.h: 332

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_sysctl.h: 335
if _libs["rkaiq"].has("rk_aiq_uapi2_sysctl_getCamInfos", "cdecl"):
    rk_aiq_uapi2_sysctl_getCamInfos = _libs["rkaiq"].get("rk_aiq_uapi2_sysctl_getCamInfos", "cdecl")
    rk_aiq_uapi2_sysctl_getCamInfos.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_ctx_camInfo_t)]
    rk_aiq_uapi2_sysctl_getCamInfos.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_sysctl.h: 346
if _libs["rkaiq"].has("rk_aiq_uapi2_sysctl_get3AStats", "cdecl"):
    rk_aiq_uapi2_sysctl_get3AStats = _libs["rkaiq"].get("rk_aiq_uapi2_sysctl_get3AStats", "cdecl")
    rk_aiq_uapi2_sysctl_get3AStats.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_isp_stats_t)]
    rk_aiq_uapi2_sysctl_get3AStats.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_sysctl.h: 361
if _libs["rkaiq"].has("rk_aiq_uapi2_sysctl_get3AStatsBlk", "cdecl"):
    rk_aiq_uapi2_sysctl_get3AStatsBlk = _libs["rkaiq"].get("rk_aiq_uapi2_sysctl_get3AStatsBlk", "cdecl")
    rk_aiq_uapi2_sysctl_get3AStatsBlk.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(POINTER(rk_aiq_isp_stats_t)), c_int]
    rk_aiq_uapi2_sysctl_get3AStatsBlk.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_sysctl.h: 373
if _libs["rkaiq"].has("rk_aiq_uapi2_sysctl_release3AStatsRef", "cdecl"):
    rk_aiq_uapi2_sysctl_release3AStatsRef = _libs["rkaiq"].get("rk_aiq_uapi2_sysctl_release3AStatsRef", "cdecl")
    rk_aiq_uapi2_sysctl_release3AStatsRef.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_isp_stats_t)]
    rk_aiq_uapi2_sysctl_release3AStatsRef.restype = None

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_sysctl.h: 384
if _libs["rkaiq"].has("rk_aiq_uapi2_sysctl_prepareRkRaw", "cdecl"):
    rk_aiq_uapi2_sysctl_prepareRkRaw = _libs["rkaiq"].get("rk_aiq_uapi2_sysctl_prepareRkRaw", "cdecl")
    rk_aiq_uapi2_sysctl_prepareRkRaw.argtypes = [POINTER(rk_aiq_sys_ctx_t), rk_aiq_raw_prop_t]
    rk_aiq_uapi2_sysctl_prepareRkRaw.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_sysctl.h: 398
if _libs["rkaiq"].has("rk_aiq_uapi2_sysctl_enqueueRkRawBuf", "cdecl"):
    rk_aiq_uapi2_sysctl_enqueueRkRawBuf = _libs["rkaiq"].get("rk_aiq_uapi2_sysctl_enqueueRkRawBuf", "cdecl")
    rk_aiq_uapi2_sysctl_enqueueRkRawBuf.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(None), c_bool]
    rk_aiq_uapi2_sysctl_enqueueRkRawBuf.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_sysctl.h: 409
if _libs["rkaiq"].has("rk_aiq_uapi2_sysctl_enqueueRkRawFile", "cdecl"):
    rk_aiq_uapi2_sysctl_enqueueRkRawFile = _libs["rkaiq"].get("rk_aiq_uapi2_sysctl_enqueueRkRawFile", "cdecl")
    rk_aiq_uapi2_sysctl_enqueueRkRawFile.argtypes = [POINTER(rk_aiq_sys_ctx_t), String]
    rk_aiq_uapi2_sysctl_enqueueRkRawFile.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_sysctl.h: 426
if _libs["rkaiq"].has("rk_aiq_uapi2_sysctl_registRkRawCb", "cdecl"):
    rk_aiq_uapi2_sysctl_registRkRawCb = _libs["rkaiq"].get("rk_aiq_uapi2_sysctl_registRkRawCb", "cdecl")
    rk_aiq_uapi2_sysctl_registRkRawCb.argtypes = [POINTER(rk_aiq_sys_ctx_t), CFUNCTYPE(UNCHECKED(None), POINTER(None))]
    rk_aiq_uapi2_sysctl_registRkRawCb.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_sysctl.h: 435
if _libs["rkaiq"].has("rk_aiq_uapi2_sysctl_getWorkingMode", "cdecl"):
    rk_aiq_uapi2_sysctl_getWorkingMode = _libs["rkaiq"].get("rk_aiq_uapi2_sysctl_getWorkingMode", "cdecl")
    rk_aiq_uapi2_sysctl_getWorkingMode.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_working_mode_t)]
    rk_aiq_uapi2_sysctl_getWorkingMode.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_sysctl.h: 445
if _libs["rkaiq"].has("rk_aiq_uapi2_sysctl_tuning_enable", "cdecl"):
    rk_aiq_uapi2_sysctl_tuning_enable = _libs["rkaiq"].get("rk_aiq_uapi2_sysctl_tuning_enable", "cdecl")
    rk_aiq_uapi2_sysctl_tuning_enable.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_bool]
    rk_aiq_uapi2_sysctl_tuning_enable.restype = c_int

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_sysctl.h: 448
if _libs["rkaiq"].has("rk_aiq_uapi2_sysctl_resetCam", "cdecl"):
    rk_aiq_uapi2_sysctl_resetCam = _libs["rkaiq"].get("rk_aiq_uapi2_sysctl_resetCam", "cdecl")
    rk_aiq_uapi2_sysctl_resetCam.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_int]
    rk_aiq_uapi2_sysctl_resetCam.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_camgroup.h: 61
class struct_rk_aiq_camgroup_ctx_s(Structure):
    pass

rk_aiq_camgroup_ctx_t = struct_rk_aiq_camgroup_ctx_s# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_camgroup.h: 61

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_camgroup.h: 73
class struct_rk_aiq_camgroup_instance_cfg_s(Structure):
    pass

struct_rk_aiq_camgroup_instance_cfg_s.__slots__ = [
    'sns_ent_nm_array',
    'sns_num',
    'config_file_dir',
    'single_iq_file',
    'group_iq_file',
    'overlap_map_file',
    'pHwEvt_cb',
    'pHwEvtCbCtx',
]
struct_rk_aiq_camgroup_instance_cfg_s._fields_ = [
    ('sns_ent_nm_array', POINTER(c_char) * int(8)),
    ('sns_num', c_int),
    ('config_file_dir', String),
    ('single_iq_file', String),
    ('group_iq_file', String),
    ('overlap_map_file', String),
    ('pHwEvt_cb', rk_aiq_hwevt_cb),
    ('pHwEvtCbCtx', POINTER(None)),
]

rk_aiq_camgroup_instance_cfg_t = struct_rk_aiq_camgroup_instance_cfg_s# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_camgroup.h: 73

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_camgroup.h: 79
class struct_rk_aiq_camgroup_camInfos_s(Structure):
    pass

struct_rk_aiq_camgroup_camInfos_s.__slots__ = [
    'valid_sns_num',
    'sns_ent_nm',
    'sns_camPhyId',
]
struct_rk_aiq_camgroup_camInfos_s._fields_ = [
    ('valid_sns_num', c_int),
    ('sns_ent_nm', POINTER(c_char) * int(8)),
    ('sns_camPhyId', c_int * int(8)),
]

rk_aiq_camgroup_camInfos_t = struct_rk_aiq_camgroup_camInfos_s# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_camgroup.h: 79

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_camgroup.h: 81
if _libs["rkaiq"].has("rk_aiq_uapi2_camgroup_create", "cdecl"):
    rk_aiq_uapi2_camgroup_create = _libs["rkaiq"].get("rk_aiq_uapi2_camgroup_create", "cdecl")
    rk_aiq_uapi2_camgroup_create.argtypes = [POINTER(rk_aiq_camgroup_instance_cfg_t)]
    rk_aiq_uapi2_camgroup_create.restype = POINTER(rk_aiq_camgroup_ctx_t)

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_camgroup.h: 84
class struct_RK_PS_SrcOverlapMap(Structure):
    pass

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_camgroup.h: 84
if _libs["rkaiq"].has("rk_aiq_uapi2_camgroup_getOverlapMap", "cdecl"):
    rk_aiq_uapi2_camgroup_getOverlapMap = _libs["rkaiq"].get("rk_aiq_uapi2_camgroup_getOverlapMap", "cdecl")
    rk_aiq_uapi2_camgroup_getOverlapMap.argtypes = [POINTER(rk_aiq_camgroup_ctx_t)]
    rk_aiq_uapi2_camgroup_getOverlapMap.restype = POINTER(struct_RK_PS_SrcOverlapMap)

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_camgroup.h: 88
if _libs["rkaiq"].has("rk_aiq_uapi2_camgroup_getOverlapMap_from_file", "cdecl"):
    rk_aiq_uapi2_camgroup_getOverlapMap_from_file = _libs["rkaiq"].get("rk_aiq_uapi2_camgroup_getOverlapMap_from_file", "cdecl")
    rk_aiq_uapi2_camgroup_getOverlapMap_from_file.argtypes = [String, POINTER(POINTER(struct_RK_PS_SrcOverlapMap))]
    rk_aiq_uapi2_camgroup_getOverlapMap_from_file.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_camgroup.h: 90
if _libs["rkaiq"].has("rk_aiq_uapi2_camgroup_getAiqCtxBySnsNm", "cdecl"):
    rk_aiq_uapi2_camgroup_getAiqCtxBySnsNm = _libs["rkaiq"].get("rk_aiq_uapi2_camgroup_getAiqCtxBySnsNm", "cdecl")
    rk_aiq_uapi2_camgroup_getAiqCtxBySnsNm.argtypes = [POINTER(rk_aiq_camgroup_ctx_t), String]
    rk_aiq_uapi2_camgroup_getAiqCtxBySnsNm.restype = POINTER(rk_aiq_sys_ctx_t)

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_camgroup.h: 94
if _libs["rkaiq"].has("rk_aiq_uapi2_camgroup_bind", "cdecl"):
    rk_aiq_uapi2_camgroup_bind = _libs["rkaiq"].get("rk_aiq_uapi2_camgroup_bind", "cdecl")
    rk_aiq_uapi2_camgroup_bind.argtypes = [POINTER(rk_aiq_camgroup_ctx_t), POINTER(POINTER(rk_aiq_sys_ctx_t)), c_int]
    rk_aiq_uapi2_camgroup_bind.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_camgroup.h: 97
if _libs["rkaiq"].has("rk_aiq_uapi2_camgroup_unbind", "cdecl"):
    rk_aiq_uapi2_camgroup_unbind = _libs["rkaiq"].get("rk_aiq_uapi2_camgroup_unbind", "cdecl")
    rk_aiq_uapi2_camgroup_unbind.argtypes = [POINTER(rk_aiq_camgroup_ctx_t), POINTER(POINTER(rk_aiq_sys_ctx_t)), c_int]
    rk_aiq_uapi2_camgroup_unbind.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_camgroup.h: 100
if _libs["rkaiq"].has("rk_aiq_uapi2_camgroup_prepare", "cdecl"):
    rk_aiq_uapi2_camgroup_prepare = _libs["rkaiq"].get("rk_aiq_uapi2_camgroup_prepare", "cdecl")
    rk_aiq_uapi2_camgroup_prepare.argtypes = [POINTER(rk_aiq_camgroup_ctx_t), rk_aiq_working_mode_t]
    rk_aiq_uapi2_camgroup_prepare.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_camgroup.h: 103
if _libs["rkaiq"].has("rk_aiq_uapi2_camgroup_start", "cdecl"):
    rk_aiq_uapi2_camgroup_start = _libs["rkaiq"].get("rk_aiq_uapi2_camgroup_start", "cdecl")
    rk_aiq_uapi2_camgroup_start.argtypes = [POINTER(rk_aiq_camgroup_ctx_t)]
    rk_aiq_uapi2_camgroup_start.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_camgroup.h: 106
if _libs["rkaiq"].has("rk_aiq_uapi2_camgroup_stop", "cdecl"):
    rk_aiq_uapi2_camgroup_stop = _libs["rkaiq"].get("rk_aiq_uapi2_camgroup_stop", "cdecl")
    rk_aiq_uapi2_camgroup_stop.argtypes = [POINTER(rk_aiq_camgroup_ctx_t)]
    rk_aiq_uapi2_camgroup_stop.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_camgroup.h: 109
if _libs["rkaiq"].has("rk_aiq_uapi2_camgroup_destroy", "cdecl"):
    rk_aiq_uapi2_camgroup_destroy = _libs["rkaiq"].get("rk_aiq_uapi2_camgroup_destroy", "cdecl")
    rk_aiq_uapi2_camgroup_destroy.argtypes = [POINTER(rk_aiq_camgroup_ctx_t)]
    rk_aiq_uapi2_camgroup_destroy.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_camgroup.h: 112
if _libs["rkaiq"].has("rk_aiq_uapi2_camgroup_getCamInfos", "cdecl"):
    rk_aiq_uapi2_camgroup_getCamInfos = _libs["rkaiq"].get("rk_aiq_uapi2_camgroup_getCamInfos", "cdecl")
    rk_aiq_uapi2_camgroup_getCamInfos.argtypes = [POINTER(rk_aiq_camgroup_ctx_t), POINTER(rk_aiq_camgroup_camInfos_t)]
    rk_aiq_uapi2_camgroup_getCamInfos.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_camgroup.h: 115
if _libs["rkaiq"].has("rk_aiq_uapi2_camgroup_resetCam", "cdecl"):
    rk_aiq_uapi2_camgroup_resetCam = _libs["rkaiq"].get("rk_aiq_uapi2_camgroup_resetCam", "cdecl")
    rk_aiq_uapi2_camgroup_resetCam.argtypes = [POINTER(rk_aiq_camgroup_ctx_t), c_int]
    rk_aiq_uapi2_camgroup_resetCam.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_custom_ae.h: 32
class struct_rk_aiq_customAe_stats_s(Structure):
    pass

struct_rk_aiq_customAe_stats_s.__slots__ = [
    'rawae_stat',
    'extra',
    'linear_exp',
    'hdr_exp',
    'next',
]
struct_rk_aiq_customAe_stats_s._fields_ = [
    ('rawae_stat', Aec_Stat_Res_t * int(3)),
    ('extra', Aec_Stat_Res_t),
    ('linear_exp', RkAiqExpParamComb_t),
    ('hdr_exp', RkAiqExpParamComb_t * int(3)),
    ('next', POINTER(struct_rk_aiq_customAe_stats_s)),
]

rk_aiq_customAe_stats_t = struct_rk_aiq_customAe_stats_s# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_custom_ae.h: 43

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_custom_ae.h: 53
class struct_rk_aiq_i2c_data_s(Structure):
    pass

struct_rk_aiq_i2c_data_s.__slots__ = [
    'bValid',
    'nNumRegs',
    'pRegAddr',
    'pAddrByteNum',
    'pRegValue',
    'pValueByteNum',
    'pDelayFrames',
]
struct_rk_aiq_i2c_data_s._fields_ = [
    ('bValid', c_bool),
    ('nNumRegs', c_uint),
    ('pRegAddr', POINTER(c_uint)),
    ('pAddrByteNum', POINTER(c_uint)),
    ('pRegValue', POINTER(c_uint)),
    ('pValueByteNum', POINTER(c_uint)),
    ('pDelayFrames', POINTER(c_uint)),
]

rk_aiq_i2c_data_t = struct_rk_aiq_i2c_data_s# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_custom_ae.h: 53

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_custom_ae.h: 56
class struct_rk_aiq_customeAe_results_singel_s(Structure):
    pass

struct_rk_aiq_customeAe_results_singel_s.__slots__ = [
    'linear_exp',
    'hdr_exp',
    'exp_i2c_params',
    'meas_win',
    'meas_weight',
    'next',
]
struct_rk_aiq_customeAe_results_singel_s._fields_ = [
    ('linear_exp', RkAiqExpParamComb_t),
    ('hdr_exp', RkAiqExpParamComb_t * int(3)),
    ('exp_i2c_params', rk_aiq_i2c_data_t),
    ('meas_win', struct_window),
    ('meas_weight', c_ubyte * int((15 * 15))),
    ('next', POINTER(struct_rk_aiq_customeAe_results_singel_s)),
]

rk_aiq_customeAe_results_single_t = struct_rk_aiq_customeAe_results_singel_s# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_custom_ae.h: 68

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_custom_ae.h: 87
class struct_rk_aiq_customeAe_results_s(Structure):
    pass

struct_rk_aiq_customeAe_results_s.__slots__ = [
    'linear_exp',
    'hdr_exp',
    'exp_i2c_params',
    'meas_win',
    'meas_weight',
    'Iris',
    'frame_length_lines',
    'is_longfrm_mode',
    'next',
]
struct_rk_aiq_customeAe_results_s._fields_ = [
    ('linear_exp', RkAiqExpParamComb_t),
    ('hdr_exp', RkAiqExpParamComb_t * int(3)),
    ('exp_i2c_params', rk_aiq_i2c_data_t),
    ('meas_win', struct_window),
    ('meas_weight', c_ubyte * int((15 * 15))),
    ('Iris', RkAiqIrisParamComb_t),
    ('frame_length_lines', uint32_t),
    ('is_longfrm_mode', c_bool),
    ('next', POINTER(struct_rk_aiq_customeAe_results_singel_s)),
]

rk_aiq_customeAe_results_t = struct_rk_aiq_customeAe_results_s# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_custom_ae.h: 87

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_custom_ae.h: 101
class struct_rk_aiq_customeAe_cbs_s(Structure):
    pass

struct_rk_aiq_customeAe_cbs_s.__slots__ = [
    'pfn_ae_init',
    'pfn_ae_run',
    'pfn_ae_ctrl',
    'pfn_ae_exit',
]
struct_rk_aiq_customeAe_cbs_s._fields_ = [
    ('pfn_ae_init', CFUNCTYPE(UNCHECKED(c_int32), POINTER(None))),
    ('pfn_ae_run', CFUNCTYPE(UNCHECKED(c_int32), POINTER(None), POINTER(rk_aiq_customAe_stats_t), POINTER(rk_aiq_customeAe_results_t))),
    ('pfn_ae_ctrl', CFUNCTYPE(UNCHECKED(c_int32), POINTER(None), uint32_t, POINTER(None))),
    ('pfn_ae_exit', CFUNCTYPE(UNCHECKED(c_int32), POINTER(None))),
]

rk_aiq_customeAe_cbs_t = struct_rk_aiq_customeAe_cbs_s# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_custom_ae.h: 101

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_custom_ae.h: 111
if _libs["rkaiq"].has("rk_aiq_uapi2_customAE_register", "cdecl"):
    rk_aiq_uapi2_customAE_register = _libs["rkaiq"].get("rk_aiq_uapi2_customAE_register", "cdecl")
    rk_aiq_uapi2_customAE_register.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_customeAe_cbs_t)]
    rk_aiq_uapi2_customAE_register.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_custom_ae.h: 122
if _libs["rkaiq"].has("rk_aiq_uapi2_customAE_enable", "cdecl"):
    rk_aiq_uapi2_customAE_enable = _libs["rkaiq"].get("rk_aiq_uapi2_customAE_enable", "cdecl")
    rk_aiq_uapi2_customAE_enable.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_bool]
    rk_aiq_uapi2_customAE_enable.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_custom_ae.h: 131
if _libs["rkaiq"].has("rk_aiq_uapi2_customAE_unRegister", "cdecl"):
    rk_aiq_uapi2_customAE_unRegister = _libs["rkaiq"].get("rk_aiq_uapi2_customAE_unRegister", "cdecl")
    rk_aiq_uapi2_customAE_unRegister.argtypes = [POINTER(rk_aiq_sys_ctx_t)]
    rk_aiq_uapi2_customAE_unRegister.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_custom_awb.h: 28
class struct_rk_aiq_customAwb_stats_s(Structure):
    pass

struct_rk_aiq_customAwb_stats_s.__slots__ = [
    'light',
    'WpNo2',
    'blockResult',
    'multiwindowLightResult',
    'excWpRangeResult',
    'WpNoHist',
    'next',
]
struct_rk_aiq_customAwb_stats_s._fields_ = [
    ('light', rk_aiq_awb_stat_wp_res_light_v201_t * int(7)),
    ('WpNo2', c_int * int(7)),
    ('blockResult', rk_aiq_awb_stat_blk_res_v201_t * int((15 * 15))),
    ('multiwindowLightResult', rk_aiq_awb_stat_wp_res_light_v201_t * int(4)),
    ('excWpRangeResult', rk_aiq_awb_stat_wp_res_v201_t * int(4)),
    ('WpNoHist', c_uint * int(8)),
    ('next', POINTER(struct_rk_aiq_customAwb_stats_s)),
]

rk_aiq_customAwb_stats_t = struct_rk_aiq_customAwb_stats_s# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_custom_awb.h: 37

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_custom_awb.h: 74
class struct_rk_aiq_customAwb_hw_cfg_s(Structure):
    pass

struct_rk_aiq_customAwb_hw_cfg_s.__slots__ = [
    'awbEnable',
    'lscBypEnable',
    'frameChoose',
    'windowSet',
    'lightNum',
    'maxR',
    'minR',
    'maxG',
    'minG',
    'maxB',
    'minB',
    'maxY',
    'minY',
    'uvDetectionEnable',
    'uvRange_param',
    'xyDetectionEnable',
    'rgb2xy_param',
    'xyRange_param',
    'threeDyuvEnable',
    'threeDyuvIllu',
    'icrgb2RYuv_matrix',
    'ic3Dyuv2Range_param',
    'multiwindow_en',
    'multiwindow',
    'excludeWpRange',
    'wpDiffWeiEnable',
    'wpDiffwei_y',
    'wpDiffwei_w',
    'xyRangeTypeForWpHist',
    'blkWeightEnable',
    'blkWeight',
    'blkMeasureMode',
    'xyRangeTypeForBlkStatistics',
    'illIdxForBlkStatistics',
]
struct_rk_aiq_customAwb_hw_cfg_s._fields_ = [
    ('awbEnable', c_bool),
    ('lscBypEnable', c_bool),
    ('frameChoose', uint8_t),
    ('windowSet', c_ushort * int(4)),
    ('lightNum', c_ubyte),
    ('maxR', c_ushort),
    ('minR', c_ushort),
    ('maxG', c_ushort),
    ('minG', c_ushort),
    ('maxB', c_ushort),
    ('minB', c_ushort),
    ('maxY', c_ushort),
    ('minY', c_ushort),
    ('uvDetectionEnable', c_bool),
    ('uvRange_param', rk_aiq_awb_uv_range_para_t * int(7)),
    ('xyDetectionEnable', c_bool),
    ('rgb2xy_param', rk_aiq_rgb2xy_para_t),
    ('xyRange_param', rk_aiq_awb_xy_range_para_t * int(7)),
    ('threeDyuvEnable', c_bool),
    ('threeDyuvIllu', c_ushort * int(4)),
    ('icrgb2RYuv_matrix', c_short * int(12)),
    ('ic3Dyuv2Range_param', rk_aiq_awb_rt3dyuv_range_para_t * int(4)),
    ('multiwindow_en', c_bool),
    ('multiwindow', (c_ushort * int(4)) * int(4)),
    ('excludeWpRange', rk_aiq_awb_exc_range_v201_t * int(7)),
    ('wpDiffWeiEnable', c_bool),
    ('wpDiffwei_y', c_ubyte * int((8 + 1))),
    ('wpDiffwei_w', c_ubyte * int((8 + 1))),
    ('xyRangeTypeForWpHist', rk_aiq_awb_xy_type_v201_t),
    ('blkWeightEnable', c_bool),
    ('blkWeight', c_ubyte * int((15 * 15))),
    ('blkMeasureMode', rk_aiq_awb_blk_stat_mode_v201_t),
    ('xyRangeTypeForBlkStatistics', rk_aiq_awb_xy_type_v201_t),
    ('illIdxForBlkStatistics', rk_aiq_awb_blk_stat_realwp_ill_e),
]

rk_aiq_customAwb_hw_cfg_t = struct_rk_aiq_customAwb_hw_cfg_s# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_custom_awb.h: 74

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_custom_awb.h: 82
class struct_rk_aiq_customAwb_single_hw_cfg_t(Structure):
    pass

struct_rk_aiq_customAwb_single_hw_cfg_t.__slots__ = [
    'windowSet',
    'multiwindow_en',
    'multiwindow',
    'blkWeightEnable',
    'blkWeight',
]
struct_rk_aiq_customAwb_single_hw_cfg_t._fields_ = [
    ('windowSet', c_ushort * int(4)),
    ('multiwindow_en', c_bool),
    ('multiwindow', (c_ushort * int(4)) * int(4)),
    ('blkWeightEnable', c_bool),
    ('blkWeight', c_ubyte * int((15 * 15))),
]

rk_aiq_customAwb_single_hw_cfg_t = struct_rk_aiq_customAwb_single_hw_cfg_t# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_custom_awb.h: 82

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_custom_awb.h: 86
class struct_rk_aiq_customeAwb_single_results_s(Structure):
    pass

struct_rk_aiq_customeAwb_single_results_s.__slots__ = [
    'awb_gain_algo',
    'awbHwConfig',
    'next',
]
struct_rk_aiq_customeAwb_single_results_s._fields_ = [
    ('awb_gain_algo', rk_aiq_wb_gain_t),
    ('awbHwConfig', rk_aiq_customAwb_single_hw_cfg_t),
    ('next', POINTER(struct_rk_aiq_customeAwb_single_results_s)),
]

rk_aiq_customeAwb_single_results_t = struct_rk_aiq_customeAwb_single_results_s# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_custom_awb.h: 91

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_custom_awb.h: 102
class struct_rk_aiq_customeAwb_results_s(Structure):
    pass

struct_rk_aiq_customeAwb_results_s.__slots__ = [
    'IsConverged',
    'awb_gain_algo',
    'awb_smooth_factor',
    'awbHwConfig',
    'next',
]
struct_rk_aiq_customeAwb_results_s._fields_ = [
    ('IsConverged', c_bool),
    ('awb_gain_algo', rk_aiq_wb_gain_t),
    ('awb_smooth_factor', c_float),
    ('awbHwConfig', rk_aiq_customAwb_hw_cfg_t),
    ('next', POINTER(rk_aiq_customeAwb_single_results_t)),
]

rk_aiq_customeAwb_results_t = struct_rk_aiq_customeAwb_results_s# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_custom_awb.h: 102

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_custom_awb.h: 116
class struct_rk_aiq_customeAwb_cbs_s(Structure):
    pass

struct_rk_aiq_customeAwb_cbs_s.__slots__ = [
    'pfn_awb_init',
    'pfn_awb_run',
    'pfn_awb_ctrl',
    'pfn_awb_exit',
]
struct_rk_aiq_customeAwb_cbs_s._fields_ = [
    ('pfn_awb_init', CFUNCTYPE(UNCHECKED(c_int32), POINTER(None))),
    ('pfn_awb_run', CFUNCTYPE(UNCHECKED(c_int32), POINTER(None), POINTER(rk_aiq_customAwb_stats_t), POINTER(rk_aiq_customeAwb_results_t))),
    ('pfn_awb_ctrl', CFUNCTYPE(UNCHECKED(c_int32), POINTER(None), uint32_t, POINTER(None))),
    ('pfn_awb_exit', CFUNCTYPE(UNCHECKED(c_int32), POINTER(None))),
]

rk_aiq_customeAwb_cbs_t = struct_rk_aiq_customeAwb_cbs_s# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_custom_awb.h: 116

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_custom_awb.h: 126
if _libs["rkaiq"].has("rk_aiq_uapi2_customAWB_register", "cdecl"):
    rk_aiq_uapi2_customAWB_register = _libs["rkaiq"].get("rk_aiq_uapi2_customAWB_register", "cdecl")
    rk_aiq_uapi2_customAWB_register.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_customeAwb_cbs_t)]
    rk_aiq_uapi2_customAWB_register.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_custom_awb.h: 137
if _libs["rkaiq"].has("rk_aiq_uapi2_customAWB_enable", "cdecl"):
    rk_aiq_uapi2_customAWB_enable = _libs["rkaiq"].get("rk_aiq_uapi2_customAWB_enable", "cdecl")
    rk_aiq_uapi2_customAWB_enable.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_bool]
    rk_aiq_uapi2_customAWB_enable.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_custom_awb.h: 146
if _libs["rkaiq"].has("rk_aiq_uapi2_customAWB_unRegister", "cdecl"):
    rk_aiq_uapi2_customAWB_unRegister = _libs["rkaiq"].get("rk_aiq_uapi2_customAWB_unRegister", "cdecl")
    rk_aiq_uapi2_customAWB_unRegister.argtypes = [POINTER(rk_aiq_sys_ctx_t)]
    rk_aiq_uapi2_customAWB_unRegister.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_debug.h: 32
if _libs["rkaiq"].has("rk_aiq_uapi2_debug_captureRawYuvSync", "cdecl"):
    rk_aiq_uapi2_debug_captureRawYuvSync = _libs["rkaiq"].get("rk_aiq_uapi2_debug_captureRawYuvSync", "cdecl")
    rk_aiq_uapi2_debug_captureRawYuvSync.argtypes = [POINTER(rk_aiq_sys_ctx_t), capture_raw_t]
    rk_aiq_uapi2_debug_captureRawYuvSync.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_debug.h: 45
if _libs["rkaiq"].has("rk_aiq_uapi2_debug_captureRawSync", "cdecl"):
    rk_aiq_uapi2_debug_captureRawSync = _libs["rkaiq"].get("rk_aiq_uapi2_debug_captureRawSync", "cdecl")
    rk_aiq_uapi2_debug_captureRawSync.argtypes = [POINTER(rk_aiq_sys_ctx_t), capture_raw_t, c_int, String, String]
    rk_aiq_uapi2_debug_captureRawSync.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_debug.h: 49
if _libs["rkaiq"].has("rk_aiq_uapi2_debug_captureRawNotify", "cdecl"):
    rk_aiq_uapi2_debug_captureRawNotify = _libs["rkaiq"].get("rk_aiq_uapi2_debug_captureRawNotify", "cdecl")
    rk_aiq_uapi2_debug_captureRawNotify.argtypes = [POINTER(rk_aiq_sys_ctx_t)]
    rk_aiq_uapi2_debug_captureRawNotify.restype = XCamReturn

enum___RkAiqUapiOpMode = c_int# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_helper.h: 26

RKAIQUAPI_OPMODE_SET = 0# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_helper.h: 26

RKAIQUAPI_OPMODE_GET = (RKAIQUAPI_OPMODE_SET + 1)# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_helper.h: 26

RkAiqUapiOpMode_t = enum___RkAiqUapiOpMode# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_helper.h: 26

RkAiqUapi = CFUNCTYPE(UNCHECKED(c_int), POINTER(None), POINTER(None))# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_helper.h: 104

RkAiqUapiCaller = CFUNCTYPE(UNCHECKED(c_int), POINTER(None), POINTER(None), POINTER(None), POINTER(POINTER(None)), c_int)# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_helper.h: 105

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_helper.h: 113
class struct___RkAiqUapiDesc(Structure):
    pass

struct___RkAiqUapiDesc.__slots__ = [
    'arg_path',
    'arg_type',
    'arg_set',
    'arg_get',
    'uapi_caller',
]
struct___RkAiqUapiDesc._fields_ = [
    ('arg_path', c_char * int(64)),
    ('arg_type', c_char * int(64)),
    ('arg_set', RkAiqUapi),
    ('arg_get', RkAiqUapi),
    ('uapi_caller', RkAiqUapiCaller),
]

RkAiqUapiDesc_t = struct___RkAiqUapiDesc# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_helper.h: 113

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_helper.h: 141
for _lib in _libs.values():
    if not _lib.has("rkaiq_uapi_unified_ctl", "cdecl"):
        continue
    rkaiq_uapi_unified_ctl = _lib.get("rkaiq_uapi_unified_ctl", "cdecl")
    rkaiq_uapi_unified_ctl.argtypes = [POINTER(rk_aiq_sys_ctx_t), String, POINTER(POINTER(c_char)), c_int]
    rkaiq_uapi_unified_ctl.restype = c_int
    break

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 74
if _libs["rkaiq"].has("rk_aiq_uapi2_setAeLock", "cdecl"):
    rk_aiq_uapi2_setAeLock = _libs["rkaiq"].get("rk_aiq_uapi2_setAeLock", "cdecl")
    rk_aiq_uapi2_setAeLock.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_bool]
    rk_aiq_uapi2_setAeLock.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 85
if _libs["rkaiq"].has("rk_aiq_uapi2_setExpMode", "cdecl"):
    rk_aiq_uapi2_setExpMode = _libs["rkaiq"].get("rk_aiq_uapi2_setExpMode", "cdecl")
    rk_aiq_uapi2_setExpMode.argtypes = [POINTER(rk_aiq_sys_ctx_t), opMode_t]
    rk_aiq_uapi2_setExpMode.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 86
if _libs["rkaiq"].has("rk_aiq_uapi2_getExpMode", "cdecl"):
    rk_aiq_uapi2_getExpMode = _libs["rkaiq"].get("rk_aiq_uapi2_getExpMode", "cdecl")
    rk_aiq_uapi2_getExpMode.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(opMode_t)]
    rk_aiq_uapi2_getExpMode.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 100
if _libs["rkaiq"].has("rk_aiq_uapi2_setExpGainRange", "cdecl"):
    rk_aiq_uapi2_setExpGainRange = _libs["rkaiq"].get("rk_aiq_uapi2_setExpGainRange", "cdecl")
    rk_aiq_uapi2_setExpGainRange.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(paRange_t)]
    rk_aiq_uapi2_setExpGainRange.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 101
if _libs["rkaiq"].has("rk_aiq_uapi2_getExpGainRange", "cdecl"):
    rk_aiq_uapi2_getExpGainRange = _libs["rkaiq"].get("rk_aiq_uapi2_getExpGainRange", "cdecl")
    rk_aiq_uapi2_getExpGainRange.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(paRange_t)]
    rk_aiq_uapi2_getExpGainRange.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 114
if _libs["rkaiq"].has("rk_aiq_uapi2_setExpTimeRange", "cdecl"):
    rk_aiq_uapi2_setExpTimeRange = _libs["rkaiq"].get("rk_aiq_uapi2_setExpTimeRange", "cdecl")
    rk_aiq_uapi2_setExpTimeRange.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(paRange_t)]
    rk_aiq_uapi2_setExpTimeRange.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 115
if _libs["rkaiq"].has("rk_aiq_uapi2_getExpTimeRange", "cdecl"):
    rk_aiq_uapi2_getExpTimeRange = _libs["rkaiq"].get("rk_aiq_uapi2_getExpTimeRange", "cdecl")
    rk_aiq_uapi2_getExpTimeRange.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(paRange_t)]
    rk_aiq_uapi2_getExpTimeRange.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 128
if _libs["rkaiq"].has("rk_aiq_uapi2_setBLCMode", "cdecl"):
    rk_aiq_uapi2_setBLCMode = _libs["rkaiq"].get("rk_aiq_uapi2_setBLCMode", "cdecl")
    rk_aiq_uapi2_setBLCMode.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_bool, aeMeasAreaType_t]
    rk_aiq_uapi2_setBLCMode.restype = XCamReturn0x7f824f6c40

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 138
if _libs["rkaiq"].has("rk_aiq_uapi2_setBLCStrength", "cdecl"):
    rk_aiq_uapi2_setBLCStrength = _libs["rkaiq"].get("rk_aiq_uapi2_setBLCStrength", "cdecl")
    rk_aiq_uapi2_setBLCStrength.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_int]
    rk_aiq_uapi2_setBLCStrength.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 150
if _libs["rkaiq"].has("rk_aiq_uapi2_setHLCMode", "cdecl"):
    rk_aiq_uapi2_setHLCMode = _libs["rkaiq"].get("rk_aiq_uapi2_setHLCMode", "cdecl")
    rk_aiq_uapi2_setHLCMode.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_bool]
    rk_aiq_uapi2_setHLCMode.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 160
if _libs["rkaiq"].has("rk_aiq_uapi2_setHLCStrength", "cdecl"):
    rk_aiq_uapi2_setHLCStrength = _libs["rkaiq"].get("rk_aiq_uapi2_setHLCStrength", "cdecl")
    rk_aiq_uapi2_setHLCStrength.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_int]
    rk_aiq_uapi2_setHLCStrength.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 171
if _libs["rkaiq"].has("rk_aiq_uapi2_setAntiFlickerEn", "cdecl"):
    rk_aiq_uapi2_setAntiFlickerEn = _libs["rkaiq"].get("rk_aiq_uapi2_setAntiFlickerEn", "cdecl")
    rk_aiq_uapi2_setAntiFlickerEn.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_bool]
    rk_aiq_uapi2_setAntiFlickerEn.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 172
if _libs["rkaiq"].has("rk_aiq_uapi2_getAntiFlickerEn", "cdecl"):
    rk_aiq_uapi2_getAntiFlickerEn = _libs["rkaiq"].get("rk_aiq_uapi2_getAntiFlickerEn", "cdecl")
    rk_aiq_uapi2_getAntiFlickerEn.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(c_bool)]
    rk_aiq_uapi2_getAntiFlickerEn.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 183
if _libs["rkaiq"].has("rk_aiq_uapi2_setAntiFlickerMode", "cdecl"):
    rk_aiq_uapi2_setAntiFlickerMode = _libs["rkaiq"].get("rk_aiq_uapi2_setAntiFlickerMode", "cdecl")
    rk_aiq_uapi2_setAntiFlickerMode.argtypes = [POINTER(rk_aiq_sys_ctx_t), antiFlickerMode_t]
    rk_aiq_uapi2_setAntiFlickerMode.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 184
if _libs["rkaiq"].has("rk_aiq_uapi2_getAntiFlickerMode", "cdecl"):
    rk_aiq_uapi2_getAntiFlickerMode = _libs["rkaiq"].get("rk_aiq_uapi2_getAntiFlickerMode", "cdecl")
    rk_aiq_uapi2_getAntiFlickerMode.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(antiFlickerMode_t)]
    rk_aiq_uapi2_getAntiFlickerMode.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 201
if _libs["rkaiq"].has("rk_aiq_uapi2_setWBMode", "cdecl"):
    rk_aiq_uapi2_setWBMode = _libs["rkaiq"].get("rk_aiq_uapi2_setWBMode", "cdecl")
    rk_aiq_uapi2_setWBMode.argtypes = [POINTER(rk_aiq_sys_ctx_t), opMode_t]
    rk_aiq_uapi2_setWBMode.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 202
if _libs["rkaiq"].has("rk_aiq_uapi2_getWBMode", "cdecl"):
    rk_aiq_uapi2_getWBMode = _libs["rkaiq"].get("rk_aiq_uapi2_getWBMode", "cdecl")
    rk_aiq_uapi2_getWBMode.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(opMode_t)]
    rk_aiq_uapi2_getWBMode.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 214
if _libs["rkaiq"].has("rk_aiq_uapi2_lockAWB", "cdecl"):
    rk_aiq_uapi2_lockAWB = _libs["rkaiq"].get("rk_aiq_uapi2_lockAWB", "cdecl")
    rk_aiq_uapi2_lockAWB.argtypes = [POINTER(rk_aiq_sys_ctx_t)]
    rk_aiq_uapi2_lockAWB.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 215
if _libs["rkaiq"].has("rk_aiq_uapi2_unlockAWB", "cdecl"):
    rk_aiq_uapi2_unlockAWB = _libs["rkaiq"].get("rk_aiq_uapi2_unlockAWB", "cdecl")
    rk_aiq_uapi2_unlockAWB.argtypes = [POINTER(rk_aiq_sys_ctx_t)]
    rk_aiq_uapi2_unlockAWB.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 226
if _libs["rkaiq"].has("rk_aiq_uapi2_setMWBScene", "cdecl"):
    rk_aiq_uapi2_setMWBScene = _libs["rkaiq"].get("rk_aiq_uapi2_setMWBScene", "cdecl")
    rk_aiq_uapi2_setMWBScene.argtypes = [POINTER(rk_aiq_sys_ctx_t), rk_aiq_wb_scene_t]
    rk_aiq_uapi2_setMWBScene.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 227
if _libs["rkaiq"].has("rk_aiq_uapi2_getMWBScene", "cdecl"):
    rk_aiq_uapi2_getMWBScene = _libs["rkaiq"].get("rk_aiq_uapi2_getMWBScene", "cdecl")
    rk_aiq_uapi2_getMWBScene.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_wb_scene_t)]
    rk_aiq_uapi2_getMWBScene.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 239
if _libs["rkaiq"].has("rk_aiq_uapi2_setMWBGain", "cdecl"):
    rk_aiq_uapi2_setMWBGain = _libs["rkaiq"].get("rk_aiq_uapi2_setMWBGain", "cdecl")
    rk_aiq_uapi2_setMWBGain.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_wb_gain_t)]
    rk_aiq_uapi2_setMWBGain.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 240
if _libs["rkaiq"].has("rk_aiq_uapi2_getWBGain", "cdecl"):
    rk_aiq_uapi2_getWBGain = _libs["rkaiq"].get("rk_aiq_uapi2_getWBGain", "cdecl")
    rk_aiq_uapi2_getWBGain.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_wb_gain_t)]
    rk_aiq_uapi2_getWBGain.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 251
if _libs["rkaiq"].has("rk_aiq_uapi2_setMWBCT", "cdecl"):
    rk_aiq_uapi2_setMWBCT = _libs["rkaiq"].get("rk_aiq_uapi2_setMWBCT", "cdecl")
    rk_aiq_uapi2_setMWBCT.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_uint]
    rk_aiq_uapi2_setMWBCT.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 252
if _libs["rkaiq"].has("rk_aiq_uapi2_getWBCT", "cdecl"):
    rk_aiq_uapi2_getWBCT = _libs["rkaiq"].get("rk_aiq_uapi2_getWBCT", "cdecl")
    rk_aiq_uapi2_getWBCT.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(c_uint)]
    rk_aiq_uapi2_getWBCT.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 263
if _libs["rkaiq"].has("rk_aiq_uapi2_setAwbGainOffsetAttrib", "cdecl"):
    rk_aiq_uapi2_setAwbGainOffsetAttrib = _libs["rkaiq"].get("rk_aiq_uapi2_setAwbGainOffsetAttrib", "cdecl")
    rk_aiq_uapi2_setAwbGainOffsetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), rk_aiq_uapiV2_wb_awb_wbGainOffset_t]
    rk_aiq_uapi2_setAwbGainOffsetAttrib.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 264
if _libs["rkaiq"].has("rk_aiq_uapi2_getAwbGainOffsetAttrib", "cdecl"):
    rk_aiq_uapi2_getAwbGainOffsetAttrib = _libs["rkaiq"].get("rk_aiq_uapi2_getAwbGainOffsetAttrib", "cdecl")
    rk_aiq_uapi2_getAwbGainOffsetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_uapiV2_wb_awb_wbGainOffset_t)]
    rk_aiq_uapi2_getAwbGainOffsetAttrib.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 275
if _libs["rkaiq"].has("rk_aiq_uapi2_setAwbGainAdjustAttrib", "cdecl"):
    rk_aiq_uapi2_setAwbGainAdjustAttrib = _libs["rkaiq"].get("rk_aiq_uapi2_setAwbGainAdjustAttrib", "cdecl")
    rk_aiq_uapi2_setAwbGainAdjustAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), rk_aiq_uapiV2_wb_awb_wbGainAdjust_t]
    rk_aiq_uapi2_setAwbGainAdjustAttrib.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 276
if _libs["rkaiq"].has("rk_aiq_uapi2_getAwbGainAdjustAttrib", "cdecl"):
    rk_aiq_uapi2_getAwbGainAdjustAttrib = _libs["rkaiq"].get("rk_aiq_uapi2_getAwbGainAdjustAttrib", "cdecl")
    rk_aiq_uapi2_getAwbGainAdjustAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_uapiV2_wb_awb_wbGainAdjust_t)]
    rk_aiq_uapi2_getAwbGainAdjustAttrib.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 287
if _libs["rkaiq"].has("rk_aiq_uapi2_setAwbMultiWindowAttrib", "cdecl"):
    rk_aiq_uapi2_setAwbMultiWindowAttrib = _libs["rkaiq"].get("rk_aiq_uapi2_setAwbMultiWindowAttrib", "cdecl")
    rk_aiq_uapi2_setAwbMultiWindowAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), rk_aiq_uapiV2_wb_awb_mulWindow_t]
    rk_aiq_uapi2_setAwbMultiWindowAttrib.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 288
if _libs["rkaiq"].has("rk_aiq_uapi2_getAwbMultiWindowAttrib", "cdecl"):
    rk_aiq_uapi2_getAwbMultiWindowAttrib = _libs["rkaiq"].get("rk_aiq_uapi2_getAwbMultiWindowAttrib", "cdecl")
    rk_aiq_uapi2_getAwbMultiWindowAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_uapiV2_wb_awb_mulWindow_t)]
    rk_aiq_uapi2_getAwbMultiWindowAttrib.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 300
if _libs["rkaiq"].has("rk_aiq_uapi2_setAwbV30AllAttrib", "cdecl"):
    rk_aiq_uapi2_setAwbV30AllAttrib = _libs["rkaiq"].get("rk_aiq_uapi2_setAwbV30AllAttrib", "cdecl")
    rk_aiq_uapi2_setAwbV30AllAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), rk_aiq_uapiV2_wbV30_attrib_t]
    rk_aiq_uapi2_setAwbV30AllAttrib.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 301
if _libs["rkaiq"].has("rk_aiq_uapi2_getAwbV30AllAttrib", "cdecl"):
    rk_aiq_uapi2_getAwbV30AllAttrib = _libs["rkaiq"].get("rk_aiq_uapi2_getAwbV30AllAttrib", "cdecl")
    rk_aiq_uapi2_getAwbV30AllAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_uapiV2_wbV30_attrib_t)]
    rk_aiq_uapi2_getAwbV30AllAttrib.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 313
if _libs["rkaiq"].has("rk_aiq_uapi2_setAwbV21AllAttrib", "cdecl"):
    rk_aiq_uapi2_setAwbV21AllAttrib = _libs["rkaiq"].get("rk_aiq_uapi2_setAwbV21AllAttrib", "cdecl")
    rk_aiq_uapi2_setAwbV21AllAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), rk_aiq_uapiV2_wbV21_attrib_t]
    rk_aiq_uapi2_setAwbV21AllAttrib.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 314
if _libs["rkaiq"].has("rk_aiq_uapi2_getAwbV21AllAttrib", "cdecl"):
    rk_aiq_uapi2_getAwbV21AllAttrib = _libs["rkaiq"].get("rk_aiq_uapi2_getAwbV21AllAttrib", "cdecl")
    rk_aiq_uapi2_getAwbV21AllAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_uapiV2_wbV21_attrib_t)]
    rk_aiq_uapi2_getAwbV21AllAttrib.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 327
if _libs["rkaiq"].has("rk_aiq_uapi2_setExpPwrLineFreqMode", "cdecl"):
    rk_aiq_uapi2_setExpPwrLineFreqMode = _libs["rkaiq"].get("rk_aiq_uapi2_setExpPwrLineFreqMode", "cdecl")
    rk_aiq_uapi2_setExpPwrLineFreqMode.argtypes = [POINTER(rk_aiq_sys_ctx_t), expPwrLineFreq_t]
    rk_aiq_uapi2_setExpPwrLineFreqMode.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 328
if _libs["rkaiq"].has("rk_aiq_uapi2_getExpPwrLineFreqMode", "cdecl"):
    rk_aiq_uapi2_getExpPwrLineFreqMode = _libs["rkaiq"].get("rk_aiq_uapi2_getExpPwrLineFreqMode", "cdecl")
    rk_aiq_uapi2_getExpPwrLineFreqMode.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(expPwrLineFreq_t)]
    rk_aiq_uapi2_getExpPwrLineFreqMode.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 340
if _libs["rkaiq"].has("rk_aiq_uapi2_setGammaCoef", "cdecl"):
    rk_aiq_uapi2_setGammaCoef = _libs["rkaiq"].get("rk_aiq_uapi2_setGammaCoef", "cdecl")
    rk_aiq_uapi2_setGammaCoef.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_float, c_float]
    rk_aiq_uapi2_setGammaCoef.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 352
if _libs["rkaiq"].has("rk_aiq_uapi2_setDarkAreaBoostStrth", "cdecl"):
    rk_aiq_uapi2_setDarkAreaBoostStrth = _libs["rkaiq"].get("rk_aiq_uapi2_setDarkAreaBoostStrth", "cdecl")
    rk_aiq_uapi2_setDarkAreaBoostStrth.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_uint]
    rk_aiq_uapi2_setDarkAreaBoostStrth.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 353
if _libs["rkaiq"].has("rk_aiq_uapi2_getDarkAreaBoostStrth", "cdecl"):
    rk_aiq_uapi2_getDarkAreaBoostStrth = _libs["rkaiq"].get("rk_aiq_uapi2_getDarkAreaBoostStrth", "cdecl")
    rk_aiq_uapi2_getDarkAreaBoostStrth.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(c_uint)]
    rk_aiq_uapi2_getDarkAreaBoostStrth.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 365
if _libs["rkaiq"].has("rk_aiq_uapi2_setMHDRStrth", "cdecl"):
    rk_aiq_uapi2_setMHDRStrth = _libs["rkaiq"].get("rk_aiq_uapi2_setMHDRStrth", "cdecl")
    rk_aiq_uapi2_setMHDRStrth.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_bool, c_uint]
    rk_aiq_uapi2_setMHDRStrth.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 366
if _libs["rkaiq"].has("rk_aiq_uapi2_getMHDRStrth", "cdecl"):
    rk_aiq_uapi2_getMHDRStrth = _libs["rkaiq"].get("rk_aiq_uapi2_getMHDRStrth", "cdecl")
    rk_aiq_uapi2_getMHDRStrth.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(c_bool), POINTER(c_uint)]
    rk_aiq_uapi2_getMHDRStrth.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 376
if _libs["rkaiq"].has("rk_aiq_uapi2_setDehazeModuleEnable", "cdecl"):
    rk_aiq_uapi2_setDehazeModuleEnable = _libs["rkaiq"].get("rk_aiq_uapi2_setDehazeModuleEnable", "cdecl")
    rk_aiq_uapi2_setDehazeModuleEnable.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_bool]
    rk_aiq_uapi2_setDehazeModuleEnable.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 386
if _libs["rkaiq"].has("rk_aiq_uapi2_setDehazeEnable", "cdecl"):
    rk_aiq_uapi2_setDehazeEnable = _libs["rkaiq"].get("rk_aiq_uapi2_setDehazeEnable", "cdecl")
    rk_aiq_uapi2_setDehazeEnable.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_bool]
    rk_aiq_uapi2_setDehazeEnable.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 398
if _libs["rkaiq"].has("rk_aiq_uapi2_setMDehazeStrth", "cdecl"):
    rk_aiq_uapi2_setMDehazeStrth = _libs["rkaiq"].get("rk_aiq_uapi2_setMDehazeStrth", "cdecl")
    rk_aiq_uapi2_setMDehazeStrth.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_uint]
    rk_aiq_uapi2_setMDehazeStrth.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 399
if _libs["rkaiq"].has("rk_aiq_uapi2_getMDehazeStrth", "cdecl"):
    rk_aiq_uapi2_getMDehazeStrth = _libs["rkaiq"].get("rk_aiq_uapi2_getMDehazeStrth", "cdecl")
    rk_aiq_uapi2_getMDehazeStrth.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(c_uint)]
    rk_aiq_uapi2_getMDehazeStrth.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 409
if _libs["rkaiq"].has("rk_aiq_uapi2_setEnhanceEnable", "cdecl"):
    rk_aiq_uapi2_setEnhanceEnable = _libs["rkaiq"].get("rk_aiq_uapi2_setEnhanceEnable", "cdecl")
    rk_aiq_uapi2_setEnhanceEnable.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_bool]
    rk_aiq_uapi2_setEnhanceEnable.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 421
if _libs["rkaiq"].has("rk_aiq_uapi2_setMEnhanceStrth", "cdecl"):
    rk_aiq_uapi2_setMEnhanceStrth = _libs["rkaiq"].get("rk_aiq_uapi2_setMEnhanceStrth", "cdecl")
    rk_aiq_uapi2_setMEnhanceStrth.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_uint]
    rk_aiq_uapi2_setMEnhanceStrth.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 422
if _libs["rkaiq"].has("rk_aiq_uapi2_getMEnhanceStrth", "cdecl"):
    rk_aiq_uapi2_getMEnhanceStrth = _libs["rkaiq"].get("rk_aiq_uapi2_getMEnhanceStrth", "cdecl")
    rk_aiq_uapi2_getMEnhanceStrth.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(c_uint)]
    rk_aiq_uapi2_getMEnhanceStrth.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 437
if _libs["rkaiq"].has("rk_aiq_uapi2_setDrcLocalTMO", "cdecl"):
    rk_aiq_uapi2_setDrcLocalTMO = _libs["rkaiq"].get("rk_aiq_uapi2_setDrcLocalTMO", "cdecl")
    rk_aiq_uapi2_setDrcLocalTMO.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_float, c_float, c_float]
    rk_aiq_uapi2_setDrcLocalTMO.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 438
if _libs["rkaiq"].has("rk_aiq_uapi2_getDrcLocalTMO", "cdecl"):
    rk_aiq_uapi2_getDrcLocalTMO = _libs["rkaiq"].get("rk_aiq_uapi2_getDrcLocalTMO", "cdecl")
    rk_aiq_uapi2_getDrcLocalTMO.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(c_float), POINTER(c_float), POINTER(c_float)]
    rk_aiq_uapi2_getDrcLocalTMO.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 455
if _libs["rkaiq"].has("rk_aiq_uapi2_setDrcLocalData", "cdecl"):
    rk_aiq_uapi2_setDrcLocalData = _libs["rkaiq"].get("rk_aiq_uapi2_setDrcLocalData", "cdecl")
    rk_aiq_uapi2_setDrcLocalData.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_float, c_float, c_float, c_int, c_float]
    rk_aiq_uapi2_setDrcLocalData.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 456
if _libs["rkaiq"].has("rk_aiq_uapi2_getDrcLocalData", "cdecl"):
    rk_aiq_uapi2_getDrcLocalData = _libs["rkaiq"].get("rk_aiq_uapi2_getDrcLocalData", "cdecl")
    rk_aiq_uapi2_getDrcLocalData.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(c_float), POINTER(c_float), POINTER(c_float), POINTER(c_int), POINTER(c_float)]
    rk_aiq_uapi2_getDrcLocalData.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 468
if _libs["rkaiq"].has("rk_aiq_uapi2_setDrcHiLit", "cdecl"):
    rk_aiq_uapi2_setDrcHiLit = _libs["rkaiq"].get("rk_aiq_uapi2_setDrcHiLit", "cdecl")
    rk_aiq_uapi2_setDrcHiLit.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_float]
    rk_aiq_uapi2_setDrcHiLit.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 469
if _libs["rkaiq"].has("rk_aiq_uapi2_getDrcHiLit", "cdecl"):
    rk_aiq_uapi2_getDrcHiLit = _libs["rkaiq"].get("rk_aiq_uapi2_getDrcHiLit", "cdecl")
    rk_aiq_uapi2_getDrcHiLit.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(c_float)]
    rk_aiq_uapi2_getDrcHiLit.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 485
if _libs["rkaiq"].has("rk_aiq_uapi2_setDrcGain", "cdecl"):
    rk_aiq_uapi2_setDrcGain = _libs["rkaiq"].get("rk_aiq_uapi2_setDrcGain", "cdecl")
    rk_aiq_uapi2_setDrcGain.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_float, c_float, c_float]
    rk_aiq_uapi2_setDrcGain.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 486
if _libs["rkaiq"].has("rk_aiq_uapi2_getDrcGain", "cdecl"):
    rk_aiq_uapi2_getDrcGain = _libs["rkaiq"].get("rk_aiq_uapi2_getDrcGain", "cdecl")
    rk_aiq_uapi2_getDrcGain.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(c_float), POINTER(c_float), POINTER(c_float)]
    rk_aiq_uapi2_getDrcGain.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 504
if _libs["rkaiq"].has("rk_aiq_uapi2_setNRMode", "cdecl"):
    rk_aiq_uapi2_setNRMode = _libs["rkaiq"].get("rk_aiq_uapi2_setNRMode", "cdecl")
    rk_aiq_uapi2_setNRMode.argtypes = [POINTER(rk_aiq_sys_ctx_t), opMode_t]
    rk_aiq_uapi2_setNRMode.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 505
if _libs["rkaiq"].has("rk_aiq_uapi2_getNRMode", "cdecl"):
    rk_aiq_uapi2_getNRMode = _libs["rkaiq"].get("rk_aiq_uapi2_getNRMode", "cdecl")
    rk_aiq_uapi2_getNRMode.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(opMode_t)]
    rk_aiq_uapi2_getNRMode.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 516
if _libs["rkaiq"].has("rk_aiq_uapi2_setANRStrth", "cdecl"):
    rk_aiq_uapi2_setANRStrth = _libs["rkaiq"].get("rk_aiq_uapi2_setANRStrth", "cdecl")
    rk_aiq_uapi2_setANRStrth.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_uint]
    rk_aiq_uapi2_setANRStrth.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 517
if _libs["rkaiq"].has("rk_aiq_uapi2_getANRStrth", "cdecl"):
    rk_aiq_uapi2_getANRStrth = _libs["rkaiq"].get("rk_aiq_uapi2_getANRStrth", "cdecl")
    rk_aiq_uapi2_getANRStrth.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(c_uint)]
    rk_aiq_uapi2_getANRStrth.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 530
if _libs["rkaiq"].has("rk_aiq_uapi2_setMSpaNRStrth", "cdecl"):
    rk_aiq_uapi2_setMSpaNRStrth = _libs["rkaiq"].get("rk_aiq_uapi2_setMSpaNRStrth", "cdecl")
    rk_aiq_uapi2_setMSpaNRStrth.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_bool, c_uint]
    rk_aiq_uapi2_setMSpaNRStrth.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 531
if _libs["rkaiq"].has("rk_aiq_uapi2_getMSpaNRStrth", "cdecl"):
    rk_aiq_uapi2_getMSpaNRStrth = _libs["rkaiq"].get("rk_aiq_uapi2_getMSpaNRStrth", "cdecl")
    rk_aiq_uapi2_getMSpaNRStrth.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(c_bool), POINTER(c_uint)]
    rk_aiq_uapi2_getMSpaNRStrth.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 543
if _libs["rkaiq"].has("rk_aiq_uapi2_setMTNRStrth", "cdecl"):
    rk_aiq_uapi2_setMTNRStrth = _libs["rkaiq"].get("rk_aiq_uapi2_setMTNRStrth", "cdecl")
    rk_aiq_uapi2_setMTNRStrth.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_bool, c_uint]
    rk_aiq_uapi2_setMTNRStrth.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 545
if _libs["rkaiq"].has("rk_aiq_uapi2_getMTNRStrth", "cdecl"):
    rk_aiq_uapi2_getMTNRStrth = _libs["rkaiq"].get("rk_aiq_uapi2_getMTNRStrth", "cdecl")
    rk_aiq_uapi2_getMTNRStrth.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(c_bool), POINTER(c_uint)]
    rk_aiq_uapi2_getMTNRStrth.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 555
if _libs["rkaiq"].has("rk_aiq_uapi2_setSharpness", "cdecl"):
    rk_aiq_uapi2_setSharpness = _libs["rkaiq"].get("rk_aiq_uapi2_setSharpness", "cdecl")
    rk_aiq_uapi2_setSharpness.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_uint]
    rk_aiq_uapi2_setSharpness.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 556
if _libs["rkaiq"].has("rk_aiq_uapi2_getSharpness", "cdecl"):
    rk_aiq_uapi2_getSharpness = _libs["rkaiq"].get("rk_aiq_uapi2_getSharpness", "cdecl")
    rk_aiq_uapi2_getSharpness.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(c_uint)]
    rk_aiq_uapi2_getSharpness.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 573
if _libs["rkaiq"].has("rk_aiq_uapi2_setFocusMode", "cdecl"):
    rk_aiq_uapi2_setFocusMode = _libs["rkaiq"].get("rk_aiq_uapi2_setFocusMode", "cdecl")
    rk_aiq_uapi2_setFocusMode.argtypes = [POINTER(rk_aiq_sys_ctx_t), opMode_t]
    rk_aiq_uapi2_setFocusMode.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 574
if _libs["rkaiq"].has("rk_aiq_uapi2_getFocusMode", "cdecl"):
    rk_aiq_uapi2_getFocusMode = _libs["rkaiq"].get("rk_aiq_uapi2_getFocusMode", "cdecl")
    rk_aiq_uapi2_getFocusMode.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(opMode_t)]
    rk_aiq_uapi2_getFocusMode.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 584
if _libs["rkaiq"].has("rk_aiq_uapi2_setFocusPosition", "cdecl"):
    rk_aiq_uapi2_setFocusPosition = _libs["rkaiq"].get("rk_aiq_uapi2_setFocusPosition", "cdecl")
    rk_aiq_uapi2_setFocusPosition.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_short]
    rk_aiq_uapi2_setFocusPosition.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 585
if _libs["rkaiq"].has("rk_aiq_uapi2_getFocusPosition", "cdecl"):
    rk_aiq_uapi2_getFocusPosition = _libs["rkaiq"].get("rk_aiq_uapi2_getFocusPosition", "cdecl")
    rk_aiq_uapi2_getFocusPosition.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(c_short)]
    rk_aiq_uapi2_getFocusPosition.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 595
if _libs["rkaiq"].has("rk_aiq_uapi2_setFocusWin", "cdecl"):
    rk_aiq_uapi2_setFocusWin = _libs["rkaiq"].get("rk_aiq_uapi2_setFocusWin", "cdecl")
    rk_aiq_uapi2_setFocusWin.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(paRect_t)]
    rk_aiq_uapi2_setFocusWin.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 596
if _libs["rkaiq"].has("rk_aiq_uapi2_getFocusWin", "cdecl"):
    rk_aiq_uapi2_getFocusWin = _libs["rkaiq"].get("rk_aiq_uapi2_getFocusWin", "cdecl")
    rk_aiq_uapi2_getFocusWin.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(paRect_t)]
    rk_aiq_uapi2_getFocusWin.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 607
if _libs["rkaiq"].has("rk_aiq_uapi2_lockFocus", "cdecl"):
    rk_aiq_uapi2_lockFocus = _libs["rkaiq"].get("rk_aiq_uapi2_lockFocus", "cdecl")
    rk_aiq_uapi2_lockFocus.argtypes = [POINTER(rk_aiq_sys_ctx_t)]
    rk_aiq_uapi2_lockFocus.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 608
if _libs["rkaiq"].has("rk_aiq_uapi2_unlockFocus", "cdecl"):
    rk_aiq_uapi2_unlockFocus = _libs["rkaiq"].get("rk_aiq_uapi2_unlockFocus", "cdecl")
    rk_aiq_uapi2_unlockFocus.argtypes = [POINTER(rk_aiq_sys_ctx_t)]
    rk_aiq_uapi2_unlockFocus.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 619
if _libs["rkaiq"].has("rk_aiq_uapi2_oneshotFocus", "cdecl"):
    rk_aiq_uapi2_oneshotFocus = _libs["rkaiq"].get("rk_aiq_uapi2_oneshotFocus", "cdecl")
    rk_aiq_uapi2_oneshotFocus.argtypes = [POINTER(rk_aiq_sys_ctx_t)]
    rk_aiq_uapi2_oneshotFocus.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 630
if _libs["rkaiq"].has("rk_aiq_uapi2_manualTrigerFocus", "cdecl"):
    rk_aiq_uapi2_manualTrigerFocus = _libs["rkaiq"].get("rk_aiq_uapi2_manualTrigerFocus", "cdecl")
    rk_aiq_uapi2_manualTrigerFocus.argtypes = [POINTER(rk_aiq_sys_ctx_t)]
    rk_aiq_uapi2_manualTrigerFocus.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 641
if _libs["rkaiq"].has("rk_aiq_uapi2_trackingFocus", "cdecl"):
    rk_aiq_uapi2_trackingFocus = _libs["rkaiq"].get("rk_aiq_uapi2_trackingFocus", "cdecl")
    rk_aiq_uapi2_trackingFocus.argtypes = [POINTER(rk_aiq_sys_ctx_t)]
    rk_aiq_uapi2_trackingFocus.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 652
if _libs["rkaiq"].has("rk_aiq_uapi2_getSearchPath", "cdecl"):
    rk_aiq_uapi2_getSearchPath = _libs["rkaiq"].get("rk_aiq_uapi2_getSearchPath", "cdecl")
    rk_aiq_uapi2_getSearchPath.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_af_sec_path_t)]
    rk_aiq_uapi2_getSearchPath.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 663
if _libs["rkaiq"].has("rk_aiq_uapi2_getSearchResult", "cdecl"):
    rk_aiq_uapi2_getSearchResult = _libs["rkaiq"].get("rk_aiq_uapi2_getSearchResult", "cdecl")
    rk_aiq_uapi2_getSearchResult.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_af_result_t)]
    rk_aiq_uapi2_getSearchResult.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 674
if _libs["rkaiq"].has("rk_aiq_uapi2_setOpZoomPosition", "cdecl"):
    rk_aiq_uapi2_setOpZoomPosition = _libs["rkaiq"].get("rk_aiq_uapi2_setOpZoomPosition", "cdecl")
    rk_aiq_uapi2_setOpZoomPosition.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_int]
    rk_aiq_uapi2_setOpZoomPosition.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 675
if _libs["rkaiq"].has("rk_aiq_uapi2_getOpZoomPosition", "cdecl"):
    rk_aiq_uapi2_getOpZoomPosition = _libs["rkaiq"].get("rk_aiq_uapi2_getOpZoomPosition", "cdecl")
    rk_aiq_uapi2_getOpZoomPosition.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(c_int)]
    rk_aiq_uapi2_getOpZoomPosition.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 676
if _libs["rkaiq"].has("rk_aiq_uapi2_endOpZoomChange", "cdecl"):
    rk_aiq_uapi2_endOpZoomChange = _libs["rkaiq"].get("rk_aiq_uapi2_endOpZoomChange", "cdecl")
    rk_aiq_uapi2_endOpZoomChange.argtypes = [POINTER(rk_aiq_sys_ctx_t)]
    rk_aiq_uapi2_endOpZoomChange.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 687
if _libs["rkaiq"].has("rk_aiq_uapi2_getZoomRange", "cdecl"):
    rk_aiq_uapi2_getZoomRange = _libs["rkaiq"].get("rk_aiq_uapi2_getZoomRange", "cdecl")
    rk_aiq_uapi2_getZoomRange.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_af_zoomrange)]
    rk_aiq_uapi2_getZoomRange.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 688
if _libs["rkaiq"].has("rk_aiq_uapi2_getFocusRange", "cdecl"):
    rk_aiq_uapi2_getFocusRange = _libs["rkaiq"].get("rk_aiq_uapi2_getFocusRange", "cdecl")
    rk_aiq_uapi2_getFocusRange.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_af_focusrange)]
    rk_aiq_uapi2_getFocusRange.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 699
if _libs["rkaiq"].has("rk_aiq_uapi2_startZoomCalib", "cdecl"):
    rk_aiq_uapi2_startZoomCalib = _libs["rkaiq"].get("rk_aiq_uapi2_startZoomCalib", "cdecl")
    rk_aiq_uapi2_startZoomCalib.argtypes = [POINTER(rk_aiq_sys_ctx_t)]
    rk_aiq_uapi2_startZoomCalib.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 700
if _libs["rkaiq"].has("rk_aiq_uapi2_resetZoom", "cdecl"):
    rk_aiq_uapi2_resetZoom = _libs["rkaiq"].get("rk_aiq_uapi2_resetZoom", "cdecl")
    rk_aiq_uapi2_resetZoom.argtypes = [POINTER(rk_aiq_sys_ctx_t)]
    rk_aiq_uapi2_resetZoom.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 711
if _libs["rkaiq"].has("rk_aiq_uapi2_setAngleZ", "cdecl"):
    rk_aiq_uapi2_setAngleZ = _libs["rkaiq"].get("rk_aiq_uapi2_setAngleZ", "cdecl")
    rk_aiq_uapi2_setAngleZ.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_float]
    rk_aiq_uapi2_setAngleZ.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 722
if _libs["rkaiq"].has("rk_aiq_uapi2_getCustomAfRes", "cdecl"):
    rk_aiq_uapi2_getCustomAfRes = _libs["rkaiq"].get("rk_aiq_uapi2_getCustomAfRes", "cdecl")
    rk_aiq_uapi2_getCustomAfRes.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_tool_customAf_res_t)]
    rk_aiq_uapi2_getCustomAfRes.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 723
if _libs["rkaiq"].has("rk_aiq_uapi2_setCustomAfRes", "cdecl"):
    rk_aiq_uapi2_setCustomAfRes = _libs["rkaiq"].get("rk_aiq_uapi2_setCustomAfRes", "cdecl")
    rk_aiq_uapi2_setCustomAfRes.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_tool_customAf_res_t)]
    rk_aiq_uapi2_setCustomAfRes.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 741
if _libs["rkaiq"].has("rk_aiq_uapi2_setCCMMode", "cdecl"):
    rk_aiq_uapi2_setCCMMode = _libs["rkaiq"].get("rk_aiq_uapi2_setCCMMode", "cdecl")
    rk_aiq_uapi2_setCCMMode.argtypes = [POINTER(rk_aiq_sys_ctx_t), opMode_t]
    rk_aiq_uapi2_setCCMMode.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 742
if _libs["rkaiq"].has("rk_aiq_uapi2_getCCMMode", "cdecl"):
    rk_aiq_uapi2_getCCMMode = _libs["rkaiq"].get("rk_aiq_uapi2_getCCMMode", "cdecl")
    rk_aiq_uapi2_getCCMMode.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(opMode_t)]
    rk_aiq_uapi2_getCCMMode.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 757
if _libs["rkaiq"].has("rk_aiq_uapi2_setMCcCoef", "cdecl"):
    rk_aiq_uapi2_setMCcCoef = _libs["rkaiq"].get("rk_aiq_uapi2_setMCcCoef", "cdecl")
    rk_aiq_uapi2_setMCcCoef.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_ccm_matrix_t)]
    rk_aiq_uapi2_setMCcCoef.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 758
if _libs["rkaiq"].has("rk_aiq_uapi2_getMCcCoef", "cdecl"):
    rk_aiq_uapi2_getMCcCoef = _libs["rkaiq"].get("rk_aiq_uapi2_getMCcCoef", "cdecl")
    rk_aiq_uapi2_getMCcCoef.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_ccm_matrix_t)]
    rk_aiq_uapi2_getMCcCoef.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 770
if _libs["rkaiq"].has("rk_aiq_uapi2_getACcmSat", "cdecl"):
    rk_aiq_uapi2_getACcmSat = _libs["rkaiq"].get("rk_aiq_uapi2_getACcmSat", "cdecl")
    rk_aiq_uapi2_getACcmSat.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(c_float)]
    rk_aiq_uapi2_getACcmSat.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 782
if _libs["rkaiq"].has("rk_aiq_uapi2_getACcmMatrixName", "cdecl"):
    rk_aiq_uapi2_getACcmMatrixName = _libs["rkaiq"].get("rk_aiq_uapi2_getACcmMatrixName", "cdecl")
    rk_aiq_uapi2_getACcmMatrixName.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(POINTER(c_char))]
    rk_aiq_uapi2_getACcmMatrixName.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 800
if _libs["rkaiq"].has("rk_aiq_uapi2_setLut3dMode", "cdecl"):
    rk_aiq_uapi2_setLut3dMode = _libs["rkaiq"].get("rk_aiq_uapi2_setLut3dMode", "cdecl")
    rk_aiq_uapi2_setLut3dMode.argtypes = [POINTER(rk_aiq_sys_ctx_t), opMode_t]
    rk_aiq_uapi2_setLut3dMode.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 801
if _libs["rkaiq"].has("rk_aiq_uapi2_getLut3dMode", "cdecl"):
    rk_aiq_uapi2_getLut3dMode = _libs["rkaiq"].get("rk_aiq_uapi2_getLut3dMode", "cdecl")
    rk_aiq_uapi2_getLut3dMode.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(opMode_t)]
    rk_aiq_uapi2_getLut3dMode.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 817
if _libs["rkaiq"].has("rk_aiq_uapi2_setM3dLut", "cdecl"):
    rk_aiq_uapi2_setM3dLut = _libs["rkaiq"].get("rk_aiq_uapi2_setM3dLut", "cdecl")
    rk_aiq_uapi2_setM3dLut.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_lut3d_table_t)]
    rk_aiq_uapi2_setM3dLut.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 818
if _libs["rkaiq"].has("rk_aiq_uapi2_getM3dLut", "cdecl"):
    rk_aiq_uapi2_getM3dLut = _libs["rkaiq"].get("rk_aiq_uapi2_getM3dLut", "cdecl")
    rk_aiq_uapi2_getM3dLut.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_lut3d_table_t)]
    rk_aiq_uapi2_getM3dLut.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 830
if _libs["rkaiq"].has("rk_aiq_uapi2_getA3dLutStrth", "cdecl"):
    rk_aiq_uapi2_getA3dLutStrth = _libs["rkaiq"].get("rk_aiq_uapi2_getA3dLutStrth", "cdecl")
    rk_aiq_uapi2_getA3dLutStrth.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(c_float)]
    rk_aiq_uapi2_getA3dLutStrth.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 842
if _libs["rkaiq"].has("rk_aiq_uapi2_getA3dLutName", "cdecl"):
    rk_aiq_uapi2_getA3dLutName = _libs["rkaiq"].get("rk_aiq_uapi2_getA3dLutName", "cdecl")
    rk_aiq_uapi2_getA3dLutName.argtypes = [POINTER(rk_aiq_sys_ctx_t), String]
    rk_aiq_uapi2_getA3dLutName.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 851
if _libs["rkaiq"].has("rk_aiq_uapi2_setLdchEn", "cdecl"):
    rk_aiq_uapi2_setLdchEn = _libs["rkaiq"].get("rk_aiq_uapi2_setLdchEn", "cdecl")
    rk_aiq_uapi2_setLdchEn.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_bool]
    rk_aiq_uapi2_setLdchEn.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 859
if _libs["rkaiq"].has("rk_aiq_uapi2_setLdchCorrectLevel", "cdecl"):
    rk_aiq_uapi2_setLdchCorrectLevel = _libs["rkaiq"].get("rk_aiq_uapi2_setLdchCorrectLevel", "cdecl")
    rk_aiq_uapi2_setLdchCorrectLevel.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_int]
    rk_aiq_uapi2_setLdchCorrectLevel.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 868
if _libs["rkaiq"].has("rk_aiq_uapi2_setFecEn", "cdecl"):
    rk_aiq_uapi2_setFecEn = _libs["rkaiq"].get("rk_aiq_uapi2_setFecEn", "cdecl")
    rk_aiq_uapi2_setFecEn.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_bool]
    rk_aiq_uapi2_setFecEn.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 877
if _libs["rkaiq"].has("rk_aiq_uapi2_setFecCorrectDirection", "cdecl"):
    rk_aiq_uapi2_setFecCorrectDirection = _libs["rkaiq"].get("rk_aiq_uapi2_setFecCorrectDirection", "cdecl")
    rk_aiq_uapi2_setFecCorrectDirection.argtypes = [POINTER(rk_aiq_sys_ctx_t), fec_correct_direction_t]
    rk_aiq_uapi2_setFecCorrectDirection.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 886
if _libs["rkaiq"].has("rk_aiq_uapi2_setFecBypass", "cdecl"):
    rk_aiq_uapi2_setFecBypass = _libs["rkaiq"].get("rk_aiq_uapi2_setFecBypass", "cdecl")
    rk_aiq_uapi2_setFecBypass.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_bool]
    rk_aiq_uapi2_setFecBypass.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 895
if _libs["rkaiq"].has("rk_aiq_uapi2_setFecCorrectLevel", "cdecl"):
    rk_aiq_uapi2_setFecCorrectLevel = _libs["rkaiq"].get("rk_aiq_uapi2_setFecCorrectLevel", "cdecl")
    rk_aiq_uapi2_setFecCorrectLevel.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_int]
    rk_aiq_uapi2_setFecCorrectLevel.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 904
if _libs["rkaiq"].has("rk_aiq_uapi2_setFecCorrectMode", "cdecl"):
    rk_aiq_uapi2_setFecCorrectMode = _libs["rkaiq"].get("rk_aiq_uapi2_setFecCorrectMode", "cdecl")
    rk_aiq_uapi2_setFecCorrectMode.argtypes = [POINTER(rk_aiq_sys_ctx_t), fec_correct_mode_t]
    rk_aiq_uapi2_setFecCorrectMode.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 914
if _libs["rkaiq"].has("rk_aiq_uapi2_setGrayMode", "cdecl"):
    rk_aiq_uapi2_setGrayMode = _libs["rkaiq"].get("rk_aiq_uapi2_setGrayMode", "cdecl")
    rk_aiq_uapi2_setGrayMode.argtypes = [POINTER(rk_aiq_sys_ctx_t), rk_aiq_gray_mode_t]
    rk_aiq_uapi2_setGrayMode.restype = XCamReturn

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_imgproc.h: 922
if _libs["rkaiq"].has("rk_aiq_uapi2_getGrayMode", "cdecl"):
    rk_aiq_uapi2_getGrayMode = _libs["rkaiq"].get("rk_aiq_uapi2_getGrayMode", "cdecl")
    rk_aiq_uapi2_getGrayMode.argtypes = [POINTER(rk_aiq_sys_ctx_t)]
    rk_aiq_uapi2_getGrayMode.restype = rk_aiq_gray_mode_t

# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_uapi_head.h: 174
class struct_uapi_rawhist_stats_s(Structure):
    pass

struct_uapi_rawhist_stats_s.__slots__ = [
    'bins',
]
struct_uapi_rawhist_stats_s._fields_ = [
    ('bins', c_uint * int(256)),
]

uapi_rawhist_stats_t = struct_uapi_rawhist_stats_s# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_uapi_head.h: 174

# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_uapi_head.h: 179
class struct_uapi_sihist_stats_s(Structure):
    pass

struct_uapi_sihist_stats_s.__slots__ = [
    'bins',
]
struct_uapi_sihist_stats_s._fields_ = [
    ('bins', c_uint * int(32)),
]

uapi_sihist_stats_t = struct_uapi_sihist_stats_s# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_uapi_head.h: 179

# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_uapi_head.h: 214
class struct_uapi_rawae_big_stats_s(Structure):
    pass

struct_uapi_rawae_big_stats_s.__slots__ = [
    'channelr_xy',
    'channelg_xy',
    'channelb_xy',
    'channely_xy',
    'wndx_sumr',
    'wndx_sumg',
    'wndx_sumb',
    'wndx_channelr',
    'wndx_channelg',
    'wndx_channelb',
    'wndx_channely',
]
struct_uapi_rawae_big_stats_s._fields_ = [
    ('channelr_xy', uint16_t * int(225)),
    ('channelg_xy', uint16_t * int(225)),
    ('channelb_xy', uint16_t * int(225)),
    ('channely_xy', uint16_t * int(225)),
    ('wndx_sumr', uint64_t * int(4)),
    ('wndx_sumg', uint64_t * int(4)),
    ('wndx_sumb', uint64_t * int(4)),
    ('wndx_channelr', uint16_t * int(4)),
    ('wndx_channelg', uint16_t * int(4)),
    ('wndx_channelb', uint16_t * int(4)),
    ('wndx_channely', uint16_t * int(4)),
]

uapi_rawae_big_stats_t = struct_uapi_rawae_big_stats_s# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_uapi_head.h: 214

# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_uapi_head.h: 228
class struct_uapi_rawae_lite_stat_s(Structure):
    pass

struct_uapi_rawae_lite_stat_s.__slots__ = [
    'channelr_xy',
    'channelg_xy',
    'channelb_xy',
    'channely_xy',
]
struct_uapi_rawae_lite_stat_s._fields_ = [
    ('channelr_xy', uint16_t * int(25)),
    ('channelg_xy', uint16_t * int(25)),
    ('channelb_xy', uint16_t * int(25)),
    ('channely_xy', uint16_t * int(25)),
]

uapi_rawae_lite_stat_t = struct_uapi_rawae_lite_stat_s# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_uapi_head.h: 228

# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_uapi_head.h: 236
class struct_uapi_yuvae_stats_s(Structure):
    pass

struct_uapi_yuvae_stats_s.__slots__ = [
    'ro_yuvae_sumy',
    'mean',
]
struct_uapi_yuvae_stats_s._fields_ = [
    ('ro_yuvae_sumy', uint64_t * int(4)),
    ('mean', c_ubyte * int(225)),
]

uapi_yuvae_stats_t = struct_uapi_yuvae_stats_s# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_uapi_head.h: 236

# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_uapi_head.h: 249
class struct_uapi_raw_stats_s(Structure):
    pass

struct_uapi_raw_stats_s.__slots__ = [
    'rawae_big',
    'rawae_lite',
    'rawhist_big',
    'rawhist_lite',
]
struct_uapi_raw_stats_s._fields_ = [
    ('rawae_big', uapi_rawae_big_stats_t),
    ('rawae_lite', uapi_rawae_lite_stat_t),
    ('rawhist_big', uapi_rawhist_stats_t),
    ('rawhist_lite', uapi_rawhist_stats_t),
]

uapi_raw_stats_t = struct_uapi_raw_stats_s# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_uapi_head.h: 249

# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_uapi_head.h: 260
class struct_uapi_ae_hwstats_s(Structure):
    pass

struct_uapi_ae_hwstats_s.__slots__ = [
    'chn',
    'extra',
    'yuvae',
    'sihist',
]
struct_uapi_ae_hwstats_s._fields_ = [
    ('chn', uapi_raw_stats_t * int(3)),
    ('extra', uapi_raw_stats_t),
    ('yuvae', uapi_yuvae_stats_t),
    ('sihist', uapi_sihist_stats_t),
]

uapi_ae_hwstats_t = struct_uapi_ae_hwstats_s# /root/camera_engine_rkaiq/include/iq_parser_v2/aec_uapi_head.h: 260

# /root/camera_engine_rkaiq/include/iq_parser_v2/RkAiqUapitypes.h: 101
class struct___aiq_scene(Structure):
    pass

struct___aiq_scene.__slots__ = [
    'main_scene',
    'sub_scene',
]
struct___aiq_scene._fields_ = [
    ('main_scene', String),
    ('sub_scene', String),
]

aiq_scene_t = struct___aiq_scene# /root/camera_engine_rkaiq/include/iq_parser_v2/RkAiqUapitypes.h: 101

# /root/camera_engine_rkaiq/include/iq_parser_v2/RkAiqUapitypes.h: 106
class struct___work_mode(Structure):
    pass

struct___work_mode.__slots__ = [
    'mode',
]
struct___work_mode._fields_ = [
    ('mode', rk_aiq_working_mode_t),
]

work_mode_t = struct___work_mode# /root/camera_engine_rkaiq/include/iq_parser_v2/RkAiqUapitypes.h: 106

# /root/camera_engine_rkaiq/include/iq_parser_v2/RkAiqUapitypes.h: 133
class struct___ablc_uapi_manual(Structure):
    pass

struct___ablc_uapi_manual.__slots__ = [
    'AblcOpMode',
]
struct___ablc_uapi_manual._fields_ = [
    ('AblcOpMode', RKAiqOPMode_t),
]

ablc_uapi_manual_t = struct___ablc_uapi_manual# /root/camera_engine_rkaiq/include/iq_parser_v2/RkAiqUapitypes.h: 133

# /root/camera_engine_rkaiq/include/iq_parser_v2/RkAiqUapitypes.h: 142
class struct___ablc_uapi_info(Structure):
    pass

struct___ablc_uapi_info.__slots__ = [
    'iso',
]
struct___ablc_uapi_info._fields_ = [
    ('iso', c_int),
]

ablc_uapi_info_t = struct___ablc_uapi_info# /root/camera_engine_rkaiq/include/iq_parser_v2/RkAiqUapitypes.h: 142

# /root/camera_engine_rkaiq/include/iq_parser_v2/RkAiqUapitypes.h: 160
class struct___abayertnr_uapi_manual(Structure):
    pass

struct___abayertnr_uapi_manual.__slots__ = [
    'AbayertnrOpMode',
]
struct___abayertnr_uapi_manual._fields_ = [
    ('AbayertnrOpMode', RKAiqOPMode_t),
]

abayertnr_uapi_manual_t = struct___abayertnr_uapi_manual# /root/camera_engine_rkaiq/include/iq_parser_v2/RkAiqUapitypes.h: 160

# /root/camera_engine_rkaiq/include/iq_parser_v2/RkAiqUapitypes.h: 169
class struct___abayertnr_uapi_info(Structure):
    pass

struct___abayertnr_uapi_info.__slots__ = [
    'iso',
]
struct___abayertnr_uapi_info._fields_ = [
    ('iso', c_int),
]

abayertnr_uapi_info_t = struct___abayertnr_uapi_info# /root/camera_engine_rkaiq/include/iq_parser_v2/RkAiqUapitypes.h: 169

# /root/camera_engine_rkaiq/include/iq_parser_v2/RkAiqUapitypes.h: 187
class struct___abayer2dnr_uapi_manual(Structure):
    pass

struct___abayer2dnr_uapi_manual.__slots__ = [
    'Abayer2dnrOpMode',
]
struct___abayer2dnr_uapi_manual._fields_ = [
    ('Abayer2dnrOpMode', RKAiqOPMode_t),
]

abayer2dnr_uapi_manual_t = struct___abayer2dnr_uapi_manual# /root/camera_engine_rkaiq/include/iq_parser_v2/RkAiqUapitypes.h: 187

# /root/camera_engine_rkaiq/include/iq_parser_v2/RkAiqUapitypes.h: 196
class struct___abayer2dnr_uapi_info(Structure):
    pass

struct___abayer2dnr_uapi_info.__slots__ = [
    'iso',
]
struct___abayer2dnr_uapi_info._fields_ = [
    ('iso', c_int),
]

abayer2dnr_uapi_info_t = struct___abayer2dnr_uapi_info# /root/camera_engine_rkaiq/include/iq_parser_v2/RkAiqUapitypes.h: 196

# /root/camera_engine_rkaiq/include/iq_parser_v2/RkAiqUapitypes.h: 214
class struct___aynr_uapi_manual(Structure):
    pass

struct___aynr_uapi_manual.__slots__ = [
    'AynrOpMode',
]
struct___aynr_uapi_manual._fields_ = [
    ('AynrOpMode', RKAiqOPMode_t),
]

aynr_uapi_manual_t = struct___aynr_uapi_manual# /root/camera_engine_rkaiq/include/iq_parser_v2/RkAiqUapitypes.h: 214

# /root/camera_engine_rkaiq/include/iq_parser_v2/RkAiqUapitypes.h: 223
class struct___aynr_uapi_info(Structure):
    pass

struct___aynr_uapi_info.__slots__ = [
    'iso',
]
struct___aynr_uapi_info._fields_ = [
    ('iso', c_int),
]

aynr_uapi_info_t = struct___aynr_uapi_info# /root/camera_engine_rkaiq/include/iq_parser_v2/RkAiqUapitypes.h: 223

# /root/camera_engine_rkaiq/include/iq_parser_v2/RkAiqUapitypes.h: 240
class struct___acnr_uapi_manual(Structure):
    pass

struct___acnr_uapi_manual.__slots__ = [
    'AcnrOpMode',
]
struct___acnr_uapi_manual._fields_ = [
    ('AcnrOpMode', RKAiqOPMode_t),
]

acnr_uapi_manual_t = struct___acnr_uapi_manual# /root/camera_engine_rkaiq/include/iq_parser_v2/RkAiqUapitypes.h: 240

# /root/camera_engine_rkaiq/include/iq_parser_v2/RkAiqUapitypes.h: 249
class struct___acnr_uapi_info(Structure):
    pass

struct___acnr_uapi_info.__slots__ = [
    'iso',
]
struct___acnr_uapi_info._fields_ = [
    ('iso', c_int),
]

acnr_uapi_info_t = struct___acnr_uapi_info# /root/camera_engine_rkaiq/include/iq_parser_v2/RkAiqUapitypes.h: 249

# /root/camera_engine_rkaiq/include/iq_parser_v2/RkAiqUapitypes.h: 267
class struct___asharp_uapi_manual(Structure):
    pass

struct___asharp_uapi_manual.__slots__ = [
    'AsharpOpMode',
]
struct___asharp_uapi_manual._fields_ = [
    ('AsharpOpMode', RKAiqOPMode_t),
]

asharp_uapi_manual_t = struct___asharp_uapi_manual# /root/camera_engine_rkaiq/include/iq_parser_v2/RkAiqUapitypes.h: 267

# /root/camera_engine_rkaiq/include/iq_parser_v2/RkAiqUapitypes.h: 276
class struct___asharp_uapi_info(Structure):
    pass

struct___asharp_uapi_info.__slots__ = [
    'iso',
]
struct___asharp_uapi_info._fields_ = [
    ('iso', c_int),
]

asharp_uapi_info_t = struct___asharp_uapi_info# /root/camera_engine_rkaiq/include/iq_parser_v2/RkAiqUapitypes.h: 276

# /root/camera_engine_rkaiq/include/iq_parser_v2/RkAiqUapitypes.h: 293
class struct___again_uapi_manual(Structure):
    pass

struct___again_uapi_manual.__slots__ = [
    'AgainOpMode',
]
struct___again_uapi_manual._fields_ = [
    ('AgainOpMode', RKAiqOPMode_t),
]

again_uapi_manual_t = struct___again_uapi_manual# /root/camera_engine_rkaiq/include/iq_parser_v2/RkAiqUapitypes.h: 293

# /root/camera_engine_rkaiq/include/iq_parser_v2/RkAiqUapitypes.h: 302
class struct___again_uapi_info(Structure):
    pass

struct___again_uapi_info.__slots__ = [
    'iso',
]
struct___again_uapi_info._fields_ = [
    ('iso', c_int),
]

again_uapi_info_t = struct___again_uapi_info# /root/camera_engine_rkaiq/include/iq_parser_v2/RkAiqUapitypes.h: 302

# /root/camera_engine_rkaiq/include/iq_parser_v2/RkAiqUapitypes.h: 358
class struct___camgroup_uapi(Structure):
    pass

struct___camgroup_uapi.__slots__ = [
    'current_index',
]
struct___camgroup_uapi._fields_ = [
    ('current_index', uint8_t),
]

camgroup_uapi_t = struct___camgroup_uapi# /root/camera_engine_rkaiq/include/iq_parser_v2/RkAiqUapitypes.h: 358

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_wrapper.h: 24
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi_sysctl_swWorkingModeDyn2", "cdecl"):
        continue
    rk_aiq_uapi_sysctl_swWorkingModeDyn2 = _lib.get("rk_aiq_uapi_sysctl_swWorkingModeDyn2", "cdecl")
    rk_aiq_uapi_sysctl_swWorkingModeDyn2.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(work_mode_t)]
    rk_aiq_uapi_sysctl_swWorkingModeDyn2.restype = c_int
    break

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_wrapper.h: 27
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi_sysctl_getWorkingModeDyn", "cdecl"):
        continue
    rk_aiq_uapi_sysctl_getWorkingModeDyn = _lib.get("rk_aiq_uapi_sysctl_getWorkingModeDyn", "cdecl")
    rk_aiq_uapi_sysctl_getWorkingModeDyn.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(work_mode_t)]
    rk_aiq_uapi_sysctl_getWorkingModeDyn.restype = c_int
    break

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_wrapper.h: 30
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_setWBMode2", "cdecl"):
        continue
    rk_aiq_uapi2_setWBMode2 = _lib.get("rk_aiq_uapi2_setWBMode2", "cdecl")
    rk_aiq_uapi2_setWBMode2.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(uapi_wb_mode_t)]
    rk_aiq_uapi2_setWBMode2.restype = c_int
    break

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_wrapper.h: 32
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_getWBMode2", "cdecl"):
        continue
    rk_aiq_uapi2_getWBMode2 = _lib.get("rk_aiq_uapi2_getWBMode2", "cdecl")
    rk_aiq_uapi2_getWBMode2.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(uapi_wb_mode_t)]
    rk_aiq_uapi2_getWBMode2.restype = c_int
    break

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_wrapper.h: 34
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_amerge_GetCtldata", "cdecl"):
        continue
    rk_aiq_user_api2_amerge_GetCtldata = _lib.get("rk_aiq_user_api2_amerge_GetCtldata", "cdecl")
    rk_aiq_user_api2_amerge_GetCtldata.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(uapiMergeCurrCtlData_t)]
    rk_aiq_user_api2_amerge_GetCtldata.restype = c_int
    break

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_wrapper.h: 37
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_set_scene", "cdecl"):
        continue
    rk_aiq_user_api2_set_scene = _lib.get("rk_aiq_user_api2_set_scene", "cdecl")
    rk_aiq_user_api2_set_scene.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(aiq_scene_t)]
    rk_aiq_user_api2_set_scene.restype = c_int
    break

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_wrapper.h: 40
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_get_scene", "cdecl"):
        continue
    rk_aiq_user_api2_get_scene = _lib.get("rk_aiq_user_api2_get_scene", "cdecl")
    rk_aiq_user_api2_get_scene.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(aiq_scene_t)]
    rk_aiq_user_api2_get_scene.restype = c_int
    break

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_wrapper.h: 43
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi_get_awb_stat", "cdecl"):
        continue
    rk_aiq_uapi_get_awb_stat = _lib.get("rk_aiq_uapi_get_awb_stat", "cdecl")
    rk_aiq_uapi_get_awb_stat.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_tool_awb_stat_res2_v30_t)]
    rk_aiq_uapi_get_awb_stat.restype = c_int
    break

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_wrapper.h: 46
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi_get_ae_hwstats", "cdecl"):
        continue
    rk_aiq_uapi_get_ae_hwstats = _lib.get("rk_aiq_uapi_get_ae_hwstats", "cdecl")
    rk_aiq_uapi_get_ae_hwstats.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(uapi_ae_hwstats_t)]
    rk_aiq_uapi_get_ae_hwstats.restype = c_int
    break

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_wrapper.h: 49
for _lib in _libs.values():
    if not _lib.has("rk_aiq_get_adpcc_manual_attr", "cdecl"):
        continue
    rk_aiq_get_adpcc_manual_attr = _lib.get("rk_aiq_get_adpcc_manual_attr", "cdecl")
    rk_aiq_get_adpcc_manual_attr.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(Adpcc_Manual_Attr_t)]
    rk_aiq_get_adpcc_manual_attr.restype = XCamReturn
    break

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_wrapper.h: 52
for _lib in _libs.values():
    if not _lib.has("rk_aiq_set_adpcc_manual_attr", "cdecl"):
        continue
    rk_aiq_set_adpcc_manual_attr = _lib.get("rk_aiq_set_adpcc_manual_attr", "cdecl")
    rk_aiq_set_adpcc_manual_attr.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(Adpcc_Manual_Attr_t)]
    rk_aiq_set_adpcc_manual_attr.restype = XCamReturn
    break

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_wrapper.h: 55
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_adrc_queryinfo", "cdecl"):
        continue
    rk_aiq_user_api2_adrc_queryinfo = _lib.get("rk_aiq_user_api2_adrc_queryinfo", "cdecl")
    rk_aiq_user_api2_adrc_queryinfo.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(DrcInfo_t)]
    rk_aiq_user_api2_adrc_queryinfo.restype = XCamReturn
    break

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_wrapper.h: 58
for _lib in _libs.values():
    if not _lib.has("rk_aiq_set_adrc_manual_attr", "cdecl"):
        continue
    rk_aiq_set_adrc_manual_attr = _lib.get("rk_aiq_set_adrc_manual_attr", "cdecl")
    rk_aiq_set_adrc_manual_attr.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(mdrcAttr_V30_t)]
    rk_aiq_set_adrc_manual_attr.restype = XCamReturn
    break

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_wrapper.h: 61
for _lib in _libs.values():
    if not _lib.has("rk_aiq_get_adrc_manual_attr", "cdecl"):
        continue
    rk_aiq_get_adrc_manual_attr = _lib.get("rk_aiq_get_adrc_manual_attr", "cdecl")
    rk_aiq_get_adrc_manual_attr.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(mdrcAttr_V30_t)]
    rk_aiq_get_adrc_manual_attr.restype = XCamReturn
    break

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_wrapper.h: 64
for _lib in _libs.values():
    if not _lib.has("rk_aiq_set_amerge_manual_attr", "cdecl"):
        continue
    rk_aiq_set_amerge_manual_attr = _lib.get("rk_aiq_set_amerge_manual_attr", "cdecl")
    rk_aiq_set_amerge_manual_attr.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(mMergeAttrV30_t)]
    rk_aiq_set_amerge_manual_attr.restype = XCamReturn
    break

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_wrapper.h: 67
for _lib in _libs.values():
    if not _lib.has("rk_aiq_get_amerge_manual_attr", "cdecl"):
        continue
    rk_aiq_get_amerge_manual_attr = _lib.get("rk_aiq_get_amerge_manual_attr", "cdecl")
    rk_aiq_get_amerge_manual_attr.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(mMergeAttrV30_t)]
    rk_aiq_get_amerge_manual_attr.restype = XCamReturn
    break

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_wrapper.h: 70
for _lib in _libs.values():
    if not _lib.has("rk_aiq_set_agamma_manual_attr", "cdecl"):
        continue
    rk_aiq_set_agamma_manual_attr = _lib.get("rk_aiq_set_agamma_manual_attr", "cdecl")
    rk_aiq_set_agamma_manual_attr.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(Agamma_api_manualV30_t)]
    rk_aiq_set_agamma_manual_attr.restype = XCamReturn
    break

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_wrapper.h: 73
for _lib in _libs.values():
    if not _lib.has("rk_aiq_get_agamma_manual_attr", "cdecl"):
        continue
    rk_aiq_get_agamma_manual_attr = _lib.get("rk_aiq_get_agamma_manual_attr", "cdecl")
    rk_aiq_get_agamma_manual_attr.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(Agamma_api_manualV30_t)]
    rk_aiq_get_agamma_manual_attr.restype = XCamReturn
    break

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_wrapper.h: 76
for _lib in _libs.values():
    if not _lib.has("rk_aiq_set_tool_ccm_mode", "cdecl"):
        continue
    rk_aiq_set_tool_ccm_mode = _lib.get("rk_aiq_set_tool_ccm_mode", "cdecl")
    rk_aiq_set_tool_ccm_mode.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(uapi_wb_mode_t)]
    rk_aiq_set_tool_ccm_mode.restype = XCamReturn
    break

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_wrapper.h: 79
for _lib in _libs.values():
    if not _lib.has("rk_aiq_get_accm_mode", "cdecl"):
        continue
    rk_aiq_get_accm_mode = _lib.get("rk_aiq_get_accm_mode", "cdecl")
    rk_aiq_get_accm_mode.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(uapi_wb_mode_t)]
    rk_aiq_get_accm_mode.restype = XCamReturn
    break

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_wrapper.h: 82
for _lib in _libs.values():
    if not _lib.has("rk_aiq_set_accm_manual_attr", "cdecl"):
        continue
    rk_aiq_set_accm_manual_attr = _lib.get("rk_aiq_set_accm_manual_attr", "cdecl")
    rk_aiq_set_accm_manual_attr.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_ccm_mccm_attrib_t)]
    rk_aiq_set_accm_manual_attr.restype = XCamReturn
    break

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_wrapper.h: 85
for _lib in _libs.values():
    if not _lib.has("rk_aiq_get_accm_manual_attr", "cdecl"):
        continue
    rk_aiq_get_accm_manual_attr = _lib.get("rk_aiq_get_accm_manual_attr", "cdecl")
    rk_aiq_get_accm_manual_attr.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_ccm_mccm_attrib_t)]
    rk_aiq_get_accm_manual_attr.restype = XCamReturn
    break

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_wrapper.h: 89
for _lib in _libs.values():
    if not _lib.has("rk_aiq_set_tool_3dlut_mode", "cdecl"):
        continue
    rk_aiq_set_tool_3dlut_mode = _lib.get("rk_aiq_set_tool_3dlut_mode", "cdecl")
    rk_aiq_set_tool_3dlut_mode.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(uapi_wb_mode_t)]
    rk_aiq_set_tool_3dlut_mode.restype = XCamReturn
    break

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_wrapper.h: 92
for _lib in _libs.values():
    if not _lib.has("rk_aiq_get_a3dlut_mode", "cdecl"):
        continue
    rk_aiq_get_a3dlut_mode = _lib.get("rk_aiq_get_a3dlut_mode", "cdecl")
    rk_aiq_get_a3dlut_mode.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(uapi_wb_mode_t)]
    rk_aiq_get_a3dlut_mode.restype = XCamReturn
    break

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_wrapper.h: 95
for _lib in _libs.values():
    if not _lib.has("rk_aiq_set_a3dlut_manual_attr", "cdecl"):
        continue
    rk_aiq_set_a3dlut_manual_attr = _lib.get("rk_aiq_set_a3dlut_manual_attr", "cdecl")
    rk_aiq_set_a3dlut_manual_attr.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_lut3d_mlut3d_attrib_t)]
    rk_aiq_set_a3dlut_manual_attr.restype = XCamReturn
    break

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_wrapper.h: 98
for _lib in _libs.values():
    if not _lib.has("rk_aiq_get_a3dlut_manual_attr", "cdecl"):
        continue
    rk_aiq_get_a3dlut_manual_attr = _lib.get("rk_aiq_get_a3dlut_manual_attr", "cdecl")
    rk_aiq_get_a3dlut_manual_attr.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_lut3d_mlut3d_attrib_t)]
    rk_aiq_get_a3dlut_manual_attr.restype = XCamReturn
    break

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_wrapper.h: 101
for _lib in _libs.values():
    if not _lib.has("rk_aiq_set_acsm_manual_attr", "cdecl"):
        continue
    rk_aiq_set_acsm_manual_attr = _lib.get("rk_aiq_set_acsm_manual_attr", "cdecl")
    rk_aiq_set_acsm_manual_attr.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(Csm_Param_t)]
    rk_aiq_set_acsm_manual_attr.restype = XCamReturn
    break

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_wrapper.h: 104
for _lib in _libs.values():
    if not _lib.has("rk_aiq_get_acsm_manual_attr", "cdecl"):
        continue
    rk_aiq_get_acsm_manual_attr = _lib.get("rk_aiq_get_acsm_manual_attr", "cdecl")
    rk_aiq_get_acsm_manual_attr.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(Csm_Param_t)]
    rk_aiq_get_acsm_manual_attr.restype = XCamReturn
    break

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_wrapper.h: 107
for _lib in _libs.values():
    if not _lib.has("rk_aiq_set_adehaze_manual_attr", "cdecl"):
        continue
    rk_aiq_set_adehaze_manual_attr = _lib.get("rk_aiq_set_adehaze_manual_attr", "cdecl")
    rk_aiq_set_adehaze_manual_attr.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(mDehazeAttr_t)]
    rk_aiq_set_adehaze_manual_attr.restype = XCamReturn
    break

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_wrapper.h: 110
for _lib in _libs.values():
    if not _lib.has("rk_aiq_get_adehaze_manual_attr", "cdecl"):
        continue
    rk_aiq_get_adehaze_manual_attr = _lib.get("rk_aiq_get_adehaze_manual_attr", "cdecl")
    rk_aiq_get_adehaze_manual_attr.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(mDehazeAttr_t)]
    rk_aiq_get_adehaze_manual_attr.restype = XCamReturn
    break

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_wrapper.h: 113
for _lib in _libs.values():
    if not _lib.has("rk_aiq_set_alsc_manual_attr", "cdecl"):
        continue
    rk_aiq_set_alsc_manual_attr = _lib.get("rk_aiq_set_alsc_manual_attr", "cdecl")
    rk_aiq_set_alsc_manual_attr.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_lsc_table_t)]
    rk_aiq_set_alsc_manual_attr.restype = XCamReturn
    break

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_wrapper.h: 116
for _lib in _libs.values():
    if not _lib.has("rk_aiq_get_alsc_manual_attr", "cdecl"):
        continue
    rk_aiq_get_alsc_manual_attr = _lib.get("rk_aiq_get_alsc_manual_attr", "cdecl")
    rk_aiq_get_alsc_manual_attr.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_lsc_table_t)]
    rk_aiq_get_alsc_manual_attr.restype = XCamReturn
    break

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_wrapper.h: 119
for _lib in _libs.values():
    if not _lib.has("rk_aiq_set_current_camindex", "cdecl"):
        continue
    rk_aiq_set_current_camindex = _lib.get("rk_aiq_set_current_camindex", "cdecl")
    rk_aiq_set_current_camindex.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(camgroup_uapi_t)]
    rk_aiq_set_current_camindex.restype = XCamReturn
    break

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_wrapper.h: 122
for _lib in _libs.values():
    if not _lib.has("rk_aiq_get_current_camindex", "cdecl"):
        continue
    rk_aiq_get_current_camindex = _lib.get("rk_aiq_get_current_camindex", "cdecl")
    rk_aiq_get_current_camindex.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(camgroup_uapi_t)]
    rk_aiq_get_current_camindex.restype = XCamReturn
    break

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_wrapper.h: 125
for _lib in _libs.values():
    if not _lib.has("rk_aiq_get_last_sysctx", "cdecl"):
        continue
    rk_aiq_get_last_sysctx = _lib.get("rk_aiq_get_last_sysctx", "cdecl")
    rk_aiq_get_last_sysctx.argtypes = [POINTER(rk_aiq_sys_ctx_t)]
    rk_aiq_get_last_sysctx.restype = POINTER(rk_aiq_sys_ctx_t)
    break

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_wrapper.h: 127
for _lib in _libs.values():
    if not _lib.has("rk_aiq_set_adebayer_attr", "cdecl"):
        continue
    rk_aiq_set_adebayer_attr = _lib.get("rk_aiq_set_adebayer_attr", "cdecl")
    rk_aiq_set_adebayer_attr.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(adebayer_attrib_t)]
    rk_aiq_set_adebayer_attr.restype = XCamReturn
    break

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_wrapper.h: 130
for _lib in _libs.values():
    if not _lib.has("rk_aiq_get_adebayer_attr", "cdecl"):
        continue
    rk_aiq_get_adebayer_attr = _lib.get("rk_aiq_get_adebayer_attr", "cdecl")
    rk_aiq_get_adebayer_attr.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(adebayer_attrib_t)]
    rk_aiq_get_adebayer_attr.restype = XCamReturn
    break

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_wrapper.h: 134
for _lib in _libs.values():
    if not _lib.has("rk_aiq_set_asharp_manual_attr", "cdecl"):
        continue
    rk_aiq_set_asharp_manual_attr = _lib.get("rk_aiq_set_asharp_manual_attr", "cdecl")
    rk_aiq_set_asharp_manual_attr.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(asharp_uapi_manual_t)]
    rk_aiq_set_asharp_manual_attr.restype = XCamReturn
    break

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_wrapper.h: 138
for _lib in _libs.values():
    if not _lib.has("rk_aiq_get_asharp_manual_attr", "cdecl"):
        continue
    rk_aiq_get_asharp_manual_attr = _lib.get("rk_aiq_get_asharp_manual_attr", "cdecl")
    rk_aiq_get_asharp_manual_attr.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(asharp_uapi_manual_t)]
    rk_aiq_get_asharp_manual_attr.restype = XCamReturn
    break

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_wrapper.h: 142
for _lib in _libs.values():
    if not _lib.has("rk_aiq_set_abayer2dnr_manual_attr", "cdecl"):
        continue
    rk_aiq_set_abayer2dnr_manual_attr = _lib.get("rk_aiq_set_abayer2dnr_manual_attr", "cdecl")
    rk_aiq_set_abayer2dnr_manual_attr.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(abayer2dnr_uapi_manual_t)]
    rk_aiq_set_abayer2dnr_manual_attr.restype = XCamReturn
    break

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_wrapper.h: 146
for _lib in _libs.values():
    if not _lib.has("rk_aiq_get_abayer2dnr_manual_attr", "cdecl"):
        continue
    rk_aiq_get_abayer2dnr_manual_attr = _lib.get("rk_aiq_get_abayer2dnr_manual_attr", "cdecl")
    rk_aiq_get_abayer2dnr_manual_attr.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(abayer2dnr_uapi_manual_t)]
    rk_aiq_get_abayer2dnr_manual_attr.restype = XCamReturn
    break

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_wrapper.h: 150
for _lib in _libs.values():
    if not _lib.has("rk_aiq_set_abayertnr_manual_attr", "cdecl"):
        continue
    rk_aiq_set_abayertnr_manual_attr = _lib.get("rk_aiq_set_abayertnr_manual_attr", "cdecl")
    rk_aiq_set_abayertnr_manual_attr.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(abayertnr_uapi_manual_t)]
    rk_aiq_set_abayertnr_manual_attr.restype = XCamReturn
    break

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_wrapper.h: 154
for _lib in _libs.values():
    if not _lib.has("rk_aiq_get_abayertnr_manual_attr", "cdecl"):
        continue
    rk_aiq_get_abayertnr_manual_attr = _lib.get("rk_aiq_get_abayertnr_manual_attr", "cdecl")
    rk_aiq_get_abayertnr_manual_attr.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(abayertnr_uapi_manual_t)]
    rk_aiq_get_abayertnr_manual_attr.restype = XCamReturn
    break

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_wrapper.h: 159
for _lib in _libs.values():
    if not _lib.has("rk_aiq_set_aynr_manual_attr", "cdecl"):
        continue
    rk_aiq_set_aynr_manual_attr = _lib.get("rk_aiq_set_aynr_manual_attr", "cdecl")
    rk_aiq_set_aynr_manual_attr.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(aynr_uapi_manual_t)]
    rk_aiq_set_aynr_manual_attr.restype = XCamReturn
    break

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_wrapper.h: 163
for _lib in _libs.values():
    if not _lib.has("rk_aiq_get_aynr_manual_attr", "cdecl"):
        continue
    rk_aiq_get_aynr_manual_attr = _lib.get("rk_aiq_get_aynr_manual_attr", "cdecl")
    rk_aiq_get_aynr_manual_attr.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(aynr_uapi_manual_t)]
    rk_aiq_get_aynr_manual_attr.restype = XCamReturn
    break

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_wrapper.h: 167
for _lib in _libs.values():
    if not _lib.has("rk_aiq_set_acnr_manual_attr", "cdecl"):
        continue
    rk_aiq_set_acnr_manual_attr = _lib.get("rk_aiq_set_acnr_manual_attr", "cdecl")
    rk_aiq_set_acnr_manual_attr.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(acnr_uapi_manual_t)]
    rk_aiq_set_acnr_manual_attr.restype = XCamReturn
    break

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_wrapper.h: 171
for _lib in _libs.values():
    if not _lib.has("rk_aiq_get_acnr_manual_attr", "cdecl"):
        continue
    rk_aiq_get_acnr_manual_attr = _lib.get("rk_aiq_get_acnr_manual_attr", "cdecl")
    rk_aiq_get_acnr_manual_attr.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(acnr_uapi_manual_t)]
    rk_aiq_get_acnr_manual_attr.restype = XCamReturn
    break

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_wrapper.h: 175
for _lib in _libs.values():
    if not _lib.has("rk_aiq_set_again_manual_attr", "cdecl"):
        continue
    rk_aiq_set_again_manual_attr = _lib.get("rk_aiq_set_again_manual_attr", "cdecl")
    rk_aiq_set_again_manual_attr.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(again_uapi_manual_t)]
    rk_aiq_set_again_manual_attr.restype = XCamReturn
    break

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_wrapper.h: 179
for _lib in _libs.values():
    if not _lib.has("rk_aiq_get_again_manual_attr", "cdecl"):
        continue
    rk_aiq_get_again_manual_attr = _lib.get("rk_aiq_get_again_manual_attr", "cdecl")
    rk_aiq_get_again_manual_attr.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(again_uapi_manual_t)]
    rk_aiq_get_again_manual_attr.restype = XCamReturn
    break

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_wrapper.h: 184
for _lib in _libs.values():
    if not _lib.has("rk_aiq_set_ablc_manual_attr", "cdecl"):
        continue
    rk_aiq_set_ablc_manual_attr = _lib.get("rk_aiq_set_ablc_manual_attr", "cdecl")
    rk_aiq_set_ablc_manual_attr.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(ablc_uapi_manual_t)]
    rk_aiq_set_ablc_manual_attr.restype = XCamReturn
    break

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_wrapper.h: 188
for _lib in _libs.values():
    if not _lib.has("rk_aiq_get_ablc_manual_attr", "cdecl"):
        continue
    rk_aiq_get_ablc_manual_attr = _lib.get("rk_aiq_get_ablc_manual_attr", "cdecl")
    rk_aiq_get_ablc_manual_attr.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(ablc_uapi_manual_t)]
    rk_aiq_get_ablc_manual_attr.restype = XCamReturn
    break

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_wrapper.h: 193
for _lib in _libs.values():
    if not _lib.has("rk_aiq_get_abayertnr_info", "cdecl"):
        continue
    rk_aiq_get_abayertnr_info = _lib.get("rk_aiq_get_abayertnr_info", "cdecl")
    rk_aiq_get_abayertnr_info.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(abayertnr_uapi_info_t)]
    rk_aiq_get_abayertnr_info.restype = XCamReturn
    break

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_wrapper.h: 197
for _lib in _libs.values():
    if not _lib.has("rk_aiq_get_abayer2dnr_info", "cdecl"):
        continue
    rk_aiq_get_abayer2dnr_info = _lib.get("rk_aiq_get_abayer2dnr_info", "cdecl")
    rk_aiq_get_abayer2dnr_info.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(abayer2dnr_uapi_info_t)]
    rk_aiq_get_abayer2dnr_info.restype = XCamReturn
    break

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_wrapper.h: 200
for _lib in _libs.values():
    if not _lib.has("rk_aiq_get_aynr_info", "cdecl"):
        continue
    rk_aiq_get_aynr_info = _lib.get("rk_aiq_get_aynr_info", "cdecl")
    rk_aiq_get_aynr_info.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(aynr_uapi_info_t)]
    rk_aiq_get_aynr_info.restype = XCamReturn
    break

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_wrapper.h: 203
for _lib in _libs.values():
    if not _lib.has("rk_aiq_get_acnr_info", "cdecl"):
        continue
    rk_aiq_get_acnr_info = _lib.get("rk_aiq_get_acnr_info", "cdecl")
    rk_aiq_get_acnr_info.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(acnr_uapi_info_t)]
    rk_aiq_get_acnr_info.restype = XCamReturn
    break

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_wrapper.h: 206
for _lib in _libs.values():
    if not _lib.has("rk_aiq_get_asharp_info", "cdecl"):
        continue
    rk_aiq_get_asharp_info = _lib.get("rk_aiq_get_asharp_info", "cdecl")
    rk_aiq_get_asharp_info.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(asharp_uapi_info_t)]
    rk_aiq_get_asharp_info.restype = XCamReturn
    break

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_wrapper.h: 210
for _lib in _libs.values():
    if not _lib.has("rk_aiq_get_again_info", "cdecl"):
        continue
    rk_aiq_get_again_info = _lib.get("rk_aiq_get_again_info", "cdecl")
    rk_aiq_get_again_info.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(again_uapi_info_t)]
    rk_aiq_get_again_info.restype = XCamReturn
    break

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_wrapper.h: 214
for _lib in _libs.values():
    if not _lib.has("rk_aiq_get_ablc_info", "cdecl"):
        continue
    rk_aiq_get_ablc_info = _lib.get("rk_aiq_get_ablc_info", "cdecl")
    rk_aiq_get_ablc_info.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(ablc_uapi_info_t)]
    rk_aiq_get_ablc_info.restype = XCamReturn
    break

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_custom_ae.h: 28
try:
    RK_AIQ_MAX_HDR_FRAME = 3
except:
    pass

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_helper.h: 28
try:
    RKAIQ_UAPI_NAME_MAX_LEN = 64
except:
    pass

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_helper.h: 29
try:
    JSON_PATCH_PATH = 'path'
except:
    pass

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_helper.h: 30
try:
    JSON_PATCH_VALUE = 'value'
except:
    pass

# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_helper.h: 102
def __RKAIQUAPI_FUNC_CAST(__api):
    return (RkAiqUapi (ord_if_char(__api))).value

rk_aiq_sys_ctx_s = struct_rk_aiq_sys_ctx_s# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_a3dlut.h: 24

rk_aiq_ctx_camInfo_s = struct_rk_aiq_ctx_camInfo_s# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_sysctl.h: 332

rk_aiq_camgroup_ctx_s = struct_rk_aiq_camgroup_ctx_s# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_camgroup.h: 61

rk_aiq_camgroup_instance_cfg_s = struct_rk_aiq_camgroup_instance_cfg_s# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_camgroup.h: 73

rk_aiq_camgroup_camInfos_s = struct_rk_aiq_camgroup_camInfos_s# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_camgroup.h: 79

RK_PS_SrcOverlapMap = struct_RK_PS_SrcOverlapMap# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_camgroup.h: 84

rk_aiq_customAe_stats_s = struct_rk_aiq_customAe_stats_s# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_custom_ae.h: 32

rk_aiq_i2c_data_s = struct_rk_aiq_i2c_data_s# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_custom_ae.h: 53

rk_aiq_customeAe_results_singel_s = struct_rk_aiq_customeAe_results_singel_s# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_custom_ae.h: 56

rk_aiq_customeAe_results_s = struct_rk_aiq_customeAe_results_s# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_custom_ae.h: 87

rk_aiq_customeAe_cbs_s = struct_rk_aiq_customeAe_cbs_s# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_custom_ae.h: 101

rk_aiq_customAwb_stats_s = struct_rk_aiq_customAwb_stats_s# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_custom_awb.h: 28

rk_aiq_customAwb_hw_cfg_s = struct_rk_aiq_customAwb_hw_cfg_s# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_custom_awb.h: 74

rk_aiq_customAwb_single_hw_cfg_t = struct_rk_aiq_customAwb_single_hw_cfg_t# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_custom_awb.h: 82

rk_aiq_customeAwb_single_results_s = struct_rk_aiq_customeAwb_single_results_s# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_custom_awb.h: 86

rk_aiq_customeAwb_results_s = struct_rk_aiq_customeAwb_results_s# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_custom_awb.h: 102

rk_aiq_customeAwb_cbs_s = struct_rk_aiq_customeAwb_cbs_s# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_custom_awb.h: 116

__RkAiqUapiDesc = struct___RkAiqUapiDesc# /root/camera_engine_rkaiq/include/uAPI2/rk_aiq_user_api2_helper.h: 113

# No inserted files

# No prefix-stripping

