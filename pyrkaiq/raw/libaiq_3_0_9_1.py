r"""Wrapper for rk_aiq_tool_api.h

Generated with:
/usr/local/bin/ctypesgen -I ../camera-engine-rkaiq/rkaiq/uAPI/ -I /usr/include/rkaiq/uAPI2/ -I /usr/include/rkaiq/iq_parser_v2 -I /usr/include/rkaiq/iq_parser/ -I /usr/include/rkaiq/common/ -I /usr/include/rkaiq/algos/ -I /usr/include/rkaiq/xcore/ -I /usr/include/rkaiq /usr/include/rkaiq/uAPI2/rk_aiq_tool_api.h /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_a3dlut.h /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_abayer2dnr_v23.h /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_abayer2dnr_v2.h /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_abayernr_v2.h /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_abayertnr_v23.h /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_abayertnr_v2.h /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_ablc.h /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_ablc_v32.h /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_acac.h /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_accm.h /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_acgc.h /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_acnr_v1.h /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_acnr_v2.h /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_acnr_v30.h /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_acp.h /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_acsm.h /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_adebayer.h /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_adegamma.h /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_adehaze.h /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_adpcc.h /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_adrc.h /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_ae.h /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_afec.h /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_af.h /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_again_v2.h /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_agamma.h /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_agic.h /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_aie.h /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_aldch.h /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_aldch_v21.h /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_alsc.h /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_amerge.h /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_anr.h /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_asharp_v33.h /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_asharp_v3.h /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_asharp_v4.h /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_atmo.h /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_awb.h /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_aynr_v22.h /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_aynr_v2.h /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_aynr_v3.h /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_camgroup.h /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_custom_ae.h /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_custom_awb.h /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_custom_awb_type_v32.h /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_custom_awb_type_v3x.h /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_debug.h /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_helper.h /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_sysctl.h /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_wrapper.h /usr/include/rkaiq/uAPI2/rk_aiq_user_api_common.h -o libaiq_3_0_9_1.py

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
            dirs.append(os.path.join(os.environ["RESOURCEPATH"], "..", "Frameworks"))

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

# No libraries

# No modules

__uint8_t = c_ubyte# /usr/include/aarch64-linux-gnu/bits/types.h: 38

__uint16_t = c_ushort# /usr/include/aarch64-linux-gnu/bits/types.h: 40

__uint32_t = c_uint# /usr/include/aarch64-linux-gnu/bits/types.h: 42

__uint64_t = c_ulong# /usr/include/aarch64-linux-gnu/bits/types.h: 45

uint8_t = __uint8_t# /usr/include/aarch64-linux-gnu/bits/stdint-uintn.h: 24

uint16_t = __uint16_t# /usr/include/aarch64-linux-gnu/bits/stdint-uintn.h: 25

uint32_t = __uint32_t# /usr/include/aarch64-linux-gnu/bits/stdint-uintn.h: 26

uint64_t = __uint64_t# /usr/include/aarch64-linux-gnu/bits/stdint-uintn.h: 27

enum_anon_37 = c_int# /usr/include/rkaiq/xcore/base/xcam_common.h: 59

XCamReturn = enum_anon_37# /usr/include/rkaiq/xcore/base/xcam_common.h: 59

enum_RKAiqOPMode_e = c_int# /usr/include/rkaiq/common/rk_aiq_comm.h: 64

RKAiqOPMode_t = enum_RKAiqOPMode_e# /usr/include/rkaiq/common/rk_aiq_comm.h: 64

# /usr/include/rkaiq/common/rk_aiq_comm.h: 127
class struct_Cam15x15UCharMatrix_s(Structure):
    pass

struct_Cam15x15UCharMatrix_s.__slots__ = [
    'uCoeff',
]
struct_Cam15x15UCharMatrix_s._fields_ = [
    ('uCoeff', uint8_t * int((15 * 15))),
]

Cam15x15UCharMatrix_t = struct_Cam15x15UCharMatrix_s# /usr/include/rkaiq/common/rk_aiq_comm.h: 127

# /usr/include/rkaiq/common/rk_aiq_comm.h: 429
class struct_Cam17x17UShortMatrix_s(Structure):
    pass

struct_Cam17x17UShortMatrix_s.__slots__ = [
    'uCoeff',
]
struct_Cam17x17UShortMatrix_s._fields_ = [
    ('uCoeff', uint16_t * int((17 * 17))),
]

Cam17x17UShortMatrix_t = struct_Cam17x17UShortMatrix_s# /usr/include/rkaiq/common/rk_aiq_comm.h: 429

enum_anon_45 = c_int# /usr/include/rkaiq/common/rk_aiq_comm.h: 496

rk_aiq_uapi_mode_sync_e = enum_anon_45# /usr/include/rkaiq/common/rk_aiq_comm.h: 496

# /usr/include/rkaiq/common/rk_aiq_comm.h: 518
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

rk_aiq_uapi_sync_t = struct_rk_aiq_uapi_sync_s# /usr/include/rkaiq/common/rk_aiq_comm.h: 518

# /usr/include/rkaiq/algos/ae/rk_aiq_types_ae_hw.h: 60
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

window_t = struct_window# /usr/include/rkaiq/algos/ae/rk_aiq_types_ae_hw.h: 60

# /usr/include/rkaiq/algos/ae/rk_aiq_types_ae_hw.h: 293
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

RkAiqExpRealParam_t = struct_RkAiqExpRealParam_s# /usr/include/rkaiq/algos/ae/rk_aiq_types_ae_hw.h: 293

# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo.h: 34
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

rk_aiq_wb_gain_t = struct_rk_aiq_wb_gain_s# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo.h: 34

# /usr/include/rkaiq/algos/accm/rk_aiq_types_accm_algo.h: 32
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

rk_aiq_ccm_matrix_t = struct_rk_aiq_ccm_matrix_s# /usr/include/rkaiq/algos/accm/rk_aiq_types_accm_algo.h: 32

# /usr/include/rkaiq/algos/a3dlut/rk_aiq_types_a3dlut_algo.h: 33
class struct_rk_aiq_lut3d_table_s(Structure):
    pass

struct_rk_aiq_lut3d_table_s.__slots__ = [
    'look_up_table_r',
    'look_up_table_g',
    'look_up_table_b',
]
struct_rk_aiq_lut3d_table_s._fields_ = [
    ('look_up_table_r', c_ushort * int(((9 * 9) * 9))),
    ('look_up_table_g', c_ushort * int(((9 * 9) * 9))),
    ('look_up_table_b', c_ushort * int(((9 * 9) * 9))),
]

rk_aiq_lut3d_table_t = struct_rk_aiq_lut3d_table_s# /usr/include/rkaiq/algos/a3dlut/rk_aiq_types_a3dlut_algo.h: 33

enum_AdpccOPMode_e = c_int# /usr/include/rkaiq/algos/adpcc/rk_aiq_types_adpcc_ext.h: 46

AdpccOPMode_t = enum_AdpccOPMode_e# /usr/include/rkaiq/algos/adpcc/rk_aiq_types_adpcc_ext.h: 46

enum_Adpcc_onfly_mode_e = c_int# /usr/include/rkaiq/algos/adpcc/rk_aiq_types_adpcc_ext.h: 52

Adpcc_onfly_mode_t = enum_Adpcc_onfly_mode_e# /usr/include/rkaiq/algos/adpcc/rk_aiq_types_adpcc_ext.h: 52

# /usr/include/rkaiq/algos/adpcc/rk_aiq_types_adpcc_ext.h: 60
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

CalibDb_Dpcc_Sensor_t = struct_CalibDb_Dpcc_Sensor_s# /usr/include/rkaiq/algos/adpcc/rk_aiq_types_adpcc_ext.h: 60

# /usr/include/rkaiq/algos/adpcc/rk_aiq_types_adpcc_ext.h: 71
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

CalibDb_Dpcc_Fast_Mode_t = struct_CalibDb_Dpcc_Fast_Mode_s# /usr/include/rkaiq/algos/adpcc/rk_aiq_types_adpcc_ext.h: 71

# /usr/include/rkaiq/algos/adpcc/rk_aiq_types_adpcc_ext.h: 223
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

Adpcc_basic_params_select_t = struct_Adpcc_basic_params_select_s# /usr/include/rkaiq/algos/adpcc/rk_aiq_types_adpcc_ext.h: 223

# /usr/include/rkaiq/algos/adpcc/rk_aiq_types_adpcc_ext.h: 227
class struct_Adpcc_basic_params_s(Structure):
    pass

struct_Adpcc_basic_params_s.__slots__ = [
    'arBasic',
]
struct_Adpcc_basic_params_s._fields_ = [
    ('arBasic', Adpcc_basic_params_select_t * int(13)),
]

Adpcc_basic_params_t = struct_Adpcc_basic_params_s# /usr/include/rkaiq/algos/adpcc/rk_aiq_types_adpcc_ext.h: 227

# /usr/include/rkaiq/algos/adpcc/rk_aiq_types_adpcc_ext.h: 481
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

Adpcc_basic_cfg_params_t = struct_Adpcc_basic_cfg_params_s# /usr/include/rkaiq/algos/adpcc/rk_aiq_types_adpcc_ext.h: 481

# /usr/include/rkaiq/algos/adpcc/rk_aiq_types_adpcc_ext.h: 523
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

Adpcc_bpt_params_t = struct_Adpcc_bpt_params_s# /usr/include/rkaiq/algos/adpcc/rk_aiq_types_adpcc_ext.h: 523

# /usr/include/rkaiq/algos/adpcc/rk_aiq_types_adpcc_ext.h: 530
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

dpcc_pdaf_point_t = struct_dpcc_pdaf_point_s# /usr/include/rkaiq/algos/adpcc/rk_aiq_types_adpcc_ext.h: 530

# /usr/include/rkaiq/algos/adpcc/rk_aiq_types_adpcc_ext.h: 566
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

Adpcc_pdaf_params_t = struct_Adpcc_pdaf_params_s# /usr/include/rkaiq/algos/adpcc/rk_aiq_types_adpcc_ext.h: 566

# /usr/include/rkaiq/algos/adpcc/rk_aiq_types_adpcc_ext.h: 574
class struct_Adpcc_Auto_Attr_s(Structure):
    pass

struct_Adpcc_Auto_Attr_s.__slots__ = [
    'stBasicParams',
    'stBptParams',
    'stPdafParams',
    'stFastMode',
    'stSensorDpcc',
]
struct_Adpcc_Auto_Attr_s._fields_ = [
    ('stBasicParams', Adpcc_basic_params_t),
    ('stBptParams', Adpcc_bpt_params_t),
    ('stPdafParams', Adpcc_pdaf_params_t),
    ('stFastMode', CalibDb_Dpcc_Fast_Mode_t),
    ('stSensorDpcc', CalibDb_Dpcc_Sensor_t),
]

Adpcc_Auto_Attr_t = struct_Adpcc_Auto_Attr_s# /usr/include/rkaiq/algos/adpcc/rk_aiq_types_adpcc_ext.h: 574

# /usr/include/rkaiq/algos/adpcc/rk_aiq_types_adpcc_ext.h: 591
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

Adpcc_fast_mode_attr_t = struct_Adpcc_fast_mode_attr_s# /usr/include/rkaiq/algos/adpcc/rk_aiq_types_adpcc_ext.h: 591

# /usr/include/rkaiq/algos/adpcc/rk_aiq_types_adpcc_ext.h: 600
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

Adpcc_onfly_cfg_t = struct_Adpcc_onfly_cfg_s# /usr/include/rkaiq/algos/adpcc/rk_aiq_types_adpcc_ext.h: 600

# /usr/include/rkaiq/algos/adpcc/rk_aiq_types_adpcc_ext.h: 611
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

Adpcc_sensor_dpcc_attr_t = struct_Adpcc_sensor_dpcc_attr_s# /usr/include/rkaiq/algos/adpcc/rk_aiq_types_adpcc_ext.h: 611

# /usr/include/rkaiq/algos/adpcc/rk_aiq_types_adpcc_ext.h: 624
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

Adpcc_Manual_Attr_t = struct_Adpcc_Manual_Attr_s# /usr/include/rkaiq/algos/adpcc/rk_aiq_types_adpcc_ext.h: 624

# /usr/include/rkaiq/algos/adpcc/rk_aiq_types_adpcc_ext.h: 631
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

rk_aiq_dpcc_attrib_V20_t = struct_rk_aiq_dpcc_attrib_V20_s# /usr/include/rkaiq/algos/adpcc/rk_aiq_types_adpcc_ext.h: 631

# /usr/include/rkaiq/iq_parser/RkAiqCalibDbTypesIsp20.h: 1139
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

CalibDb_BayerNR_Params_t = struct_CalibDb_BayerNR_Params_s# /usr/include/rkaiq/iq_parser/RkAiqCalibDbTypesIsp20.h: 1139

# /usr/include/rkaiq/iq_parser/RkAiqCalibDbTypesIsp20.h: 1144
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

CalibDb_BayerNr_ModeCell_t = struct_CalibDb_BayerNr_ModeCell_s# /usr/include/rkaiq/iq_parser/RkAiqCalibDbTypesIsp20.h: 1144

# /usr/include/rkaiq/iq_parser/RkAiqCalibDbTypesIsp20.h: 1150
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

CalibDb_BayerNr_t = struct_CalibDb_BayerNr_s# /usr/include/rkaiq/iq_parser/RkAiqCalibDbTypesIsp20.h: 1150

# /usr/include/rkaiq/iq_parser/RkAiqCalibDbTypesIsp20.h: 1398
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

CalibDb_UVNR_Params_t = struct_CalibDb_UVNR_Params_s# /usr/include/rkaiq/iq_parser/RkAiqCalibDbTypesIsp20.h: 1398

# /usr/include/rkaiq/iq_parser/RkAiqCalibDbTypesIsp20.h: 1403
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

CalibDb_UVNR_ModeCell_t = struct_CalibDb_UVNR_ModeCell_s# /usr/include/rkaiq/iq_parser/RkAiqCalibDbTypesIsp20.h: 1403

# /usr/include/rkaiq/iq_parser/RkAiqCalibDbTypesIsp20.h: 1409
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

CalibDb_UVNR_t = struct_CalibDb_UVNR_s# /usr/include/rkaiq/iq_parser/RkAiqCalibDbTypesIsp20.h: 1409

# /usr/include/rkaiq/iq_parser/RkAiqCalibDbTypesIsp20.h: 1469
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

CalibDb_YNR_ISO_t = struct_CalibDb_YNR_ISO_s# /usr/include/rkaiq/iq_parser/RkAiqCalibDbTypesIsp20.h: 1469

# /usr/include/rkaiq/iq_parser/RkAiqCalibDbTypesIsp20.h: 1475
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

CalibDb_YNR_Setting_t = struct_CalibDb_YNR_Setting_s# /usr/include/rkaiq/iq_parser/RkAiqCalibDbTypesIsp20.h: 1475

# /usr/include/rkaiq/iq_parser/RkAiqCalibDbTypesIsp20.h: 1480
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

CalibDb_YNR_ModeCell_t = struct_CalibDb_YNR_ModeCell_s# /usr/include/rkaiq/iq_parser/RkAiqCalibDbTypesIsp20.h: 1480

# /usr/include/rkaiq/iq_parser/RkAiqCalibDbTypesIsp20.h: 1486
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

CalibDb_YNR_t = struct_CalibDb_YNR_s# /usr/include/rkaiq/iq_parser/RkAiqCalibDbTypesIsp20.h: 1486

# /usr/include/rkaiq/iq_parser/RkAiqCalibDbTypesIsp20.h: 1539
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

# /usr/include/rkaiq/iq_parser/RkAiqCalibDbTypesIsp20.h: 1544
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

# /usr/include/rkaiq/iq_parser/RkAiqCalibDbTypesIsp20.h: 1594
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

CalibDb_MFNR_Setting_t = struct_CalibDb_MFNR_Setting_s# /usr/include/rkaiq/iq_parser/RkAiqCalibDbTypesIsp20.h: 1594

# /usr/include/rkaiq/iq_parser/RkAiqCalibDbTypesIsp20.h: 1602
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

CalibDb_MFNR_Dynamic_t = struct_CalibDb_MFNR_Dynamic_s# /usr/include/rkaiq/iq_parser/RkAiqCalibDbTypesIsp20.h: 1602

# /usr/include/rkaiq/iq_parser/RkAiqCalibDbTypesIsp20.h: 1625
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

CalibDb_MFNR_Motion_t = struct_CalibDb_MFNR_Motion_s# /usr/include/rkaiq/iq_parser/RkAiqCalibDbTypesIsp20.h: 1625

# /usr/include/rkaiq/iq_parser/RkAiqCalibDbTypesIsp20.h: 1632
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

CalibDb_MFNR_ModeCell_t = struct_CalibDb_MFNR_ModeCell_s# /usr/include/rkaiq/iq_parser/RkAiqCalibDbTypesIsp20.h: 1632

# /usr/include/rkaiq/iq_parser/RkAiqCalibDbTypesIsp20.h: 1645
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

CalibDb_MFNR_t = struct_CalibDb_MFNR_s# /usr/include/rkaiq/iq_parser/RkAiqCalibDbTypesIsp20.h: 1645

enum_CtrlDataType_e = c_int# /usr/include/rkaiq/iq_parser_v2/adehaze_head.h: 37

CtrlDataType_t = enum_CtrlDataType_e# /usr/include/rkaiq/iq_parser_v2/adehaze_head.h: 37

# /usr/include/rkaiq/iq_parser_v2/adehaze_head.h: 241
class struct_DehazeDataV11_s(Structure):
    pass

struct_DehazeDataV11_s.__slots__ = [
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
struct_DehazeDataV11_s._fields_ = [
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

DehazeDataV11_t = struct_DehazeDataV11_s# /usr/include/rkaiq/iq_parser_v2/adehaze_head.h: 241

# /usr/include/rkaiq/iq_parser_v2/adehaze_head.h: 262
class struct_Dehaze_Setting_V11_s(Structure):
    pass

struct_Dehaze_Setting_V11_s.__slots__ = [
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
struct_Dehaze_Setting_V11_s._fields_ = [
    ('en', c_bool),
    ('air_lc_en', c_bool),
    ('stab_fnum', c_float),
    ('sigma', c_float),
    ('wt_sigma', c_float),
    ('air_sigma', c_float),
    ('tmax_sigma', c_float),
    ('pre_wet', c_float),
    ('DehazeData', DehazeDataV11_t),
]

Dehaze_Setting_V11_t = struct_Dehaze_Setting_V11_s# /usr/include/rkaiq/iq_parser_v2/adehaze_head.h: 262

# /usr/include/rkaiq/iq_parser_v2/adehaze_head.h: 271
class struct_EnhanceDataV11_s(Structure):
    pass

struct_EnhanceDataV11_s.__slots__ = [
    'CtrlData',
    'enhance_value',
    'enhance_chroma',
]
struct_EnhanceDataV11_s._fields_ = [
    ('CtrlData', c_float * int(13)),
    ('enhance_value', c_float * int(13)),
    ('enhance_chroma', c_float * int(13)),
]

EnhanceDataV11_t = struct_EnhanceDataV11_s# /usr/include/rkaiq/iq_parser_v2/adehaze_head.h: 271

# /usr/include/rkaiq/iq_parser_v2/adehaze_head.h: 280
class struct_Enhance_Setting_V11_s(Structure):
    pass

struct_Enhance_Setting_V11_s.__slots__ = [
    'en',
    'enhance_curve',
    'EnhanceData',
]
struct_Enhance_Setting_V11_s._fields_ = [
    ('en', c_bool),
    ('enhance_curve', c_float * int(17)),
    ('EnhanceData', EnhanceDataV11_t),
]

Enhance_Setting_V11_t = struct_Enhance_Setting_V11_s# /usr/include/rkaiq/iq_parser_v2/adehaze_head.h: 280

# /usr/include/rkaiq/iq_parser_v2/adehaze_head.h: 297
class struct_HistDataV11_s(Structure):
    pass

struct_HistDataV11_s.__slots__ = [
    'CtrlData',
    'hist_gratio',
    'hist_th_off',
    'hist_k',
    'hist_min',
    'hist_scale',
    'cfg_gratio',
]
struct_HistDataV11_s._fields_ = [
    ('CtrlData', c_float * int(13)),
    ('hist_gratio', c_float * int(13)),
    ('hist_th_off', c_float * int(13)),
    ('hist_k', c_float * int(13)),
    ('hist_min', c_float * int(13)),
    ('hist_scale', c_float * int(13)),
    ('cfg_gratio', c_float * int(13)),
]

HistDataV11_t = struct_HistDataV11_s# /usr/include/rkaiq/iq_parser_v2/adehaze_head.h: 297

# /usr/include/rkaiq/iq_parser_v2/adehaze_head.h: 306
class struct_Hist_setting_V11_s(Structure):
    pass

struct_Hist_setting_V11_s.__slots__ = [
    'en',
    'hist_para_en',
    'HistData',
]
struct_Hist_setting_V11_s._fields_ = [
    ('en', c_bool),
    ('hist_para_en', c_bool),
    ('HistData', HistDataV11_t),
]

Hist_setting_V11_t = struct_Hist_setting_V11_s# /usr/include/rkaiq/iq_parser_v2/adehaze_head.h: 306

# /usr/include/rkaiq/iq_parser_v2/adehaze_head.h: 323
class struct_CalibDbDehazeV11_s(Structure):
    pass

struct_CalibDbDehazeV11_s.__slots__ = [
    'Enable',
    'CtrlDataType',
    'cfg_alpha',
    'ByPassThr',
    'dehaze_setting',
    'enhance_setting',
    'hist_setting',
]
struct_CalibDbDehazeV11_s._fields_ = [
    ('Enable', c_bool),
    ('CtrlDataType', CtrlDataType_t),
    ('cfg_alpha', c_float),
    ('ByPassThr', c_float),
    ('dehaze_setting', Dehaze_Setting_V11_t),
    ('enhance_setting', Enhance_Setting_V11_t),
    ('hist_setting', Hist_setting_V11_t),
]

CalibDbDehazeV11_t = struct_CalibDbDehazeV11_s# /usr/include/rkaiq/iq_parser_v2/adehaze_head.h: 323

# /usr/include/rkaiq/iq_parser_v2/adehaze_head.h: 328
class struct_CalibDbV2_dehaze_v11_s(Structure):
    pass

struct_CalibDbV2_dehaze_v11_s.__slots__ = [
    'DehazeTuningPara',
]
struct_CalibDbV2_dehaze_v11_s._fields_ = [
    ('DehazeTuningPara', CalibDbDehazeV11_t),
]

CalibDbV2_dehaze_v11_t = struct_CalibDbV2_dehaze_v11_s# /usr/include/rkaiq/iq_parser_v2/adehaze_head.h: 328

# /usr/include/rkaiq/iq_parser_v2/adehaze_head.h: 342
class struct_EnhanceDataV12_s(Structure):
    pass

struct_EnhanceDataV12_s.__slots__ = [
    'CtrlData',
    'enhance_curve',
    'enh_luma',
    'enhance_value',
    'enhance_chroma',
]
struct_EnhanceDataV12_s._fields_ = [
    ('CtrlData', c_float),
    ('enhance_curve', c_float * int(17)),
    ('enh_luma', c_float * int(17)),
    ('enhance_value', c_float),
    ('enhance_chroma', c_float),
]

EnhanceDataV12_t = struct_EnhanceDataV12_s# /usr/include/rkaiq/iq_parser_v2/adehaze_head.h: 342

# /usr/include/rkaiq/iq_parser_v2/adehaze_head.h: 353
class struct_Enhance_Setting_V12_s(Structure):
    pass

struct_Enhance_Setting_V12_s.__slots__ = [
    'en',
    'color_deviate_en',
    'enh_luma_en',
    'EnhanceData',
]
struct_Enhance_Setting_V12_s._fields_ = [
    ('en', c_bool),
    ('color_deviate_en', c_bool),
    ('enh_luma_en', c_bool),
    ('EnhanceData', EnhanceDataV12_t * int(13)),
]

Enhance_Setting_V12_t = struct_Enhance_Setting_V12_s# /usr/include/rkaiq/iq_parser_v2/adehaze_head.h: 353

enum_HistWrMode_e = c_int# /usr/include/rkaiq/iq_parser_v2/adehaze_head.h: 359

HistWrMode_t = enum_HistWrMode_e# /usr/include/rkaiq/iq_parser_v2/adehaze_head.h: 359

# /usr/include/rkaiq/iq_parser_v2/adehaze_head.h: 368
class struct_Manual_curve_s(Structure):
    pass

struct_Manual_curve_s.__slots__ = [
    'CtrlData',
    'curve_x',
    'curve_y',
]
struct_Manual_curve_s._fields_ = [
    ('CtrlData', c_float),
    ('curve_x', c_int * int(17)),
    ('curve_y', c_int * int(17)),
]

Manual_curve_t = struct_Manual_curve_s# /usr/include/rkaiq/iq_parser_v2/adehaze_head.h: 368

# /usr/include/rkaiq/iq_parser_v2/adehaze_head.h: 379
class struct_hist_wr_semiauto_s(Structure):
    pass

struct_hist_wr_semiauto_s.__slots__ = [
    'CtrlData',
    'clim0',
    'clim1',
    'dark_th',
]
struct_hist_wr_semiauto_s._fields_ = [
    ('CtrlData', c_float * int(13)),
    ('clim0', c_float * int(13)),
    ('clim1', c_float * int(13)),
    ('dark_th', c_float * int(13)),
]

hist_wr_semiauto_t = struct_hist_wr_semiauto_s# /usr/include/rkaiq/iq_parser_v2/adehaze_head.h: 379

# /usr/include/rkaiq/iq_parser_v2/adehaze_head.h: 388
class struct_HistWr_s(Structure):
    pass

struct_HistWr_s.__slots__ = [
    'mode',
    'manual_curve',
    'semiauto_curve',
]
struct_HistWr_s._fields_ = [
    ('mode', HistWrMode_t),
    ('manual_curve', Manual_curve_t * int(13)),
    ('semiauto_curve', hist_wr_semiauto_t),
]

HistWr_t = struct_HistWr_s# /usr/include/rkaiq/iq_parser_v2/adehaze_head.h: 388

# /usr/include/rkaiq/iq_parser_v2/adehaze_head.h: 399
class struct_Hist_setting_V12_s(Structure):
    pass

struct_Hist_setting_V12_s.__slots__ = [
    'en',
    'hist_para_en',
    'hist_wr',
    'HistData',
]
struct_Hist_setting_V12_s._fields_ = [
    ('en', c_bool),
    ('hist_para_en', c_bool),
    ('hist_wr', HistWr_t),
    ('HistData', HistDataV11_t),
]

Hist_setting_V12_t = struct_Hist_setting_V12_s# /usr/include/rkaiq/iq_parser_v2/adehaze_head.h: 399

# /usr/include/rkaiq/iq_parser_v2/adehaze_head.h: 416
class struct_CalibDbDehazeV12_s(Structure):
    pass

struct_CalibDbDehazeV12_s.__slots__ = [
    'Enable',
    'CtrlDataType',
    'cfg_alpha',
    'ByPassThr',
    'dehaze_setting',
    'enhance_setting',
    'hist_setting',
]
struct_CalibDbDehazeV12_s._fields_ = [
    ('Enable', c_bool),
    ('CtrlDataType', CtrlDataType_t),
    ('cfg_alpha', c_float),
    ('ByPassThr', c_float),
    ('dehaze_setting', Dehaze_Setting_V11_t),
    ('enhance_setting', Enhance_Setting_V12_t),
    ('hist_setting', Hist_setting_V12_t),
]

CalibDbDehazeV12_t = struct_CalibDbDehazeV12_s# /usr/include/rkaiq/iq_parser_v2/adehaze_head.h: 416

# /usr/include/rkaiq/iq_parser_v2/adehaze_head.h: 421
class struct_CalibDbV2_dehaze_v12_s(Structure):
    pass

struct_CalibDbV2_dehaze_v12_s.__slots__ = [
    'DehazeTuningPara',
]
struct_CalibDbV2_dehaze_v12_s._fields_ = [
    ('DehazeTuningPara', CalibDbDehazeV12_t),
]

CalibDbV2_dehaze_v12_t = struct_CalibDbV2_dehaze_v12_s# /usr/include/rkaiq/iq_parser_v2/adehaze_head.h: 421

# /usr/include/rkaiq/iq_parser_v2/amerge_head.h: 38
class struct_MergeOECurveV10_s(Structure):
    pass

struct_MergeOECurveV10_s.__slots__ = [
    'CtrlData',
    'Smooth',
    'Offset',
]
struct_MergeOECurveV10_s._fields_ = [
    ('CtrlData', c_float * int(13)),
    ('Smooth', c_float * int(13)),
    ('Offset', c_float * int(13)),
]

MergeOECurveV10_t = struct_MergeOECurveV10_s# /usr/include/rkaiq/iq_parser_v2/amerge_head.h: 38

# /usr/include/rkaiq/iq_parser_v2/amerge_head.h: 51
class struct_MergeMDCurveV10_s(Structure):
    pass

struct_MergeMDCurveV10_s.__slots__ = [
    'MoveCoef',
    'LM_smooth',
    'LM_offset',
    'MS_smooth',
    'MS_offset',
]
struct_MergeMDCurveV10_s._fields_ = [
    ('MoveCoef', c_float * int(13)),
    ('LM_smooth', c_float * int(13)),
    ('LM_offset', c_float * int(13)),
    ('MS_smooth', c_float * int(13)),
    ('MS_offset', c_float * int(13)),
]

MergeMDCurveV10_t = struct_MergeMDCurveV10_s# /usr/include/rkaiq/iq_parser_v2/amerge_head.h: 51

# /usr/include/rkaiq/iq_parser_v2/amerge_head.h: 68
class struct_MergeV10_s(Structure):
    pass

struct_MergeV10_s.__slots__ = [
    'CtrlDataType',
    'OECurve',
    'MDCurve',
    'ByPassThr',
    'OECurve_damp',
    'MDCurveLM_damp',
    'MDCurveMS_damp',
]
struct_MergeV10_s._fields_ = [
    ('CtrlDataType', CtrlDataType_t),
    ('OECurve', MergeOECurveV10_t),
    ('MDCurve', MergeMDCurveV10_t),
    ('ByPassThr', c_float),
    ('OECurve_damp', c_float),
    ('MDCurveLM_damp', c_float),
    ('MDCurveMS_damp', c_float),
]

MergeV10_t = struct_MergeV10_s# /usr/include/rkaiq/iq_parser_v2/amerge_head.h: 68

# /usr/include/rkaiq/iq_parser_v2/amerge_head.h: 73
class struct_CalibDbV2_merge_v10_s(Structure):
    pass

struct_CalibDbV2_merge_v10_s.__slots__ = [
    'MergeTuningPara',
]
struct_CalibDbV2_merge_v10_s._fields_ = [
    ('MergeTuningPara', MergeV10_t),
]

CalibDbV2_merge_v10_t = struct_CalibDbV2_merge_v10_s# /usr/include/rkaiq/iq_parser_v2/amerge_head.h: 73

enum_MergeBaseFrame_e = c_int# /usr/include/rkaiq/iq_parser_v2/amerge_head.h: 79

MergeBaseFrame_t = enum_MergeBaseFrame_e# /usr/include/rkaiq/iq_parser_v2/amerge_head.h: 79

# /usr/include/rkaiq/iq_parser_v2/amerge_head.h: 92
class struct_LongFrameModeData_s(Structure):
    pass

struct_LongFrameModeData_s.__slots__ = [
    'OECurve',
    'MDCurve',
    'OECurve_damp',
    'MDCurveLM_damp',
    'MDCurveMS_damp',
]
struct_LongFrameModeData_s._fields_ = [
    ('OECurve', MergeOECurveV10_t),
    ('MDCurve', MergeMDCurveV10_t),
    ('OECurve_damp', c_float),
    ('MDCurveLM_damp', c_float),
    ('MDCurveMS_damp', c_float),
]

LongFrameModeData_t = struct_LongFrameModeData_s# /usr/include/rkaiq/iq_parser_v2/amerge_head.h: 92

# /usr/include/rkaiq/iq_parser_v2/amerge_head.h: 103
class struct_MergeMDCurveV11Short_s(Structure):
    pass

struct_MergeMDCurveV11Short_s.__slots__ = [
    'MoveCoef',
    'Coef',
    'ms_thd0',
    'lm_thd0',
]
struct_MergeMDCurveV11Short_s._fields_ = [
    ('MoveCoef', c_float * int(13)),
    ('Coef', c_float * int(13)),
    ('ms_thd0', c_float * int(13)),
    ('lm_thd0', c_float * int(13)),
]

MergeMDCurveV11Short_t = struct_MergeMDCurveV11Short_s# /usr/include/rkaiq/iq_parser_v2/amerge_head.h: 103

# /usr/include/rkaiq/iq_parser_v2/amerge_head.h: 114
class struct_ShortFrameModeData_s(Structure):
    pass

struct_ShortFrameModeData_s.__slots__ = [
    'OECurve',
    'MDCurve',
    'OECurve_damp',
    'MDCurve_damp',
]
struct_ShortFrameModeData_s._fields_ = [
    ('OECurve', MergeOECurveV10_t),
    ('MDCurve', MergeMDCurveV11Short_t),
    ('OECurve_damp', c_float),
    ('MDCurve_damp', c_float),
]

ShortFrameModeData_t = struct_ShortFrameModeData_s# /usr/include/rkaiq/iq_parser_v2/amerge_head.h: 114

# /usr/include/rkaiq/iq_parser_v2/amerge_head.h: 127
class struct_MergeV11_s(Structure):
    pass

struct_MergeV11_s.__slots__ = [
    'BaseFrm',
    'CtrlDataType',
    'ByPassThr',
    'LongFrmModeData',
    'ShortFrmModeData',
]
struct_MergeV11_s._fields_ = [
    ('BaseFrm', MergeBaseFrame_t),
    ('CtrlDataType', CtrlDataType_t),
    ('ByPassThr', c_float),
    ('LongFrmModeData', LongFrameModeData_t),
    ('ShortFrmModeData', ShortFrameModeData_t),
]

MergeV11_t = struct_MergeV11_s# /usr/include/rkaiq/iq_parser_v2/amerge_head.h: 127

# /usr/include/rkaiq/iq_parser_v2/amerge_head.h: 132
class struct_CalibDbV2_merge_v11_s(Structure):
    pass

struct_CalibDbV2_merge_v11_s.__slots__ = [
    'MergeTuningPara',
]
struct_CalibDbV2_merge_v11_s._fields_ = [
    ('MergeTuningPara', MergeV11_t),
]

CalibDbV2_merge_v11_t = struct_CalibDbV2_merge_v11_s# /usr/include/rkaiq/iq_parser_v2/amerge_head.h: 132

# /usr/include/rkaiq/iq_parser_v2/amerge_head.h: 142
class struct_MergeEachChnCurveV12_s(Structure):
    pass

struct_MergeEachChnCurveV12_s.__slots__ = [
    'CtrlData',
    'Smooth',
    'Offset',
]
struct_MergeEachChnCurveV12_s._fields_ = [
    ('CtrlData', c_float * int(13)),
    ('Smooth', c_float * int(13)),
    ('Offset', c_float * int(13)),
]

MergeEachChnCurveV12_t = struct_MergeEachChnCurveV12_s# /usr/include/rkaiq/iq_parser_v2/amerge_head.h: 142

# /usr/include/rkaiq/iq_parser_v2/amerge_head.h: 159
class struct_LongFrameModeDataV12_s(Structure):
    pass

struct_LongFrameModeDataV12_s.__slots__ = [
    'EnableEachChn',
    'OECurve',
    'MDCurve',
    'EachChnCurve',
    'OECurve_damp',
    'MDCurveLM_damp',
    'MDCurveMS_damp',
]
struct_LongFrameModeDataV12_s._fields_ = [
    ('EnableEachChn', c_bool),
    ('OECurve', MergeOECurveV10_t),
    ('MDCurve', MergeMDCurveV10_t),
    ('EachChnCurve', MergeEachChnCurveV12_t),
    ('OECurve_damp', c_float),
    ('MDCurveLM_damp', c_float),
    ('MDCurveMS_damp', c_float),
]

LongFrameModeDataV12_t = struct_LongFrameModeDataV12_s# /usr/include/rkaiq/iq_parser_v2/amerge_head.h: 159

# /usr/include/rkaiq/iq_parser_v2/amerge_head.h: 172
class struct_MergeV12_s(Structure):
    pass

struct_MergeV12_s.__slots__ = [
    'BaseFrm',
    'CtrlDataType',
    'ByPassThr',
    'LongFrmModeData',
    'ShortFrmModeData',
]
struct_MergeV12_s._fields_ = [
    ('BaseFrm', MergeBaseFrame_t),
    ('CtrlDataType', CtrlDataType_t),
    ('ByPassThr', c_float),
    ('LongFrmModeData', LongFrameModeDataV12_t),
    ('ShortFrmModeData', ShortFrameModeData_t),
]

MergeV12_t = struct_MergeV12_s# /usr/include/rkaiq/iq_parser_v2/amerge_head.h: 172

# /usr/include/rkaiq/iq_parser_v2/amerge_head.h: 177
class struct_CalibDbV2_merge_v12_s(Structure):
    pass

struct_CalibDbV2_merge_v12_s.__slots__ = [
    'MergeTuningPara',
]
struct_CalibDbV2_merge_v12_s._fields_ = [
    ('MergeTuningPara', MergeV12_t),
]

CalibDbV2_merge_v12_t = struct_CalibDbV2_merge_v12_s# /usr/include/rkaiq/iq_parser_v2/amerge_head.h: 177

# /usr/include/rkaiq/iq_parser_v2/amerge_uapi_head.h: 34
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

uapiMergeCurrCtlData_t = struct_uapiMergeCurrCtlData_s# /usr/include/rkaiq/iq_parser_v2/amerge_uapi_head.h: 34

# /usr/include/rkaiq/iq_parser_v2/amerge_uapi_head.h: 41
class struct_mMergeOECurveV10_s(Structure):
    pass

struct_mMergeOECurveV10_s.__slots__ = [
    'Smooth',
    'Offset',
]
struct_mMergeOECurveV10_s._fields_ = [
    ('Smooth', c_float),
    ('Offset', c_float),
]

mMergeOECurveV10_t = struct_mMergeOECurveV10_s# /usr/include/rkaiq/iq_parser_v2/amerge_uapi_head.h: 41

# /usr/include/rkaiq/iq_parser_v2/amerge_uapi_head.h: 52
class struct_mMergeMDCurveV10_s(Structure):
    pass

struct_mMergeMDCurveV10_s.__slots__ = [
    'LM_smooth',
    'LM_offset',
    'MS_smooth',
    'MS_offset',
]
struct_mMergeMDCurveV10_s._fields_ = [
    ('LM_smooth', c_float),
    ('LM_offset', c_float),
    ('MS_smooth', c_float),
    ('MS_offset', c_float),
]

mMergeMDCurveV10_t = struct_mMergeMDCurveV10_s# /usr/include/rkaiq/iq_parser_v2/amerge_uapi_head.h: 52

# /usr/include/rkaiq/iq_parser_v2/amerge_uapi_head.h: 59
class struct_mMergeAttrV10_s(Structure):
    pass

struct_mMergeAttrV10_s.__slots__ = [
    'OECurve',
    'MDCurve',
]
struct_mMergeAttrV10_s._fields_ = [
    ('OECurve', mMergeOECurveV10_t),
    ('MDCurve', mMergeMDCurveV10_t),
]

mMergeAttrV10_t = struct_mMergeAttrV10_s# /usr/include/rkaiq/iq_parser_v2/amerge_uapi_head.h: 59

# /usr/include/rkaiq/iq_parser_v2/amerge_uapi_head.h: 66
class struct_mLongFrameModeData_s(Structure):
    pass

struct_mLongFrameModeData_s.__slots__ = [
    'OECurve',
    'MDCurve',
]
struct_mLongFrameModeData_s._fields_ = [
    ('OECurve', mMergeOECurveV10_t),
    ('MDCurve', mMergeMDCurveV10_t),
]

mLongFrameModeData_t = struct_mLongFrameModeData_s# /usr/include/rkaiq/iq_parser_v2/amerge_uapi_head.h: 66

# /usr/include/rkaiq/iq_parser_v2/amerge_uapi_head.h: 75
class struct_mMergeMDCurveV11Short_s(Structure):
    pass

struct_mMergeMDCurveV11Short_s.__slots__ = [
    'Coef',
    'ms_thd0',
    'lm_thd0',
]
struct_mMergeMDCurveV11Short_s._fields_ = [
    ('Coef', c_float),
    ('ms_thd0', c_float),
    ('lm_thd0', c_float),
]

mMergeMDCurveV11Short_t = struct_mMergeMDCurveV11Short_s# /usr/include/rkaiq/iq_parser_v2/amerge_uapi_head.h: 75

# /usr/include/rkaiq/iq_parser_v2/amerge_uapi_head.h: 82
class struct_mShortFrameModeData_s(Structure):
    pass

struct_mShortFrameModeData_s.__slots__ = [
    'OECurve',
    'MDCurve',
]
struct_mShortFrameModeData_s._fields_ = [
    ('OECurve', mMergeOECurveV10_t),
    ('MDCurve', mMergeMDCurveV11Short_t),
]

mShortFrameModeData_t = struct_mShortFrameModeData_s# /usr/include/rkaiq/iq_parser_v2/amerge_uapi_head.h: 82

# /usr/include/rkaiq/iq_parser_v2/amerge_uapi_head.h: 91
class struct_mMergeAttrV11_s(Structure):
    pass

struct_mMergeAttrV11_s.__slots__ = [
    'BaseFrm',
    'LongFrmModeData',
    'ShortFrmModeData',
]
struct_mMergeAttrV11_s._fields_ = [
    ('BaseFrm', MergeBaseFrame_t),
    ('LongFrmModeData', mLongFrameModeData_t),
    ('ShortFrmModeData', mShortFrameModeData_t),
]

mMergeAttrV11_t = struct_mMergeAttrV11_s# /usr/include/rkaiq/iq_parser_v2/amerge_uapi_head.h: 91

# /usr/include/rkaiq/iq_parser_v2/amerge_uapi_head.h: 98
class struct_mMergeEachChnCurveV12_s(Structure):
    pass

struct_mMergeEachChnCurveV12_s.__slots__ = [
    'Smooth',
    'Offset',
]
struct_mMergeEachChnCurveV12_s._fields_ = [
    ('Smooth', c_float),
    ('Offset', c_float),
]

mMergeEachChnCurveV12_t = struct_mMergeEachChnCurveV12_s# /usr/include/rkaiq/iq_parser_v2/amerge_uapi_head.h: 98

# /usr/include/rkaiq/iq_parser_v2/amerge_uapi_head.h: 109
class struct_mLongFrameModeDataV12_s(Structure):
    pass

struct_mLongFrameModeDataV12_s.__slots__ = [
    'EnableEachChn',
    'OECurve',
    'MDCurve',
    'EachChnCurve',
]
struct_mLongFrameModeDataV12_s._fields_ = [
    ('EnableEachChn', c_bool),
    ('OECurve', mMergeOECurveV10_t),
    ('MDCurve', mMergeMDCurveV10_t),
    ('EachChnCurve', mMergeEachChnCurveV12_t),
]

mLongFrameModeDataV12_t = struct_mLongFrameModeDataV12_s# /usr/include/rkaiq/iq_parser_v2/amerge_uapi_head.h: 109

# /usr/include/rkaiq/iq_parser_v2/amerge_uapi_head.h: 118
class struct_mMergeAttrV12_s(Structure):
    pass

struct_mMergeAttrV12_s.__slots__ = [
    'BaseFrm',
    'LongFrmModeData',
    'ShortFrmModeData',
]
struct_mMergeAttrV12_s._fields_ = [
    ('BaseFrm', MergeBaseFrame_t),
    ('LongFrmModeData', mLongFrameModeDataV12_t),
    ('ShortFrmModeData', mShortFrameModeData_t),
]

mMergeAttrV12_t = struct_mMergeAttrV12_s# /usr/include/rkaiq/iq_parser_v2/amerge_uapi_head.h: 118

enum_merge_OpMode_e = c_int# /usr/include/rkaiq/algos/amerge/rk_aiq_types_amerge_algo_int.h: 21

merge_OpMode_t = enum_merge_OpMode_e# /usr/include/rkaiq/algos/amerge/rk_aiq_types_amerge_algo_int.h: 21

MergeCurrCtlData_t = uapiMergeCurrCtlData_t# /usr/include/rkaiq/algos/amerge/rk_aiq_types_amerge_algo_int.h: 23

# /usr/include/rkaiq/algos/amerge/rk_aiq_types_amerge_algo_int.h: 33
class struct_mergeAttrV10_s(Structure):
    pass

struct_mergeAttrV10_s.__slots__ = [
    'sync',
    'opMode',
    'stManual',
    'stAuto',
    'Info',
]
struct_mergeAttrV10_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('opMode', merge_OpMode_t),
    ('stManual', mMergeAttrV10_t),
    ('stAuto', CalibDbV2_merge_v10_t),
    ('Info', MergeCurrCtlData_t),
]

mergeAttrV10_t = struct_mergeAttrV10_s# /usr/include/rkaiq/algos/amerge/rk_aiq_types_amerge_algo_int.h: 33

# /usr/include/rkaiq/algos/amerge/rk_aiq_types_amerge_algo_int.h: 43
class struct_mergeAttrV11_s(Structure):
    pass

struct_mergeAttrV11_s.__slots__ = [
    'sync',
    'opMode',
    'stManual',
    'stAuto',
    'Info',
]
struct_mergeAttrV11_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('opMode', merge_OpMode_t),
    ('stManual', mMergeAttrV11_t),
    ('stAuto', CalibDbV2_merge_v11_t),
    ('Info', MergeCurrCtlData_t),
]

mergeAttrV11_t = struct_mergeAttrV11_s# /usr/include/rkaiq/algos/amerge/rk_aiq_types_amerge_algo_int.h: 43

# /usr/include/rkaiq/algos/amerge/rk_aiq_types_amerge_algo_int.h: 53
class struct_mergeAttrV12_s(Structure):
    pass

struct_mergeAttrV12_s.__slots__ = [
    'sync',
    'opMode',
    'stManual',
    'stAuto',
    'Info',
]
struct_mergeAttrV12_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('opMode', merge_OpMode_t),
    ('stManual', mMergeAttrV12_t),
    ('stAuto', CalibDbV2_merge_v12_t),
    ('Info', MergeCurrCtlData_t),
]

mergeAttrV12_t = struct_mergeAttrV12_s# /usr/include/rkaiq/algos/amerge/rk_aiq_types_amerge_algo_int.h: 53

enum_GlobalLumaMode_e = c_int# /usr/include/rkaiq/iq_parser_v2/atmo_head.h: 30

GlobalLumaMode_t = enum_GlobalLumaMode_e# /usr/include/rkaiq/iq_parser_v2/atmo_head.h: 30

# /usr/include/rkaiq/iq_parser_v2/atmo_head.h: 43
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

GlobalLumaData_t = struct_GlobalLumaData_s# /usr/include/rkaiq/iq_parser_v2/atmo_head.h: 43

# /usr/include/rkaiq/iq_parser_v2/atmo_head.h: 53
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

CalibDbGlobalLuma_t = struct_CalibDbGlobalLuma_s# /usr/include/rkaiq/iq_parser_v2/atmo_head.h: 53

enum_DetailsHighLightMode_e = c_int# /usr/include/rkaiq/iq_parser_v2/atmo_head.h: 58

DetailsHighLightMode_t = enum_DetailsHighLightMode_e# /usr/include/rkaiq/iq_parser_v2/atmo_head.h: 58

# /usr/include/rkaiq/iq_parser_v2/atmo_head.h: 71
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

HighLightData_t = struct_HighLightData_s# /usr/include/rkaiq/iq_parser_v2/atmo_head.h: 71

# /usr/include/rkaiq/iq_parser_v2/atmo_head.h: 81
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

CalibDbDetailsHighLight_t = struct_CalibDbDetailsHighLight_s# /usr/include/rkaiq/iq_parser_v2/atmo_head.h: 81

enum_DetailsLowLightMode_e = c_int# /usr/include/rkaiq/iq_parser_v2/atmo_head.h: 87

DetailsLowLightMode_t = enum_DetailsLowLightMode_e# /usr/include/rkaiq/iq_parser_v2/atmo_head.h: 87

# /usr/include/rkaiq/iq_parser_v2/atmo_head.h: 103
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

LowLightData_t = struct_LowLightData_s# /usr/include/rkaiq/iq_parser_v2/atmo_head.h: 103

# /usr/include/rkaiq/iq_parser_v2/atmo_head.h: 113
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

CalibDbDetailsLowLight_t = struct_CalibDbDetailsLowLight_s# /usr/include/rkaiq/iq_parser_v2/atmo_head.h: 113

enum_TmoTypeMode_e = c_int# /usr/include/rkaiq/iq_parser_v2/atmo_head.h: 118

TmoTypeMode_t = enum_TmoTypeMode_e# /usr/include/rkaiq/iq_parser_v2/atmo_head.h: 118

# /usr/include/rkaiq/iq_parser_v2/atmo_head.h: 131
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

TmoData_t = struct_TmoData_s# /usr/include/rkaiq/iq_parser_v2/atmo_head.h: 131

# /usr/include/rkaiq/iq_parser_v2/atmo_head.h: 141
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

CalibDbLocalTMO_t = struct_CalibDbLocalTMO_s# /usr/include/rkaiq/iq_parser_v2/atmo_head.h: 141

# /usr/include/rkaiq/iq_parser_v2/atmo_head.h: 155
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

CalibDbGlobaTMO_t = struct_CalibDbGlobaTMO_s# /usr/include/rkaiq/iq_parser_v2/atmo_head.h: 155

# /usr/include/rkaiq/iq_parser_v2/atmo_head.h: 173
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

CalibDbTmoV20_t = struct_CalibDbTmoV20_s# /usr/include/rkaiq/iq_parser_v2/atmo_head.h: 173

# /usr/include/rkaiq/iq_parser_v2/atmo_head.h: 179
class struct_CalibDbV2_tmo_s(Structure):
    pass

struct_CalibDbV2_tmo_s.__slots__ = [
    'TmoTuningPara',
]
struct_CalibDbV2_tmo_s._fields_ = [
    ('TmoTuningPara', CalibDbTmoV20_t),
]

CalibDbV2_tmo_t = struct_CalibDbV2_tmo_s# /usr/include/rkaiq/iq_parser_v2/atmo_head.h: 179

# /usr/include/rkaiq/algos/atmo/rk_aiq_types_atmo_algo_int.h: 90
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

tmoCtrlData_t = struct_tmoCtrlData_s# /usr/include/rkaiq/algos/atmo/rk_aiq_types_atmo_algo_int.h: 90

# /usr/include/rkaiq/algos/atmo/rk_aiq_types_atmo_algo_int.h: 100
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

AGlobalTmoData_t = struct_AGlobalTmoData_s# /usr/include/rkaiq/algos/atmo/rk_aiq_types_atmo_algo_int.h: 100

# /usr/include/rkaiq/algos/atmo/rk_aiq_types_atmo_algo_int.h: 109
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

atmoAttr_t = struct_atmoAttr_s# /usr/include/rkaiq/algos/atmo/rk_aiq_types_atmo_algo_int.h: 109

# /usr/include/rkaiq/algos/atmo/rk_aiq_types_atmo_algo_int.h: 120
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

mtmoAttr_t = struct_mtmoAttr_s# /usr/include/rkaiq/algos/atmo/rk_aiq_types_atmo_algo_int.h: 120

# /usr/include/rkaiq/algos/atmo/rk_aiq_types_atmo_algo_int.h: 126
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

atmoAttr_V2_t = struct_atmoAttr_V2_s# /usr/include/rkaiq/algos/atmo/rk_aiq_types_atmo_algo_int.h: 126

# /usr/include/rkaiq/algos/atmo/rk_aiq_types_atmo_algo_int.h: 132
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

mtmoAttr_V2_t = struct_mtmoAttr_V2_s# /usr/include/rkaiq/algos/atmo/rk_aiq_types_atmo_algo_int.h: 132

enum_tmo_OpMode_s = c_int# /usr/include/rkaiq/algos/atmo/rk_aiq_types_atmo_algo_int.h: 141

tmo_OpMode_t = enum_tmo_OpMode_s# /usr/include/rkaiq/algos/atmo/rk_aiq_types_atmo_algo_int.h: 141

# /usr/include/rkaiq/algos/atmo/rk_aiq_types_atmo_algo_int.h: 156
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

TmoCurrCtlData_t = struct_TmoCurrCtlData_s# /usr/include/rkaiq/algos/atmo/rk_aiq_types_atmo_algo_int.h: 156

# /usr/include/rkaiq/algos/atmo/rk_aiq_types_atmo_algo_int.h: 165
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

TmoCurrRegData_t = struct_TmoCurrRegData_s# /usr/include/rkaiq/algos/atmo/rk_aiq_types_atmo_algo_int.h: 165

# /usr/include/rkaiq/algos/atmo/rk_aiq_types_atmo_algo_int.h: 170
class struct_DarkArea_s(Structure):
    pass

struct_DarkArea_s.__slots__ = [
    'level',
]
struct_DarkArea_s._fields_ = [
    ('level', c_int),
]

DarkArea_t = struct_DarkArea_s# /usr/include/rkaiq/algos/atmo/rk_aiq_types_atmo_algo_int.h: 170

# /usr/include/rkaiq/algos/atmo/rk_aiq_types_atmo_algo_int.h: 175
class struct_FastMode_s(Structure):
    pass

struct_FastMode_s.__slots__ = [
    'level',
]
struct_FastMode_s._fields_ = [
    ('level', c_int),
]

FastMode_t = struct_FastMode_s# /usr/include/rkaiq/algos/atmo/rk_aiq_types_atmo_algo_int.h: 175

# /usr/include/rkaiq/algos/atmo/rk_aiq_types_atmo_algo_int.h: 187
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

tmoAttr_t = struct_tmoAttr_s# /usr/include/rkaiq/algos/atmo/rk_aiq_types_atmo_algo_int.h: 187

# /usr/include/rkaiq/iq_parser_v2/adrc_head.h: 38
class struct_AdrcGain_s(Structure):
    pass

struct_AdrcGain_s.__slots__ = [
    'CtrlData',
    'DrcGain',
    'Alpha',
    'Clip',
]
struct_AdrcGain_s._fields_ = [
    ('CtrlData', c_float * int(13)),
    ('DrcGain', c_float * int(13)),
    ('Alpha', c_float * int(13)),
    ('Clip', c_float * int(13)),
]

AdrcGain_t = struct_AdrcGain_s# /usr/include/rkaiq/iq_parser_v2/adrc_head.h: 38

# /usr/include/rkaiq/iq_parser_v2/adrc_head.h: 45
class struct_HighLight_s(Structure):
    pass

struct_HighLight_s.__slots__ = [
    'CtrlData',
    'Strength',
]
struct_HighLight_s._fields_ = [
    ('CtrlData', c_float * int(13)),
    ('Strength', c_float * int(13)),
]

HighLight_t = struct_HighLight_s# /usr/include/rkaiq/iq_parser_v2/adrc_head.h: 45

# /usr/include/rkaiq/iq_parser_v2/adrc_head.h: 56
class struct_LocalData_s(Structure):
    pass

struct_LocalData_s.__slots__ = [
    'CtrlData',
    'LocalWeit',
    'GlobalContrast',
    'LoLitContrast',
]
struct_LocalData_s._fields_ = [
    ('CtrlData', c_float * int(13)),
    ('LocalWeit', c_float * int(13)),
    ('GlobalContrast', c_float * int(13)),
    ('LoLitContrast', c_float * int(13)),
]

LocalData_t = struct_LocalData_s# /usr/include/rkaiq/iq_parser_v2/adrc_head.h: 56

# /usr/include/rkaiq/iq_parser_v2/adrc_head.h: 75
class struct_local_s(Structure):
    pass

struct_local_s.__slots__ = [
    'LocalTMOData',
    'curPixWeit',
    'preFrameWeit',
    'Range_force_sgm',
    'Range_sgm_cur',
    'Range_sgm_pre',
    'Space_sgm_cur',
    'Space_sgm_pre',
]
struct_local_s._fields_ = [
    ('LocalTMOData', LocalData_t),
    ('curPixWeit', c_float),
    ('preFrameWeit', c_float),
    ('Range_force_sgm', c_float),
    ('Range_sgm_cur', c_float),
    ('Range_sgm_pre', c_float),
    ('Space_sgm_cur', c_int),
    ('Space_sgm_pre', c_int),
]

local_t = struct_local_s# /usr/include/rkaiq/iq_parser_v2/adrc_head.h: 75

enum_CompressMode_e = c_int# /usr/include/rkaiq/iq_parser_v2/adrc_head.h: 80

CompressMode_t = enum_CompressMode_e# /usr/include/rkaiq/iq_parser_v2/adrc_head.h: 80

# /usr/include/rkaiq/iq_parser_v2/adrc_head.h: 87
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

Compress_t = struct_Compress_s# /usr/include/rkaiq/iq_parser_v2/adrc_head.h: 87

# /usr/include/rkaiq/iq_parser_v2/adrc_head.h: 114
class struct_CalibDbV2_Adrc_V10_s(Structure):
    pass

struct_CalibDbV2_Adrc_V10_s.__slots__ = [
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
    'damp',
]
struct_CalibDbV2_Adrc_V10_s._fields_ = [
    ('Enable', c_bool),
    ('CtrlDataType', CtrlDataType_t),
    ('DrcGain', AdrcGain_t),
    ('HiLight', HighLight_t),
    ('LocalTMOSetting', local_t),
    ('CompressSetting', Compress_t),
    ('Scale_y', c_int * int(17)),
    ('ByPassThr', c_float),
    ('Edge_Weit', c_float),
    ('OutPutLongFrame', c_bool),
    ('IIR_frame', c_int),
    ('damp', c_float),
]

CalibDbV2_Adrc_V10_t = struct_CalibDbV2_Adrc_V10_s# /usr/include/rkaiq/iq_parser_v2/adrc_head.h: 114

# /usr/include/rkaiq/iq_parser_v2/adrc_head.h: 119
class struct_CalibDbV2_drc_V10_s(Structure):
    pass

struct_CalibDbV2_drc_V10_s.__slots__ = [
    'DrcTuningPara',
]
struct_CalibDbV2_drc_V10_s._fields_ = [
    ('DrcTuningPara', CalibDbV2_Adrc_V10_t),
]

CalibDbV2_drc_V10_t = struct_CalibDbV2_drc_V10_s# /usr/include/rkaiq/iq_parser_v2/adrc_head.h: 119

# /usr/include/rkaiq/iq_parser_v2/adrc_head.h: 135
class struct_LocalDataV2_s(Structure):
    pass

struct_LocalDataV2_s.__slots__ = [
    'CtrlData',
    'LocalWeit',
    'LocalAutoEnable',
    'LocalAutoWeit',
    'GlobalContrast',
    'LoLitContrast',
]
struct_LocalDataV2_s._fields_ = [
    ('CtrlData', c_float * int(13)),
    ('LocalWeit', c_float * int(13)),
    ('LocalAutoEnable', c_int * int(13)),
    ('LocalAutoWeit', c_float * int(13)),
    ('GlobalContrast', c_float * int(13)),
    ('LoLitContrast', c_float * int(13)),
]

LocalDataV2_t = struct_LocalDataV2_s# /usr/include/rkaiq/iq_parser_v2/adrc_head.h: 135

# /usr/include/rkaiq/iq_parser_v2/adrc_head.h: 154
class struct_localV11_s(Structure):
    pass

struct_localV11_s.__slots__ = [
    'LocalData',
    'curPixWeit',
    'preFrameWeit',
    'Range_force_sgm',
    'Range_sgm_cur',
    'Range_sgm_pre',
    'Space_sgm_cur',
    'Space_sgm_pre',
]
struct_localV11_s._fields_ = [
    ('LocalData', LocalDataV2_t),
    ('curPixWeit', c_float),
    ('preFrameWeit', c_float),
    ('Range_force_sgm', c_float),
    ('Range_sgm_cur', c_float),
    ('Range_sgm_pre', c_float),
    ('Space_sgm_cur', c_int),
    ('Space_sgm_pre', c_int),
]

localV11_t = struct_localV11_s# /usr/include/rkaiq/iq_parser_v2/adrc_head.h: 154

# /usr/include/rkaiq/iq_parser_v2/adrc_head.h: 181
class struct_CalibDbV2_Adrc_V11_s(Structure):
    pass

struct_CalibDbV2_Adrc_V11_s.__slots__ = [
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
    'damp',
]
struct_CalibDbV2_Adrc_V11_s._fields_ = [
    ('Enable', c_bool),
    ('CtrlDataType', CtrlDataType_t),
    ('DrcGain', AdrcGain_t),
    ('HiLight', HighLight_t),
    ('LocalSetting', localV11_t),
    ('CompressSetting', Compress_t),
    ('Scale_y', c_int * int(17)),
    ('ByPassThr', c_float),
    ('Edge_Weit', c_float),
    ('OutPutLongFrame', c_bool),
    ('IIR_frame', c_int),
    ('damp', c_float),
]

CalibDbV2_Adrc_V11_t = struct_CalibDbV2_Adrc_V11_s# /usr/include/rkaiq/iq_parser_v2/adrc_head.h: 181

# /usr/include/rkaiq/iq_parser_v2/adrc_head.h: 186
class struct_CalibDbV2_drc_V11_s(Structure):
    pass

struct_CalibDbV2_drc_V11_s.__slots__ = [
    'DrcTuningPara',
]
struct_CalibDbV2_drc_V11_s._fields_ = [
    ('DrcTuningPara', CalibDbV2_Adrc_V11_t),
]

CalibDbV2_drc_V11_t = struct_CalibDbV2_drc_V11_s# /usr/include/rkaiq/iq_parser_v2/adrc_head.h: 186

# /usr/include/rkaiq/iq_parser_v2/adrc_head.h: 194
class struct_MotionData_s(Structure):
    pass

struct_MotionData_s.__slots__ = [
    'MotionCoef',
    'MotionStr',
]
struct_MotionData_s._fields_ = [
    ('MotionCoef', c_float * int(13)),
    ('MotionStr', c_float * int(13)),
]

MotionData_t = struct_MotionData_s# /usr/include/rkaiq/iq_parser_v2/adrc_head.h: 194

# /usr/include/rkaiq/iq_parser_v2/adrc_head.h: 215
class struct_localV12_s(Structure):
    pass

struct_localV12_s.__slots__ = [
    'LocalData',
    'MotionData',
    'curPixWeit',
    'preFrameWeit',
    'Range_force_sgm',
    'Range_sgm_cur',
    'Range_sgm_pre',
    'Space_sgm_cur',
    'Space_sgm_pre',
]
struct_localV12_s._fields_ = [
    ('LocalData', LocalDataV2_t),
    ('MotionData', MotionData_t),
    ('curPixWeit', c_float),
    ('preFrameWeit', c_float),
    ('Range_force_sgm', c_float),
    ('Range_sgm_cur', c_float),
    ('Range_sgm_pre', c_float),
    ('Space_sgm_cur', c_int),
    ('Space_sgm_pre', c_int),
]

localV12_t = struct_localV12_s# /usr/include/rkaiq/iq_parser_v2/adrc_head.h: 215

# /usr/include/rkaiq/iq_parser_v2/adrc_head.h: 224
class struct_HighLightDataV12_s(Structure):
    pass

struct_HighLightDataV12_s.__slots__ = [
    'CtrlData',
    'Strength',
    'gas_t',
]
struct_HighLightDataV12_s._fields_ = [
    ('CtrlData', c_float * int(13)),
    ('Strength', c_float * int(13)),
    ('gas_t', c_float * int(13)),
]

HighLightDataV12_t = struct_HighLightDataV12_s# /usr/include/rkaiq/iq_parser_v2/adrc_head.h: 224

# /usr/include/rkaiq/iq_parser_v2/adrc_head.h: 237
class struct_HighLightV12_s(Structure):
    pass

struct_HighLightV12_s.__slots__ = [
    'HiLightData',
    'gas_l0',
    'gas_l1',
    'gas_l2',
    'gas_l3',
]
struct_HighLightV12_s._fields_ = [
    ('HiLightData', HighLightDataV12_t),
    ('gas_l0', c_int),
    ('gas_l1', c_int),
    ('gas_l2', c_int),
    ('gas_l3', c_int),
]

HighLightV12_t = struct_HighLightV12_s# /usr/include/rkaiq/iq_parser_v2/adrc_head.h: 237

# /usr/include/rkaiq/iq_parser_v2/adrc_head.h: 264
class struct_CalibDbV2_Adrc_V12_s(Structure):
    pass

struct_CalibDbV2_Adrc_V12_s.__slots__ = [
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
    'damp',
]
struct_CalibDbV2_Adrc_V12_s._fields_ = [
    ('Enable', c_bool),
    ('CtrlDataType', CtrlDataType_t),
    ('DrcGain', AdrcGain_t),
    ('HiLight', HighLightV12_t),
    ('LocalSetting', localV12_t),
    ('CompressSetting', Compress_t),
    ('Scale_y', c_int * int(17)),
    ('ByPassThr', c_float),
    ('Edge_Weit', c_float),
    ('OutPutLongFrame', c_bool),
    ('IIR_frame', c_int),
    ('damp', c_float),
]

CalibDbV2_Adrc_V12_t = struct_CalibDbV2_Adrc_V12_s# /usr/include/rkaiq/iq_parser_v2/adrc_head.h: 264

# /usr/include/rkaiq/iq_parser_v2/adrc_head.h: 269
class struct_CalibDbV2_drc_V12_s(Structure):
    pass

struct_CalibDbV2_drc_V12_s.__slots__ = [
    'DrcTuningPara',
]
struct_CalibDbV2_drc_V12_s._fields_ = [
    ('DrcTuningPara', CalibDbV2_Adrc_V12_t),
]

CalibDbV2_drc_V12_t = struct_CalibDbV2_drc_V12_s# /usr/include/rkaiq/iq_parser_v2/adrc_head.h: 269

# /usr/include/rkaiq/iq_parser_v2/adrc_head.h: 284
class struct_localV12Lite_s(Structure):
    pass

struct_localV12Lite_s.__slots__ = [
    'LocalData',
    'MotionData',
    'curPixWeit',
    'Range_force_sgm',
    'Range_sgm_cur',
    'Space_sgm_cur',
]
struct_localV12Lite_s._fields_ = [
    ('LocalData', LocalDataV2_t),
    ('MotionData', MotionData_t),
    ('curPixWeit', c_float),
    ('Range_force_sgm', c_float),
    ('Range_sgm_cur', c_float),
    ('Space_sgm_cur', c_int),
]

localV12Lite_t = struct_localV12Lite_s# /usr/include/rkaiq/iq_parser_v2/adrc_head.h: 284

# /usr/include/rkaiq/iq_parser_v2/adrc_head.h: 311
class struct_CalibDbV2_Adrc_v12_lite_s(Structure):
    pass

struct_CalibDbV2_Adrc_v12_lite_s.__slots__ = [
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
    'damp',
]
struct_CalibDbV2_Adrc_v12_lite_s._fields_ = [
    ('Enable', c_bool),
    ('CtrlDataType', CtrlDataType_t),
    ('DrcGain', AdrcGain_t),
    ('HiLight', HighLightV12_t),
    ('LocalSetting', localV12Lite_t),
    ('CompressSetting', Compress_t),
    ('Scale_y', c_int * int(17)),
    ('ByPassThr', c_float),
    ('Edge_Weit', c_float),
    ('OutPutLongFrame', c_bool),
    ('IIR_frame', c_int),
    ('damp', c_float),
]

CalibDbV2_Adrc_v12_lite_t = struct_CalibDbV2_Adrc_v12_lite_s# /usr/include/rkaiq/iq_parser_v2/adrc_head.h: 311

# /usr/include/rkaiq/iq_parser_v2/adrc_head.h: 316
class struct_CalibDbV2_drc_v12_lite_s(Structure):
    pass

struct_CalibDbV2_drc_v12_lite_s.__slots__ = [
    'DrcTuningPara',
]
struct_CalibDbV2_drc_v12_lite_s._fields_ = [
    ('DrcTuningPara', CalibDbV2_Adrc_v12_lite_t),
]

CalibDbV2_drc_v12_lite_t = struct_CalibDbV2_drc_v12_lite_s# /usr/include/rkaiq/iq_parser_v2/adrc_head.h: 316

# /usr/include/rkaiq/iq_parser_v2/adrc_uapi_head.h: 31
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

mDrcGain_t = struct_mDrcGain_t# /usr/include/rkaiq/iq_parser_v2/adrc_uapi_head.h: 31

# /usr/include/rkaiq/iq_parser_v2/adrc_uapi_head.h: 36
class struct_mDrcHiLit_s(Structure):
    pass

struct_mDrcHiLit_s.__slots__ = [
    'Strength',
]
struct_mDrcHiLit_s._fields_ = [
    ('Strength', c_float),
]

mDrcHiLit_t = struct_mDrcHiLit_s# /usr/include/rkaiq/iq_parser_v2/adrc_uapi_head.h: 36

# /usr/include/rkaiq/iq_parser_v2/adrc_uapi_head.h: 45
class struct_mLocalDataV10_s(Structure):
    pass

struct_mLocalDataV10_s.__slots__ = [
    'LocalWeit',
    'GlobalContrast',
    'LoLitContrast',
]
struct_mLocalDataV10_s._fields_ = [
    ('LocalWeit', c_float),
    ('GlobalContrast', c_float),
    ('LoLitContrast', c_float),
]

mLocalDataV10_t = struct_mLocalDataV10_s# /usr/include/rkaiq/iq_parser_v2/adrc_uapi_head.h: 45

# /usr/include/rkaiq/iq_parser_v2/adrc_uapi_head.h: 64
class struct_mDrcLocalV10_s(Structure):
    pass

struct_mDrcLocalV10_s.__slots__ = [
    'LocalTMOData',
    'curPixWeit',
    'preFrameWeit',
    'Range_force_sgm',
    'Range_sgm_cur',
    'Range_sgm_pre',
    'Space_sgm_cur',
    'Space_sgm_pre',
]
struct_mDrcLocalV10_s._fields_ = [
    ('LocalTMOData', mLocalDataV10_t),
    ('curPixWeit', c_float),
    ('preFrameWeit', c_float),
    ('Range_force_sgm', c_float),
    ('Range_sgm_cur', c_float),
    ('Range_sgm_pre', c_float),
    ('Space_sgm_cur', c_int),
    ('Space_sgm_pre', c_int),
]

mDrcLocalV10_t = struct_mDrcLocalV10_s# /usr/include/rkaiq/iq_parser_v2/adrc_uapi_head.h: 64

# /usr/include/rkaiq/iq_parser_v2/adrc_uapi_head.h: 71
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

mDrcCompress_t = struct_mDrcCompress_s# /usr/include/rkaiq/iq_parser_v2/adrc_uapi_head.h: 71

# /usr/include/rkaiq/iq_parser_v2/adrc_uapi_head.h: 92
class struct_mdrcAttr_V10_s(Structure):
    pass

struct_mdrcAttr_V10_s.__slots__ = [
    'Enable',
    'DrcGain',
    'HiLight',
    'LocalTMOSetting',
    'CompressSetting',
    'Scale_y',
    'Edge_Weit',
    'OutPutLongFrame',
    'IIR_frame',
]
struct_mdrcAttr_V10_s._fields_ = [
    ('Enable', c_bool),
    ('DrcGain', mDrcGain_t),
    ('HiLight', mDrcHiLit_t),
    ('LocalTMOSetting', mDrcLocalV10_t),
    ('CompressSetting', mDrcCompress_t),
    ('Scale_y', c_int * int(17)),
    ('Edge_Weit', c_float),
    ('OutPutLongFrame', c_bool),
    ('IIR_frame', c_int),
]

mdrcAttr_V10_t = struct_mdrcAttr_V10_s# /usr/include/rkaiq/iq_parser_v2/adrc_uapi_head.h: 92

# /usr/include/rkaiq/iq_parser_v2/adrc_uapi_head.h: 99
class struct_DrcInfo_s(Structure):
    pass

struct_DrcInfo_s.__slots__ = [
    'EnvLv',
    'ISO',
]
struct_DrcInfo_s._fields_ = [
    ('EnvLv', c_float),
    ('ISO', c_float),
]

DrcInfo_t = struct_DrcInfo_s# /usr/include/rkaiq/iq_parser_v2/adrc_uapi_head.h: 99

# /usr/include/rkaiq/iq_parser_v2/adrc_uapi_head.h: 106
class struct_DrcInfoV10_s(Structure):
    pass

struct_DrcInfoV10_s.__slots__ = [
    'CtrlInfo',
    'ValidParams',
]
struct_DrcInfoV10_s._fields_ = [
    ('CtrlInfo', DrcInfo_t),
    ('ValidParams', mdrcAttr_V10_t),
]

DrcInfoV10_t = struct_DrcInfoV10_s# /usr/include/rkaiq/iq_parser_v2/adrc_uapi_head.h: 106

# /usr/include/rkaiq/iq_parser_v2/adrc_uapi_head.h: 120
class struct_mLocalDataV11_s(Structure):
    pass

struct_mLocalDataV11_s.__slots__ = [
    'LocalWeit',
    'LocalAutoEnable',
    'LocalAutoWeit',
    'GlobalContrast',
    'LoLitContrast',
]
struct_mLocalDataV11_s._fields_ = [
    ('LocalWeit', c_float),
    ('LocalAutoEnable', c_int),
    ('LocalAutoWeit', c_float),
    ('GlobalContrast', c_float),
    ('LoLitContrast', c_float),
]

mLocalDataV11_t = struct_mLocalDataV11_s# /usr/include/rkaiq/iq_parser_v2/adrc_uapi_head.h: 120

# /usr/include/rkaiq/iq_parser_v2/adrc_uapi_head.h: 139
class struct_mDrcLocalV11_s(Structure):
    pass

struct_mDrcLocalV11_s.__slots__ = [
    'LocalData',
    'curPixWeit',
    'preFrameWeit',
    'Range_force_sgm',
    'Range_sgm_cur',
    'Range_sgm_pre',
    'Space_sgm_cur',
    'Space_sgm_pre',
]
struct_mDrcLocalV11_s._fields_ = [
    ('LocalData', mLocalDataV11_t),
    ('curPixWeit', c_float),
    ('preFrameWeit', c_float),
    ('Range_force_sgm', c_float),
    ('Range_sgm_cur', c_float),
    ('Range_sgm_pre', c_float),
    ('Space_sgm_cur', c_int),
    ('Space_sgm_pre', c_int),
]

mDrcLocalV11_t = struct_mDrcLocalV11_s# /usr/include/rkaiq/iq_parser_v2/adrc_uapi_head.h: 139

# /usr/include/rkaiq/iq_parser_v2/adrc_uapi_head.h: 160
class struct_mdrcAttr_V11_s(Structure):
    pass

struct_mdrcAttr_V11_s.__slots__ = [
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
struct_mdrcAttr_V11_s._fields_ = [
    ('Enable', c_bool),
    ('DrcGain', mDrcGain_t),
    ('HiLight', mDrcHiLit_t),
    ('LocalSetting', mDrcLocalV11_t),
    ('CompressSetting', mDrcCompress_t),
    ('Scale_y', c_int * int(17)),
    ('Edge_Weit', c_float),
    ('OutPutLongFrame', c_bool),
    ('IIR_frame', c_int),
]

mdrcAttr_V11_t = struct_mdrcAttr_V11_s# /usr/include/rkaiq/iq_parser_v2/adrc_uapi_head.h: 160

# /usr/include/rkaiq/iq_parser_v2/adrc_uapi_head.h: 167
class struct_DrcInfoV11_s(Structure):
    pass

struct_DrcInfoV11_s.__slots__ = [
    'CtrlInfo',
    'ValidParams',
]
struct_DrcInfoV11_s._fields_ = [
    ('CtrlInfo', DrcInfo_t),
    ('ValidParams', mdrcAttr_V11_t),
]

DrcInfoV11_t = struct_DrcInfoV11_s# /usr/include/rkaiq/iq_parser_v2/adrc_uapi_head.h: 167

# /usr/include/rkaiq/iq_parser_v2/adrc_uapi_head.h: 175
class struct_mHighLightDataV12_s(Structure):
    pass

struct_mHighLightDataV12_s.__slots__ = [
    'Strength',
    'gas_t',
]
struct_mHighLightDataV12_s._fields_ = [
    ('Strength', c_float),
    ('gas_t', c_float),
]

mHighLightDataV12_t = struct_mHighLightDataV12_s# /usr/include/rkaiq/iq_parser_v2/adrc_uapi_head.h: 175

# /usr/include/rkaiq/iq_parser_v2/adrc_uapi_head.h: 188
class struct_mHighLightV12_s(Structure):
    pass

struct_mHighLightV12_s.__slots__ = [
    'HiLightData',
    'gas_l0',
    'gas_l1',
    'gas_l2',
    'gas_l3',
]
struct_mHighLightV12_s._fields_ = [
    ('HiLightData', mHighLightDataV12_t),
    ('gas_l0', c_int),
    ('gas_l1', c_int),
    ('gas_l2', c_int),
    ('gas_l3', c_int),
]

mHighLightV12_t = struct_mHighLightV12_s# /usr/include/rkaiq/iq_parser_v2/adrc_uapi_head.h: 188

# /usr/include/rkaiq/iq_parser_v2/adrc_uapi_head.h: 193
class struct_mMotionData_s(Structure):
    pass

struct_mMotionData_s.__slots__ = [
    'MotionStr',
]
struct_mMotionData_s._fields_ = [
    ('MotionStr', c_float),
]

mMotionData_t = struct_mMotionData_s# /usr/include/rkaiq/iq_parser_v2/adrc_uapi_head.h: 193

# /usr/include/rkaiq/iq_parser_v2/adrc_uapi_head.h: 214
class struct_mDrcLocalV12_s(Structure):
    pass

struct_mDrcLocalV12_s.__slots__ = [
    'LocalData',
    'MotionData',
    'curPixWeit',
    'preFrameWeit',
    'Range_force_sgm',
    'Range_sgm_cur',
    'Range_sgm_pre',
    'Space_sgm_cur',
    'Space_sgm_pre',
]
struct_mDrcLocalV12_s._fields_ = [
    ('LocalData', mLocalDataV11_t),
    ('MotionData', mMotionData_t),
    ('curPixWeit', c_float),
    ('preFrameWeit', c_float),
    ('Range_force_sgm', c_float),
    ('Range_sgm_cur', c_float),
    ('Range_sgm_pre', c_float),
    ('Space_sgm_cur', c_int),
    ('Space_sgm_pre', c_int),
]

mDrcLocalV12_t = struct_mDrcLocalV12_s# /usr/include/rkaiq/iq_parser_v2/adrc_uapi_head.h: 214

# /usr/include/rkaiq/iq_parser_v2/adrc_uapi_head.h: 235
class struct_mdrcAttr_V12_s(Structure):
    pass

struct_mdrcAttr_V12_s.__slots__ = [
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
struct_mdrcAttr_V12_s._fields_ = [
    ('Enable', c_bool),
    ('DrcGain', mDrcGain_t),
    ('HiLight', mHighLightV12_t),
    ('LocalSetting', mDrcLocalV12_t),
    ('CompressSetting', mDrcCompress_t),
    ('Scale_y', c_int * int(17)),
    ('Edge_Weit', c_float),
    ('OutPutLongFrame', c_bool),
    ('IIR_frame', c_int),
]

mdrcAttr_V12_t = struct_mdrcAttr_V12_s# /usr/include/rkaiq/iq_parser_v2/adrc_uapi_head.h: 235

# /usr/include/rkaiq/iq_parser_v2/adrc_uapi_head.h: 242
class struct_DrcInfoV12_s(Structure):
    pass

struct_DrcInfoV12_s.__slots__ = [
    'CtrlInfo',
    'ValidParams',
]
struct_DrcInfoV12_s._fields_ = [
    ('CtrlInfo', DrcInfo_t),
    ('ValidParams', mdrcAttr_V12_t),
]

DrcInfoV12_t = struct_DrcInfoV12_s# /usr/include/rkaiq/iq_parser_v2/adrc_uapi_head.h: 242

# /usr/include/rkaiq/iq_parser_v2/adrc_uapi_head.h: 258
class struct_mDrcLocalV12Lite_s(Structure):
    pass

struct_mDrcLocalV12Lite_s.__slots__ = [
    'LocalData',
    'MotionData',
    'curPixWeit',
    'Range_force_sgm',
    'Range_sgm_cur',
    'Space_sgm_cur',
]
struct_mDrcLocalV12Lite_s._fields_ = [
    ('LocalData', mLocalDataV11_t),
    ('MotionData', mMotionData_t),
    ('curPixWeit', c_float),
    ('Range_force_sgm', c_float),
    ('Range_sgm_cur', c_float),
    ('Space_sgm_cur', c_int),
]

mDrcLocalV12Lite_t = struct_mDrcLocalV12Lite_s# /usr/include/rkaiq/iq_parser_v2/adrc_uapi_head.h: 258

# /usr/include/rkaiq/iq_parser_v2/adrc_uapi_head.h: 279
class struct_mdrcAttr_v12_lite_s(Structure):
    pass

struct_mdrcAttr_v12_lite_s.__slots__ = [
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
struct_mdrcAttr_v12_lite_s._fields_ = [
    ('Enable', c_bool),
    ('DrcGain', mDrcGain_t),
    ('HiLight', mHighLightV12_t),
    ('LocalSetting', mDrcLocalV12Lite_t),
    ('CompressSetting', mDrcCompress_t),
    ('Scale_y', c_int * int(17)),
    ('Edge_Weit', c_float),
    ('OutPutLongFrame', c_bool),
    ('IIR_frame', c_int),
]

mdrcAttr_v12_lite_t = struct_mdrcAttr_v12_lite_s# /usr/include/rkaiq/iq_parser_v2/adrc_uapi_head.h: 279

# /usr/include/rkaiq/iq_parser_v2/adrc_uapi_head.h: 286
class struct_DrcInfoV12Lite_s(Structure):
    pass

struct_DrcInfoV12Lite_s.__slots__ = [
    'CtrlInfo',
    'ValidParams',
]
struct_DrcInfoV12Lite_s._fields_ = [
    ('CtrlInfo', DrcInfo_t),
    ('ValidParams', mdrcAttr_v12_lite_t),
]

DrcInfoV12Lite_t = struct_DrcInfoV12Lite_s# /usr/include/rkaiq/iq_parser_v2/adrc_uapi_head.h: 286

enum_drc_OpMode_s = c_int# /usr/include/rkaiq/algos/adrc/rk_aiq_types_adrc_algo_int.h: 26

drc_OpMode_t = enum_drc_OpMode_s# /usr/include/rkaiq/algos/adrc/rk_aiq_types_adrc_algo_int.h: 26

# /usr/include/rkaiq/algos/adrc/rk_aiq_types_adrc_algo_int.h: 36
class struct_drcAttrV10_s(Structure):
    pass

struct_drcAttrV10_s.__slots__ = [
    'sync',
    'opMode',
    'stAuto',
    'stManual',
    'Info',
]
struct_drcAttrV10_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('opMode', drc_OpMode_t),
    ('stAuto', CalibDbV2_drc_V10_t),
    ('stManual', mdrcAttr_V10_t),
    ('Info', DrcInfoV10_t),
]

drcAttrV10_t = struct_drcAttrV10_s# /usr/include/rkaiq/algos/adrc/rk_aiq_types_adrc_algo_int.h: 36

# /usr/include/rkaiq/algos/adrc/rk_aiq_types_adrc_algo_int.h: 47
class struct_drcAttrV11_s(Structure):
    pass

struct_drcAttrV11_s.__slots__ = [
    'sync',
    'opMode',
    'stAuto',
    'stManual',
    'Info',
]
struct_drcAttrV11_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('opMode', drc_OpMode_t),
    ('stAuto', CalibDbV2_drc_V11_t),
    ('stManual', mdrcAttr_V11_t),
    ('Info', DrcInfoV11_t),
]

drcAttrV11_t = struct_drcAttrV11_s# /usr/include/rkaiq/algos/adrc/rk_aiq_types_adrc_algo_int.h: 47

# /usr/include/rkaiq/algos/adrc/rk_aiq_types_adrc_algo_int.h: 57
class struct_drcAttrV12_s(Structure):
    pass

struct_drcAttrV12_s.__slots__ = [
    'sync',
    'opMode',
    'stAuto',
    'stManual',
    'Info',
]
struct_drcAttrV12_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('opMode', drc_OpMode_t),
    ('stAuto', CalibDbV2_drc_V12_t),
    ('stManual', mdrcAttr_V12_t),
    ('Info', DrcInfoV12_t),
]

drcAttrV12_t = struct_drcAttrV12_s# /usr/include/rkaiq/algos/adrc/rk_aiq_types_adrc_algo_int.h: 57

# /usr/include/rkaiq/algos/adrc/rk_aiq_types_adrc_algo_int.h: 67
class struct_drcAttrV12Lite_s(Structure):
    pass

struct_drcAttrV12Lite_s.__slots__ = [
    'sync',
    'opMode',
    'stAuto',
    'stManual',
    'Info',
]
struct_drcAttrV12Lite_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('opMode', drc_OpMode_t),
    ('stAuto', CalibDbV2_drc_v12_lite_t),
    ('stManual', mdrcAttr_v12_lite_t),
    ('Info', DrcInfoV12Lite_t),
]

drcAttrV12Lite_t = struct_drcAttrV12Lite_s# /usr/include/rkaiq/algos/adrc/rk_aiq_types_adrc_algo_int.h: 67

enum_GammaType_e = c_int# /usr/include/rkaiq/iq_parser_v2/agamma_head.h: 33

GammaType_t = enum_GammaType_e# /usr/include/rkaiq/iq_parser_v2/agamma_head.h: 33

# /usr/include/rkaiq/iq_parser_v2/agamma_head.h: 45
class struct_CalibDbGammaV10_s(Structure):
    pass

struct_CalibDbGammaV10_s.__slots__ = [
    'Gamma_en',
    'Gamma_out_segnum',
    'Gamma_out_offset',
    'Gamma_curve',
]
struct_CalibDbGammaV10_s._fields_ = [
    ('Gamma_en', c_bool),
    ('Gamma_out_segnum', GammaType_t),
    ('Gamma_out_offset', uint16_t),
    ('Gamma_curve', uint16_t * int(45)),
]

CalibDbGammaV10_t = struct_CalibDbGammaV10_s# /usr/include/rkaiq/iq_parser_v2/agamma_head.h: 45

# /usr/include/rkaiq/iq_parser_v2/agamma_head.h: 50
class struct_CalibDbV2_gamma_v10_s(Structure):
    pass

struct_CalibDbV2_gamma_v10_s.__slots__ = [
    'GammaTuningPara',
]
struct_CalibDbV2_gamma_v10_s._fields_ = [
    ('GammaTuningPara', CalibDbGammaV10_t),
]

CalibDbV2_gamma_v10_t = struct_CalibDbV2_gamma_v10_s# /usr/include/rkaiq/iq_parser_v2/agamma_head.h: 50

# /usr/include/rkaiq/iq_parser_v2/agamma_head.h: 60
class struct_CalibDbGammaV11_s(Structure):
    pass

struct_CalibDbGammaV11_s.__slots__ = [
    'Gamma_en',
    'Gamma_out_offset',
    'Gamma_curve',
]
struct_CalibDbGammaV11_s._fields_ = [
    ('Gamma_en', c_bool),
    ('Gamma_out_offset', uint16_t),
    ('Gamma_curve', uint16_t * int(49)),
]

CalibDbGammaV11_t = struct_CalibDbGammaV11_s# /usr/include/rkaiq/iq_parser_v2/agamma_head.h: 60

# /usr/include/rkaiq/iq_parser_v2/agamma_head.h: 65
class struct_CalibDbV2_gamma_v11_s(Structure):
    pass

struct_CalibDbV2_gamma_v11_s.__slots__ = [
    'GammaTuningPara',
]
struct_CalibDbV2_gamma_v11_s._fields_ = [
    ('GammaTuningPara', CalibDbGammaV11_t),
]

CalibDbV2_gamma_v11_t = struct_CalibDbV2_gamma_v11_s# /usr/include/rkaiq/iq_parser_v2/agamma_head.h: 65

# /usr/include/rkaiq/iq_parser_v2/agamma_uapi_head.h: 32
class struct_AgammaApiManualV10_s(Structure):
    pass

struct_AgammaApiManualV10_s.__slots__ = [
    'Gamma_en',
    'Gamma_out_segnum',
    'Gamma_out_offset',
    'Gamma_curve',
]
struct_AgammaApiManualV10_s._fields_ = [
    ('Gamma_en', c_bool),
    ('Gamma_out_segnum', GammaType_t),
    ('Gamma_out_offset', uint16_t),
    ('Gamma_curve', uint16_t * int(45)),
]

AgammaApiManualV10_t = struct_AgammaApiManualV10_s# /usr/include/rkaiq/iq_parser_v2/agamma_uapi_head.h: 32

# /usr/include/rkaiq/iq_parser_v2/agamma_uapi_head.h: 41
class struct_AgammaApiManualV11_s(Structure):
    pass

struct_AgammaApiManualV11_s.__slots__ = [
    'Gamma_en',
    'Gamma_out_offset',
    'Gamma_curve',
]
struct_AgammaApiManualV11_s._fields_ = [
    ('Gamma_en', c_bool),
    ('Gamma_out_offset', uint16_t),
    ('Gamma_curve', uint16_t * int(49)),
]

AgammaApiManualV11_t = struct_AgammaApiManualV11_s# /usr/include/rkaiq/iq_parser_v2/agamma_uapi_head.h: 41

enum_rk_aiq_gamma_op_mode_s = c_int# /usr/include/rkaiq/algos/agamma/rk_aiq_types_agamma_algo_int.h: 30

rk_aiq_gamma_op_mode_t = enum_rk_aiq_gamma_op_mode_s# /usr/include/rkaiq/algos/agamma/rk_aiq_types_agamma_algo_int.h: 30

# /usr/include/rkaiq/algos/agamma/rk_aiq_types_agamma_algo_int.h: 39
class struct_rk_aiq_gamma_v10_attr_s(Structure):
    pass

struct_rk_aiq_gamma_v10_attr_s.__slots__ = [
    'sync',
    'mode',
    'stManual',
    'stAuto',
]
struct_rk_aiq_gamma_v10_attr_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('mode', rk_aiq_gamma_op_mode_t),
    ('stManual', AgammaApiManualV10_t),
    ('stAuto', CalibDbV2_gamma_v10_t),
]

rk_aiq_gamma_v10_attr_t = struct_rk_aiq_gamma_v10_attr_s# /usr/include/rkaiq/algos/agamma/rk_aiq_types_agamma_algo_int.h: 39

# /usr/include/rkaiq/algos/agamma/rk_aiq_types_agamma_algo_int.h: 48
class struct_rk_aiq_gamma_v11_attr_s(Structure):
    pass

struct_rk_aiq_gamma_v11_attr_s.__slots__ = [
    'sync',
    'mode',
    'stManual',
    'stAuto',
]
struct_rk_aiq_gamma_v11_attr_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('mode', rk_aiq_gamma_op_mode_t),
    ('stManual', AgammaApiManualV11_t),
    ('stAuto', CalibDbV2_gamma_v11_t),
]

rk_aiq_gamma_v11_attr_t = struct_rk_aiq_gamma_v11_attr_s# /usr/include/rkaiq/algos/agamma/rk_aiq_types_agamma_algo_int.h: 48

# /usr/include/rkaiq/iq_parser_v2/adegamma_head.h: 46
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

AdegmmaParaV2_t = struct_AdegmmaParaV2_s# /usr/include/rkaiq/iq_parser_v2/adegamma_head.h: 46

# /usr/include/rkaiq/iq_parser_v2/adegamma_head.h: 51
class struct_CalibDbV2_Adegmma_s(Structure):
    pass

struct_CalibDbV2_Adegmma_s.__slots__ = [
    'DegammaTuningPara',
]
struct_CalibDbV2_Adegmma_s._fields_ = [
    ('DegammaTuningPara', AdegmmaParaV2_t),
]

CalibDbV2_Adegmma_t = struct_CalibDbV2_Adegmma_s# /usr/include/rkaiq/iq_parser_v2/adegamma_head.h: 51

enum_rk_aiq_degamma_op_mode_s = c_int# /usr/include/rkaiq/algos/adegamma/rk_aiq_types_adegamma_algo_int.h: 46

rk_aiq_degamma_op_mode_t = enum_rk_aiq_degamma_op_mode_s# /usr/include/rkaiq/algos/adegamma/rk_aiq_types_adegamma_algo_int.h: 46

# /usr/include/rkaiq/algos/adegamma/rk_aiq_types_adegamma_algo_int.h: 54
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

Adegamma_api_manual_t = struct_Adegamma_api_manual_s# /usr/include/rkaiq/algos/adegamma/rk_aiq_types_adegamma_algo_int.h: 54

# /usr/include/rkaiq/algos/adegamma/rk_aiq_types_adegamma_algo_int.h: 69
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

rk_aiq_degamma_attr_t = struct_rk_aiq_degamma_attr_s# /usr/include/rkaiq/algos/adegamma/rk_aiq_types_adegamma_algo_int.h: 69

# /usr/include/rkaiq/iq_parser_v2/adehaze_uapi_head.h: 66
class struct_mDehazeDataV11_s(Structure):
    pass

struct_mDehazeDataV11_s.__slots__ = [
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
struct_mDehazeDataV11_s._fields_ = [
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

mDehazeDataV11_t = struct_mDehazeDataV11_s# /usr/include/rkaiq/iq_parser_v2/adehaze_uapi_head.h: 66

# /usr/include/rkaiq/iq_parser_v2/adehaze_uapi_head.h: 87
class struct_mDehaze_setting_v11_s(Structure):
    pass

struct_mDehaze_setting_v11_s.__slots__ = [
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
struct_mDehaze_setting_v11_s._fields_ = [
    ('en', c_bool),
    ('air_lc_en', c_bool),
    ('stab_fnum', c_float),
    ('sigma', c_float),
    ('wt_sigma', c_float),
    ('air_sigma', c_float),
    ('tmax_sigma', c_float),
    ('pre_wet', c_float),
    ('DehazeData', mDehazeDataV11_t),
]

mDehaze_setting_v11_t = struct_mDehaze_setting_v11_s# /usr/include/rkaiq/iq_parser_v2/adehaze_uapi_head.h: 87

# /usr/include/rkaiq/iq_parser_v2/adehaze_uapi_head.h: 94
class struct_mEnhanceDataV11_s(Structure):
    pass

struct_mEnhanceDataV11_s.__slots__ = [
    'enhance_value',
    'enhance_chroma',
]
struct_mEnhanceDataV11_s._fields_ = [
    ('enhance_value', c_float),
    ('enhance_chroma', c_float),
]

mEnhanceDataV11_t = struct_mEnhanceDataV11_s# /usr/include/rkaiq/iq_parser_v2/adehaze_uapi_head.h: 94

# /usr/include/rkaiq/iq_parser_v2/adehaze_uapi_head.h: 103
class struct_mEnhance_setting_v11_s(Structure):
    pass

struct_mEnhance_setting_v11_s.__slots__ = [
    'en',
    'enhance_curve',
    'EnhanceData',
]
struct_mEnhance_setting_v11_s._fields_ = [
    ('en', c_bool),
    ('enhance_curve', c_float * int(17)),
    ('EnhanceData', mEnhanceDataV11_t),
]

mEnhance_setting_v11_t = struct_mEnhance_setting_v11_s# /usr/include/rkaiq/iq_parser_v2/adehaze_uapi_head.h: 103

# /usr/include/rkaiq/iq_parser_v2/adehaze_uapi_head.h: 118
class struct_mHistDataV11_s(Structure):
    pass

struct_mHistDataV11_s.__slots__ = [
    'hist_gratio',
    'hist_th_off',
    'hist_k',
    'hist_min',
    'hist_scale',
    'cfg_gratio',
]
struct_mHistDataV11_s._fields_ = [
    ('hist_gratio', c_float),
    ('hist_th_off', c_float),
    ('hist_k', c_float),
    ('hist_min', c_float),
    ('hist_scale', c_float),
    ('cfg_gratio', c_float),
]

mHistDataV11_t = struct_mHistDataV11_s# /usr/include/rkaiq/iq_parser_v2/adehaze_uapi_head.h: 118

# /usr/include/rkaiq/iq_parser_v2/adehaze_uapi_head.h: 127
class struct_mHist_setting_v11_s(Structure):
    pass

struct_mHist_setting_v11_s.__slots__ = [
    'en',
    'hist_para_en',
    'HistData',
]
struct_mHist_setting_v11_s._fields_ = [
    ('en', c_bool),
    ('hist_para_en', c_bool),
    ('HistData', mHistDataV11_t),
]

mHist_setting_v11_t = struct_mHist_setting_v11_s# /usr/include/rkaiq/iq_parser_v2/adehaze_uapi_head.h: 127

# /usr/include/rkaiq/iq_parser_v2/adehaze_uapi_head.h: 140
class struct_mDehazeAttrV11_s(Structure):
    pass

struct_mDehazeAttrV11_s.__slots__ = [
    'Enable',
    'cfg_alpha',
    'dehaze_setting',
    'enhance_setting',
    'hist_setting',
]
struct_mDehazeAttrV11_s._fields_ = [
    ('Enable', c_bool),
    ('cfg_alpha', c_float),
    ('dehaze_setting', mDehaze_setting_v11_t),
    ('enhance_setting', mEnhance_setting_v11_t),
    ('hist_setting', mHist_setting_v11_t),
]

mDehazeAttrV11_t = struct_mDehazeAttrV11_s# /usr/include/rkaiq/iq_parser_v2/adehaze_uapi_head.h: 140

# /usr/include/rkaiq/iq_parser_v2/adehaze_uapi_head.h: 159
class struct_mDehazeAttrInfoV11_s(Structure):
    pass

struct_mDehazeAttrInfoV11_s.__slots__ = [
    'ISO',
    'EnvLv',
    'updateMDehazeStrth',
    'MDehazeStrth',
    'updateMEnhanceStrth',
    'MEnhanceStrth',
    'updateMEnhanceChromeStrth',
    'MEnhanceChromeStrth',
]
struct_mDehazeAttrInfoV11_s._fields_ = [
    ('ISO', c_float),
    ('EnvLv', c_float),
    ('updateMDehazeStrth', c_bool),
    ('MDehazeStrth', c_uint),
    ('updateMEnhanceStrth', c_bool),
    ('MEnhanceStrth', c_uint),
    ('updateMEnhanceChromeStrth', c_bool),
    ('MEnhanceChromeStrth', c_uint),
]

mDehazeAttrInfoV11_t = struct_mDehazeAttrInfoV11_s# /usr/include/rkaiq/iq_parser_v2/adehaze_uapi_head.h: 159

# /usr/include/rkaiq/iq_parser_v2/adehaze_uapi_head.h: 170
class struct_mEnhanceDataV12_s(Structure):
    pass

struct_mEnhanceDataV12_s.__slots__ = [
    'enhance_curve',
    'enh_luma',
    'enhance_value',
    'enhance_chroma',
]
struct_mEnhanceDataV12_s._fields_ = [
    ('enhance_curve', c_float * int(17)),
    ('enh_luma', c_float * int(17)),
    ('enhance_value', c_float),
    ('enhance_chroma', c_float),
]

mEnhanceDataV12_t = struct_mEnhanceDataV12_s# /usr/include/rkaiq/iq_parser_v2/adehaze_uapi_head.h: 170

# /usr/include/rkaiq/iq_parser_v2/adehaze_uapi_head.h: 181
class struct_mEnhance_setting_v12_s(Structure):
    pass

struct_mEnhance_setting_v12_s.__slots__ = [
    'en',
    'color_deviate_en',
    'enh_luma_en',
    'EnhanceData',
]
struct_mEnhance_setting_v12_s._fields_ = [
    ('en', c_bool),
    ('color_deviate_en', c_bool),
    ('enh_luma_en', c_bool),
    ('EnhanceData', mEnhanceDataV12_t),
]

mEnhance_setting_v12_t = struct_mEnhance_setting_v12_s# /usr/include/rkaiq/iq_parser_v2/adehaze_uapi_head.h: 181

# /usr/include/rkaiq/iq_parser_v2/adehaze_uapi_head.h: 188
class struct_mManual_curve_s(Structure):
    pass

struct_mManual_curve_s.__slots__ = [
    'curve_x',
    'curve_y',
]
struct_mManual_curve_s._fields_ = [
    ('curve_x', c_int * int(17)),
    ('curve_y', c_int * int(17)),
]

mManual_curve_t = struct_mManual_curve_s# /usr/include/rkaiq/iq_parser_v2/adehaze_uapi_head.h: 188

# /usr/include/rkaiq/iq_parser_v2/adehaze_uapi_head.h: 197
class struct_mhist_wr_semiauto_s(Structure):
    pass

struct_mhist_wr_semiauto_s.__slots__ = [
    'clim0',
    'clim1',
    'dark_th',
]
struct_mhist_wr_semiauto_s._fields_ = [
    ('clim0', c_float),
    ('clim1', c_float),
    ('dark_th', c_float),
]

mhist_wr_semiauto_t = struct_mhist_wr_semiauto_s# /usr/include/rkaiq/iq_parser_v2/adehaze_uapi_head.h: 197

# /usr/include/rkaiq/iq_parser_v2/adehaze_uapi_head.h: 206
class struct_mHistWr_s(Structure):
    pass

struct_mHistWr_s.__slots__ = [
    'mode',
    'manual_curve',
    'semiauto_curve',
]
struct_mHistWr_s._fields_ = [
    ('mode', HistWrMode_t),
    ('manual_curve', mManual_curve_t),
    ('semiauto_curve', mhist_wr_semiauto_t),
]

mHistWr_t = struct_mHistWr_s# /usr/include/rkaiq/iq_parser_v2/adehaze_uapi_head.h: 206

# /usr/include/rkaiq/iq_parser_v2/adehaze_uapi_head.h: 217
class struct_mHist_setting_v12_s(Structure):
    pass

struct_mHist_setting_v12_s.__slots__ = [
    'en',
    'hist_para_en',
    'hist_wr',
    'HistData',
]
struct_mHist_setting_v12_s._fields_ = [
    ('en', c_bool),
    ('hist_para_en', c_bool),
    ('hist_wr', mHistWr_t),
    ('HistData', mHistDataV11_t),
]

mHist_setting_v12_t = struct_mHist_setting_v12_s# /usr/include/rkaiq/iq_parser_v2/adehaze_uapi_head.h: 217

# /usr/include/rkaiq/iq_parser_v2/adehaze_uapi_head.h: 230
class struct_mDehazeAttrV12_s(Structure):
    pass

struct_mDehazeAttrV12_s.__slots__ = [
    'Enable',
    'cfg_alpha',
    'dehaze_setting',
    'enhance_setting',
    'hist_setting',
]
struct_mDehazeAttrV12_s._fields_ = [
    ('Enable', c_bool),
    ('cfg_alpha', c_float),
    ('dehaze_setting', mDehaze_setting_v11_t),
    ('enhance_setting', mEnhance_setting_v12_t),
    ('hist_setting', mHist_setting_v12_t),
]

mDehazeAttrV12_t = struct_mDehazeAttrV12_s# /usr/include/rkaiq/iq_parser_v2/adehaze_uapi_head.h: 230

enum_dehaze_api_mode_s = c_int# /usr/include/rkaiq/algos/adehaze/rk_aiq_types_adehaze_algo_int.h: 43

dehaze_api_mode_t = enum_dehaze_api_mode_s# /usr/include/rkaiq/algos/adehaze/rk_aiq_types_adehaze_algo_int.h: 43

# /usr/include/rkaiq/algos/adehaze/rk_aiq_types_adehaze_algo_int.h: 57
class struct_adehaze_sw_v11_s(Structure):
    pass

struct_adehaze_sw_v11_s.__slots__ = [
    'sync',
    'mode',
    'stAuto',
    'stManual',
    'Info',
]
struct_adehaze_sw_v11_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('mode', dehaze_api_mode_t),
    ('stAuto', CalibDbV2_dehaze_v11_t),
    ('stManual', mDehazeAttrV11_t),
    ('Info', mDehazeAttrInfoV11_t),
]

adehaze_sw_v11_t = struct_adehaze_sw_v11_s# /usr/include/rkaiq/algos/adehaze/rk_aiq_types_adehaze_algo_int.h: 57

# /usr/include/rkaiq/algos/adehaze/rk_aiq_types_adehaze_algo_int.h: 67
class struct_adehaze_sw_v12_s(Structure):
    pass

struct_adehaze_sw_v12_s.__slots__ = [
    'sync',
    'mode',
    'stAuto',
    'stManual',
    'Info',
]
struct_adehaze_sw_v12_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('mode', dehaze_api_mode_t),
    ('stAuto', CalibDbV2_dehaze_v12_t),
    ('stManual', mDehazeAttrV12_t),
    ('Info', mDehazeAttrInfoV11_t),
]

adehaze_sw_v12_t = struct_adehaze_sw_v12_s# /usr/include/rkaiq/algos/adehaze/rk_aiq_types_adehaze_algo_int.h: 67

enum_rk_aiq_ie_effect_e = c_int# /usr/include/rkaiq/algos/aie/rk_aiq_types_aie_algo.h: 31

rk_aiq_ie_effect_t = enum_rk_aiq_ie_effect_e# /usr/include/rkaiq/algos/aie/rk_aiq_types_aie_algo.h: 31

# /usr/include/rkaiq/algos/anr/rk_aiq_types_anr_algo_int.h: 121
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

RKAnr_Bayernr_Params_t = struct_RKAnr_Bayernr_Params_s# /usr/include/rkaiq/algos/anr/rk_aiq_types_anr_algo_int.h: 121

# /usr/include/rkaiq/algos/anr/rk_aiq_types_anr_algo_int.h: 171
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

RKAnr_Bayernr_Params_Select_t = struct_RKAnr_Bayernr_Params_Select_s# /usr/include/rkaiq/algos/anr/rk_aiq_types_anr_algo_int.h: 171

# /usr/include/rkaiq/algos/anr/rk_aiq_types_anr_algo_int.h: 212
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

RKAnr_Mfnr_Params_t = struct_RKAnr_Mfnr_Params_s# /usr/include/rkaiq/algos/anr/rk_aiq_types_anr_algo_int.h: 212

# /usr/include/rkaiq/algos/anr/rk_aiq_types_anr_algo_int.h: 251
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

RKAnr_Mfnr_Params_Select_t = struct_RKAnr_Mfnr_Params_Select_s# /usr/include/rkaiq/algos/anr/rk_aiq_types_anr_algo_int.h: 251

# /usr/include/rkaiq/algos/anr/rk_aiq_types_anr_algo_int.h: 329
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

RKAnr_Uvnr_Params_t = struct_RKAnr_Uvnr_Params_s# /usr/include/rkaiq/algos/anr/rk_aiq_types_anr_algo_int.h: 329

# /usr/include/rkaiq/algos/anr/rk_aiq_types_anr_algo_int.h: 401
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

RKAnr_Uvnr_Params_Select_t = struct_RKAnr_Uvnr_Params_Select_s# /usr/include/rkaiq/algos/anr/rk_aiq_types_anr_algo_int.h: 401

# /usr/include/rkaiq/algos/anr/rk_aiq_types_anr_algo_int.h: 449
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

RKAnr_Ynr_Params_Select_t = struct_RKAnr_Ynr_Params_Select_s# /usr/include/rkaiq/algos/anr/rk_aiq_types_anr_algo_int.h: 449

# /usr/include/rkaiq/algos/anr/rk_aiq_types_anr_algo_int.h: 460
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

RKAnr_Ynr_Params_t = struct_RKAnr_Ynr_Params_s# /usr/include/rkaiq/algos/anr/rk_aiq_types_anr_algo_int.h: 460

enum_ANROPMode_e = c_int# /usr/include/rkaiq/algos/anr/rk_aiq_types_anr_algo_int.h: 490

ANROPMode_t = enum_ANROPMode_e# /usr/include/rkaiq/algos/anr/rk_aiq_types_anr_algo_int.h: 490

# /usr/include/rkaiq/algos/anr/rk_aiq_types_anr_algo_int.h: 507
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

RKAnr_Mfnr_Dynamic_t = struct_RKAnr_Mfnr_Dynamic_s# /usr/include/rkaiq/algos/anr/rk_aiq_types_anr_algo_int.h: 507

# /usr/include/rkaiq/algos/anr/rk_aiq_types_anr_algo_int.h: 524
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

ANR_Manual_Attr_t = struct_ANR_Manual_Attr_s# /usr/include/rkaiq/algos/anr/rk_aiq_types_anr_algo_int.h: 524

# /usr/include/rkaiq/algos/anr/rk_aiq_types_anr_algo_int.h: 551
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

ANR_Auto_Attr_t = struct_ANR_Auto_Attr_s# /usr/include/rkaiq/algos/anr/rk_aiq_types_anr_algo_int.h: 551

# /usr/include/rkaiq/algos/anr/rk_aiq_types_anr_algo_int.h: 594
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

rk_aiq_nr_attrib_t = struct_rk_aiq_nr_attrib_s# /usr/include/rkaiq/algos/anr/rk_aiq_types_anr_algo_int.h: 594

# /usr/include/rkaiq/algos/anr/rk_aiq_types_anr_algo_int.h: 634
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

rk_aiq_nr_IQPara_t = struct_rk_aiq_nr_IQPara_s# /usr/include/rkaiq/algos/anr/rk_aiq_types_anr_algo_int.h: 634

# /usr/include/rkaiq/iq_parser_v2/ablc_uapi_head.h: 40
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

AblcSelect_t = struct_AblcSelect_s# /usr/include/rkaiq/iq_parser_v2/ablc_uapi_head.h: 40

AblcManualAttr_t = AblcSelect_t# /usr/include/rkaiq/iq_parser_v2/ablc_uapi_head.h: 42

# /usr/include/rkaiq/iq_parser_v2/ablc_uapi_head.h: 63
class struct_AblcExpInfo_s(Structure):
    pass

struct_AblcExpInfo_s.__slots__ = [
    'hdr_mode',
    'arTime',
    'arAGain',
    'arDGain',
    'isp_dgain',
    'arIso',
    'isoLow',
    'isoHigh',
]
struct_AblcExpInfo_s._fields_ = [
    ('hdr_mode', c_int),
    ('arTime', c_float * int(3)),
    ('arAGain', c_float * int(3)),
    ('arDGain', c_float * int(3)),
    ('isp_dgain', c_float * int(3)),
    ('arIso', c_int * int(3)),
    ('isoLow', c_int),
    ('isoHigh', c_int),
]

AblcExpInfo_t = struct_AblcExpInfo_s# /usr/include/rkaiq/iq_parser_v2/ablc_uapi_head.h: 63

# /usr/include/rkaiq/iq_parser_v2/ablc_uapi_head.h: 72
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

rk_aiq_ablc_info_t = struct_rk_aiq_ablc_info_s# /usr/include/rkaiq/iq_parser_v2/ablc_uapi_head.h: 72

enum_AblcOPMode_e = c_int# /usr/include/rkaiq/algos/ablc/rk_aiq_types_ablc_algo_int.h: 59

AblcOPMode_t = enum_AblcOPMode_e# /usr/include/rkaiq/algos/ablc/rk_aiq_types_ablc_algo_int.h: 59

# /usr/include/rkaiq/algos/ablc/rk_aiq_types_ablc_algo_int.h: 76
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
    ('iso', c_float * int(13)),
    ('blc_r', c_float * int(13)),
    ('blc_gr', c_float * int(13)),
    ('blc_gb', c_float * int(13)),
    ('blc_b', c_float * int(13)),
]

AblcParams_t = struct_AblcParams_s# /usr/include/rkaiq/algos/ablc/rk_aiq_types_ablc_algo_int.h: 76

# /usr/include/rkaiq/algos/ablc/rk_aiq_types_ablc_algo_int.h: 116
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

rk_aiq_blc_attrib_t = struct_rk_aiq_blc_attrib_s# /usr/include/rkaiq/algos/ablc/rk_aiq_types_ablc_algo_int.h: 116

enum_fec_correct_direction_e = c_int# /usr/include/rkaiq/algos/afec/rk_aiq_types_afec_algo.h: 26

fec_correct_direction_t = enum_fec_correct_direction_e# /usr/include/rkaiq/algos/afec/rk_aiq_types_afec_algo.h: 26

enum_fec_correct_mode_e = c_int# /usr/include/rkaiq/algos/afec/rk_aiq_types_afec_algo.h: 32

fec_correct_mode_t = enum_fec_correct_mode_e# /usr/include/rkaiq/algos/afec/rk_aiq_types_afec_algo.h: 32

# /usr/include/rkaiq/iq_parser_v2/csm_head.h: 40
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

Csm_Param_t = struct___csm_param# /usr/include/rkaiq/iq_parser_v2/csm_head.h: 40

rk_aiq_acsm_params_t = Csm_Param_t# /usr/include/rkaiq/algos/acsm/rk_aiq_types_acsm_algo.h: 25

# /usr/include/rkaiq/iq_parser_v2/cgc_head.h: 34
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

Cgc_Param_t = struct___cgc_param# /usr/include/rkaiq/iq_parser_v2/cgc_head.h: 34

rk_aiq_acgc_params_t = Cgc_Param_t# /usr/include/rkaiq/algos/acgc/rk_aiq_types_acgc_algo.h: 25

# /usr/include/rkaiq/algos/af/rk_aiq_types_af_algo.h: 81
class struct_anon_102(Structure):
    pass

struct_anon_102.__slots__ = [
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
struct_anon_102._fields_ = [
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

rk_aiq_af_algo_sp_meas_t = struct_anon_102# /usr/include/rkaiq/algos/af/rk_aiq_types_af_algo.h: 81

# /usr/include/rkaiq/algos/af/rk_aiq_types_af_algo.h: 115
class struct_anon_103(Structure):
    pass

struct_anon_103.__slots__ = [
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
struct_anon_103._fields_ = [
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

rk_aiq_af_algo_meas_v20_t = struct_anon_103# /usr/include/rkaiq/algos/af/rk_aiq_types_af_algo.h: 115

# /usr/include/rkaiq/algos/af/rk_aiq_types_af_algo.h: 213
class struct_anon_105(Structure):
    pass

struct_anon_105.__slots__ = [
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
struct_anon_105._fields_ = [
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

rk_aiq_af_algo_meas_v30_t = struct_anon_105# /usr/include/rkaiq/algos/af/rk_aiq_types_af_algo.h: 213

# /usr/include/rkaiq/algos/af/rk_aiq_types_af_algo.h: 295
class struct_anon_106(Structure):
    pass

struct_anon_106.__slots__ = [
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
    'vldg_sel',
    'sobel_sel',
    'v_dnscl_mode',
    'from_awb',
    'from_ynr',
    'ae_config_use',
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
    'gaus_coe',
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
struct_anon_106._fields_ = [
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
    ('vldg_sel', c_ubyte),
    ('sobel_sel', c_ubyte),
    ('v_dnscl_mode', c_ubyte),
    ('from_awb', c_ubyte),
    ('from_ynr', c_ubyte),
    ('ae_config_use', c_ubyte),
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
    ('gaus_coe', c_char * int(9)),
    ('v1_iir_coe', c_short * int(3)),
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

rk_aiq_af_algo_meas_v31_t = struct_anon_106# /usr/include/rkaiq/algos/af/rk_aiq_types_af_algo.h: 295

# /usr/include/rkaiq/algos/af/rk_aiq_types_af_algo.h: 399
class struct_anon_107(Structure):
    pass

struct_anon_107.__slots__ = [
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
    'vldg_sel',
    'sobel_sel',
    'v_dnscl_mode',
    'from_awb',
    'from_ynr',
    'ae_config_use',
    'ae_sel',
    'from_bnr',
    'bnrin_shift',
    'hiir_left_border_mode',
    'avg_ds_en',
    'avg_ds_mode',
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
    'gaus_coe',
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
    'hldg_dilate_num',
    'v_fv_thresh',
    'h_fv_thresh',
    'v_fv_limit',
    'v_fv_slope',
    'h_fv_limit',
    'h_fv_slope',
    'v1_fv_shift',
    'v2_fv_shift',
    'h1_fv_shift',
    'h2_fv_shift',
    'v1_acc_mode',
    'v2_acc_mode',
    'h1_acc_mode',
    'h2_acc_mode',
    'highlit_thresh',
    'bls_en',
    'bls_offset',
]
struct_anon_107._fields_ = [
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
    ('vldg_sel', c_ubyte),
    ('sobel_sel', c_ubyte),
    ('v_dnscl_mode', c_ubyte),
    ('from_awb', c_ubyte),
    ('from_ynr', c_ubyte),
    ('ae_config_use', c_ubyte),
    ('ae_sel', c_ubyte),
    ('from_bnr', c_ubyte),
    ('bnrin_shift', c_ubyte),
    ('hiir_left_border_mode', c_ubyte),
    ('avg_ds_en', c_ubyte),
    ('avg_ds_mode', c_ubyte),
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
    ('gaus_coe', c_char * int(9)),
    ('v1_iir_coe', c_short * int(3)),
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
    ('hldg_dilate_num', c_ubyte),
    ('v_fv_thresh', c_ushort),
    ('h_fv_thresh', c_ushort),
    ('v_fv_limit', c_ushort),
    ('v_fv_slope', c_ushort),
    ('h_fv_limit', c_ushort),
    ('h_fv_slope', c_ushort),
    ('v1_fv_shift', c_ubyte),
    ('v2_fv_shift', c_ubyte),
    ('h1_fv_shift', c_ubyte),
    ('h2_fv_shift', c_ubyte),
    ('v1_acc_mode', c_ubyte),
    ('v2_acc_mode', c_ubyte),
    ('h1_acc_mode', c_ubyte),
    ('h2_acc_mode', c_ubyte),
    ('highlit_thresh', c_ushort),
    ('bls_en', c_ubyte),
    ('bls_offset', c_short),
]

rk_aiq_af_algo_meas_v32_t = struct_anon_107# /usr/include/rkaiq/algos/af/rk_aiq_types_af_algo.h: 399

# /usr/include/rkaiq/algos/abayer2dnr2/rk_aiq_types_abayer2dnr_hw_v2.h: 61
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

RK_Bayer2dnr_Fix_V2_t = struct_RK_Bayer2dnr_Fix_V2_s# /usr/include/rkaiq/algos/abayer2dnr2/rk_aiq_types_abayer2dnr_hw_v2.h: 61

# /usr/include/rkaiq/algos/abayertnr2/rk_aiq_types_abayertnr_hw_v2.h: 88
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

RK_Bayertnr_Fix_V2_t = struct_RK_Bayertnr_Fix_V2_s# /usr/include/rkaiq/algos/abayertnr2/rk_aiq_types_abayertnr_hw_v2.h: 88

# /usr/include/rkaiq/algos/acnr2/rk_aiq_types_acnr_hw_v2.h: 70
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

RK_CNR_Fix_V2_t = struct_RK_CNR_Fix_V2_s# /usr/include/rkaiq/algos/acnr2/rk_aiq_types_acnr_hw_v2.h: 70

# /usr/include/rkaiq/algos/again2/rk_aiq_types_again_hw_v2.h: 41
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

RK_GAIN_Fix_V2_t = struct_RK_GAIN_Fix_V2_s# /usr/include/rkaiq/algos/again2/rk_aiq_types_again_hw_v2.h: 41

# /usr/include/rkaiq/algos/asharp4/rk_aiq_types_asharp_hw_v4.h: 67
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

RK_SHARP_Fix_V4_t = struct_RK_SHARP_Fix_V4_s# /usr/include/rkaiq/algos/asharp4/rk_aiq_types_asharp_hw_v4.h: 67

# /usr/include/rkaiq/algos/aynr3/rk_aiq_types_aynr_hw_v3.h: 107
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

RK_YNR_Fix_V3_t = struct_RK_YNR_Fix_V3_s# /usr/include/rkaiq/algos/aynr3/rk_aiq_types_aynr_hw_v3.h: 107

# /usr/include/rkaiq/algos/abayer2dnrV23/rk_aiq_types_abayer2dnr_hw_v23.h: 61
class struct_RK_Bayer2dnr_Fix_V23_s(Structure):
    pass

struct_RK_Bayer2dnr_Fix_V23_s.__slots__ = [
    'bay3d_gain_en',
    'lg2_mode',
    'gauss_en',
    'log_bypass',
    'bayer_en',
    'dgain',
    'pix_diff',
    'diff_thld',
    'softthld',
    'bltflt_streng',
    'reg_w1',
    'sigma_x',
    'sigma_y',
    'weit_d',
    'lg2_lgoff',
    'lg2_off',
    'dat_max',
    'rgain_off',
    'bgain_off',
    'gain_x',
    'gain_y',
]
struct_RK_Bayer2dnr_Fix_V23_s._fields_ = [
    ('bay3d_gain_en', uint8_t),
    ('lg2_mode', uint8_t),
    ('gauss_en', uint8_t),
    ('log_bypass', uint8_t),
    ('bayer_en', uint8_t),
    ('dgain', uint16_t * int(3)),
    ('pix_diff', uint16_t),
    ('diff_thld', uint16_t),
    ('softthld', uint16_t),
    ('bltflt_streng', uint16_t),
    ('reg_w1', uint16_t),
    ('sigma_x', uint16_t * int(16)),
    ('sigma_y', uint16_t * int(16)),
    ('weit_d', uint16_t * int(3)),
    ('lg2_lgoff', uint16_t),
    ('lg2_off', uint16_t),
    ('dat_max', uint32_t),
    ('rgain_off', uint16_t),
    ('bgain_off', uint16_t),
    ('gain_x', uint8_t * int(16)),
    ('gain_y', uint16_t * int(16)),
]

RK_Bayer2dnr_Fix_V23_t = struct_RK_Bayer2dnr_Fix_V23_s# /usr/include/rkaiq/algos/abayer2dnrV23/rk_aiq_types_abayer2dnr_hw_v23.h: 61

# /usr/include/rkaiq/algos/abayertnrV23/rk_aiq_types_abayertnr_hw_v23.h: 107
class struct_RK_Bayertnr_Fix_V23_s(Structure):
    pass

struct_RK_Bayertnr_Fix_V23_s.__slots__ = [
    'soft_st',
    'soft_mode',
    'bay3d_en',
    'bypass_en',
    'hibypass_en',
    'lobypass_en',
    'himed_bypass_en',
    'higaus_bypass_en',
    'hiabs_possel',
    'hichnsplit_en',
    'lomed_bypass_en',
    'logaus5_bypass_en',
    'logaus3_bypass_en',
    'glbpk_en',
    'loswitch_protect',
    'bwsaving_en',
    'softwgt',
    'hidif_th',
    'glbpk2',
    'hiwgt_opt_en',
    'hichncor_en',
    'bwopt_gain_dis',
    'lo4x8_en',
    'lo4x4_en',
    'hisig_ind_sel',
    'pksig_ind_sel',
    'iirwr_rnd_en',
    'curds_high_en',
    'higaus3_mode',
    'higaus5x5_en',
    'wgtmix_opt_en',
    'wgtmm_opt_en',
    'wgtmm_sel_en',
    'wgtlmt',
    'wgtratio',
    'sig0_x',
    'sig0_y',
    'sig1_x',
    'sig1_y',
    'sig2_y',
    'wgtmin',
    'hisigrat0',
    'hisigrat1',
    'hisigoff0',
    'hisigoff1',
    'losigoff',
    'losigrat',
    'rgain_off',
    'bgain_off',
    'siggaus0',
    'siggaus1',
    'siggaus2',
    'siggaus3',
]
struct_RK_Bayertnr_Fix_V23_s._fields_ = [
    ('soft_st', uint8_t),
    ('soft_mode', uint8_t),
    ('bay3d_en', uint8_t),
    ('bypass_en', uint8_t),
    ('hibypass_en', uint8_t),
    ('lobypass_en', uint8_t),
    ('himed_bypass_en', uint8_t),
    ('higaus_bypass_en', uint8_t),
    ('hiabs_possel', uint8_t),
    ('hichnsplit_en', uint8_t),
    ('lomed_bypass_en', uint8_t),
    ('logaus5_bypass_en', uint8_t),
    ('logaus3_bypass_en', uint8_t),
    ('glbpk_en', uint8_t),
    ('loswitch_protect', uint8_t),
    ('bwsaving_en', uint8_t),
    ('softwgt', uint16_t),
    ('hidif_th', uint16_t),
    ('glbpk2', uint32_t),
    ('hiwgt_opt_en', uint8_t),
    ('hichncor_en', uint8_t),
    ('bwopt_gain_dis', uint8_t),
    ('lo4x8_en', uint8_t),
    ('lo4x4_en', uint8_t),
    ('hisig_ind_sel', uint8_t),
    ('pksig_ind_sel', uint8_t),
    ('iirwr_rnd_en', uint8_t),
    ('curds_high_en', uint8_t),
    ('higaus3_mode', uint8_t),
    ('higaus5x5_en', uint8_t),
    ('wgtmix_opt_en', uint8_t),
    ('wgtmm_opt_en', uint8_t),
    ('wgtmm_sel_en', uint8_t),
    ('wgtlmt', uint16_t),
    ('wgtratio', uint16_t),
    ('sig0_x', uint16_t * int(16)),
    ('sig0_y', uint16_t * int(16)),
    ('sig1_x', uint16_t * int(16)),
    ('sig1_y', uint16_t * int(16)),
    ('sig2_y', uint16_t * int(16)),
    ('wgtmin', uint16_t),
    ('hisigrat0', uint16_t),
    ('hisigrat1', uint16_t),
    ('hisigoff0', uint16_t),
    ('hisigoff1', uint16_t),
    ('losigoff', uint16_t),
    ('losigrat', uint16_t),
    ('rgain_off', uint16_t),
    ('bgain_off', uint16_t),
    ('siggaus0', uint8_t),
    ('siggaus1', uint8_t),
    ('siggaus2', uint8_t),
    ('siggaus3', uint8_t),
]

RK_Bayertnr_Fix_V23_t = struct_RK_Bayertnr_Fix_V23_s# /usr/include/rkaiq/algos/abayertnrV23/rk_aiq_types_abayertnr_hw_v23.h: 107

# /usr/include/rkaiq/iq_parser_v2/ablc_uapi_head_v32.h: 33
class struct_AblcSelect_V32_s(Structure):
    pass

struct_AblcSelect_V32_s.__slots__ = [
    'enable',
    'blc_r',
    'blc_gr',
    'blc_gb',
    'blc_b',
]
struct_AblcSelect_V32_s._fields_ = [
    ('enable', c_bool),
    ('blc_r', c_float),
    ('blc_gr', c_float),
    ('blc_gb', c_float),
    ('blc_b', c_float),
]

AblcSelect_V32_t = struct_AblcSelect_V32_s# /usr/include/rkaiq/iq_parser_v2/ablc_uapi_head_v32.h: 33

# /usr/include/rkaiq/iq_parser_v2/ablc_uapi_head_v32.h: 42
class struct_AblcOBSelect_V32_s(Structure):
    pass

struct_AblcOBSelect_V32_s.__slots__ = [
    'enable',
    'ob_offset',
    'ob_predgain',
]
struct_AblcOBSelect_V32_s._fields_ = [
    ('enable', c_bool),
    ('ob_offset', c_float),
    ('ob_predgain', c_float),
]

AblcOBSelect_V32_t = struct_AblcOBSelect_V32_s# /usr/include/rkaiq/iq_parser_v2/ablc_uapi_head_v32.h: 42

# /usr/include/rkaiq/iq_parser_v2/ablc_uapi_head_v32.h: 81
class struct_AblcExpInfo_V32_s(Structure):
    pass

struct_AblcExpInfo_V32_s.__slots__ = [
    'hdr_mode',
    'snr_mode',
    'bayertnr_en',
    'arTime',
    'arAGain',
    'arDGain',
    'isp_dgain',
    'arIso',
    'isoLevelLow',
    'isoLevelHig',
]
struct_AblcExpInfo_V32_s._fields_ = [
    ('hdr_mode', c_int),
    ('snr_mode', c_int),
    ('bayertnr_en', c_int),
    ('arTime', c_float * int(3)),
    ('arAGain', c_float * int(3)),
    ('arDGain', c_float * int(3)),
    ('isp_dgain', c_float * int(3)),
    ('arIso', c_int * int(3)),
    ('isoLevelLow', c_int),
    ('isoLevelHig', c_int),
]

AblcExpInfo_V32_t = struct_AblcExpInfo_V32_s# /usr/include/rkaiq/iq_parser_v2/ablc_uapi_head_v32.h: 81

# /usr/include/rkaiq/iq_parser_v2/ablc_uapi_head_v32.h: 90
class struct_rk_aiq_blc_info_v32_s(Structure):
    pass

struct_rk_aiq_blc_info_v32_s.__slots__ = [
    'sync',
    'iso',
    'expo_info',
]
struct_rk_aiq_blc_info_v32_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('iso', c_int),
    ('expo_info', AblcExpInfo_V32_t),
]

rk_aiq_blc_info_v32_t = struct_rk_aiq_blc_info_v32_s# /usr/include/rkaiq/iq_parser_v2/ablc_uapi_head_v32.h: 90

enum_AblcOPMode_V32_e = c_int# /usr/include/rkaiq/algos/ablcV32/rk_aiq_types_ablc_algo_int_v32.h: 53

AblcOPMode_V32_t = enum_AblcOPMode_V32_e# /usr/include/rkaiq/algos/ablcV32/rk_aiq_types_ablc_algo_int_v32.h: 53

# /usr/include/rkaiq/algos/ablcV32/rk_aiq_types_ablc_algo_int_v32.h: 69
class struct_AblcParams_V32_s(Structure):
    pass

struct_AblcParams_V32_s.__slots__ = [
    'enable',
    'iso',
    'blc_r',
    'blc_gr',
    'blc_gb',
    'blc_b',
]
struct_AblcParams_V32_s._fields_ = [
    ('enable', c_bool),
    ('iso', c_float * int(13)),
    ('blc_r', c_float * int(13)),
    ('blc_gr', c_float * int(13)),
    ('blc_gb', c_float * int(13)),
    ('blc_b', c_float * int(13)),
]

AblcParams_V32_t = struct_AblcParams_V32_s# /usr/include/rkaiq/algos/ablcV32/rk_aiq_types_ablc_algo_int_v32.h: 69

# /usr/include/rkaiq/algos/ablcV32/rk_aiq_types_ablc_algo_int_v32.h: 85
class struct_AblcOBParams_V32_s(Structure):
    pass

struct_AblcOBParams_V32_s.__slots__ = [
    'enable',
    'iso',
    'ob_offset',
    'ob_predgain',
]
struct_AblcOBParams_V32_s._fields_ = [
    ('enable', c_bool),
    ('iso', c_float * int(13)),
    ('ob_offset', c_float * int(13)),
    ('ob_predgain', c_float * int(13)),
]

AblcOBParams_V32_t = struct_AblcOBParams_V32_s# /usr/include/rkaiq/algos/ablcV32/rk_aiq_types_ablc_algo_int_v32.h: 85

AblcManualAttr_V32_t = AblcSelect_V32_t# /usr/include/rkaiq/algos/ablcV32/rk_aiq_types_ablc_algo_int_v32.h: 88

AblcManualOBAttr_V32_t = AblcOBSelect_V32_t# /usr/include/rkaiq/algos/ablcV32/rk_aiq_types_ablc_algo_int_v32.h: 89

# /usr/include/rkaiq/algos/ablcV32/rk_aiq_types_ablc_algo_int_v32.h: 118
class struct_rk_aiq_blc_attrib_V32_s(Structure):
    pass

struct_rk_aiq_blc_attrib_V32_s.__slots__ = [
    'sync',
    'eMode',
    'stBlc0Auto',
    'stBlc1Auto',
    'stBlcOBAuto',
    'stBlc0Manual',
    'stBlc1Manual',
    'stBlcOBManual',
]
struct_rk_aiq_blc_attrib_V32_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('eMode', AblcOPMode_V32_t),
    ('stBlc0Auto', AblcParams_V32_t),
    ('stBlc1Auto', AblcParams_V32_t),
    ('stBlcOBAuto', AblcOBParams_V32_t),
    ('stBlc0Manual', AblcManualAttr_V32_t),
    ('stBlc1Manual', AblcManualAttr_V32_t),
    ('stBlcOBManual', AblcManualOBAttr_V32_t),
]

rk_aiq_blc_attrib_V32_t = struct_rk_aiq_blc_attrib_V32_s# /usr/include/rkaiq/algos/ablcV32/rk_aiq_types_ablc_algo_int_v32.h: 118

# /usr/include/rkaiq/algos/acnrV30/rk_aiq_types_acnr_hw_v30.h: 81
class struct_RK_CNR_Fix_V30_s(Structure):
    pass

struct_RK_CNR_Fix_V30_s.__slots__ = [
    'cnr_en',
    'exgain_bypass',
    'yuv422_mode',
    'thumb_mode',
    'bf3x3_wgt0_sel',
    'gain_iso',
    'global_gain_alpha',
    'global_gain',
    'thumb_sigma_c',
    'thumb_sigma_y',
    'thumb_bf_ratio',
    'lbf1x7_weit_d',
    'iir_uvgain',
    'iir_strength',
    'exp_shift',
    'wgt_slope',
    'chroma_ghost',
    'iir_uv_clip',
    'gaus_coe',
    'gaus_ratio',
    'bf_wgt_clip',
    'global_alpha',
    'uv_gain',
    'sigma_r',
    'bf_ratio',
    'adj_offset',
    'adj_ratio',
    'sigma_y',
    'iir_gain_alpha',
    'iir_global_gain',
]
struct_RK_CNR_Fix_V30_s._fields_ = [
    ('cnr_en', uint8_t),
    ('exgain_bypass', uint8_t),
    ('yuv422_mode', uint8_t),
    ('thumb_mode', uint8_t),
    ('bf3x3_wgt0_sel', uint8_t),
    ('gain_iso', uint8_t),
    ('global_gain_alpha', uint8_t),
    ('global_gain', uint16_t),
    ('thumb_sigma_c', uint16_t),
    ('thumb_sigma_y', uint16_t),
    ('thumb_bf_ratio', uint16_t),
    ('lbf1x7_weit_d', uint8_t * int(4)),
    ('iir_uvgain', uint8_t),
    ('iir_strength', uint8_t),
    ('exp_shift', uint8_t),
    ('wgt_slope', uint16_t),
    ('chroma_ghost', uint8_t),
    ('iir_uv_clip', uint8_t),
    ('gaus_coe', uint8_t * int(6)),
    ('gaus_ratio', uint16_t),
    ('bf_wgt_clip', uint8_t),
    ('global_alpha', uint16_t),
    ('uv_gain', uint8_t),
    ('sigma_r', uint16_t),
    ('bf_ratio', uint8_t),
    ('adj_offset', uint16_t),
    ('adj_ratio', uint16_t),
    ('sigma_y', uint8_t * int(13)),
    ('iir_gain_alpha', uint8_t),
    ('iir_global_gain', uint8_t),
]

RK_CNR_Fix_V30_t = struct_RK_CNR_Fix_V30_s# /usr/include/rkaiq/algos/acnrV30/rk_aiq_types_acnr_hw_v30.h: 81

# /usr/include/rkaiq/algos/asharpV33/rk_aiq_types_asharp_hw_v33.h: 90
class struct_RK_SHARP_Fix_V33_s(Structure):
    pass

struct_RK_SHARP_Fix_V33_s.__slots__ = [
    'sharp_noiseclip_mode',
    'sharp_radius_ds_mode',
    'sharp_exgain_bypass',
    'sharp_center_mode',
    'sharp_bypass',
    'sharp_en',
    'sharp_pbf_ratio',
    'sharp_gaus_ratio',
    'sharp_bf_ratio',
    'sharp_sharp_ratio',
    'sharp_luma_dx',
    'sharp_pbf_sigma_inv',
    'sharp_bf_sigma_inv',
    'sharp_pbf_sigma_shift',
    'sharp_bf_sigma_shift',
    'sharp_clip_hf',
    'sharp_pbf_coef',
    'sharp_bf_coef',
    'sharp_gaus_coef',
    'sharp_global_gain',
    'sharp_global_gain_alpha',
    'sharp_local_gainscale',
    'sharp_gain_adj',
    'sharp_center_wid',
    'sharp_center_het',
    'sharp_strength',
    'sharp_noise_sigma',
    'sharp_enhance_bit',
    'sharp_noise_strength',
    'sharp_clip_hf_mode',
    'sharp_add_mode',
    'sharp_ehf_th',
    'sharp_clip_neg',
]
struct_RK_SHARP_Fix_V33_s._fields_ = [
    ('sharp_noiseclip_mode', uint8_t),
    ('sharp_radius_ds_mode', uint8_t),
    ('sharp_exgain_bypass', uint8_t),
    ('sharp_center_mode', uint8_t),
    ('sharp_bypass', uint8_t),
    ('sharp_en', uint8_t),
    ('sharp_pbf_ratio', uint8_t),
    ('sharp_gaus_ratio', uint8_t),
    ('sharp_bf_ratio', uint8_t),
    ('sharp_sharp_ratio', uint8_t),
    ('sharp_luma_dx', uint8_t * int(7)),
    ('sharp_pbf_sigma_inv', uint16_t * int(8)),
    ('sharp_bf_sigma_inv', uint16_t * int(8)),
    ('sharp_pbf_sigma_shift', uint8_t),
    ('sharp_bf_sigma_shift', uint8_t),
    ('sharp_clip_hf', uint16_t * int(8)),
    ('sharp_pbf_coef', uint8_t * int(3)),
    ('sharp_bf_coef', uint8_t * int(3)),
    ('sharp_gaus_coef', uint8_t * int(6)),
    ('sharp_global_gain', uint16_t),
    ('sharp_global_gain_alpha', uint8_t),
    ('sharp_local_gainscale', uint8_t),
    ('sharp_gain_adj', uint16_t * int(14)),
    ('sharp_center_wid', uint16_t),
    ('sharp_center_het', uint16_t),
    ('sharp_strength', uint8_t * int(22)),
    ('sharp_noise_sigma', uint16_t),
    ('sharp_enhance_bit', uint8_t),
    ('sharp_noise_strength', uint16_t),
    ('sharp_clip_hf_mode', uint8_t),
    ('sharp_add_mode', uint8_t),
    ('sharp_ehf_th', uint16_t * int(8)),
    ('sharp_clip_neg', uint16_t * int(8)),
]

RK_SHARP_Fix_V33_t = struct_RK_SHARP_Fix_V33_s# /usr/include/rkaiq/algos/asharpV33/rk_aiq_types_asharp_hw_v33.h: 90

# /usr/include/rkaiq/algos/aynrV22/rk_aiq_types_aynr_hw_v22.h: 113
class struct_RK_YNR_Fix_V22_s(Structure):
    pass

struct_RK_YNR_Fix_V22_s.__slots__ = [
    'rnr_en',
    'gate_dis',
    'thumb_mix_cur_en',
    'global_gain_alpha',
    'global_gain',
    'flt1x1_bypass_sel',
    'nlm11x11_bypass',
    'flt1x1_bypass',
    'lgft3x3_bypass',
    'lbft5x5_bypass',
    'bft3x3_bypass',
    'ynr_en',
    'rnr_max_r',
    'local_gainscale',
    'rnr_center_coorh',
    'rnr_center_coorv',
    'localgain_adj_thresh',
    'localgain_adj',
    'low_bf_inv1',
    'low_bf_inv0',
    'low_peak_supress',
    'low_thred_adj',
    'low_dist_adj',
    'low_edge_adj_thresh',
    'low_bi_weight',
    'low_weight',
    'low_center_weight',
    'frame_full_size',
    'lbf_weight_thres',
    'low_gauss1_coeff2',
    'low_gauss1_coeff1',
    'low_gauss1_coeff0',
    'low_gauss2_coeff2',
    'low_gauss2_coeff1',
    'low_gauss2_coeff0',
    'luma_points_x',
    'lsgm_y',
    'rnr_strength',
    'nlm_min_sigma',
    'nlm_hi_gain_alpha',
    'nlm_hi_bf_scale',
    'nlm_coe_0',
    'nlm_coe_1',
    'nlm_coe_2',
    'nlm_coe_3',
    'nlm_coe_4',
    'nlm_coe_5',
    'nlm_center_weight',
    'nlm_weight_offset',
    'nlm_nr_weight',
]
struct_RK_YNR_Fix_V22_s._fields_ = [
    ('rnr_en', uint8_t),
    ('gate_dis', uint8_t),
    ('thumb_mix_cur_en', uint8_t),
    ('global_gain_alpha', uint8_t),
    ('global_gain', uint16_t),
    ('flt1x1_bypass_sel', uint8_t),
    ('nlm11x11_bypass', uint8_t),
    ('flt1x1_bypass', uint8_t),
    ('lgft3x3_bypass', uint8_t),
    ('lbft5x5_bypass', uint8_t),
    ('bft3x3_bypass', uint8_t),
    ('ynr_en', uint8_t),
    ('rnr_max_r', uint16_t),
    ('local_gainscale', uint16_t),
    ('rnr_center_coorh', uint16_t),
    ('rnr_center_coorv', uint16_t),
    ('localgain_adj_thresh', uint16_t),
    ('localgain_adj', uint16_t),
    ('low_bf_inv1', uint16_t),
    ('low_bf_inv0', uint16_t),
    ('low_peak_supress', uint16_t),
    ('low_thred_adj', uint16_t),
    ('low_dist_adj', uint16_t),
    ('low_edge_adj_thresh', uint16_t),
    ('low_bi_weight', uint16_t),
    ('low_weight', uint16_t),
    ('low_center_weight', uint16_t),
    ('frame_full_size', uint16_t),
    ('lbf_weight_thres', uint16_t),
    ('low_gauss1_coeff2', uint16_t),
    ('low_gauss1_coeff1', uint16_t),
    ('low_gauss1_coeff0', uint16_t),
    ('low_gauss2_coeff2', uint16_t),
    ('low_gauss2_coeff1', uint16_t),
    ('low_gauss2_coeff0', uint16_t),
    ('luma_points_x', uint16_t * int(17)),
    ('lsgm_y', uint16_t * int(17)),
    ('rnr_strength', uint8_t * int(17)),
    ('nlm_min_sigma', uint16_t),
    ('nlm_hi_gain_alpha', uint8_t),
    ('nlm_hi_bf_scale', uint16_t),
    ('nlm_coe_0', uint8_t),
    ('nlm_coe_1', uint8_t),
    ('nlm_coe_2', uint8_t),
    ('nlm_coe_3', uint8_t),
    ('nlm_coe_4', uint8_t),
    ('nlm_coe_5', uint8_t),
    ('nlm_center_weight', uint32_t),
    ('nlm_weight_offset', uint16_t),
    ('nlm_nr_weight', uint16_t),
]

RK_YNR_Fix_V22_t = struct_RK_YNR_Fix_V22_s# /usr/include/rkaiq/algos/aynrV22/rk_aiq_types_aynr_hw_v22.h: 113

# /usr/include/rkaiq/common/rk_aiq_types.h: 92
class struct_rk_aiq_color_info_s(Structure):
    pass

struct_rk_aiq_color_info_s.__slots__ = [
    'sensorGain',
    'awbGain',
]
struct_rk_aiq_color_info_s._fields_ = [
    ('sensorGain', c_float),
    ('awbGain', c_float * int(2)),
]

rk_aiq_color_info_t = struct_rk_aiq_color_info_s# /usr/include/rkaiq/common/rk_aiq_types.h: 92

enum_rk_aiq_af_sec_stat_e = c_int# /usr/include/rkaiq/common/rk_aiq_types.h: 120

rk_aiq_af_sec_stat_t = enum_rk_aiq_af_sec_stat_e# /usr/include/rkaiq/common/rk_aiq_types.h: 120

# /usr/include/rkaiq/common/rk_aiq_types.h: 367
class struct_anon_118(Structure):
    pass

struct_anon_118.__slots__ = [
    'start_ma',
    'rated_ma',
    'step_mode',
]
struct_anon_118._fields_ = [
    ('start_ma', c_int),
    ('rated_ma', c_int),
    ('step_mode', c_int),
]

rk_aiq_lens_vcmcfg = struct_anon_118# /usr/include/rkaiq/common/rk_aiq_types.h: 367

# /usr/include/rkaiq/common/rk_aiq_types.h: 374
class struct_anon_119(Structure):
    pass

struct_anon_119.__slots__ = [
    'stat',
    'search_num',
    'pos',
    'sharpness',
]
struct_anon_119._fields_ = [
    ('stat', rk_aiq_af_sec_stat_t),
    ('search_num', c_int32),
    ('pos', c_int32 * int(64)),
    ('sharpness', c_float * int(64)),
]

rk_aiq_af_sec_path_t = struct_anon_119# /usr/include/rkaiq/common/rk_aiq_types.h: 374

# /usr/include/rkaiq/common/rk_aiq_types.h: 379
class struct_anon_120(Structure):
    pass

struct_anon_120.__slots__ = [
    'stat',
    'final_pos',
]
struct_anon_120._fields_ = [
    ('stat', rk_aiq_af_sec_stat_t),
    ('final_pos', c_int32),
]

rk_aiq_af_result_t = struct_anon_120# /usr/include/rkaiq/common/rk_aiq_types.h: 379

# /usr/include/rkaiq/common/rk_aiq_types.h: 386
class struct_anon_121(Structure):
    pass

struct_anon_121.__slots__ = [
    'min_pos',
    'max_pos',
    'min_fl',
    'max_fl',
]
struct_anon_121._fields_ = [
    ('min_pos', c_int),
    ('max_pos', c_int),
    ('min_fl', c_float),
    ('max_fl', c_float),
]

rk_aiq_af_zoomrange = struct_anon_121# /usr/include/rkaiq/common/rk_aiq_types.h: 386

# /usr/include/rkaiq/common/rk_aiq_types.h: 391
class struct_anon_122(Structure):
    pass

struct_anon_122.__slots__ = [
    'min_pos',
    'max_pos',
]
struct_anon_122._fields_ = [
    ('min_pos', c_int),
    ('max_pos', c_int),
]

rk_aiq_af_focusrange = struct_anon_122# /usr/include/rkaiq/common/rk_aiq_types.h: 391

enum_rk_aiq_gray_mode_e = c_int# /usr/include/rkaiq/common/rk_aiq_types.h: 557

rk_aiq_gray_mode_t = enum_rk_aiq_gray_mode_e# /usr/include/rkaiq/common/rk_aiq_types.h: 557

# /usr/include/rkaiq/algos/a3dlut/rk_aiq_types_a3dlut_ext.h: 33
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

rk_aiq_lut3d_mlut3d_attrib_t = struct_rk_aiq_lut3d_mlut3d_attrib_s# /usr/include/rkaiq/algos/a3dlut/rk_aiq_types_a3dlut_ext.h: 33

enum_rk_aiq_lut3d_op_mode_s = c_int# /usr/include/rkaiq/algos/a3dlut/rk_aiq_types_a3dlut_ext.h: 40

rk_aiq_lut3d_op_mode_t = enum_rk_aiq_lut3d_op_mode_s# /usr/include/rkaiq/algos/a3dlut/rk_aiq_types_a3dlut_ext.h: 40

# /usr/include/rkaiq/algos/a3dlut/rk_aiq_types_a3dlut_ext.h: 50
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

rk_aiq_lut3d_attrib_t = struct_rk_aiq_lut3d_attrib_s# /usr/include/rkaiq/algos/a3dlut/rk_aiq_types_a3dlut_ext.h: 50

# /usr/include/rkaiq/algos/a3dlut/rk_aiq_types_a3dlut_ext.h: 64
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

rk_aiq_lut3d_querry_info_t = struct_rk_aiq_lut3d_querry_info_s# /usr/include/rkaiq/algos/a3dlut/rk_aiq_types_a3dlut_ext.h: 64

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_a3dlut.h: 24
class struct_rk_aiq_sys_ctx_s(Structure):
    pass

rk_aiq_sys_ctx_t = struct_rk_aiq_sys_ctx_s# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_a3dlut.h: 24

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_a3dlut.h: 31
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_a3dlut_SetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_a3dlut_SetAttrib = _lib.get("rk_aiq_user_api2_a3dlut_SetAttrib", "cdecl")
    rk_aiq_user_api2_a3dlut_SetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_lut3d_attrib_t)]
    rk_aiq_user_api2_a3dlut_SetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_a3dlut.h: 33
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_a3dlut_GetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_a3dlut_GetAttrib = _lib.get("rk_aiq_user_api2_a3dlut_GetAttrib", "cdecl")
    rk_aiq_user_api2_a3dlut_GetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_lut3d_attrib_t)]
    rk_aiq_user_api2_a3dlut_GetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_a3dlut.h: 35
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_a3dlut_Query3dlutInfo", "cdecl"):
        continue
    rk_aiq_user_api2_a3dlut_Query3dlutInfo = _lib.get("rk_aiq_user_api2_a3dlut_Query3dlutInfo", "cdecl")
    rk_aiq_user_api2_a3dlut_Query3dlutInfo.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_lut3d_querry_info_t)]
    rk_aiq_user_api2_a3dlut_Query3dlutInfo.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_a3dlut.h: 36
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_a3dlut_SetAcolorSwInfo", "cdecl"):
        continue
    rk_aiq_user_api2_a3dlut_SetAcolorSwInfo = _lib.get("rk_aiq_user_api2_a3dlut_SetAcolorSwInfo", "cdecl")
    rk_aiq_user_api2_a3dlut_SetAcolorSwInfo.argtypes = [POINTER(rk_aiq_sys_ctx_t), rk_aiq_color_info_t]
    rk_aiq_user_api2_a3dlut_SetAcolorSwInfo.restype = XCamReturn
    break

# /usr/include/rkaiq/iq_parser_v2/bayer2dnr_uapi_head_v2.h: 66
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

RK_Bayer2dnr_Params_V2_Select_t = struct_RK_Bayer2dnr_Params_V2_Select_s# /usr/include/rkaiq/iq_parser_v2/bayer2dnr_uapi_head_v2.h: 66

# /usr/include/rkaiq/iq_parser_v2/bayer2dnr_uapi_head_v2.h: 107
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

RK_Bayer2dnr_Params_V2_t = struct_RK_Bayer2dnr_Params_V2_s# /usr/include/rkaiq/iq_parser_v2/bayer2dnr_uapi_head_v2.h: 107

# /usr/include/rkaiq/iq_parser_v2/bayer2dnr_uapi_head_v2.h: 134
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

Abayer2dnr_ExpInfo_V2_t = struct_Abayer2dnr_ExpInfo_V2_s# /usr/include/rkaiq/iq_parser_v2/bayer2dnr_uapi_head_v2.h: 134

# /usr/include/rkaiq/iq_parser_v2/bayer2dnr_uapi_head_v2.h: 143
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

rk_aiq_bayer2dnr_info_v2_t = struct_rk_aiq_bayer2dnr_info_v2_s# /usr/include/rkaiq/iq_parser_v2/bayer2dnr_uapi_head_v2.h: 143

enum_Abayer2dnr_OPMode_V2_e = c_int# /usr/include/rkaiq/algos/abayer2dnr2/rk_aiq_types_abayer2dnr_algo_int_v2.h: 67

Abayer2dnr_OPMode_V2_t = enum_Abayer2dnr_OPMode_V2_e# /usr/include/rkaiq/algos/abayer2dnr2/rk_aiq_types_abayer2dnr_algo_int_v2.h: 67

# /usr/include/rkaiq/algos/abayer2dnr2/rk_aiq_types_abayer2dnr_algo_int_v2.h: 140
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

Abayer2dnr_Manual_Attr_V2_t = struct_Abayer2dnr_Manual_Attr_V2_s# /usr/include/rkaiq/algos/abayer2dnr2/rk_aiq_types_abayer2dnr_algo_int_v2.h: 140

# /usr/include/rkaiq/algos/abayer2dnr2/rk_aiq_types_abayer2dnr_algo_int_v2.h: 149
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

Abayer2dnr_Auto_Attr_V2_t = struct_Abayer2dnr_Auto_Attr_V2_s# /usr/include/rkaiq/algos/abayer2dnr2/rk_aiq_types_abayer2dnr_algo_int_v2.h: 149

# /usr/include/rkaiq/algos/abayer2dnr2/rk_aiq_types_abayer2dnr_algo_int_v2.h: 173
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

rk_aiq_bayer2dnr_attrib_v2_t = struct_rk_aiq_bayer2dnr_attrib_v2_s# /usr/include/rkaiq/algos/abayer2dnr2/rk_aiq_types_abayer2dnr_algo_int_v2.h: 173

# /usr/include/rkaiq/algos/abayer2dnr2/rk_aiq_types_abayer2dnr_algo_int_v2.h: 180
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

rk_aiq_bayer2dnr_strength_v2_t = struct_rk_aiq_bayer2dnr_strength_v2_s# /usr/include/rkaiq/algos/abayer2dnr2/rk_aiq_types_abayer2dnr_algo_int_v2.h: 180

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_abayer2dnr_v2.h: 31
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_abayer2dnrV2_SetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_abayer2dnrV2_SetAttrib = _lib.get("rk_aiq_user_api2_abayer2dnrV2_SetAttrib", "cdecl")
    rk_aiq_user_api2_abayer2dnrV2_SetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_bayer2dnr_attrib_v2_t)]
    rk_aiq_user_api2_abayer2dnrV2_SetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_abayer2dnr_v2.h: 34
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_abayer2dnrV2_GetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_abayer2dnrV2_GetAttrib = _lib.get("rk_aiq_user_api2_abayer2dnrV2_GetAttrib", "cdecl")
    rk_aiq_user_api2_abayer2dnrV2_GetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_bayer2dnr_attrib_v2_t)]
    rk_aiq_user_api2_abayer2dnrV2_GetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_abayer2dnr_v2.h: 37
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_abayer2dnrV2_SetStrength", "cdecl"):
        continue
    rk_aiq_user_api2_abayer2dnrV2_SetStrength = _lib.get("rk_aiq_user_api2_abayer2dnrV2_SetStrength", "cdecl")
    rk_aiq_user_api2_abayer2dnrV2_SetStrength.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_bayer2dnr_strength_v2_t)]
    rk_aiq_user_api2_abayer2dnrV2_SetStrength.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_abayer2dnr_v2.h: 40
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_abayer2dnrV2_GetStrength", "cdecl"):
        continue
    rk_aiq_user_api2_abayer2dnrV2_GetStrength = _lib.get("rk_aiq_user_api2_abayer2dnrV2_GetStrength", "cdecl")
    rk_aiq_user_api2_abayer2dnrV2_GetStrength.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_bayer2dnr_strength_v2_t)]
    rk_aiq_user_api2_abayer2dnrV2_GetStrength.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_abayer2dnr_v2.h: 43
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_abayer2dnrV2_GetInfo", "cdecl"):
        continue
    rk_aiq_user_api2_abayer2dnrV2_GetInfo = _lib.get("rk_aiq_user_api2_abayer2dnrV2_GetInfo", "cdecl")
    rk_aiq_user_api2_abayer2dnrV2_GetInfo.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_bayer2dnr_info_v2_t)]
    rk_aiq_user_api2_abayer2dnrV2_GetInfo.restype = XCamReturn
    break

# /usr/include/rkaiq/iq_parser_v2/bayer2dnr_uapi_head_v23.h: 88
class struct_RK_Bayer2dnr_Params_V23_Select_s(Structure):
    pass

struct_RK_Bayer2dnr_Params_V23_Select_s.__slots__ = [
    'enable',
    'lumapoint',
    'sigma',
    'gauss_guide',
    'filter_strength',
    'edgesofts',
    'ratio',
    'weight',
    'pix_diff',
    'diff_thld',
    'trans_mode',
    'trans_offset',
    'itrans_offset',
    'trans_datmax',
    'gain_bypass',
    'gain_scale',
    'gain_lumapoint',
    'gain_adj',
    'hdrdgain_ctrl_en',
    'hdr_dgain_scale_s',
    'hdr_dgain_scale_m',
]
struct_RK_Bayer2dnr_Params_V23_Select_s._fields_ = [
    ('enable', c_bool),
    ('lumapoint', c_int * int(16)),
    ('sigma', c_int * int(16)),
    ('gauss_guide', c_bool),
    ('filter_strength', c_float),
    ('edgesofts', c_float),
    ('ratio', c_float),
    ('weight', c_float),
    ('pix_diff', uint16_t),
    ('diff_thld', uint16_t),
    ('trans_mode', uint8_t),
    ('trans_offset', uint16_t),
    ('itrans_offset', uint16_t),
    ('trans_datmax', uint32_t),
    ('gain_bypass', c_bool),
    ('gain_scale', c_float),
    ('gain_lumapoint', uint16_t * int(16)),
    ('gain_adj', uint16_t * int(16)),
    ('hdrdgain_ctrl_en', c_bool),
    ('hdr_dgain_scale_s', c_float),
    ('hdr_dgain_scale_m', c_float),
]

RK_Bayer2dnrV23_Params_Select_t = struct_RK_Bayer2dnr_Params_V23_Select_s# /usr/include/rkaiq/iq_parser_v2/bayer2dnr_uapi_head_v23.h: 88

# /usr/include/rkaiq/iq_parser_v2/bayer2dnr_uapi_head_v23.h: 121
class struct_Abayer2dnr_ExpInfo_V23_s(Structure):
    pass

struct_Abayer2dnr_ExpInfo_V23_s.__slots__ = [
    'hdr_mode',
    'snr_mode',
    'gray_mode',
    'bayertnr_en',
    'arTime',
    'arAGain',
    'arDGain',
    'isp_dgain',
    'blc_ob_predgain',
    'arIso',
    'isoLevelLow',
    'isoLevelHig',
]
struct_Abayer2dnr_ExpInfo_V23_s._fields_ = [
    ('hdr_mode', c_int),
    ('snr_mode', c_int),
    ('gray_mode', c_int),
    ('bayertnr_en', c_int),
    ('arTime', c_float * int(3)),
    ('arAGain', c_float * int(3)),
    ('arDGain', c_float * int(3)),
    ('isp_dgain', c_float * int(3)),
    ('blc_ob_predgain', c_float),
    ('arIso', c_int * int(3)),
    ('isoLevelLow', c_int),
    ('isoLevelHig', c_int),
]

Abayer2dnr_ExpInfo_V23_t = struct_Abayer2dnr_ExpInfo_V23_s# /usr/include/rkaiq/iq_parser_v2/bayer2dnr_uapi_head_v23.h: 121

# /usr/include/rkaiq/iq_parser_v2/bayer2dnr_uapi_head_v23.h: 130
class struct_rk_aiq_bayer2dnr_info_v23_s(Structure):
    pass

struct_rk_aiq_bayer2dnr_info_v23_s.__slots__ = [
    'sync',
    'iso',
    'expo_info',
]
struct_rk_aiq_bayer2dnr_info_v23_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('iso', c_int),
    ('expo_info', Abayer2dnr_ExpInfo_V23_t),
]

rk_aiq_bayer2dnr_info_v23_t = struct_rk_aiq_bayer2dnr_info_v23_s# /usr/include/rkaiq/iq_parser_v2/bayer2dnr_uapi_head_v23.h: 130

enum_Abayer2dnr_OPMode_V23_e = c_int# /usr/include/rkaiq/algos/abayer2dnrV23/rk_aiq_types_abayer2dnr_algo_int_v23.h: 66

Abayer2dnr_OPMode_V23_t = enum_Abayer2dnr_OPMode_V23_e# /usr/include/rkaiq/algos/abayer2dnrV23/rk_aiq_types_abayer2dnr_algo_int_v23.h: 66

# /usr/include/rkaiq/algos/abayer2dnrV23/rk_aiq_types_abayer2dnr_algo_int_v23.h: 119
class struct_RK_Bayer2dnr_Params_V23_s(Structure):
    pass

struct_RK_Bayer2dnr_Params_V23_s.__slots__ = [
    'enable',
    'hdrdgain_ctrl_en',
    'iso',
    'Bayer2dnrParamsISO',
]
struct_RK_Bayer2dnr_Params_V23_s._fields_ = [
    ('enable', c_int),
    ('hdrdgain_ctrl_en', c_bool),
    ('iso', c_float * int(13)),
    ('Bayer2dnrParamsISO', RK_Bayer2dnrV23_Params_Select_t * int(13)),
]

RK_Bayer2dnr_Params_V23_t = struct_RK_Bayer2dnr_Params_V23_s# /usr/include/rkaiq/algos/abayer2dnrV23/rk_aiq_types_abayer2dnr_algo_int_v23.h: 119

# /usr/include/rkaiq/algos/abayer2dnrV23/rk_aiq_types_abayer2dnr_algo_int_v23.h: 127
class struct_Abayer2dnr_Manual_Attr_V23_s(Structure):
    pass

struct_Abayer2dnr_Manual_Attr_V23_s.__slots__ = [
    'st2DSelect',
    'st2Dfix',
]
struct_Abayer2dnr_Manual_Attr_V23_s._fields_ = [
    ('st2DSelect', RK_Bayer2dnrV23_Params_Select_t),
    ('st2Dfix', RK_Bayer2dnr_Fix_V23_t),
]

Abayer2dnr_Manual_Attr_V23_t = struct_Abayer2dnr_Manual_Attr_V23_s# /usr/include/rkaiq/algos/abayer2dnrV23/rk_aiq_types_abayer2dnr_algo_int_v23.h: 127

# /usr/include/rkaiq/algos/abayer2dnrV23/rk_aiq_types_abayer2dnr_algo_int_v23.h: 136
class struct_Abayer2dnr_Auto_Attr_V23_s(Structure):
    pass

struct_Abayer2dnr_Auto_Attr_V23_s.__slots__ = [
    'st2DParams',
    'st2DSelect',
]
struct_Abayer2dnr_Auto_Attr_V23_s._fields_ = [
    ('st2DParams', RK_Bayer2dnr_Params_V23_t),
    ('st2DSelect', RK_Bayer2dnrV23_Params_Select_t),
]

Abayer2dnr_Auto_Attr_V23_t = struct_Abayer2dnr_Auto_Attr_V23_s# /usr/include/rkaiq/algos/abayer2dnrV23/rk_aiq_types_abayer2dnr_algo_int_v23.h: 136

# /usr/include/rkaiq/algos/abayer2dnrV23/rk_aiq_types_abayer2dnr_algo_int_v23.h: 160
class struct_rk_aiq_bayer2dnr_attrib_v23_s(Structure):
    pass

struct_rk_aiq_bayer2dnr_attrib_v23_s.__slots__ = [
    'sync',
    'eMode',
    'stAuto',
    'stManual',
]
struct_rk_aiq_bayer2dnr_attrib_v23_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('eMode', Abayer2dnr_OPMode_V23_t),
    ('stAuto', Abayer2dnr_Auto_Attr_V23_t),
    ('stManual', Abayer2dnr_Manual_Attr_V23_t),
]

rk_aiq_bayer2dnr_attrib_v23_t = struct_rk_aiq_bayer2dnr_attrib_v23_s# /usr/include/rkaiq/algos/abayer2dnrV23/rk_aiq_types_abayer2dnr_algo_int_v23.h: 160

# /usr/include/rkaiq/algos/abayer2dnrV23/rk_aiq_types_abayer2dnr_algo_int_v23.h: 168
class struct_rk_aiq_bayer2dnr_strength_v23_s(Structure):
    pass

struct_rk_aiq_bayer2dnr_strength_v23_s.__slots__ = [
    'sync',
    'percent',
    'strength_enable',
]
struct_rk_aiq_bayer2dnr_strength_v23_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('percent', c_float),
    ('strength_enable', c_bool),
]

rk_aiq_bayer2dnr_strength_v23_t = struct_rk_aiq_bayer2dnr_strength_v23_s# /usr/include/rkaiq/algos/abayer2dnrV23/rk_aiq_types_abayer2dnr_algo_int_v23.h: 168

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_abayer2dnr_v23.h: 28
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_abayer2dnrV23_SetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_abayer2dnrV23_SetAttrib = _lib.get("rk_aiq_user_api2_abayer2dnrV23_SetAttrib", "cdecl")
    rk_aiq_user_api2_abayer2dnrV23_SetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_bayer2dnr_attrib_v23_t)]
    rk_aiq_user_api2_abayer2dnrV23_SetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_abayer2dnr_v23.h: 31
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_abayer2dnrV23_GetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_abayer2dnrV23_GetAttrib = _lib.get("rk_aiq_user_api2_abayer2dnrV23_GetAttrib", "cdecl")
    rk_aiq_user_api2_abayer2dnrV23_GetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_bayer2dnr_attrib_v23_t)]
    rk_aiq_user_api2_abayer2dnrV23_GetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_abayer2dnr_v23.h: 34
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_abayer2dnrV23_SetStrength", "cdecl"):
        continue
    rk_aiq_user_api2_abayer2dnrV23_SetStrength = _lib.get("rk_aiq_user_api2_abayer2dnrV23_SetStrength", "cdecl")
    rk_aiq_user_api2_abayer2dnrV23_SetStrength.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_bayer2dnr_strength_v23_t)]
    rk_aiq_user_api2_abayer2dnrV23_SetStrength.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_abayer2dnr_v23.h: 37
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_abayer2dnrV23_GetStrength", "cdecl"):
        continue
    rk_aiq_user_api2_abayer2dnrV23_GetStrength = _lib.get("rk_aiq_user_api2_abayer2dnrV23_GetStrength", "cdecl")
    rk_aiq_user_api2_abayer2dnrV23_GetStrength.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_bayer2dnr_strength_v23_t)]
    rk_aiq_user_api2_abayer2dnrV23_GetStrength.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_abayer2dnr_v23.h: 40
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_abayer2dnrV23_GetInfo", "cdecl"):
        continue
    rk_aiq_user_api2_abayer2dnrV23_GetInfo = _lib.get("rk_aiq_user_api2_abayer2dnrV23_GetInfo", "cdecl")
    rk_aiq_user_api2_abayer2dnrV23_GetInfo.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_bayer2dnr_info_v23_t)]
    rk_aiq_user_api2_abayer2dnrV23_GetInfo.restype = XCamReturn
    break

enum_Abayernr_OPMode_e = c_int# /usr/include/rkaiq/algos/arawnr2/rk_aiq_types_abayernr_algo_int_v2.h: 63

Abayernr_OPMode_t = enum_Abayernr_OPMode_e# /usr/include/rkaiq/algos/arawnr2/rk_aiq_types_abayernr_algo_int_v2.h: 63

# /usr/include/rkaiq/algos/arawnr2/rk_aiq_types_abayernr_algo_int_v2.h: 101
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

RK_Bayernr_2D_Params_V2_t = struct_RK_Bayernr_2D_Params_V2_s# /usr/include/rkaiq/algos/arawnr2/rk_aiq_types_abayernr_algo_int_v2.h: 101

# /usr/include/rkaiq/algos/arawnr2/rk_aiq_types_abayernr_algo_int_v2.h: 125
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

RK_Bayernr_2D_Params_V2_Select_t = struct_RK_Bayernr_2D_Params_V2_Select_s# /usr/include/rkaiq/algos/arawnr2/rk_aiq_types_abayernr_algo_int_v2.h: 125

# /usr/include/rkaiq/algos/arawnr2/rk_aiq_types_abayernr_algo_int_v2.h: 141
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

RK_Bayernr_3D_Params_V2_t = struct_RK_Bayernr_3D_Params_V2_s# /usr/include/rkaiq/algos/arawnr2/rk_aiq_types_abayernr_algo_int_v2.h: 141

# /usr/include/rkaiq/algos/arawnr2/rk_aiq_types_abayernr_algo_int_v2.h: 161
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

RK_Bayernr_3D_Params_V2_Select_t = struct_RK_Bayernr_3D_Params_V2_Select_s# /usr/include/rkaiq/algos/arawnr2/rk_aiq_types_abayernr_algo_int_v2.h: 161

# /usr/include/rkaiq/algos/arawnr2/rk_aiq_types_abayernr_algo_int_v2.h: 171
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

Abayernr_Manual_Attr_V2_t = struct_Abayernr_Manual_Attr_V2_s# /usr/include/rkaiq/algos/arawnr2/rk_aiq_types_abayernr_algo_int_v2.h: 171

# /usr/include/rkaiq/algos/arawnr2/rk_aiq_types_abayernr_algo_int_v2.h: 184
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

Abayernr_Auto_Attr_V2_t = struct_Abayernr_Auto_Attr_V2_s# /usr/include/rkaiq/algos/arawnr2/rk_aiq_types_abayernr_algo_int_v2.h: 184

# /usr/include/rkaiq/algos/arawnr2/rk_aiq_types_abayernr_algo_int_v2.h: 210
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

rk_aiq_bayernr_attrib_v2_t = struct_rk_aiq_bayernr_attrib_v2_s# /usr/include/rkaiq/algos/arawnr2/rk_aiq_types_abayernr_algo_int_v2.h: 210

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_abayernr_v2.h: 32
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_abayernrV2_SetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_abayernrV2_SetAttrib = _lib.get("rk_aiq_user_api2_abayernrV2_SetAttrib", "cdecl")
    rk_aiq_user_api2_abayernrV2_SetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_bayernr_attrib_v2_t)]
    rk_aiq_user_api2_abayernrV2_SetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_abayernr_v2.h: 35
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_abayernrV2_GetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_abayernrV2_GetAttrib = _lib.get("rk_aiq_user_api2_abayernrV2_GetAttrib", "cdecl")
    rk_aiq_user_api2_abayernrV2_GetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_bayernr_attrib_v2_t)]
    rk_aiq_user_api2_abayernrV2_GetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_abayernr_v2.h: 38
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_abayernrV2_SetSFStrength", "cdecl"):
        continue
    rk_aiq_user_api2_abayernrV2_SetSFStrength = _lib.get("rk_aiq_user_api2_abayernrV2_SetSFStrength", "cdecl")
    rk_aiq_user_api2_abayernrV2_SetSFStrength.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_float]
    rk_aiq_user_api2_abayernrV2_SetSFStrength.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_abayernr_v2.h: 41
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_abayernrV2_SetTFStrength", "cdecl"):
        continue
    rk_aiq_user_api2_abayernrV2_SetTFStrength = _lib.get("rk_aiq_user_api2_abayernrV2_SetTFStrength", "cdecl")
    rk_aiq_user_api2_abayernrV2_SetTFStrength.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_float]
    rk_aiq_user_api2_abayernrV2_SetTFStrength.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_abayernr_v2.h: 44
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_abayernrV2_GetSFStrength", "cdecl"):
        continue
    rk_aiq_user_api2_abayernrV2_GetSFStrength = _lib.get("rk_aiq_user_api2_abayernrV2_GetSFStrength", "cdecl")
    rk_aiq_user_api2_abayernrV2_GetSFStrength.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(c_float)]
    rk_aiq_user_api2_abayernrV2_GetSFStrength.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_abayernr_v2.h: 47
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_abayernrV2_GetTFStrength", "cdecl"):
        continue
    rk_aiq_user_api2_abayernrV2_GetTFStrength = _lib.get("rk_aiq_user_api2_abayernrV2_GetTFStrength", "cdecl")
    rk_aiq_user_api2_abayernrV2_GetTFStrength.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(c_float)]
    rk_aiq_user_api2_abayernrV2_GetTFStrength.restype = XCamReturn
    break

# /usr/include/rkaiq/iq_parser_v2/bayertnr_uapi_head_v2.h: 81
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

RK_Bayertnr_Params_V2_Select_t = struct_RK_Bayertnr_Params_V2_Select_s# /usr/include/rkaiq/iq_parser_v2/bayertnr_uapi_head_v2.h: 81

# /usr/include/rkaiq/iq_parser_v2/bayertnr_uapi_head_v2.h: 106
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

Abayertnr_ExpInfo_V2_t = struct_Abayertnr_ExpInfo_V2_s# /usr/include/rkaiq/iq_parser_v2/bayertnr_uapi_head_v2.h: 106

# /usr/include/rkaiq/iq_parser_v2/bayertnr_uapi_head_v2.h: 116
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

rk_aiq_bayertnr_info_v2_t = struct_rk_aiq_bayertnr_info_v2_s# /usr/include/rkaiq/iq_parser_v2/bayertnr_uapi_head_v2.h: 116

enum_Abayertnr_OPMode_V2_e = c_int# /usr/include/rkaiq/algos/abayertnr2/rk_aiq_types_abayertnr_algo_int_v2.h: 66

Abayertnr_OPMode_V2_t = enum_Abayertnr_OPMode_V2_e# /usr/include/rkaiq/algos/abayertnr2/rk_aiq_types_abayertnr_algo_int_v2.h: 66

# /usr/include/rkaiq/algos/abayertnr2/rk_aiq_types_abayertnr_algo_int_v2.h: 111
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

RK_Bayertnr_Params_V2_t = struct_RK_Bayertnr_Params_V2_s# /usr/include/rkaiq/algos/abayertnr2/rk_aiq_types_abayertnr_algo_int_v2.h: 111

# /usr/include/rkaiq/algos/abayertnr2/rk_aiq_types_abayertnr_algo_int_v2.h: 152
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

Abayertnr_Manual_Attr_V2_t = struct_Abayertnr_Manual_Attr_V2_s# /usr/include/rkaiq/algos/abayertnr2/rk_aiq_types_abayertnr_algo_int_v2.h: 152

# /usr/include/rkaiq/algos/abayertnr2/rk_aiq_types_abayertnr_algo_int_v2.h: 161
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

Abayertnr_Auto_Attr_V2_t = struct_Abayertnr_Auto_Attr_V2_s# /usr/include/rkaiq/algos/abayertnr2/rk_aiq_types_abayertnr_algo_int_v2.h: 161

# /usr/include/rkaiq/algos/abayertnr2/rk_aiq_types_abayertnr_algo_int_v2.h: 184
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

rk_aiq_bayertnr_attrib_v2_t = struct_rk_aiq_bayertnr_attrib_v2_s# /usr/include/rkaiq/algos/abayertnr2/rk_aiq_types_abayertnr_algo_int_v2.h: 184

# /usr/include/rkaiq/algos/abayertnr2/rk_aiq_types_abayertnr_algo_int_v2.h: 190
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

rk_aiq_bayertnr_strength_v2_t = struct_rk_aiq_bayertnr_strength_v2_s# /usr/include/rkaiq/algos/abayertnr2/rk_aiq_types_abayertnr_algo_int_v2.h: 190

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_abayertnr_v2.h: 31
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_abayertnrV2_SetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_abayertnrV2_SetAttrib = _lib.get("rk_aiq_user_api2_abayertnrV2_SetAttrib", "cdecl")
    rk_aiq_user_api2_abayertnrV2_SetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_bayertnr_attrib_v2_t)]
    rk_aiq_user_api2_abayertnrV2_SetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_abayertnr_v2.h: 34
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_abayertnrV2_GetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_abayertnrV2_GetAttrib = _lib.get("rk_aiq_user_api2_abayertnrV2_GetAttrib", "cdecl")
    rk_aiq_user_api2_abayertnrV2_GetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_bayertnr_attrib_v2_t)]
    rk_aiq_user_api2_abayertnrV2_GetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_abayertnr_v2.h: 37
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_abayertnrV2_SetStrength", "cdecl"):
        continue
    rk_aiq_user_api2_abayertnrV2_SetStrength = _lib.get("rk_aiq_user_api2_abayertnrV2_SetStrength", "cdecl")
    rk_aiq_user_api2_abayertnrV2_SetStrength.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_bayertnr_strength_v2_t)]
    rk_aiq_user_api2_abayertnrV2_SetStrength.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_abayertnr_v2.h: 40
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_abayertnrV2_GetStrength", "cdecl"):
        continue
    rk_aiq_user_api2_abayertnrV2_GetStrength = _lib.get("rk_aiq_user_api2_abayertnrV2_GetStrength", "cdecl")
    rk_aiq_user_api2_abayertnrV2_GetStrength.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_bayertnr_strength_v2_t)]
    rk_aiq_user_api2_abayertnrV2_GetStrength.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_abayertnr_v2.h: 43
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_abayertnrV2_GetInfo", "cdecl"):
        continue
    rk_aiq_user_api2_abayertnrV2_GetInfo = _lib.get("rk_aiq_user_api2_abayertnrV2_GetInfo", "cdecl")
    rk_aiq_user_api2_abayertnrV2_GetInfo.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_bayertnr_info_v2_t)]
    rk_aiq_user_api2_abayertnrV2_GetInfo.restype = XCamReturn
    break

# /usr/include/rkaiq/iq_parser_v2/bayertnr_uapi_head_v23.h: 134
class struct_RK_Bayertnr_Params_V23_Select_s(Structure):
    pass

struct_RK_Bayertnr_Params_V23_Select_s.__slots__ = [
    'enable',
    'lumapoint',
    'sigma',
    'lumapoint2',
    'lo_sigma',
    'hi_sigma',
    'thumbds_w',
    'thumbds_h',
    'lo_enable',
    'hi_enable',
    'lo_med_en',
    'lo_gsbay_en',
    'lo_gslum_en',
    'hi_med_en',
    'hi_gslum_en',
    'trans_en',
    'wgt_use_mode',
    'wgt_mge_mode',
    'hi_guass',
    'kl_guass',
    'global_pk_en',
    'global_pksq',
    'lo_filter_strength',
    'hi_filter_strength',
    'soft_threshold_ratio',
    'lo_clipwgt',
    'hi_wgt_comp',
    'hidif_th',
    'lo_filter_rat0',
    'lo_filter_thed0',
    'hi_filter_abs_ctrl',
    'hi_filter_filt_bay',
    'hi_filter_filt_avg',
    'hi_filter_filt_mode',
    'hi_filter_rat0',
    'hi_filter_thed0',
    'hi_filter_rat1',
    'hi_filter_thed1',
    'guass_guide_coeff0',
    'guass_guide_coeff1',
    'guass_guide_coeff2',
    'guass_guide_coeff3',
]
struct_RK_Bayertnr_Params_V23_Select_s._fields_ = [
    ('enable', c_bool),
    ('lumapoint', c_int * int(16)),
    ('sigma', c_int * int(16)),
    ('lumapoint2', c_int * int(16)),
    ('lo_sigma', c_int * int(16)),
    ('hi_sigma', c_int * int(16)),
    ('thumbds_w', uint8_t),
    ('thumbds_h', uint8_t),
    ('lo_enable', c_bool),
    ('hi_enable', c_bool),
    ('lo_med_en', c_bool),
    ('lo_gsbay_en', c_bool),
    ('lo_gslum_en', c_bool),
    ('hi_med_en', c_bool),
    ('hi_gslum_en', c_bool),
    ('trans_en', c_bool),
    ('wgt_use_mode', c_bool),
    ('wgt_mge_mode', c_bool),
    ('hi_guass', c_bool),
    ('kl_guass', c_bool),
    ('global_pk_en', c_bool),
    ('global_pksq', c_int),
    ('lo_filter_strength', c_float),
    ('hi_filter_strength', c_float),
    ('soft_threshold_ratio', c_float),
    ('lo_clipwgt', c_float),
    ('hi_wgt_comp', c_float),
    ('hidif_th', c_int),
    ('lo_filter_rat0', c_float),
    ('lo_filter_thed0', uint16_t),
    ('hi_filter_abs_ctrl', uint8_t),
    ('hi_filter_filt_bay', uint8_t),
    ('hi_filter_filt_avg', uint8_t),
    ('hi_filter_filt_mode', uint8_t),
    ('hi_filter_rat0', c_float),
    ('hi_filter_thed0', uint16_t),
    ('hi_filter_rat1', c_float),
    ('hi_filter_thed1', uint16_t),
    ('guass_guide_coeff0', uint8_t),
    ('guass_guide_coeff1', uint8_t),
    ('guass_guide_coeff2', uint8_t),
    ('guass_guide_coeff3', uint8_t),
]

RK_Bayertnr_Params_V23_Select_t = struct_RK_Bayertnr_Params_V23_Select_s# /usr/include/rkaiq/iq_parser_v2/bayertnr_uapi_head_v23.h: 134

# /usr/include/rkaiq/iq_parser_v2/bayertnr_uapi_head_v23.h: 256
class struct_RK_Bayertnr_Param_V23L_Select_s(Structure):
    pass

struct_RK_Bayertnr_Param_V23L_Select_s.__slots__ = [
    'enable',
    'lumapoint',
    'sigma',
    'lumapoint2',
    'lo_sigma',
    'hi_sigma',
    'thumbds_w',
    'thumbds_h',
    'lo_enable',
    'hi_enable',
    'lo_gsbay_en',
    'lo_gslum_en',
    'hi_gslum_en',
    'trans_en',
    'wgt_use_mode',
    'wgt_mge_mode',
    'global_pk_en',
    'global_pksq',
    'lo_filter_strength',
    'hi_filter_strength',
    'soft_threshold_ratio',
    'lo_clipwgt',
    'hi_wgt_comp',
    'hidif_th',
    'lo_filter_rat0',
    'lo_filter_thed0',
    'hi_filter_abs_ctrl',
    'wgtmm_opt_en',
    'wgtmm_sel_en',
    'wgtmin',
    'hi_filter_rat0',
    'hi_filter_thed0',
    'hi_filter_rat1',
    'hi_filter_thed1',
    'guass_guide_coeff0',
    'guass_guide_coeff1',
    'guass_guide_coeff2',
]
struct_RK_Bayertnr_Param_V23L_Select_s._fields_ = [
    ('enable', c_bool),
    ('lumapoint', c_int * int(16)),
    ('sigma', c_int * int(16)),
    ('lumapoint2', c_int * int(16)),
    ('lo_sigma', c_int * int(16)),
    ('hi_sigma', c_int * int(16)),
    ('thumbds_w', uint8_t),
    ('thumbds_h', uint8_t),
    ('lo_enable', c_bool),
    ('hi_enable', c_bool),
    ('lo_gsbay_en', c_bool),
    ('lo_gslum_en', c_bool),
    ('hi_gslum_en', c_bool),
    ('trans_en', c_bool),
    ('wgt_use_mode', c_bool),
    ('wgt_mge_mode', c_bool),
    ('global_pk_en', c_bool),
    ('global_pksq', c_int),
    ('lo_filter_strength', c_float),
    ('hi_filter_strength', c_float),
    ('soft_threshold_ratio', c_float),
    ('lo_clipwgt', c_float),
    ('hi_wgt_comp', c_float),
    ('hidif_th', c_int),
    ('lo_filter_rat0', c_float),
    ('lo_filter_thed0', uint16_t),
    ('hi_filter_abs_ctrl', uint8_t),
    ('wgtmm_opt_en', c_bool),
    ('wgtmm_sel_en', c_bool),
    ('wgtmin', c_float),
    ('hi_filter_rat0', c_float),
    ('hi_filter_thed0', uint16_t),
    ('hi_filter_rat1', c_float),
    ('hi_filter_thed1', uint16_t),
    ('guass_guide_coeff0', uint8_t),
    ('guass_guide_coeff1', uint8_t),
    ('guass_guide_coeff2', uint8_t),
]

RK_Bayertnr_Param_V23L_Select_t = struct_RK_Bayertnr_Param_V23L_Select_s# /usr/include/rkaiq/iq_parser_v2/bayertnr_uapi_head_v23.h: 256

# /usr/include/rkaiq/iq_parser_v2/bayertnr_uapi_head_v23.h: 283
class struct_Abayertnr_ExpInfo_V23_s(Structure):
    pass

struct_Abayertnr_ExpInfo_V23_s.__slots__ = [
    'hdr_mode',
    'snr_mode',
    'arTime',
    'arAGain',
    'arDGain',
    'isp_dgain',
    'blc_ob_predgain',
    'arIso',
    'isoLevelLow',
    'isoLevelHig',
]
struct_Abayertnr_ExpInfo_V23_s._fields_ = [
    ('hdr_mode', c_int),
    ('snr_mode', c_int),
    ('arTime', c_float * int(3)),
    ('arAGain', c_float * int(3)),
    ('arDGain', c_float * int(3)),
    ('isp_dgain', c_float * int(3)),
    ('blc_ob_predgain', c_float),
    ('arIso', c_int * int(3)),
    ('isoLevelLow', c_int),
    ('isoLevelHig', c_int),
]

Abayertnr_ExpInfo_V23_t = struct_Abayertnr_ExpInfo_V23_s# /usr/include/rkaiq/iq_parser_v2/bayertnr_uapi_head_v23.h: 283

# /usr/include/rkaiq/iq_parser_v2/bayertnr_uapi_head_v23.h: 292
class struct_rk_aiq_bayertnr_info_v23_s(Structure):
    pass

struct_rk_aiq_bayertnr_info_v23_s.__slots__ = [
    'sync',
    'iso',
    'expo_info',
]
struct_rk_aiq_bayertnr_info_v23_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('iso', c_int),
    ('expo_info', Abayertnr_ExpInfo_V23_t),
]

rk_aiq_bayertnr_info_v23_t = struct_rk_aiq_bayertnr_info_v23_s# /usr/include/rkaiq/iq_parser_v2/bayertnr_uapi_head_v23.h: 292

enum_Abayertnr_OPMode_V23_e = c_int# /usr/include/rkaiq/algos/abayertnrV23/rk_aiq_types_abayertnr_algo_int_v23.h: 67

Abayertnr_OPMode_V23_t = enum_Abayertnr_OPMode_V23_e# /usr/include/rkaiq/algos/abayertnrV23/rk_aiq_types_abayertnr_algo_int_v23.h: 67

# /usr/include/rkaiq/algos/abayertnrV23/rk_aiq_types_abayertnr_algo_int_v23.h: 148
class struct_RK_Bayertnr_Params_V23_s(Structure):
    pass

struct_RK_Bayertnr_Params_V23_s.__slots__ = [
    'enable',
    'iso',
    'bayertnrParamISO',
]
struct_RK_Bayertnr_Params_V23_s._fields_ = [
    ('enable', c_bool),
    ('iso', c_float * int(13)),
    ('bayertnrParamISO', RK_Bayertnr_Params_V23_Select_t * int(13)),
]

RK_Bayertnr_Params_V23_t = struct_RK_Bayertnr_Params_V23_s# /usr/include/rkaiq/algos/abayertnrV23/rk_aiq_types_abayertnr_algo_int_v23.h: 148

# /usr/include/rkaiq/algos/abayertnrV23/rk_aiq_types_abayertnr_algo_int_v23.h: 154
class struct_RK_Bayertnr_Params_V23L_s(Structure):
    pass

struct_RK_Bayertnr_Params_V23L_s.__slots__ = [
    'enable',
    'iso',
    'bayertnrParamISO',
]
struct_RK_Bayertnr_Params_V23L_s._fields_ = [
    ('enable', c_bool),
    ('iso', c_float * int(13)),
    ('bayertnrParamISO', RK_Bayertnr_Param_V23L_Select_t * int(13)),
]

RK_Bayertnr_Params_V23L_t = struct_RK_Bayertnr_Params_V23L_s# /usr/include/rkaiq/algos/abayertnrV23/rk_aiq_types_abayertnr_algo_int_v23.h: 154

# /usr/include/rkaiq/algos/abayertnrV23/rk_aiq_types_abayertnr_algo_int_v23.h: 161
class struct_Abayertnr_Manual_Attr_V23_s(Structure):
    pass

struct_Abayertnr_Manual_Attr_V23_s.__slots__ = [
    'st3DSelect',
    'st3DFix',
]
struct_Abayertnr_Manual_Attr_V23_s._fields_ = [
    ('st3DSelect', RK_Bayertnr_Params_V23_Select_t),
    ('st3DFix', RK_Bayertnr_Fix_V23_t),
]

Abayertnr_Manual_Attr_V23_t = struct_Abayertnr_Manual_Attr_V23_s# /usr/include/rkaiq/algos/abayertnrV23/rk_aiq_types_abayertnr_algo_int_v23.h: 161

# /usr/include/rkaiq/algos/abayertnrV23/rk_aiq_types_abayertnr_algo_int_v23.h: 167
class struct_Abayertnr_Manual_Attr_V23L_s(Structure):
    pass

struct_Abayertnr_Manual_Attr_V23L_s.__slots__ = [
    'st3DSelect',
    'st3DFix',
]
struct_Abayertnr_Manual_Attr_V23L_s._fields_ = [
    ('st3DSelect', RK_Bayertnr_Param_V23L_Select_t),
    ('st3DFix', RK_Bayertnr_Fix_V23_t),
]

Abayertnr_Manual_Attr_V23L_t = struct_Abayertnr_Manual_Attr_V23L_s# /usr/include/rkaiq/algos/abayertnrV23/rk_aiq_types_abayertnr_algo_int_v23.h: 167

# /usr/include/rkaiq/algos/abayertnrV23/rk_aiq_types_abayertnr_algo_int_v23.h: 174
class struct_Abayertnr_Auto_Attr_V23_s(Structure):
    pass

struct_Abayertnr_Auto_Attr_V23_s.__slots__ = [
    'st3DParams',
    'st3DSelect',
]
struct_Abayertnr_Auto_Attr_V23_s._fields_ = [
    ('st3DParams', RK_Bayertnr_Params_V23_t),
    ('st3DSelect', RK_Bayertnr_Params_V23_Select_t),
]

Abayertnr_Auto_Attr_V23_t = struct_Abayertnr_Auto_Attr_V23_s# /usr/include/rkaiq/algos/abayertnrV23/rk_aiq_types_abayertnr_algo_int_v23.h: 174

# /usr/include/rkaiq/algos/abayertnrV23/rk_aiq_types_abayertnr_algo_int_v23.h: 179
class struct_Abayertnr_Auto_Attr_V23L_s(Structure):
    pass

struct_Abayertnr_Auto_Attr_V23L_s.__slots__ = [
    'st3DParams',
    'st3DSelect',
]
struct_Abayertnr_Auto_Attr_V23L_s._fields_ = [
    ('st3DParams', RK_Bayertnr_Params_V23L_t),
    ('st3DSelect', RK_Bayertnr_Param_V23L_Select_t),
]

Abayertnr_Auto_Attr_V23L_t = struct_Abayertnr_Auto_Attr_V23L_s# /usr/include/rkaiq/algos/abayertnrV23/rk_aiq_types_abayertnr_algo_int_v23.h: 179

# /usr/include/rkaiq/algos/abayertnrV23/rk_aiq_types_abayertnr_algo_int_v23.h: 208
class struct_rk_aiq_bayertnr_attrib_v23_s(Structure):
    pass

struct_rk_aiq_bayertnr_attrib_v23_s.__slots__ = [
    'sync',
    'eMode',
    'stAuto',
    'stManual',
]
struct_rk_aiq_bayertnr_attrib_v23_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('eMode', Abayertnr_OPMode_V23_t),
    ('stAuto', Abayertnr_Auto_Attr_V23_t),
    ('stManual', Abayertnr_Manual_Attr_V23_t),
]

rk_aiq_bayertnr_attrib_v23_t = struct_rk_aiq_bayertnr_attrib_v23_s# /usr/include/rkaiq/algos/abayertnrV23/rk_aiq_types_abayertnr_algo_int_v23.h: 208

# /usr/include/rkaiq/algos/abayertnrV23/rk_aiq_types_abayertnr_algo_int_v23.h: 215
class struct_rk_aiq_bayertnr_attrib_v23L_s(Structure):
    pass

struct_rk_aiq_bayertnr_attrib_v23L_s.__slots__ = [
    'sync',
    'eMode',
    'stAuto',
    'stManual',
]
struct_rk_aiq_bayertnr_attrib_v23L_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('eMode', Abayertnr_OPMode_V23_t),
    ('stAuto', Abayertnr_Auto_Attr_V23L_t),
    ('stManual', Abayertnr_Manual_Attr_V23L_t),
]

rk_aiq_bayertnr_attrib_v23L_t = struct_rk_aiq_bayertnr_attrib_v23L_s# /usr/include/rkaiq/algos/abayertnrV23/rk_aiq_types_abayertnr_algo_int_v23.h: 215

# /usr/include/rkaiq/algos/abayertnrV23/rk_aiq_types_abayertnr_algo_int_v23.h: 221
class struct_rk_aiq_bayertnr_strength_v23_s(Structure):
    pass

struct_rk_aiq_bayertnr_strength_v23_s.__slots__ = [
    'sync',
    'percent',
    'strength_enable',
]
struct_rk_aiq_bayertnr_strength_v23_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('percent', c_float),
    ('strength_enable', c_bool),
]

rk_aiq_bayertnr_strength_v23_t = struct_rk_aiq_bayertnr_strength_v23_s# /usr/include/rkaiq/algos/abayertnrV23/rk_aiq_types_abayertnr_algo_int_v23.h: 221

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_abayertnr_v23.h: 28
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_abayertnrV23_SetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_abayertnrV23_SetAttrib = _lib.get("rk_aiq_user_api2_abayertnrV23_SetAttrib", "cdecl")
    rk_aiq_user_api2_abayertnrV23_SetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_bayertnr_attrib_v23_t)]
    rk_aiq_user_api2_abayertnrV23_SetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_abayertnr_v23.h: 31
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_abayertnrV23_GetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_abayertnrV23_GetAttrib = _lib.get("rk_aiq_user_api2_abayertnrV23_GetAttrib", "cdecl")
    rk_aiq_user_api2_abayertnrV23_GetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_bayertnr_attrib_v23_t)]
    rk_aiq_user_api2_abayertnrV23_GetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_abayertnr_v23.h: 33
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_abayertnrV23Lite_SetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_abayertnrV23Lite_SetAttrib = _lib.get("rk_aiq_user_api2_abayertnrV23Lite_SetAttrib", "cdecl")
    rk_aiq_user_api2_abayertnrV23Lite_SetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_bayertnr_attrib_v23L_t)]
    rk_aiq_user_api2_abayertnrV23Lite_SetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_abayertnr_v23.h: 36
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_abayertnrV23Lite_GetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_abayertnrV23Lite_GetAttrib = _lib.get("rk_aiq_user_api2_abayertnrV23Lite_GetAttrib", "cdecl")
    rk_aiq_user_api2_abayertnrV23Lite_GetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_bayertnr_attrib_v23L_t)]
    rk_aiq_user_api2_abayertnrV23Lite_GetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_abayertnr_v23.h: 39
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_abayertnrV23_SetStrength", "cdecl"):
        continue
    rk_aiq_user_api2_abayertnrV23_SetStrength = _lib.get("rk_aiq_user_api2_abayertnrV23_SetStrength", "cdecl")
    rk_aiq_user_api2_abayertnrV23_SetStrength.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_bayertnr_strength_v23_t)]
    rk_aiq_user_api2_abayertnrV23_SetStrength.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_abayertnr_v23.h: 43
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_abayertnrV23_GetStrength", "cdecl"):
        continue
    rk_aiq_user_api2_abayertnrV23_GetStrength = _lib.get("rk_aiq_user_api2_abayertnrV23_GetStrength", "cdecl")
    rk_aiq_user_api2_abayertnrV23_GetStrength.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_bayertnr_strength_v23_t)]
    rk_aiq_user_api2_abayertnrV23_GetStrength.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_abayertnr_v23.h: 47
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_abayertnrV23_GetInfo", "cdecl"):
        continue
    rk_aiq_user_api2_abayertnrV23_GetInfo = _lib.get("rk_aiq_user_api2_abayertnrV23_GetInfo", "cdecl")
    rk_aiq_user_api2_abayertnrV23_GetInfo.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_bayertnr_info_v23_t)]
    rk_aiq_user_api2_abayertnrV23_GetInfo.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_ablc.h: 31
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_ablc_SetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_ablc_SetAttrib = _lib.get("rk_aiq_user_api2_ablc_SetAttrib", "cdecl")
    rk_aiq_user_api2_ablc_SetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_blc_attrib_t)]
    rk_aiq_user_api2_ablc_SetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_ablc.h: 33
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_ablc_GetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_ablc_GetAttrib = _lib.get("rk_aiq_user_api2_ablc_GetAttrib", "cdecl")
    rk_aiq_user_api2_ablc_GetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_blc_attrib_t)]
    rk_aiq_user_api2_ablc_GetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_ablc.h: 35
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_ablc_GetInfo", "cdecl"):
        continue
    rk_aiq_user_api2_ablc_GetInfo = _lib.get("rk_aiq_user_api2_ablc_GetInfo", "cdecl")
    rk_aiq_user_api2_ablc_GetInfo.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_ablc_info_t)]
    rk_aiq_user_api2_ablc_GetInfo.restype = XCamReturn
    break

# /usr/include/rkaiq/iq_parser_v2/ccm_head.h: 45
class struct_CalibDbV2_Ccm_Gain_Sat_Curve_s(Structure):
    pass

struct_CalibDbV2_Ccm_Gain_Sat_Curve_s.__slots__ = [
    'gains',
    'sat',
]
struct_CalibDbV2_Ccm_Gain_Sat_Curve_s._fields_ = [
    ('gains', c_float * int(4)),
    ('sat', c_float * int(4)),
]

CalibDbV2_Ccm_Gain_Sat_Curve_t = struct_CalibDbV2_Ccm_Gain_Sat_Curve_s# /usr/include/rkaiq/iq_parser_v2/ccm_head.h: 45

# /usr/include/rkaiq/iq_parser_v2/ccm_head.h: 52
class struct_CalibDbV2_Ccm_Gain_Scale_s(Structure):
    pass

struct_CalibDbV2_Ccm_Gain_Scale_s.__slots__ = [
    'gain',
    'scale',
]
struct_CalibDbV2_Ccm_Gain_Scale_s._fields_ = [
    ('gain', c_float * int(9)),
    ('scale', c_float * int(9)),
]

CalibDbV2_Ccm_Gain_Scale_t = struct_CalibDbV2_Ccm_Gain_Scale_s# /usr/include/rkaiq/iq_parser_v2/ccm_head.h: 52

# /usr/include/rkaiq/iq_parser_v2/ccm_head.h: 90
class struct_CalibDbV2_Ccm_Luma_Ccm_s(Structure):
    pass

struct_CalibDbV2_Ccm_Luma_Ccm_s.__slots__ = [
    'rgb2y_para',
    'low_bound_pos_bit',
    'y_alpha_curve',
    'gain_alphaScale_curve',
]
struct_CalibDbV2_Ccm_Luma_Ccm_s._fields_ = [
    ('rgb2y_para', c_float * int(3)),
    ('low_bound_pos_bit', c_float),
    ('y_alpha_curve', c_float * int(17)),
    ('gain_alphaScale_curve', CalibDbV2_Ccm_Gain_Scale_t),
]

CalibDbV2_Ccm_Luma_Ccm_t = struct_CalibDbV2_Ccm_Luma_Ccm_s# /usr/include/rkaiq/iq_parser_v2/ccm_head.h: 90

# /usr/include/rkaiq/iq_parser_v2/ccm_head.h: 99
class struct_CalibDbV2_Ccm_Alp_Sym_Para_s(Structure):
    pass

struct_CalibDbV2_Ccm_Alp_Sym_Para_s.__slots__ = [
    'highy_adj_en',
    'bound_pos_bit',
    'y_alpha_curve',
]
struct_CalibDbV2_Ccm_Alp_Sym_Para_s._fields_ = [
    ('highy_adj_en', c_bool),
    ('bound_pos_bit', c_float),
    ('y_alpha_curve', c_float * int(17)),
]

CalibDbV2_Ccm_Alp_Sym_Para_t = struct_CalibDbV2_Ccm_Alp_Sym_Para_s# /usr/include/rkaiq/iq_parser_v2/ccm_head.h: 99

# /usr/include/rkaiq/iq_parser_v2/ccm_head.h: 110
class struct_CalibDbV2_Ccm_Alp_Asym_Para_s(Structure):
    pass

struct_CalibDbV2_Ccm_Alp_Asym_Para_s.__slots__ = [
    'bound_pos_bit',
    'right_pos_bit',
    'y_alpha_left_curve',
    'y_alpha_right_curve',
]
struct_CalibDbV2_Ccm_Alp_Asym_Para_s._fields_ = [
    ('bound_pos_bit', c_float),
    ('right_pos_bit', c_float),
    ('y_alpha_left_curve', c_float * int(9)),
    ('y_alpha_right_curve', c_float * int(9)),
]

CalibDbV2_Ccm_Alp_Asym_Para_t = struct_CalibDbV2_Ccm_Alp_Asym_Para_s# /usr/include/rkaiq/iq_parser_v2/ccm_head.h: 110

# /usr/include/rkaiq/iq_parser_v2/ccm_head.h: 123
class struct_CalibDbV2_Ccm_Luma_Ccm_V2_s(Structure):
    pass

struct_CalibDbV2_Ccm_Luma_Ccm_V2_s.__slots__ = [
    'rgb2y_para',
    'asym_enable',
    'y_alp_sym',
    'y_alp_asym',
    'gain_alphaScale_curve',
]
struct_CalibDbV2_Ccm_Luma_Ccm_V2_s._fields_ = [
    ('rgb2y_para', c_float * int(3)),
    ('asym_enable', c_bool),
    ('y_alp_sym', CalibDbV2_Ccm_Alp_Sym_Para_t),
    ('y_alp_asym', CalibDbV2_Ccm_Alp_Asym_Para_t),
    ('gain_alphaScale_curve', CalibDbV2_Ccm_Gain_Scale_t),
]

CalibDbV2_Ccm_Luma_Ccm_V2_t = struct_CalibDbV2_Ccm_Luma_Ccm_V2_s# /usr/include/rkaiq/iq_parser_v2/ccm_head.h: 123

# /usr/include/rkaiq/iq_parser_v2/ccm_head.h: 165
class struct_CalibDbV2_Ccm_Control_Para_s(Structure):
    pass

struct_CalibDbV2_Ccm_Control_Para_s.__slots__ = [
    'enable',
    'wbgain_tolerance',
    'gain_tolerance',
]
struct_CalibDbV2_Ccm_Control_Para_s._fields_ = [
    ('enable', c_bool),
    ('wbgain_tolerance', c_float),
    ('gain_tolerance', c_float),
]

CalibDbV2_Ccm_Control_Para_t = struct_CalibDbV2_Ccm_Control_Para_s# /usr/include/rkaiq/iq_parser_v2/ccm_head.h: 165

# /usr/include/rkaiq/iq_parser_v2/ccm_head.h: 174
class struct_CalibDbV2_Ccm_Enh_para_s(Structure):
    pass

struct_CalibDbV2_Ccm_Enh_para_s.__slots__ = [
    'gains',
    'enh_adj_en',
    'enh_rat_max',
]
struct_CalibDbV2_Ccm_Enh_para_s._fields_ = [
    ('gains', c_float * int(9)),
    ('enh_adj_en', c_ushort * int(9)),
    ('enh_rat_max', c_float * int(9)),
]

CalibDbV2_Ccm_Enh_para_t = struct_CalibDbV2_Ccm_Enh_para_s# /usr/include/rkaiq/iq_parser_v2/ccm_head.h: 174

# /usr/include/rkaiq/iq_parser_v2/ccm_head.h: 181
class struct_CalibDbV2_Ccm_Enhance_Para_s(Structure):
    pass

struct_CalibDbV2_Ccm_Enhance_Para_s.__slots__ = [
    'enh_ctl',
    'enh_rgb2y_para',
]
struct_CalibDbV2_Ccm_Enhance_Para_s._fields_ = [
    ('enh_ctl', CalibDbV2_Ccm_Enh_para_t),
    ('enh_rgb2y_para', c_ubyte * int(3)),
]

CalibDbV2_Ccm_Enhance_Para_t = struct_CalibDbV2_Ccm_Enhance_Para_s# /usr/include/rkaiq/iq_parser_v2/ccm_head.h: 181

# /usr/include/rkaiq/iq_parser_v2/ccm_uapi_head.h: 43
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

rk_aiq_ccm_mccm_attrib_t = struct_rk_aiq_ccm_mccm_attrib_s# /usr/include/rkaiq/iq_parser_v2/ccm_uapi_head.h: 43

# /usr/include/rkaiq/iq_parser_v2/ccm_uapi_head.h: 66
class struct_rk_aiq_ccm_mccm_attrib_v2_s(Structure):
    pass

struct_rk_aiq_ccm_mccm_attrib_v2_s.__slots__ = [
    'ccMatrix',
    'ccOffsets',
    'highy_adj_en',
    'asym_enable',
    'bound_pos_bit',
    'right_pos_bit',
    'y_alpha_curve',
    'enh_adj_en',
    'enh_rgb2y_para',
    'enh_rat_max',
]
struct_rk_aiq_ccm_mccm_attrib_v2_s._fields_ = [
    ('ccMatrix', c_float * int(9)),
    ('ccOffsets', c_float * int(3)),
    ('highy_adj_en', c_bool),
    ('asym_enable', c_bool),
    ('bound_pos_bit', c_float),
    ('right_pos_bit', c_float),
    ('y_alpha_curve', c_float * int(18)),
    ('enh_adj_en', c_ushort),
    ('enh_rgb2y_para', c_ubyte * int(3)),
    ('enh_rat_max', c_float),
]

rk_aiq_ccm_mccm_attrib_v2_t = struct_rk_aiq_ccm_mccm_attrib_v2_s# /usr/include/rkaiq/iq_parser_v2/ccm_uapi_head.h: 66

enum_rk_aiq_ccm_op_mode_s = c_int# /usr/include/rkaiq/iq_parser_v2/ccm_uapi_head.h: 73

rk_aiq_ccm_op_mode_t = enum_rk_aiq_ccm_op_mode_s# /usr/include/rkaiq/iq_parser_v2/ccm_uapi_head.h: 73

# /usr/include/rkaiq/iq_parser_v2/ccm_uapi_head.h: 96
class struct_rk_aiq_ccm_querry_info_s(Structure):
    pass

struct_rk_aiq_ccm_querry_info_s.__slots__ = [
    'ccm_en',
    'ccMatrix',
    'ccOffsets',
    'highy_adj_en',
    'asym_enable',
    'y_alpha_curve',
    'low_bound_pos_bit',
    'right_pos_bit',
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
    ('highy_adj_en', c_bool),
    ('asym_enable', c_bool),
    ('y_alpha_curve', c_float * int(18)),
    ('low_bound_pos_bit', c_float),
    ('right_pos_bit', c_float),
    ('color_inhibition_level', c_float),
    ('color_saturation_level', c_float),
    ('finalSat', c_float),
    ('ccmname1', c_char * int(25)),
    ('ccmname2', c_char * int(25)),
]

rk_aiq_ccm_querry_info_t = struct_rk_aiq_ccm_querry_info_s# /usr/include/rkaiq/iq_parser_v2/ccm_uapi_head.h: 96

# /usr/include/rkaiq/algos/accm/rk_aiq_types_accm_algo_int.h: 43
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

rk_aiq_ccm_color_inhibition_t = struct_rk_aiq_ccm_color_inhibition_s# /usr/include/rkaiq/algos/accm/rk_aiq_types_accm_algo_int.h: 43

# /usr/include/rkaiq/algos/accm/rk_aiq_types_accm_algo_int.h: 48
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

rk_aiq_ccm_color_saturation_t = struct_rk_aiq_ccm_color_saturation_s# /usr/include/rkaiq/algos/accm/rk_aiq_types_accm_algo_int.h: 48

# /usr/include/rkaiq/algos/accm/rk_aiq_types_accm_algo_int.h: 53
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

rk_aiq_ccm_accm_attrib_t = struct_rk_aiq_ccm_accm_attrib_s# /usr/include/rkaiq/algos/accm/rk_aiq_types_accm_algo_int.h: 53

# /usr/include/rkaiq/algos/accm/rk_aiq_types_accm_algo_int.h: 61
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

rk_aiq_ccm_attrib_t = struct_rk_aiq_ccm_attrib_s# /usr/include/rkaiq/algos/accm/rk_aiq_types_accm_algo_int.h: 61

# /usr/include/rkaiq/algos/accm/rk_aiq_types_accm_algo_int.h: 69
class struct_rk_aiq_ccm_v2_attrib_s(Structure):
    pass

struct_rk_aiq_ccm_v2_attrib_s.__slots__ = [
    'sync',
    'byPass',
    'mode',
    'stManual',
    'stAuto',
]
struct_rk_aiq_ccm_v2_attrib_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('byPass', c_bool),
    ('mode', rk_aiq_ccm_op_mode_t),
    ('stManual', rk_aiq_ccm_mccm_attrib_v2_t),
    ('stAuto', rk_aiq_ccm_accm_attrib_t),
]

rk_aiq_ccm_v2_attrib_t = struct_rk_aiq_ccm_v2_attrib_s# /usr/include/rkaiq/algos/accm/rk_aiq_types_accm_algo_int.h: 69

# /usr/include/rkaiq/algos/accm/rk_aiq_types_accm_algo_int.h: 81
class struct_rk_aiq_ccm_illucfg_s(Structure):
    pass

struct_rk_aiq_ccm_illucfg_s.__slots__ = [
    'name',
    'awbGain',
    'minDist',
    'matrixUsed',
    'matrixUsed_len',
    'gain_sat_curve',
]
struct_rk_aiq_ccm_illucfg_s._fields_ = [
    ('name', c_char * int(20)),
    ('awbGain', c_float * int(2)),
    ('minDist', c_float),
    ('matrixUsed', (c_char * int(25)) * int(5)),
    ('matrixUsed_len', c_int),
    ('gain_sat_curve', CalibDbV2_Ccm_Gain_Sat_Curve_t),
]

rk_aiq_ccm_illucfg_t = struct_rk_aiq_ccm_illucfg_s# /usr/include/rkaiq/algos/accm/rk_aiq_types_accm_algo_int.h: 81

# /usr/include/rkaiq/algos/accm/rk_aiq_types_accm_algo_int.h: 89
class struct_rk_aiq_ccm_matrixcfg_s(Structure):
    pass

struct_rk_aiq_ccm_matrixcfg_s.__slots__ = [
    'name',
    'illumination',
    'saturation',
    'ccMatrix',
    'ccOffsets',
]
struct_rk_aiq_ccm_matrixcfg_s._fields_ = [
    ('name', c_char * int(25)),
    ('illumination', c_char * int(20)),
    ('saturation', c_float),
    ('ccMatrix', c_float * int(9)),
    ('ccOffsets', c_float * int(3)),
]

rk_aiq_ccm_matrixcfg_t = struct_rk_aiq_ccm_matrixcfg_s# /usr/include/rkaiq/algos/accm/rk_aiq_types_accm_algo_int.h: 89

# /usr/include/rkaiq/algos/accm/rk_aiq_types_accm_algo_int.h: 99
class struct_rk_aiq_ccm_iqparam_attrib_s(Structure):
    pass

struct_rk_aiq_ccm_iqparam_attrib_s.__slots__ = [
    'control',
    'lumaCCM',
    'damp_enable',
    'aCcmCof',
    'aCcmCof_len',
    'matrixAll',
    'matrixAll_len',
]
struct_rk_aiq_ccm_iqparam_attrib_s._fields_ = [
    ('control', CalibDbV2_Ccm_Control_Para_t),
    ('lumaCCM', CalibDbV2_Ccm_Luma_Ccm_t),
    ('damp_enable', c_bool),
    ('aCcmCof', rk_aiq_ccm_illucfg_t * int(9)),
    ('aCcmCof_len', c_int),
    ('matrixAll', rk_aiq_ccm_matrixcfg_t * int((9 * 5))),
    ('matrixAll_len', c_int),
]

rk_aiq_ccm_iqparam_attrib_t = struct_rk_aiq_ccm_iqparam_attrib_s# /usr/include/rkaiq/algos/accm/rk_aiq_types_accm_algo_int.h: 99

# /usr/include/rkaiq/algos/accm/rk_aiq_types_accm_algo_int.h: 110
class struct_rk_aiq_ccm_v2_iqparam_attrib_s(Structure):
    pass

struct_rk_aiq_ccm_v2_iqparam_attrib_s.__slots__ = [
    'control',
    'lumaCCM',
    'enhCCM',
    'damp_enable',
    'aCcmCof',
    'aCcmCof_len',
    'matrixAll',
    'matrixAll_len',
]
struct_rk_aiq_ccm_v2_iqparam_attrib_s._fields_ = [
    ('control', CalibDbV2_Ccm_Control_Para_t),
    ('lumaCCM', CalibDbV2_Ccm_Luma_Ccm_V2_t),
    ('enhCCM', CalibDbV2_Ccm_Enhance_Para_t),
    ('damp_enable', c_bool),
    ('aCcmCof', rk_aiq_ccm_illucfg_t * int(9)),
    ('aCcmCof_len', c_int),
    ('matrixAll', rk_aiq_ccm_matrixcfg_t * int((9 * 5))),
    ('matrixAll_len', c_int),
]

rk_aiq_ccm_v2_iqparam_attrib_t = struct_rk_aiq_ccm_v2_iqparam_attrib_s# /usr/include/rkaiq/algos/accm/rk_aiq_types_accm_algo_int.h: 110

# /usr/include/rkaiq/algos/accm/rk_aiq_types_accm_algo_int.h: 115
class struct_rk_aiq_ccm_calib_attrib_s(Structure):
    pass

struct_rk_aiq_ccm_calib_attrib_s.__slots__ = [
    'sync',
    'iqparam',
]
struct_rk_aiq_ccm_calib_attrib_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('iqparam', rk_aiq_ccm_iqparam_attrib_t),
]

rk_aiq_ccm_calib_attrib_t = struct_rk_aiq_ccm_calib_attrib_s# /usr/include/rkaiq/algos/accm/rk_aiq_types_accm_algo_int.h: 115

# /usr/include/rkaiq/algos/accm/rk_aiq_types_accm_algo_int.h: 120
class struct_rk_aiq_ccm_v2_calib_attrib_s(Structure):
    pass

struct_rk_aiq_ccm_v2_calib_attrib_s.__slots__ = [
    'sync',
    'iqparam',
]
struct_rk_aiq_ccm_v2_calib_attrib_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('iqparam', rk_aiq_ccm_v2_iqparam_attrib_t),
]

rk_aiq_ccm_v2_calib_attrib_t = struct_rk_aiq_ccm_v2_calib_attrib_s# /usr/include/rkaiq/algos/accm/rk_aiq_types_accm_algo_int.h: 120

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_accm.h: 29
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_accm_SetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_accm_SetAttrib = _lib.get("rk_aiq_user_api2_accm_SetAttrib", "cdecl")
    rk_aiq_user_api2_accm_SetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_ccm_attrib_t)]
    rk_aiq_user_api2_accm_SetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_accm.h: 31
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_accm_GetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_accm_GetAttrib = _lib.get("rk_aiq_user_api2_accm_GetAttrib", "cdecl")
    rk_aiq_user_api2_accm_GetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_ccm_attrib_t)]
    rk_aiq_user_api2_accm_GetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_accm.h: 33
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_accm_SetIqParam", "cdecl"):
        continue
    rk_aiq_user_api2_accm_SetIqParam = _lib.get("rk_aiq_user_api2_accm_SetIqParam", "cdecl")
    rk_aiq_user_api2_accm_SetIqParam.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_ccm_calib_attrib_t)]
    rk_aiq_user_api2_accm_SetIqParam.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_accm.h: 35
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_accm_GetIqParam", "cdecl"):
        continue
    rk_aiq_user_api2_accm_GetIqParam = _lib.get("rk_aiq_user_api2_accm_GetIqParam", "cdecl")
    rk_aiq_user_api2_accm_GetIqParam.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_ccm_calib_attrib_t)]
    rk_aiq_user_api2_accm_GetIqParam.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_accm.h: 37
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_accm_v2_SetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_accm_v2_SetAttrib = _lib.get("rk_aiq_user_api2_accm_v2_SetAttrib", "cdecl")
    rk_aiq_user_api2_accm_v2_SetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_ccm_v2_attrib_t)]
    rk_aiq_user_api2_accm_v2_SetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_accm.h: 39
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_accm_v2_GetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_accm_v2_GetAttrib = _lib.get("rk_aiq_user_api2_accm_v2_GetAttrib", "cdecl")
    rk_aiq_user_api2_accm_v2_GetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_ccm_v2_attrib_t)]
    rk_aiq_user_api2_accm_v2_GetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_accm.h: 41
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_accm_v2_SetIqParam", "cdecl"):
        continue
    rk_aiq_user_api2_accm_v2_SetIqParam = _lib.get("rk_aiq_user_api2_accm_v2_SetIqParam", "cdecl")
    rk_aiq_user_api2_accm_v2_SetIqParam.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_ccm_v2_calib_attrib_t)]
    rk_aiq_user_api2_accm_v2_SetIqParam.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_accm.h: 43
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_accm_v2_GetIqParam", "cdecl"):
        continue
    rk_aiq_user_api2_accm_v2_GetIqParam = _lib.get("rk_aiq_user_api2_accm_v2_GetIqParam", "cdecl")
    rk_aiq_user_api2_accm_v2_GetIqParam.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_ccm_v2_calib_attrib_t)]
    rk_aiq_user_api2_accm_v2_GetIqParam.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_accm.h: 45
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_accm_QueryCcmInfo", "cdecl"):
        continue
    rk_aiq_user_api2_accm_QueryCcmInfo = _lib.get("rk_aiq_user_api2_accm_QueryCcmInfo", "cdecl")
    rk_aiq_user_api2_accm_QueryCcmInfo.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_ccm_querry_info_t)]
    rk_aiq_user_api2_accm_QueryCcmInfo.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_accm.h: 47
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_GetAcolorSwInfo", "cdecl"):
        continue
    rk_aiq_user_api2_GetAcolorSwInfo = _lib.get("rk_aiq_user_api2_GetAcolorSwInfo", "cdecl")
    rk_aiq_user_api2_GetAcolorSwInfo.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_color_info_t)]
    rk_aiq_user_api2_GetAcolorSwInfo.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_accm.h: 49
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_accm_SetAcolorSwInfo", "cdecl"):
        continue
    rk_aiq_user_api2_accm_SetAcolorSwInfo = _lib.get("rk_aiq_user_api2_accm_SetAcolorSwInfo", "cdecl")
    rk_aiq_user_api2_accm_SetAcolorSwInfo.argtypes = [POINTER(rk_aiq_sys_ctx_t), rk_aiq_color_info_t]
    rk_aiq_user_api2_accm_SetAcolorSwInfo.restype = XCamReturn
    break

enum_Acnr_OPMode_e = c_int# /usr/include/rkaiq/algos/acnr/rk_aiq_types_acnr_algo_int_v1.h: 90

Acnr_OPMode_t = enum_Acnr_OPMode_e# /usr/include/rkaiq/algos/acnr/rk_aiq_types_acnr_algo_int_v1.h: 90

# /usr/include/rkaiq/algos/acnr/rk_aiq_types_acnr_algo_int_v1.h: 153
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

RK_CNR_Params_V1_t = struct_RK_CNR_Params_V1_s# /usr/include/rkaiq/algos/acnr/rk_aiq_types_acnr_algo_int_v1.h: 153

# /usr/include/rkaiq/algos/acnr/rk_aiq_types_acnr_algo_int_v1.h: 199
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

RK_CNR_Params_V1_Select_t = struct_RK_CNR_Params_V1_Select_s# /usr/include/rkaiq/algos/acnr/rk_aiq_types_acnr_algo_int_v1.h: 199

# /usr/include/rkaiq/algos/acnr/rk_aiq_types_acnr_algo_int_v1.h: 207
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

Acnr_Manual_Attr_V1_t = struct_Acnr_Manual_Attr_V1_s# /usr/include/rkaiq/algos/acnr/rk_aiq_types_acnr_algo_int_v1.h: 207

# /usr/include/rkaiq/algos/acnr/rk_aiq_types_acnr_algo_int_v1.h: 217
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

Acnr_Auto_Attr_V1_t = struct_Acnr_Auto_Attr_V1_s# /usr/include/rkaiq/algos/acnr/rk_aiq_types_acnr_algo_int_v1.h: 217

# /usr/include/rkaiq/algos/acnr/rk_aiq_types_acnr_algo_int_v1.h: 242
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

rk_aiq_cnr_attrib_v1_t = struct_rk_aiq_cnr_attrib_v1_s# /usr/include/rkaiq/algos/acnr/rk_aiq_types_acnr_algo_int_v1.h: 242

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_acnr_v1.h: 31
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_acnrV1_SetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_acnrV1_SetAttrib = _lib.get("rk_aiq_user_api2_acnrV1_SetAttrib", "cdecl")
    rk_aiq_user_api2_acnrV1_SetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_cnr_attrib_v1_t)]
    rk_aiq_user_api2_acnrV1_SetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_acnr_v1.h: 34
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_acnrV1_GetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_acnrV1_GetAttrib = _lib.get("rk_aiq_user_api2_acnrV1_GetAttrib", "cdecl")
    rk_aiq_user_api2_acnrV1_GetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_cnr_attrib_v1_t)]
    rk_aiq_user_api2_acnrV1_GetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_acnr_v1.h: 37
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_acnrV1_SetStrength", "cdecl"):
        continue
    rk_aiq_user_api2_acnrV1_SetStrength = _lib.get("rk_aiq_user_api2_acnrV1_SetStrength", "cdecl")
    rk_aiq_user_api2_acnrV1_SetStrength.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_float]
    rk_aiq_user_api2_acnrV1_SetStrength.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_acnr_v1.h: 40
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_acnrV1_GetStrength", "cdecl"):
        continue
    rk_aiq_user_api2_acnrV1_GetStrength = _lib.get("rk_aiq_user_api2_acnrV1_GetStrength", "cdecl")
    rk_aiq_user_api2_acnrV1_GetStrength.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(c_float)]
    rk_aiq_user_api2_acnrV1_GetStrength.restype = XCamReturn
    break

# /usr/include/rkaiq/iq_parser_v2/cnr_uapi_head_v2.h: 88
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

RK_CNR_Params_V2_Select_t = struct_RK_CNR_Params_V2_Select_s# /usr/include/rkaiq/iq_parser_v2/cnr_uapi_head_v2.h: 88

# /usr/include/rkaiq/iq_parser_v2/cnr_uapi_head_v2.h: 116
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

AcnrV2_ExpInfo_t = struct_AcnrV2_ExpInfo_s# /usr/include/rkaiq/iq_parser_v2/cnr_uapi_head_v2.h: 116

# /usr/include/rkaiq/iq_parser_v2/cnr_uapi_head_v2.h: 125
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

rk_aiq_cnr_info_v2_t = struct_rk_aiq_cnr_info_v2_s# /usr/include/rkaiq/iq_parser_v2/cnr_uapi_head_v2.h: 125

enum_AcnrV2_OPMode_e = c_int# /usr/include/rkaiq/algos/acnr2/rk_aiq_types_acnr_algo_int_v2.h: 100

AcnrV2_OPMode_t = enum_AcnrV2_OPMode_e# /usr/include/rkaiq/algos/acnr2/rk_aiq_types_acnr_algo_int_v2.h: 100

# /usr/include/rkaiq/algos/acnr2/rk_aiq_types_acnr_algo_int_v2.h: 158
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

RK_CNR_Params_V2_t = struct_RK_CNR_Params_V2_s# /usr/include/rkaiq/algos/acnr2/rk_aiq_types_acnr_algo_int_v2.h: 158

# /usr/include/rkaiq/algos/acnr2/rk_aiq_types_acnr_algo_int_v2.h: 220
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

Acnr_Manual_Attr_V2_t = struct_Acnr_Manual_Attr_V2_s# /usr/include/rkaiq/algos/acnr2/rk_aiq_types_acnr_algo_int_v2.h: 220

# /usr/include/rkaiq/algos/acnr2/rk_aiq_types_acnr_algo_int_v2.h: 229
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

Acnr_Auto_Attr_V2_t = struct_Acnr_Auto_Attr_V2_s# /usr/include/rkaiq/algos/acnr2/rk_aiq_types_acnr_algo_int_v2.h: 229

# /usr/include/rkaiq/algos/acnr2/rk_aiq_types_acnr_algo_int_v2.h: 255
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

rk_aiq_cnr_attrib_v2_t = struct_rk_aiq_cnr_attrib_v2_s# /usr/include/rkaiq/algos/acnr2/rk_aiq_types_acnr_algo_int_v2.h: 255

# /usr/include/rkaiq/algos/acnr2/rk_aiq_types_acnr_algo_int_v2.h: 262
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

rk_aiq_cnr_strength_v2_t = struct_rk_aiq_cnr_strength_v2_s# /usr/include/rkaiq/algos/acnr2/rk_aiq_types_acnr_algo_int_v2.h: 262

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_acnr_v2.h: 31
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_acnrV2_SetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_acnrV2_SetAttrib = _lib.get("rk_aiq_user_api2_acnrV2_SetAttrib", "cdecl")
    rk_aiq_user_api2_acnrV2_SetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_cnr_attrib_v2_t)]
    rk_aiq_user_api2_acnrV2_SetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_acnr_v2.h: 34
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_acnrV2_GetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_acnrV2_GetAttrib = _lib.get("rk_aiq_user_api2_acnrV2_GetAttrib", "cdecl")
    rk_aiq_user_api2_acnrV2_GetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_cnr_attrib_v2_t)]
    rk_aiq_user_api2_acnrV2_GetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_acnr_v2.h: 37
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_acnrV2_SetStrength", "cdecl"):
        continue
    rk_aiq_user_api2_acnrV2_SetStrength = _lib.get("rk_aiq_user_api2_acnrV2_SetStrength", "cdecl")
    rk_aiq_user_api2_acnrV2_SetStrength.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_cnr_strength_v2_t)]
    rk_aiq_user_api2_acnrV2_SetStrength.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_acnr_v2.h: 40
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_acnrV2_GetStrength", "cdecl"):
        continue
    rk_aiq_user_api2_acnrV2_GetStrength = _lib.get("rk_aiq_user_api2_acnrV2_GetStrength", "cdecl")
    rk_aiq_user_api2_acnrV2_GetStrength.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_cnr_strength_v2_t)]
    rk_aiq_user_api2_acnrV2_GetStrength.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_acnr_v2.h: 43
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_acnrV2_GetInfo", "cdecl"):
        continue
    rk_aiq_user_api2_acnrV2_GetInfo = _lib.get("rk_aiq_user_api2_acnrV2_GetInfo", "cdecl")
    rk_aiq_user_api2_acnrV2_GetInfo.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_cnr_info_v2_t)]
    rk_aiq_user_api2_acnrV2_GetInfo.restype = XCamReturn
    break

# /usr/include/rkaiq/iq_parser_v2/cnr_uapi_head_v30.h: 104
class struct_RK_CNR_Params_V30_Select_s(Structure):
    pass

struct_RK_CNR_Params_V30_Select_s.__slots__ = [
    'enable',
    'down_scale_x',
    'down_scale_y',
    'thumb_sigma',
    'thumb_bf_ratio',
    'chroma_filter_strength',
    'chroma_filter_wgt_clip',
    'anti_chroma_ghost',
    'chroma_filter_uv_gain',
    'wgt_slope',
    'gaus_ratio',
    'bf_sigmaR',
    'bf_uvgain',
    'bf_ratio',
    'hbf_wgt_clip',
    'bf_wgt0_sel',
    'global_alpha',
    'saturation_adj_offset',
    'saturation_adj_ratio',
    'global_gain',
    'global_gain_alpha',
    'local_gain_scale',
    'global_gain_thumb',
    'global_gain_alpha_thumb',
    'gain_adj_strength_ratio',
    'thumb_filter_wgt_coeff',
    'gaus_coeff',
]
struct_RK_CNR_Params_V30_Select_s._fields_ = [
    ('enable', c_bool),
    ('down_scale_x', uint8_t),
    ('down_scale_y', uint8_t),
    ('thumb_sigma', c_float),
    ('thumb_bf_ratio', c_float),
    ('chroma_filter_strength', c_float),
    ('chroma_filter_wgt_clip', c_float),
    ('anti_chroma_ghost', c_float),
    ('chroma_filter_uv_gain', c_float),
    ('wgt_slope', c_float),
    ('gaus_ratio', c_float),
    ('bf_sigmaR', c_float),
    ('bf_uvgain', c_float),
    ('bf_ratio', c_float),
    ('hbf_wgt_clip', c_float),
    ('bf_wgt0_sel', c_bool),
    ('global_alpha', c_float),
    ('saturation_adj_offset', c_float),
    ('saturation_adj_ratio', c_float),
    ('global_gain', c_float),
    ('global_gain_alpha', c_float),
    ('local_gain_scale', c_float),
    ('global_gain_thumb', c_float),
    ('global_gain_alpha_thumb', c_float),
    ('gain_adj_strength_ratio', c_float * int(13)),
    ('thumb_filter_wgt_coeff', c_float * int(4)),
    ('gaus_coeff', c_float * int(6)),
]

RK_CNR_Params_V30_Select_t = struct_RK_CNR_Params_V30_Select_s# /usr/include/rkaiq/iq_parser_v2/cnr_uapi_head_v30.h: 104

# /usr/include/rkaiq/iq_parser_v2/cnr_uapi_head_v30.h: 135
class struct_AcnrV30_ExpInfo_s(Structure):
    pass

struct_AcnrV30_ExpInfo_s.__slots__ = [
    'hdr_mode',
    'snr_mode',
    'arTime',
    'arAGain',
    'arDGain',
    'isp_dgain',
    'blc_ob_predgain',
    'arIso',
    'isoLevelLow',
    'isoLevelHig',
    'rawWidth',
    'rawHeight',
]
struct_AcnrV30_ExpInfo_s._fields_ = [
    ('hdr_mode', c_int),
    ('snr_mode', c_int),
    ('arTime', c_float * int(3)),
    ('arAGain', c_float * int(3)),
    ('arDGain', c_float * int(3)),
    ('isp_dgain', c_float * int(3)),
    ('blc_ob_predgain', c_float),
    ('arIso', c_int * int(3)),
    ('isoLevelLow', c_int),
    ('isoLevelHig', c_int),
    ('rawWidth', c_int),
    ('rawHeight', c_int),
]

AcnrV30_ExpInfo_t = struct_AcnrV30_ExpInfo_s# /usr/include/rkaiq/iq_parser_v2/cnr_uapi_head_v30.h: 135

# /usr/include/rkaiq/iq_parser_v2/cnr_uapi_head_v30.h: 144
class struct_rk_aiq_cnr_info_v30_s(Structure):
    pass

struct_rk_aiq_cnr_info_v30_s.__slots__ = [
    'sync',
    'iso',
    'expo_info',
]
struct_rk_aiq_cnr_info_v30_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('iso', c_int),
    ('expo_info', AcnrV30_ExpInfo_t),
]

rk_aiq_cnr_info_v30_t = struct_rk_aiq_cnr_info_v30_s# /usr/include/rkaiq/iq_parser_v2/cnr_uapi_head_v30.h: 144

enum_AcnrV30_OPMode_e = c_int# /usr/include/rkaiq/algos/acnrV30/rk_aiq_types_acnr_algo_int_v30.h: 111

AcnrV30_OPMode_t = enum_AcnrV30_OPMode_e# /usr/include/rkaiq/algos/acnrV30/rk_aiq_types_acnr_algo_int_v30.h: 111

# /usr/include/rkaiq/algos/acnrV30/rk_aiq_types_acnr_algo_int_v30.h: 175
class struct_RK_CNR_Params_V30_s(Structure):
    pass

struct_RK_CNR_Params_V30_s.__slots__ = [
    'enable',
    'iso',
    'CnrParamsISO',
]
struct_RK_CNR_Params_V30_s._fields_ = [
    ('enable', c_int),
    ('iso', c_float * int(13)),
    ('CnrParamsISO', RK_CNR_Params_V30_Select_t * int(13)),
]

RK_CNR_Params_V30_t = struct_RK_CNR_Params_V30_s# /usr/include/rkaiq/algos/acnrV30/rk_aiq_types_acnr_algo_int_v30.h: 175

# /usr/include/rkaiq/algos/acnrV30/rk_aiq_types_acnr_algo_int_v30.h: 184
class struct_Acnr_Manual_Attr_V30_s(Structure):
    pass

struct_Acnr_Manual_Attr_V30_s.__slots__ = [
    'stSelect',
    'stFix',
]
struct_Acnr_Manual_Attr_V30_s._fields_ = [
    ('stSelect', RK_CNR_Params_V30_Select_t),
    ('stFix', RK_CNR_Fix_V30_t),
]

Acnr_Manual_Attr_V30_t = struct_Acnr_Manual_Attr_V30_s# /usr/include/rkaiq/algos/acnrV30/rk_aiq_types_acnr_algo_int_v30.h: 184

# /usr/include/rkaiq/algos/acnrV30/rk_aiq_types_acnr_algo_int_v30.h: 193
class struct_Acnr_Auto_Attr_V30_s(Structure):
    pass

struct_Acnr_Auto_Attr_V30_s.__slots__ = [
    'stParams',
    'stSelect',
]
struct_Acnr_Auto_Attr_V30_s._fields_ = [
    ('stParams', RK_CNR_Params_V30_t),
    ('stSelect', RK_CNR_Params_V30_Select_t),
]

Acnr_Auto_Attr_V30_t = struct_Acnr_Auto_Attr_V30_s# /usr/include/rkaiq/algos/acnrV30/rk_aiq_types_acnr_algo_int_v30.h: 193

# /usr/include/rkaiq/algos/acnrV30/rk_aiq_types_acnr_algo_int_v30.h: 218
class struct_rk_aiq_cnr_attrib_v30_s(Structure):
    pass

struct_rk_aiq_cnr_attrib_v30_s.__slots__ = [
    'sync',
    'eMode',
    'stAuto',
    'stManual',
]
struct_rk_aiq_cnr_attrib_v30_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('eMode', AcnrV30_OPMode_t),
    ('stAuto', Acnr_Auto_Attr_V30_t),
    ('stManual', Acnr_Manual_Attr_V30_t),
]

rk_aiq_cnr_attrib_v30_t = struct_rk_aiq_cnr_attrib_v30_s# /usr/include/rkaiq/algos/acnrV30/rk_aiq_types_acnr_algo_int_v30.h: 218

# /usr/include/rkaiq/algos/acnrV30/rk_aiq_types_acnr_algo_int_v30.h: 225
class struct_rk_aiq_cnr_strength_v30_s(Structure):
    pass

struct_rk_aiq_cnr_strength_v30_s.__slots__ = [
    'sync',
    'percent',
    'strength_enable',
]
struct_rk_aiq_cnr_strength_v30_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('percent', c_float),
    ('strength_enable', c_bool),
]

rk_aiq_cnr_strength_v30_t = struct_rk_aiq_cnr_strength_v30_s# /usr/include/rkaiq/algos/acnrV30/rk_aiq_types_acnr_algo_int_v30.h: 225

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_acnr_v30.h: 28
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_acnrV30_SetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_acnrV30_SetAttrib = _lib.get("rk_aiq_user_api2_acnrV30_SetAttrib", "cdecl")
    rk_aiq_user_api2_acnrV30_SetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_cnr_attrib_v30_t)]
    rk_aiq_user_api2_acnrV30_SetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_acnr_v30.h: 31
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_acnrV30_GetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_acnrV30_GetAttrib = _lib.get("rk_aiq_user_api2_acnrV30_GetAttrib", "cdecl")
    rk_aiq_user_api2_acnrV30_GetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_cnr_attrib_v30_t)]
    rk_aiq_user_api2_acnrV30_GetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_acnr_v30.h: 34
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_acnrV30_SetStrength", "cdecl"):
        continue
    rk_aiq_user_api2_acnrV30_SetStrength = _lib.get("rk_aiq_user_api2_acnrV30_SetStrength", "cdecl")
    rk_aiq_user_api2_acnrV30_SetStrength.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_cnr_strength_v30_t)]
    rk_aiq_user_api2_acnrV30_SetStrength.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_acnr_v30.h: 37
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_acnrV30_GetStrength", "cdecl"):
        continue
    rk_aiq_user_api2_acnrV30_GetStrength = _lib.get("rk_aiq_user_api2_acnrV30_GetStrength", "cdecl")
    rk_aiq_user_api2_acnrV30_GetStrength.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_cnr_strength_v30_t)]
    rk_aiq_user_api2_acnrV30_GetStrength.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_acnr_v30.h: 40
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_acnrV30_GetInfo", "cdecl"):
        continue
    rk_aiq_user_api2_acnrV30_GetInfo = _lib.get("rk_aiq_user_api2_acnrV30_GetInfo", "cdecl")
    rk_aiq_user_api2_acnrV30_GetInfo.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_cnr_info_v30_t)]
    rk_aiq_user_api2_acnrV30_GetInfo.restype = XCamReturn
    break

# /usr/include/rkaiq/iq_parser_v2/acp_uapi_head.h: 35
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

acp_attrib_t = struct_acp_attrib_s# /usr/include/rkaiq/iq_parser_v2/acp_uapi_head.h: 35

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_acp.h: 30
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_acp_SetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_acp_SetAttrib = _lib.get("rk_aiq_user_api2_acp_SetAttrib", "cdecl")
    rk_aiq_user_api2_acp_SetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(acp_attrib_t)]
    rk_aiq_user_api2_acp_SetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_acp.h: 32
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_acp_GetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_acp_GetAttrib = _lib.get("rk_aiq_user_api2_acp_GetAttrib", "cdecl")
    rk_aiq_user_api2_acp_GetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(acp_attrib_t)]
    rk_aiq_user_api2_acp_GetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/iq_parser_v2/debayer_head.h: 90
class struct_CalibDbV2_Debayer_GInterp_s(Structure):
    pass

struct_CalibDbV2_Debayer_GInterp_s.__slots__ = [
    'iso',
    'debayer_clip_en',
    'debayer_gain_offset',
    'debayer_max_ratio',
]
struct_CalibDbV2_Debayer_GInterp_s._fields_ = [
    ('iso', c_float * int(13)),
    ('debayer_clip_en', c_ubyte * int(13)),
    ('debayer_gain_offset', c_ushort * int(13)),
    ('debayer_max_ratio', c_ubyte * int(13)),
]

CalibDbV2_Debayer_GInterp_t = struct_CalibDbV2_Debayer_GInterp_s# /usr/include/rkaiq/iq_parser_v2/debayer_head.h: 90

# /usr/include/rkaiq/iq_parser_v2/debayer_head.h: 112
class struct_CalibDbV2_Debayer_GDirectWgt_s(Structure):
    pass

struct_CalibDbV2_Debayer_GDirectWgt_s.__slots__ = [
    'iso',
    'debayer_hf_offset',
    'debayer_thed0',
    'debayer_thed1',
    'debayer_dist_scale',
    'debayer_select_thed',
]
struct_CalibDbV2_Debayer_GDirectWgt_s._fields_ = [
    ('iso', c_float * int(13)),
    ('debayer_hf_offset', c_ushort * int(13)),
    ('debayer_thed0', c_ubyte * int(13)),
    ('debayer_thed1', c_ubyte * int(13)),
    ('debayer_dist_scale', c_ubyte * int(13)),
    ('debayer_select_thed', c_ubyte * int(13)),
]

CalibDbV2_Debayer_GDirectWgt_t = struct_CalibDbV2_Debayer_GDirectWgt_s# /usr/include/rkaiq/iq_parser_v2/debayer_head.h: 112

# /usr/include/rkaiq/iq_parser_v2/debayer_head.h: 124
class struct_CalibDbV2_Debayer_GFilter_s(Structure):
    pass

struct_CalibDbV2_Debayer_GFilter_s.__slots__ = [
    'iso',
    'debayer_gfilter_en',
    'debayer_gfilter_offset',
]
struct_CalibDbV2_Debayer_GFilter_s._fields_ = [
    ('iso', c_float * int(13)),
    ('debayer_gfilter_en', c_ubyte * int(13)),
    ('debayer_gfilter_offset', c_ushort * int(13)),
]

CalibDbV2_Debayer_GFilter_t = struct_CalibDbV2_Debayer_GFilter_s# /usr/include/rkaiq/iq_parser_v2/debayer_head.h: 124

# /usr/include/rkaiq/iq_parser_v2/debayer_head.h: 179
class struct_CalibDbV2_Debayer_CFilter_s(Structure):
    pass

struct_CalibDbV2_Debayer_CFilter_s.__slots__ = [
    'iso',
    'debayer_cfilter_en',
    'debayer_loggd_offset',
    'debayer_cfilter_str',
    'debayer_wet_clip',
    'debayer_wet_ghost',
    'debayer_wgtslope',
    'debayer_bf_sgm',
    'debayer_bf_clip',
    'debayer_bf_curwgt',
    'debayer_loghf_offset',
    'debayer_alpha_offset',
    'debayer_alpha_scale',
    'debayer_edge_offset',
    'debayer_edge_scale',
]
struct_CalibDbV2_Debayer_CFilter_s._fields_ = [
    ('iso', c_float * int(13)),
    ('debayer_cfilter_en', c_ubyte * int(13)),
    ('debayer_loggd_offset', c_ushort * int(13)),
    ('debayer_cfilter_str', c_float * int(13)),
    ('debayer_wet_clip', c_float * int(13)),
    ('debayer_wet_ghost', c_float * int(13)),
    ('debayer_wgtslope', c_float * int(13)),
    ('debayer_bf_sgm', c_float * int(13)),
    ('debayer_bf_clip', c_ubyte * int(13)),
    ('debayer_bf_curwgt', c_ubyte * int(13)),
    ('debayer_loghf_offset', c_ushort * int(13)),
    ('debayer_alpha_offset', c_ushort * int(13)),
    ('debayer_alpha_scale', c_float * int(13)),
    ('debayer_edge_offset', c_ushort * int(13)),
    ('debayer_edge_scale', c_float * int(13)),
]

CalibDbV2_Debayer_CFilter_t = struct_CalibDbV2_Debayer_CFilter_s# /usr/include/rkaiq/iq_parser_v2/debayer_head.h: 179

# /usr/include/rkaiq/iq_parser_v2/debayer_head.h: 213
class struct_CalibDbV2_Debayer_Tuning_s(Structure):
    pass

struct_CalibDbV2_Debayer_Tuning_s.__slots__ = [
    'debayer_en',
    'lowfreq_filter1',
    'highfreq_filter2',
    'c_alpha_gaus_coe',
    'c_guid_gaus_coe',
    'c_ce_gaus_coe',
    'g_interp',
    'g_drctwgt',
    'g_filter',
    'c_filter',
]
struct_CalibDbV2_Debayer_Tuning_s._fields_ = [
    ('debayer_en', c_bool),
    ('lowfreq_filter1', c_int * int(4)),
    ('highfreq_filter2', c_int * int(4)),
    ('c_alpha_gaus_coe', c_int * int(3)),
    ('c_guid_gaus_coe', c_int * int(3)),
    ('c_ce_gaus_coe', c_int * int(3)),
    ('g_interp', CalibDbV2_Debayer_GInterp_t),
    ('g_drctwgt', CalibDbV2_Debayer_GDirectWgt_t),
    ('g_filter', CalibDbV2_Debayer_GFilter_t),
    ('c_filter', CalibDbV2_Debayer_CFilter_t),
]

CalibDbV2_Debayer_Tuning_t = struct_CalibDbV2_Debayer_Tuning_s# /usr/include/rkaiq/iq_parser_v2/debayer_head.h: 213

# /usr/include/rkaiq/iq_parser_v2/debayer_head.h: 241
class struct_CalibDbV2_Debayer_Tuning_Lite_s(Structure):
    pass

struct_CalibDbV2_Debayer_Tuning_Lite_s.__slots__ = [
    'debayer_en',
    'lowfreq_filter1',
    'highfreq_filter2',
    'g_interp',
    'g_drctwgt',
    'g_filter',
]
struct_CalibDbV2_Debayer_Tuning_Lite_s._fields_ = [
    ('debayer_en', c_bool),
    ('lowfreq_filter1', c_int * int(4)),
    ('highfreq_filter2', c_int * int(4)),
    ('g_interp', CalibDbV2_Debayer_GInterp_t),
    ('g_drctwgt', CalibDbV2_Debayer_GDirectWgt_t),
    ('g_filter', CalibDbV2_Debayer_GFilter_t),
]

CalibDbV2_Debayer_Tuning_Lite_t = struct_CalibDbV2_Debayer_Tuning_Lite_s# /usr/include/rkaiq/iq_parser_v2/debayer_head.h: 241

enum_rk_aiq_debayer_op_mode_e = c_int# /usr/include/rkaiq/algos/adebayer/rk_aiq_types_adebayer_algo_int.h: 13

rk_aiq_debayer_op_mode_t = enum_rk_aiq_debayer_op_mode_e# /usr/include/rkaiq/algos/adebayer/rk_aiq_types_adebayer_algo_int.h: 13

# /usr/include/rkaiq/algos/adebayer/rk_aiq_types_adebayer_algo_int.h: 38
class struct_AdebayerSeletedParamV1_s(Structure):
    pass

struct_AdebayerSeletedParamV1_s.__slots__ = [
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
struct_AdebayerSeletedParamV1_s._fields_ = [
    ('filter1', c_int8 * int(5)),
    ('filter2', c_int8 * int(5)),
    ('gain_offset', uint8_t),
    ('sharp_strength', uint8_t),
    ('hf_offset', uint8_t),
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

AdebayerSeletedParamV1_t = struct_AdebayerSeletedParamV1_s# /usr/include/rkaiq/algos/adebayer/rk_aiq_types_adebayer_algo_int.h: 38

# /usr/include/rkaiq/algos/adebayer/rk_aiq_types_adebayer_algo_int.h: 87
class struct_AdebayerSeletedParamV2_s(Structure):
    pass

struct_AdebayerSeletedParamV2_s.__slots__ = [
    'debayer_en',
    'lowfreq_filter1',
    'highfreq_filter2',
    'c_alpha_gaus_coe',
    'c_guid_gaus_coe',
    'c_ce_gaus_coe',
    'debayer_clip_en',
    'debayer_gain_offset',
    'debayer_max_ratio',
    'debayer_hf_offset',
    'debayer_thed0',
    'debayer_thed1',
    'debayer_dist_scale',
    'debayer_select_thed',
    'debayer_gfilter_en',
    'debayer_gfilter_offset',
    'debayer_cfilter_en',
    'debayer_loggd_offset',
    'debayer_cfilter_str',
    'debayer_wet_clip',
    'debayer_wet_ghost',
    'debayer_wgtslope',
    'debayer_bf_sgm',
    'debayer_bf_clip',
    'debayer_bf_curwgt',
    'debayer_loghf_offset',
    'debayer_alpha_offset',
    'debayer_alpha_scale',
    'debayer_edge_offset',
    'debayer_edge_scale',
]
struct_AdebayerSeletedParamV2_s._fields_ = [
    ('debayer_en', c_bool),
    ('lowfreq_filter1', c_int * int(4)),
    ('highfreq_filter2', c_int * int(4)),
    ('c_alpha_gaus_coe', c_int * int(3)),
    ('c_guid_gaus_coe', c_int * int(3)),
    ('c_ce_gaus_coe', c_int * int(3)),
    ('debayer_clip_en', c_ubyte),
    ('debayer_gain_offset', c_ushort),
    ('debayer_max_ratio', c_ubyte),
    ('debayer_hf_offset', c_ushort),
    ('debayer_thed0', c_ubyte),
    ('debayer_thed1', c_ubyte),
    ('debayer_dist_scale', c_ubyte),
    ('debayer_select_thed', c_ubyte),
    ('debayer_gfilter_en', c_ubyte),
    ('debayer_gfilter_offset', c_ushort),
    ('debayer_cfilter_en', c_ubyte),
    ('debayer_loggd_offset', c_ushort),
    ('debayer_cfilter_str', c_float),
    ('debayer_wet_clip', c_float),
    ('debayer_wet_ghost', c_float),
    ('debayer_wgtslope', c_float),
    ('debayer_bf_sgm', c_float),
    ('debayer_bf_clip', c_ubyte),
    ('debayer_bf_curwgt', c_ubyte),
    ('debayer_loghf_offset', c_ushort),
    ('debayer_alpha_offset', c_ushort),
    ('debayer_alpha_scale', c_float),
    ('debayer_edge_offset', c_ushort),
    ('debayer_edge_scale', c_float),
]

AdebayerSeletedParamV2_t = struct_AdebayerSeletedParamV2_s# /usr/include/rkaiq/algos/adebayer/rk_aiq_types_adebayer_algo_int.h: 87

# /usr/include/rkaiq/algos/adebayer/rk_aiq_types_adebayer_algo_int.h: 112
class struct_AdebayerSeletedParamV2Lite_s(Structure):
    pass

struct_AdebayerSeletedParamV2Lite_s.__slots__ = [
    'debayer_en',
    'lowfreq_filter1',
    'highfreq_filter2',
    'debayer_clip_en',
    'debayer_gain_offset',
    'debayer_max_ratio',
    'debayer_hf_offset',
    'debayer_thed0',
    'debayer_thed1',
    'debayer_dist_scale',
    'debayer_select_thed',
    'debayer_gfilter_en',
    'debayer_gfilter_offset',
]
struct_AdebayerSeletedParamV2Lite_s._fields_ = [
    ('debayer_en', c_bool),
    ('lowfreq_filter1', c_int * int(4)),
    ('highfreq_filter2', c_int * int(4)),
    ('debayer_clip_en', c_ubyte),
    ('debayer_gain_offset', c_ushort),
    ('debayer_max_ratio', c_ubyte),
    ('debayer_hf_offset', c_ushort),
    ('debayer_thed0', c_ubyte),
    ('debayer_thed1', c_ubyte),
    ('debayer_dist_scale', c_ubyte),
    ('debayer_select_thed', c_ubyte),
    ('debayer_gfilter_en', c_ubyte),
    ('debayer_gfilter_offset', c_ushort),
]

AdebayerSeletedParamV2Lite_t = struct_AdebayerSeletedParamV2Lite_s# /usr/include/rkaiq/algos/adebayer/rk_aiq_types_adebayer_algo_int.h: 112

# /usr/include/rkaiq/algos/adebayer/rk_aiq_uapi_adebayer_int.h: 16
class struct_adebayer_attrib_auto_s(Structure):
    pass

struct_adebayer_attrib_auto_s.__slots__ = [
    'sharp_strength',
    'low_freq_thresh',
    'high_freq_thresh',
]
struct_adebayer_attrib_auto_s._fields_ = [
    ('sharp_strength', uint8_t * int(9)),
    ('low_freq_thresh', uint8_t),
    ('high_freq_thresh', uint8_t),
]

adebayer_attrib_auto_t = struct_adebayer_attrib_auto_s# /usr/include/rkaiq/algos/adebayer/rk_aiq_uapi_adebayer_int.h: 16

adebayer_attrib_manual_t = AdebayerSeletedParamV1_t# /usr/include/rkaiq/algos/adebayer/rk_aiq_uapi_adebayer_int.h: 18

# /usr/include/rkaiq/algos/adebayer/rk_aiq_uapi_adebayer_int.h: 28
class struct_adebayer_attrib_s(Structure):
    pass

struct_adebayer_attrib_s.__slots__ = [
    'sync',
    'mode',
    'enable',
    'stManual',
    'stAuto',
]
struct_adebayer_attrib_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('mode', rk_aiq_debayer_op_mode_t),
    ('enable', uint8_t),
    ('stManual', adebayer_attrib_manual_t),
    ('stAuto', adebayer_attrib_auto_t),
]

adebayer_attrib_t = struct_adebayer_attrib_s# /usr/include/rkaiq/algos/adebayer/rk_aiq_uapi_adebayer_int.h: 28

adebayer_attrib_v2_manual_t = AdebayerSeletedParamV2_t# /usr/include/rkaiq/algos/adebayer/rk_aiq_uapi_adebayer_int.h: 30

adebayer_attrib_v2_auto_t = CalibDbV2_Debayer_Tuning_t# /usr/include/rkaiq/algos/adebayer/rk_aiq_uapi_adebayer_int.h: 31

# /usr/include/rkaiq/algos/adebayer/rk_aiq_uapi_adebayer_int.h: 40
class struct_adebayer_v2_attrib_s(Structure):
    pass

struct_adebayer_v2_attrib_s.__slots__ = [
    'sync',
    'mode',
    'stManual',
    'stAuto',
]
struct_adebayer_v2_attrib_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('mode', rk_aiq_debayer_op_mode_t),
    ('stManual', adebayer_attrib_v2_manual_t),
    ('stAuto', adebayer_attrib_v2_auto_t),
]

adebayer_v2_attrib_t = struct_adebayer_v2_attrib_s# /usr/include/rkaiq/algos/adebayer/rk_aiq_uapi_adebayer_int.h: 40

adebayer_attrib_v2lite_manual_t = AdebayerSeletedParamV2Lite_t# /usr/include/rkaiq/algos/adebayer/rk_aiq_uapi_adebayer_int.h: 42

adebayer_attrib_v2lite_auto_t = CalibDbV2_Debayer_Tuning_Lite_t# /usr/include/rkaiq/algos/adebayer/rk_aiq_uapi_adebayer_int.h: 43

# /usr/include/rkaiq/algos/adebayer/rk_aiq_uapi_adebayer_int.h: 52
class struct_adebayer_v2lite_attrib_s(Structure):
    pass

struct_adebayer_v2lite_attrib_s.__slots__ = [
    'sync',
    'mode',
    'stManual',
    'stAuto',
]
struct_adebayer_v2lite_attrib_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('mode', rk_aiq_debayer_op_mode_t),
    ('stManual', adebayer_attrib_v2lite_manual_t),
    ('stAuto', adebayer_attrib_v2lite_auto_t),
]

adebayer_v2lite_attrib_t = struct_adebayer_v2lite_attrib_s# /usr/include/rkaiq/algos/adebayer/rk_aiq_uapi_adebayer_int.h: 52

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_adebayer.h: 31
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_adebayer_SetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_adebayer_SetAttrib = _lib.get("rk_aiq_user_api2_adebayer_SetAttrib", "cdecl")
    rk_aiq_user_api2_adebayer_SetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), adebayer_attrib_t]
    rk_aiq_user_api2_adebayer_SetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_adebayer.h: 33
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_adebayer_GetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_adebayer_GetAttrib = _lib.get("rk_aiq_user_api2_adebayer_GetAttrib", "cdecl")
    rk_aiq_user_api2_adebayer_GetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(adebayer_attrib_t)]
    rk_aiq_user_api2_adebayer_GetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_adebayer.h: 35
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_adebayer_v2_SetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_adebayer_v2_SetAttrib = _lib.get("rk_aiq_user_api2_adebayer_v2_SetAttrib", "cdecl")
    rk_aiq_user_api2_adebayer_v2_SetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), adebayer_v2_attrib_t]
    rk_aiq_user_api2_adebayer_v2_SetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_adebayer.h: 37
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_adebayer_v2_GetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_adebayer_v2_GetAttrib = _lib.get("rk_aiq_user_api2_adebayer_v2_GetAttrib", "cdecl")
    rk_aiq_user_api2_adebayer_v2_GetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(adebayer_v2_attrib_t)]
    rk_aiq_user_api2_adebayer_v2_GetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_adebayer.h: 39
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_adebayer_v2_lite_SetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_adebayer_v2_lite_SetAttrib = _lib.get("rk_aiq_user_api2_adebayer_v2_lite_SetAttrib", "cdecl")
    rk_aiq_user_api2_adebayer_v2_lite_SetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), adebayer_v2lite_attrib_t]
    rk_aiq_user_api2_adebayer_v2_lite_SetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_adebayer.h: 41
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_adebayer_v2_lite_GetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_adebayer_v2_lite_GetAttrib = _lib.get("rk_aiq_user_api2_adebayer_v2_lite_GetAttrib", "cdecl")
    rk_aiq_user_api2_adebayer_v2_lite_GetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(adebayer_v2lite_attrib_t)]
    rk_aiq_user_api2_adebayer_v2_lite_GetAttrib.restype = XCamReturn
    break

rk_aiq_degamma_attrib_t = rk_aiq_degamma_attr_t# /usr/include/rkaiq/algos/adegamma/rk_aiq_uapi_adegamma_int.h: 15

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_adegamma.h: 31
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_adegamma_SetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_adegamma_SetAttrib = _lib.get("rk_aiq_user_api2_adegamma_SetAttrib", "cdecl")
    rk_aiq_user_api2_adegamma_SetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), rk_aiq_degamma_attrib_t]
    rk_aiq_user_api2_adegamma_SetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_adegamma.h: 33
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_adegamma_GetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_adegamma_GetAttrib = _lib.get("rk_aiq_user_api2_adegamma_GetAttrib", "cdecl")
    rk_aiq_user_api2_adegamma_GetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_degamma_attrib_t)]
    rk_aiq_user_api2_adegamma_GetAttrib.restype = XCamReturn
    break

aDehazeDataV21_t = DehazeDataV11_t# /usr/include/rkaiq/iq_parser_v2/adehaze_uapi_compact.h: 25

# /usr/include/rkaiq/iq_parser_v2/adehaze_uapi_compact.h: 46
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

aDehaze_Setting_V21_t = struct_aDehaze_Setting_V21_s# /usr/include/rkaiq/iq_parser_v2/adehaze_uapi_compact.h: 46

aEnhanceDataV21_t = EnhanceDataV11_t# /usr/include/rkaiq/iq_parser_v2/adehaze_uapi_compact.h: 48

# /usr/include/rkaiq/iq_parser_v2/adehaze_uapi_compact.h: 57
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

aEnhance_Setting_V21_t = struct_aEnhance_Setting_V21_s# /usr/include/rkaiq/iq_parser_v2/adehaze_uapi_compact.h: 57

aHistDataV21_t = HistDataV11_t# /usr/include/rkaiq/iq_parser_v2/adehaze_uapi_compact.h: 59

# /usr/include/rkaiq/iq_parser_v2/adehaze_uapi_compact.h: 68
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

aHist_setting_V21_t = struct_aHist_setting_V21_s# /usr/include/rkaiq/iq_parser_v2/adehaze_uapi_compact.h: 68

# /usr/include/rkaiq/iq_parser_v2/adehaze_uapi_compact.h: 85
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

aDehazeAttrData_t = struct_aDehazeAttrData_s# /usr/include/rkaiq/iq_parser_v2/adehaze_uapi_compact.h: 85

# /usr/include/rkaiq/iq_parser_v2/adehaze_uapi_compact.h: 90
class struct_aDehazeAttr_s(Structure):
    pass

struct_aDehazeAttr_s.__slots__ = [
    'DehazeTuningPara',
]
struct_aDehazeAttr_s._fields_ = [
    ('DehazeTuningPara', aDehazeAttrData_t),
]

aDehazeAttr_t = struct_aDehazeAttr_s# /usr/include/rkaiq/iq_parser_v2/adehaze_uapi_compact.h: 90

mDehazeDataV21_t = mDehazeDataV11_t# /usr/include/rkaiq/iq_parser_v2/adehaze_uapi_compact.h: 92

# /usr/include/rkaiq/iq_parser_v2/adehaze_uapi_compact.h: 113
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

mDehaze_Setting_V21_t = struct_mDehaze_Setting_V21_s# /usr/include/rkaiq/iq_parser_v2/adehaze_uapi_compact.h: 113

mEnhanceDataV21_t = mEnhanceDataV11_t# /usr/include/rkaiq/iq_parser_v2/adehaze_uapi_compact.h: 115

# /usr/include/rkaiq/iq_parser_v2/adehaze_uapi_compact.h: 124
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

mEnhance_Setting_V21_t = struct_mEnhance_Setting_V21_s# /usr/include/rkaiq/iq_parser_v2/adehaze_uapi_compact.h: 124

mHistDataV21_t = mHistDataV11_t# /usr/include/rkaiq/iq_parser_v2/adehaze_uapi_compact.h: 126

# /usr/include/rkaiq/iq_parser_v2/adehaze_uapi_compact.h: 135
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

mHist_setting_V21_t = struct_mHist_setting_V21_s# /usr/include/rkaiq/iq_parser_v2/adehaze_uapi_compact.h: 135

# /usr/include/rkaiq/iq_parser_v2/adehaze_uapi_compact.h: 148
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

mDehazeAttr_t = struct_mDehazeAttr_s# /usr/include/rkaiq/iq_parser_v2/adehaze_uapi_compact.h: 148

# /usr/include/rkaiq/iq_parser_v2/adehaze_uapi_compact.h: 153
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

EnhanceManuAttr_t = struct_EnhanceManuAttr_s# /usr/include/rkaiq/iq_parser_v2/adehaze_uapi_compact.h: 153

# /usr/include/rkaiq/iq_parser_v2/adehaze_uapi_compact.h: 158
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

DehazeManuAttr_t = struct_DehazeManuAttr_s# /usr/include/rkaiq/iq_parser_v2/adehaze_uapi_compact.h: 158

# /usr/include/rkaiq/iq_parser_v2/adehaze_uapi_compact.h: 168
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

adehaze_sw_V2_t = struct_adehaze_sw_V2_s# /usr/include/rkaiq/iq_parser_v2/adehaze_uapi_compact.h: 168

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_adehaze.h: 31
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_adehaze_setSwAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_adehaze_setSwAttrib = _lib.get("rk_aiq_user_api2_adehaze_setSwAttrib", "cdecl")
    rk_aiq_user_api2_adehaze_setSwAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), adehaze_sw_V2_t]
    rk_aiq_user_api2_adehaze_setSwAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_adehaze.h: 33
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_adehaze_getSwAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_adehaze_getSwAttrib = _lib.get("rk_aiq_user_api2_adehaze_getSwAttrib", "cdecl")
    rk_aiq_user_api2_adehaze_getSwAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(adehaze_sw_V2_t)]
    rk_aiq_user_api2_adehaze_getSwAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_adehaze.h: 40
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_adehaze_v11_setSwAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_adehaze_v11_setSwAttrib = _lib.get("rk_aiq_user_api2_adehaze_v11_setSwAttrib", "cdecl")
    rk_aiq_user_api2_adehaze_v11_setSwAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(adehaze_sw_v11_t)]
    rk_aiq_user_api2_adehaze_v11_setSwAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_adehaze.h: 42
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_adehaze_v11_getSwAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_adehaze_v11_getSwAttrib = _lib.get("rk_aiq_user_api2_adehaze_v11_getSwAttrib", "cdecl")
    rk_aiq_user_api2_adehaze_v11_getSwAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(adehaze_sw_v11_t)]
    rk_aiq_user_api2_adehaze_v11_getSwAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_adehaze.h: 44
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_adehaze_v12_setSwAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_adehaze_v12_setSwAttrib = _lib.get("rk_aiq_user_api2_adehaze_v12_setSwAttrib", "cdecl")
    rk_aiq_user_api2_adehaze_v12_setSwAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(adehaze_sw_v12_t)]
    rk_aiq_user_api2_adehaze_v12_setSwAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_adehaze.h: 46
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_adehaze_v12_getSwAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_adehaze_v12_getSwAttrib = _lib.get("rk_aiq_user_api2_adehaze_v12_getSwAttrib", "cdecl")
    rk_aiq_user_api2_adehaze_v12_getSwAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(adehaze_sw_v12_t)]
    rk_aiq_user_api2_adehaze_v12_getSwAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_adpcc.h: 31
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_adpcc_SetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_adpcc_SetAttrib = _lib.get("rk_aiq_user_api2_adpcc_SetAttrib", "cdecl")
    rk_aiq_user_api2_adpcc_SetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_dpcc_attrib_V20_t)]
    rk_aiq_user_api2_adpcc_SetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_adpcc.h: 33
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_adpcc_GetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_adpcc_GetAttrib = _lib.get("rk_aiq_user_api2_adpcc_GetAttrib", "cdecl")
    rk_aiq_user_api2_adpcc_GetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_dpcc_attrib_V20_t)]
    rk_aiq_user_api2_adpcc_GetAttrib.restype = XCamReturn
    break

enum_AdrcVersion_e = c_int# /usr/include/rkaiq/iq_parser_v2/adrc_uapi_compact.h: 28

AdrcVersion_t = enum_AdrcVersion_e# /usr/include/rkaiq/iq_parser_v2/adrc_uapi_compact.h: 28

adrcAttr_V21_t = CalibDbV2_drc_V10_t# /usr/include/rkaiq/iq_parser_v2/adrc_uapi_compact.h: 30

adrcAttr_V30_t = CalibDbV2_drc_V11_t# /usr/include/rkaiq/iq_parser_v2/adrc_uapi_compact.h: 31

mdrcAttr_V21_t = mdrcAttr_V10_t# /usr/include/rkaiq/iq_parser_v2/adrc_uapi_compact.h: 32

mdrcAttr_V30_t = mdrcAttr_V11_t# /usr/include/rkaiq/iq_parser_v2/adrc_uapi_compact.h: 33

DrcCtrlInfo_t = DrcInfo_t# /usr/include/rkaiq/iq_parser_v2/adrc_uapi_compact.h: 34

# /usr/include/rkaiq/iq_parser_v2/adrc_uapi_compact.h: 43
class struct_DrcInfoV30_s(Structure):
    pass

struct_DrcInfoV30_s.__slots__ = [
    'CtrlInfo',
    'ValidParamsV21',
    'ValidParamsV30',
]
struct_DrcInfoV30_s._fields_ = [
    ('CtrlInfo', DrcCtrlInfo_t),
    ('ValidParamsV21', mdrcAttr_V21_t),
    ('ValidParamsV30', mdrcAttr_V30_t),
]

DrcInfoV30_t = struct_DrcInfoV30_s# /usr/include/rkaiq/iq_parser_v2/adrc_uapi_compact.h: 43

# /usr/include/rkaiq/iq_parser_v2/adrc_uapi_compact.h: 55
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
    ('Info', DrcInfoV30_t),
]

drcAttr_t = struct_drcAttr_s# /usr/include/rkaiq/iq_parser_v2/adrc_uapi_compact.h: 55

drc_attrib_t = drcAttr_t# /usr/include/rkaiq/iq_parser_v2/adrc_uapi_compact.h: 57

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_adrc.h: 31
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_adrc_SetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_adrc_SetAttrib = _lib.get("rk_aiq_user_api2_adrc_SetAttrib", "cdecl")
    rk_aiq_user_api2_adrc_SetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), drc_attrib_t]
    rk_aiq_user_api2_adrc_SetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_adrc.h: 32
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_adrc_GetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_adrc_GetAttrib = _lib.get("rk_aiq_user_api2_adrc_GetAttrib", "cdecl")
    rk_aiq_user_api2_adrc_GetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(drc_attrib_t)]
    rk_aiq_user_api2_adrc_GetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_adrc.h: 34
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_adrc_v10_SetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_adrc_v10_SetAttrib = _lib.get("rk_aiq_user_api2_adrc_v10_SetAttrib", "cdecl")
    rk_aiq_user_api2_adrc_v10_SetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(drcAttrV10_t)]
    rk_aiq_user_api2_adrc_v10_SetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_adrc.h: 36
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_adrc_v10_GetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_adrc_v10_GetAttrib = _lib.get("rk_aiq_user_api2_adrc_v10_GetAttrib", "cdecl")
    rk_aiq_user_api2_adrc_v10_GetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(drcAttrV10_t)]
    rk_aiq_user_api2_adrc_v10_GetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_adrc.h: 37
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_adrc_v11_SetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_adrc_v11_SetAttrib = _lib.get("rk_aiq_user_api2_adrc_v11_SetAttrib", "cdecl")
    rk_aiq_user_api2_adrc_v11_SetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(drcAttrV11_t)]
    rk_aiq_user_api2_adrc_v11_SetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_adrc.h: 39
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_adrc_v11_GetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_adrc_v11_GetAttrib = _lib.get("rk_aiq_user_api2_adrc_v11_GetAttrib", "cdecl")
    rk_aiq_user_api2_adrc_v11_GetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(drcAttrV11_t)]
    rk_aiq_user_api2_adrc_v11_GetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_adrc.h: 40
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_adrc_v12_SetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_adrc_v12_SetAttrib = _lib.get("rk_aiq_user_api2_adrc_v12_SetAttrib", "cdecl")
    rk_aiq_user_api2_adrc_v12_SetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(drcAttrV12_t)]
    rk_aiq_user_api2_adrc_v12_SetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_adrc.h: 42
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_adrc_v12_GetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_adrc_v12_GetAttrib = _lib.get("rk_aiq_user_api2_adrc_v12_GetAttrib", "cdecl")
    rk_aiq_user_api2_adrc_v12_GetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(drcAttrV12_t)]
    rk_aiq_user_api2_adrc_v12_GetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_adrc.h: 43
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_adrc_v12_lite_SetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_adrc_v12_lite_SetAttrib = _lib.get("rk_aiq_user_api2_adrc_v12_lite_SetAttrib", "cdecl")
    rk_aiq_user_api2_adrc_v12_lite_SetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(drcAttrV12Lite_t)]
    rk_aiq_user_api2_adrc_v12_lite_SetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_adrc.h: 45
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_adrc_v12_lite_GetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_adrc_v12_lite_GetAttrib = _lib.get("rk_aiq_user_api2_adrc_v12_lite_GetAttrib", "cdecl")
    rk_aiq_user_api2_adrc_v12_lite_GetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(drcAttrV12Lite_t)]
    rk_aiq_user_api2_adrc_v12_lite_GetAttrib.restype = XCamReturn
    break

enum__CalibDb_HdrAeRatioTypeV2_e = c_int# /usr/include/rkaiq/iq_parser_v2/aec_head.h: 45

CalibDb_HdrAeRatioTypeV2_t = enum__CalibDb_HdrAeRatioTypeV2_e# /usr/include/rkaiq/iq_parser_v2/aec_head.h: 45

enum__CalibDb_AeStrategyModeV2_e = c_int# /usr/include/rkaiq/iq_parser_v2/aec_head.h: 50

CalibDb_AeStrategyModeV2_t = enum__CalibDb_AeStrategyModeV2_e# /usr/include/rkaiq/iq_parser_v2/aec_head.h: 50

enum__CalibDb_AeHdrLongFrmModeV2_e = c_int# /usr/include/rkaiq/iq_parser_v2/aec_head.h: 56

CalibDb_AeHdrLongFrmModeV2_t = enum__CalibDb_AeHdrLongFrmModeV2_e# /usr/include/rkaiq/iq_parser_v2/aec_head.h: 56

enum__CalibDb_AecMeasAreaModeV2_e = c_int# /usr/include/rkaiq/iq_parser_v2/aec_head.h: 65

CalibDb_AecMeasAreaModeV2_t = enum__CalibDb_AecMeasAreaModeV2_e# /usr/include/rkaiq/iq_parser_v2/aec_head.h: 65

enum__CalibDb_FlickerFreqV2_e = c_int# /usr/include/rkaiq/iq_parser_v2/aec_head.h: 72

CalibDb_FlickerFreqV2_t = enum__CalibDb_FlickerFreqV2_e# /usr/include/rkaiq/iq_parser_v2/aec_head.h: 72

enum__CalibDb_AntiFlickerModeV2_e = c_int# /usr/include/rkaiq/iq_parser_v2/aec_head.h: 77

CalibDb_AntiFlickerModeV2_t = enum__CalibDb_AntiFlickerModeV2_e# /usr/include/rkaiq/iq_parser_v2/aec_head.h: 77

enum__CalibDb_IrisTypeV2_e = c_int# /usr/include/rkaiq/iq_parser_v2/aec_head.h: 83

CalibDb_IrisTypeV2_t = enum__CalibDb_IrisTypeV2_e# /usr/include/rkaiq/iq_parser_v2/aec_head.h: 83

enum__CalibDb_DelayTypeV2_e = c_int# /usr/include/rkaiq/iq_parser_v2/aec_head.h: 88

CalibDb_DelayTypeV2_t = enum__CalibDb_DelayTypeV2_e# /usr/include/rkaiq/iq_parser_v2/aec_head.h: 88

enum__CalibDb_CamYRangeModeV2_e = c_int# /usr/include/rkaiq/iq_parser_v2/aec_head.h: 95

CalibDb_CamYRangeModeV2_t = enum__CalibDb_CamYRangeModeV2_e# /usr/include/rkaiq/iq_parser_v2/aec_head.h: 95

enum__CalibDb_CamRawStatsModeV2_e = c_int# /usr/include/rkaiq/iq_parser_v2/aec_head.h: 104

CalibDb_CamRawStatsModeV2_t = enum__CalibDb_CamRawStatsModeV2_e# /usr/include/rkaiq/iq_parser_v2/aec_head.h: 104

enum__CalibDb_CamHistStatsModeV2_e = c_int# /usr/include/rkaiq/iq_parser_v2/aec_head.h: 114

CalibDb_CamHistStatsModeV2_t = enum__CalibDb_CamHistStatsModeV2_e# /usr/include/rkaiq/iq_parser_v2/aec_head.h: 114

# /usr/include/rkaiq/iq_parser_v2/aec_head.h: 146
class struct_CalibDb_AeDyDamp_s(Structure):
    pass

struct_CalibDb_AeDyDamp_s.__slots__ = [
    'DyDampEn',
    'SlowOPType',
    'SlowRange',
    'SlowDamp',
]
struct_CalibDb_AeDyDamp_s._fields_ = [
    ('DyDampEn', c_bool),
    ('SlowOPType', RKAiqOPMode_t),
    ('SlowRange', c_float),
    ('SlowDamp', c_float),
]

CalibDb_AeDyDamp_t = struct_CalibDb_AeDyDamp_s# /usr/include/rkaiq/iq_parser_v2/aec_head.h: 146

# /usr/include/rkaiq/iq_parser_v2/aec_head.h: 167
class struct_CalibDb_AeSpeedV2_s(Structure):
    pass

struct_CalibDb_AeSpeedV2_s.__slots__ = [
    'SmoothEn',
    'DampOver',
    'DampUnder',
    'DampDark2Bright',
    'DampBright2Dark',
    'DyDamp',
]
struct_CalibDb_AeSpeedV2_s._fields_ = [
    ('SmoothEn', c_bool),
    ('DampOver', c_float),
    ('DampUnder', c_float),
    ('DampDark2Bright', c_float),
    ('DampBright2Dark', c_float),
    ('DyDamp', CalibDb_AeDyDamp_t),
]

CalibDb_AeSpeedV2_t = struct_CalibDb_AeSpeedV2_s# /usr/include/rkaiq/iq_parser_v2/aec_head.h: 167

# /usr/include/rkaiq/iq_parser_v2/aec_head.h: 176
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

CalibDb_AeFrmRateAttrV2_t = struct_CalibDb_AeFrmRateAttrV2_s# /usr/include/rkaiq/iq_parser_v2/aec_head.h: 176

# /usr/include/rkaiq/iq_parser_v2/aec_head.h: 187
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

CalibDb_AntiFlickerAttrV2_t = struct_CalibDb_AntiFlickerAttrV2_s# /usr/include/rkaiq/iq_parser_v2/aec_head.h: 187

# /usr/include/rkaiq/iq_parser_v2/aec_head.h: 343
class struct_CalibDb_LinExpInitExpV2_s(Structure):
    pass

struct_CalibDb_LinExpInitExpV2_s.__slots__ = [
    'InitTimeValue',
    'InitGainValue',
    'InitIspDGainValue',
    'InitPIrisGainValue',
    'InitDCIrisDutyValue',
    'InitHDCIrisTargetValue',
]
struct_CalibDb_LinExpInitExpV2_s._fields_ = [
    ('InitTimeValue', c_float),
    ('InitGainValue', c_float),
    ('InitIspDGainValue', c_float),
    ('InitPIrisGainValue', c_int),
    ('InitDCIrisDutyValue', c_int),
    ('InitHDCIrisTargetValue', c_int),
]

CalibDb_LinExpInitExpV2_t = struct_CalibDb_LinExpInitExpV2_s# /usr/include/rkaiq/iq_parser_v2/aec_head.h: 343

# /usr/include/rkaiq/iq_parser_v2/aec_head.h: 358
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

CalibDb_LinAeRoute_AttrV2_t = struct_CalibDb_LinAeRoute_AttrV2_s# /usr/include/rkaiq/iq_parser_v2/aec_head.h: 358

# /usr/include/rkaiq/iq_parser_v2/aec_head.h: 367
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

CalibDb_AecDynamicSetpointV2_t = struct_CalibDb_AecDynamicSetpointV2_s# /usr/include/rkaiq/iq_parser_v2/aec_head.h: 367

# /usr/include/rkaiq/iq_parser_v2/aec_head.h: 382
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

CalibDb_BacklitSetPointV2_t = struct_CalibDb_BacklitSetPointV2_s# /usr/include/rkaiq/iq_parser_v2/aec_head.h: 382

# /usr/include/rkaiq/iq_parser_v2/aec_head.h: 408
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

CalibDb_AecBacklightV2_t = struct_CalibDb_AecBacklightV2_s# /usr/include/rkaiq/iq_parser_v2/aec_head.h: 408

# /usr/include/rkaiq/iq_parser_v2/aec_head.h: 420
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

CalibDb_OverExpSetPointV2_t = struct_CalibDb_OverExpSetPointV2_s# /usr/include/rkaiq/iq_parser_v2/aec_head.h: 420

# /usr/include/rkaiq/iq_parser_v2/aec_head.h: 440
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

CalibDb_AecOverExpCtrlV2_t = struct_CalibDb_AecOverExpCtrlV2_s# /usr/include/rkaiq/iq_parser_v2/aec_head.h: 440

# /usr/include/rkaiq/iq_parser_v2/aec_head.h: 472
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

CalibDb_LinearAE_AttrV2_t = struct_CalibDb_LinearAE_AttrV2_s# /usr/include/rkaiq/iq_parser_v2/aec_head.h: 472

# /usr/include/rkaiq/iq_parser_v2/aec_head.h: 497
class struct_CalibDb_HdrExpInitExpV2_s(Structure):
    pass

struct_CalibDb_HdrExpInitExpV2_s.__slots__ = [
    'InitTimeValue',
    'InitGainValue',
    'InitIspDGainValue',
    'InitPIrisGainValue',
    'InitDCIrisDutyValue',
    'InitHDCIrisTargetValue',
]
struct_CalibDb_HdrExpInitExpV2_s._fields_ = [
    ('InitTimeValue', c_float * int(3)),
    ('InitGainValue', c_float * int(3)),
    ('InitIspDGainValue', c_float * int(3)),
    ('InitPIrisGainValue', c_int),
    ('InitDCIrisDutyValue', c_int),
    ('InitHDCIrisTargetValue', c_int),
]

CalibDb_HdrExpInitExpV2_t = struct_CalibDb_HdrExpInitExpV2_s# /usr/include/rkaiq/iq_parser_v2/aec_head.h: 497

# /usr/include/rkaiq/iq_parser_v2/aec_head.h: 515
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

CalibDb_ExpRatioV2_t = struct_CalibDb_ExpRatioV2_s# /usr/include/rkaiq/iq_parser_v2/aec_head.h: 515

# /usr/include/rkaiq/iq_parser_v2/aec_head.h: 523
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

CalibDb_ExpRatioCtrlV2_t = struct_CalibDb_ExpRatioCtrlV2_s# /usr/include/rkaiq/iq_parser_v2/aec_head.h: 523

# /usr/include/rkaiq/iq_parser_v2/aec_head.h: 556
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

CalibDb_HdrAeRoute_AttrV2_t = struct_CalibDb_HdrAeRoute_AttrV2_s# /usr/include/rkaiq/iq_parser_v2/aec_head.h: 556

# /usr/include/rkaiq/iq_parser_v2/aec_head.h: 575
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

CalibDb_LfrmSetPointV2_t = struct_CalibDb_LfrmSetPointV2_s# /usr/include/rkaiq/iq_parser_v2/aec_head.h: 575

# /usr/include/rkaiq/iq_parser_v2/aec_head.h: 590
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

CalibDb_LfrmCtrlV2_t = struct_CalibDb_LfrmCtrlV2_s# /usr/include/rkaiq/iq_parser_v2/aec_head.h: 590

# /usr/include/rkaiq/iq_parser_v2/aec_head.h: 600
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

CalibDb_MfrmCtrlV2_t = struct_CalibDb_MfrmCtrlV2_s# /usr/include/rkaiq/iq_parser_v2/aec_head.h: 600

# /usr/include/rkaiq/iq_parser_v2/aec_head.h: 613
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

CalibDb_SfrmSetPointV2_t = struct_CalibDb_SfrmSetPointV2_s# /usr/include/rkaiq/iq_parser_v2/aec_head.h: 613

# /usr/include/rkaiq/iq_parser_v2/aec_head.h: 625
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

CalibDb_SfrmCtrlV2_t = struct_CalibDb_SfrmCtrlV2_s# /usr/include/rkaiq/iq_parser_v2/aec_head.h: 625

# /usr/include/rkaiq/iq_parser_v2/aec_head.h: 636
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

CalibDb_LongFrmCtrlV2_t = struct_CalibDb_LongFrmCtrlV2_s# /usr/include/rkaiq/iq_parser_v2/aec_head.h: 636

# /usr/include/rkaiq/iq_parser_v2/aec_head.h: 674
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

CalibDb_HdrAE_AttrV2_t = struct_CalibDb_HdrAE_AttrV2_s# /usr/include/rkaiq/iq_parser_v2/aec_head.h: 674

# /usr/include/rkaiq/iq_parser_v2/aec_head.h: 696
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

CalibDb_LinAlterExpV2_t = struct_CalibDb_LinAlterExpV2_s# /usr/include/rkaiq/iq_parser_v2/aec_head.h: 696

# /usr/include/rkaiq/iq_parser_v2/aec_head.h: 713
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

CalibDb_HdrAlterExpV2_t = struct_CalibDb_HdrAlterExpV2_s# /usr/include/rkaiq/iq_parser_v2/aec_head.h: 713

# /usr/include/rkaiq/iq_parser_v2/aec_head.h: 723
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

CalibDb_AlterExpV2_t = struct_CalibDb_AlterExpV2_s# /usr/include/rkaiq/iq_parser_v2/aec_head.h: 723

# /usr/include/rkaiq/iq_parser_v2/aec_head.h: 734
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

CalibDb_AeSyncTestV2_t = struct_CalibDb_AeSyncTestV2_s# /usr/include/rkaiq/iq_parser_v2/aec_head.h: 734

# /usr/include/rkaiq/iq_parser_v2/aec_head.h: 750
class struct_CalibDb_MIris_AttrV2_s(Structure):
    pass

struct_CalibDb_MIris_AttrV2_s.__slots__ = [
    'PIrisGainValue',
    'DCIrisHoldValue',
    'HDCIrisTargetValue',
]
struct_CalibDb_MIris_AttrV2_s._fields_ = [
    ('PIrisGainValue', c_int),
    ('DCIrisHoldValue', c_int),
    ('HDCIrisTargetValue', c_int),
]

CalibDb_MIris_AttrV2_t = struct_CalibDb_MIris_AttrV2_s# /usr/include/rkaiq/iq_parser_v2/aec_head.h: 750

# /usr/include/rkaiq/iq_parser_v2/aec_head.h: 764
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

CalibDb_PIris_AttrV2_t = struct_CalibDb_PIris_AttrV2_s# /usr/include/rkaiq/iq_parser_v2/aec_head.h: 764

# /usr/include/rkaiq/iq_parser_v2/aec_head.h: 781
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

CalibDb_DCIris_AttrV2_t = struct_CalibDb_DCIris_AttrV2_s# /usr/include/rkaiq/iq_parser_v2/aec_head.h: 781

# /usr/include/rkaiq/iq_parser_v2/aec_head.h: 816
class struct_CalibDb_HDCIris_AttrV2_s(Structure):
    pass

struct_CalibDb_HDCIris_AttrV2_s.__slots__ = [
    'DampOver',
    'DampUnder',
    'ZeroIsMax',
    'MinTarget',
    'MaxTarget',
    'ZoomTargetDot',
    'ZoomDot',
    'IrisTargetDot',
    'GainDot',
    'ZoomTargetDot_len',
    'IrisTargetDot_len',
]
struct_CalibDb_HDCIris_AttrV2_s._fields_ = [
    ('DampOver', c_float),
    ('DampUnder', c_float),
    ('ZeroIsMax', c_bool),
    ('MinTarget', c_int),
    ('MaxTarget', c_int),
    ('ZoomTargetDot', c_int * int(256)),
    ('ZoomDot', c_int * int(256)),
    ('IrisTargetDot', c_int * int(256)),
    ('GainDot', c_int * int(256)),
    ('ZoomTargetDot_len', c_int),
    ('IrisTargetDot_len', c_int),
]

CalibDb_HDCIris_AttrV2_t = struct_CalibDb_HDCIris_AttrV2_s# /usr/include/rkaiq/iq_parser_v2/aec_head.h: 816

# /usr/include/rkaiq/iq_parser_v2/aec_head.h: 842
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
    'HDCIrisAttr',
]
struct_CalibDb_AecIrisCtrlV2_s._fields_ = [
    ('Enable', c_bool),
    ('IrisType', CalibDb_IrisTypeV2_t),
    ('ManualEn', c_bool),
    ('ManualAttr', CalibDb_MIris_AttrV2_t),
    ('InitAttr', CalibDb_MIris_AttrV2_t),
    ('PIrisAttr', CalibDb_PIris_AttrV2_t),
    ('DCIrisAttr', CalibDb_DCIris_AttrV2_t),
    ('HDCIrisAttr', CalibDb_HDCIris_AttrV2_t),
]

CalibDb_AecIrisCtrlV2_t = struct_CalibDb_AecIrisCtrlV2_s# /usr/include/rkaiq/iq_parser_v2/aec_head.h: 842

# /usr/include/rkaiq/algos/ae/rk_aiq_types_ae_algo_int.h: 367
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

Aec_AeRange_t = struct_Aec_AeRange_s# /usr/include/rkaiq/algos/ae/rk_aiq_types_ae_algo_int.h: 367

# /usr/include/rkaiq/algos/ae/rk_aiq_types_ae_algo_int.h: 374
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

Aec_LinAeRange_t = struct_Aec_LinAeRange_s# /usr/include/rkaiq/algos/ae/rk_aiq_types_ae_algo_int.h: 374

# /usr/include/rkaiq/algos/ae/rk_aiq_types_ae_algo_int.h: 381
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

Aec_HdrAeRange_t = struct_Aec_HdrAeRange_s# /usr/include/rkaiq/algos/ae/rk_aiq_types_ae_algo_int.h: 381

# /usr/include/rkaiq/algos/ae/rk_aiq_types_ae_algo_int.h: 391
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

Aec_uapi_advanced_attr_t = struct_Aec_uapi_advanced_attr_s# /usr/include/rkaiq/algos/ae/rk_aiq_types_ae_algo_int.h: 391

Uapi_AeSpeedV2_t = CalibDb_AeSpeedV2_t# /usr/include/rkaiq/algos/ae/rk_aiq_uapi_ae_int_types_v2.h: 18

Uapi_AeFpsAttrV2_t = CalibDb_AeFrmRateAttrV2_t# /usr/include/rkaiq/algos/ae/rk_aiq_uapi_ae_int_types_v2.h: 26

Uapi_AntiFlickerV2_t = CalibDb_AntiFlickerAttrV2_t# /usr/include/rkaiq/algos/ae/rk_aiq_uapi_ae_int_types_v2.h: 28

Uapi_DelayTypeV2_t = CalibDb_DelayTypeV2_t# /usr/include/rkaiq/algos/ae/rk_aiq_uapi_ae_int_types_v2.h: 30

# /usr/include/rkaiq/algos/ae/rk_aiq_uapi_ae_int_types_v2.h: 45
class struct_Uapi_AeAttrV2_s(Structure):
    pass

struct_Uapi_AeAttrV2_s.__slots__ = [
    'stAeSpeed',
    'DelayType',
    'BlackDelay',
    'WhiteDelay',
    'stFrmRate',
    'stAntiFlicker',
    'LinAeRange',
    'HdrAeRange',
]
struct_Uapi_AeAttrV2_s._fields_ = [
    ('stAeSpeed', Uapi_AeSpeedV2_t),
    ('DelayType', Uapi_DelayTypeV2_t),
    ('BlackDelay', uint8_t),
    ('WhiteDelay', uint8_t),
    ('stFrmRate', Uapi_AeFpsAttrV2_t),
    ('stAntiFlicker', Uapi_AntiFlickerV2_t),
    ('LinAeRange', Aec_LinAeRange_t),
    ('HdrAeRange', Aec_HdrAeRange_t),
]

Uapi_AeAttrV2_t = struct_Uapi_AeAttrV2_s# /usr/include/rkaiq/algos/ae/rk_aiq_uapi_ae_int_types_v2.h: 45

# /usr/include/rkaiq/algos/ae/rk_aiq_uapi_ae_int_types_v2.h: 66
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

Uapi_LinMeAttrV2_t = struct_Uapi_LinMeAttrV2_s# /usr/include/rkaiq/algos/ae/rk_aiq_uapi_ae_int_types_v2.h: 66

# /usr/include/rkaiq/algos/ae/rk_aiq_uapi_ae_int_types_v2.h: 86
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

Uapi_HdrMeAttrV2_t = struct_Uapi_HdrMeAttrV2_s# /usr/include/rkaiq/algos/ae/rk_aiq_uapi_ae_int_types_v2.h: 86

# /usr/include/rkaiq/algos/ae/rk_aiq_uapi_ae_int_types_v2.h: 94
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

Uapi_MeAttrV2_t = struct_Uapi_MeAttrV2_s# /usr/include/rkaiq/algos/ae/rk_aiq_uapi_ae_int_types_v2.h: 94

Uapi_ExpSwAttr_AdvancedV2_t = Aec_uapi_advanced_attr_t# /usr/include/rkaiq/algos/ae/rk_aiq_uapi_ae_int_types_v2.h: 96

# /usr/include/rkaiq/algos/ae/rk_aiq_uapi_ae_int_types_v2.h: 115
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

Uapi_ExpSwAttrV2_t = struct_Uapi_ExpSwAttrV2_s# /usr/include/rkaiq/algos/ae/rk_aiq_uapi_ae_int_types_v2.h: 115

# /usr/include/rkaiq/algos/ae/rk_aiq_uapi_ae_int_types_v2.h: 125
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

Uapi_LinAeRouteAttr_t = struct_Uapi_LinAeRouteAttr_s# /usr/include/rkaiq/algos/ae/rk_aiq_uapi_ae_int_types_v2.h: 125

# /usr/include/rkaiq/algos/ae/rk_aiq_uapi_ae_int_types_v2.h: 130
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

Uapi_HdrAeRouteAttr_t = struct_Uapi_HdrAeRouteAttr_s# /usr/include/rkaiq/algos/ae/rk_aiq_uapi_ae_int_types_v2.h: 130

# /usr/include/rkaiq/algos/ae/rk_aiq_uapi_ae_int_types_v2.h: 140
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

Uapi_IrisAttrV2_t = struct_Uapi_IrisAttrV2_s# /usr/include/rkaiq/algos/ae/rk_aiq_uapi_ae_int_types_v2.h: 140

# /usr/include/rkaiq/algos/ae/rk_aiq_uapi_ae_int_types_v2.h: 150
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

Uapi_AecSyncTest_t = struct_Uapi_AecSyncTest_s# /usr/include/rkaiq/algos/ae/rk_aiq_uapi_ae_int_types_v2.h: 150

# /usr/include/rkaiq/algos/ae/rk_aiq_uapi_ae_int_types_v2.h: 160
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

Uapi_LinExpAttrV2_t = struct_Uapi_LinExpAttrV2_s# /usr/include/rkaiq/algos/ae/rk_aiq_uapi_ae_int_types_v2.h: 160

# /usr/include/rkaiq/algos/ae/rk_aiq_uapi_ae_int_types_v2.h: 165
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

Uapi_HdrExpAttrV2_t = struct_Uapi_HdrExpAttrV2_s# /usr/include/rkaiq/algos/ae/rk_aiq_uapi_ae_int_types_v2.h: 165

# /usr/include/rkaiq/algos/ae/rk_aiq_uapi_ae_int_types_v2.h: 175
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

Uapi_ExpWin_t = struct_Uapi_ExpWin_s# /usr/include/rkaiq/algos/ae/rk_aiq_uapi_ae_int_types_v2.h: 175

# /usr/include/rkaiq/algos/ae/rk_aiq_uapi_ae_int_types_v2.h: 196
class struct_Uapi_LinAeInfo_s(Structure):
    pass

struct_Uapi_LinAeInfo_s.__slots__ = [
    'LumaDeviation',
    'MeanLuma',
    'LinAeRange',
    'LinearExp',
]
struct_Uapi_LinAeInfo_s._fields_ = [
    ('LumaDeviation', c_float),
    ('MeanLuma', c_float),
    ('LinAeRange', Aec_LinAeRange_t),
    ('LinearExp', RkAiqExpRealParam_t),
]

Uapi_LinAeInfo_t = struct_Uapi_LinAeInfo_s# /usr/include/rkaiq/algos/ae/rk_aiq_uapi_ae_int_types_v2.h: 196

# /usr/include/rkaiq/algos/ae/rk_aiq_uapi_ae_int_types_v2.h: 217
class struct_Uapi_HdrAeInfo_s(Structure):
    pass

struct_Uapi_HdrAeInfo_s.__slots__ = [
    'HdrLumaDeviation',
    'Frm0Luma',
    'Frm1Luma',
    'Frm2Luma',
    'HdrAeRange',
    'HdrExp',
]
struct_Uapi_HdrAeInfo_s._fields_ = [
    ('HdrLumaDeviation', c_float * int(3)),
    ('Frm0Luma', c_float),
    ('Frm1Luma', c_float),
    ('Frm2Luma', c_float),
    ('HdrAeRange', Aec_HdrAeRange_t),
    ('HdrExp', RkAiqExpRealParam_t * int(3)),
]

Uapi_HdrAeInfo_t = struct_Uapi_HdrAeInfo_s# /usr/include/rkaiq/algos/ae/rk_aiq_uapi_ae_int_types_v2.h: 217

# /usr/include/rkaiq/algos/ae/rk_aiq_uapi_ae_int_types_v2.h: 258
class struct_Uapi_ExpQueryInfo_s(Structure):
    pass

struct_Uapi_ExpQueryInfo_s.__slots__ = [
    'IsConverged',
    'EnvChange',
    'IsExpMax',
    'LinAeInfo',
    'HdrAeInfo',
    'LinePeriodsPerField',
    'PixelPeriodsPerLine',
    'PixelClockFreqMHZ',
    'GlobalEnvLv',
    'OverExpROIPdf',
    'HighLightROIPdf',
    'LowLightROIPdf',
    'Fps',
]
struct_Uapi_ExpQueryInfo_s._fields_ = [
    ('IsConverged', c_bool),
    ('EnvChange', c_bool),
    ('IsExpMax', c_bool),
    ('LinAeInfo', Uapi_LinAeInfo_t),
    ('HdrAeInfo', Uapi_HdrAeInfo_t),
    ('LinePeriodsPerField', c_float),
    ('PixelPeriodsPerLine', c_float),
    ('PixelClockFreqMHZ', c_float),
    ('GlobalEnvLv', c_float),
    ('OverExpROIPdf', c_float),
    ('HighLightROIPdf', c_float),
    ('LowLightROIPdf', c_float),
    ('Fps', c_float),
]

Uapi_ExpQueryInfo_t = struct_Uapi_ExpQueryInfo_s# /usr/include/rkaiq/algos/ae/rk_aiq_uapi_ae_int_types_v2.h: 258

# /usr/include/rkaiq/algos/ae/rk_aiq_uapi_ae_int_types_v2.h: 272
class struct_Uapi_AecStatsCfg_s(Structure):
    pass

struct_Uapi_AecStatsCfg_s.__slots__ = [
    'sync',
    'updateStats',
    'YChannelEn',
    'RChannelEn',
    'GChannelEn',
    'BChannelEn',
]
struct_Uapi_AecStatsCfg_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('updateStats', c_bool),
    ('YChannelEn', c_bool),
    ('RChannelEn', c_bool),
    ('GChannelEn', c_bool),
    ('BChannelEn', c_bool),
]

Uapi_AecStatsCfg_t = struct_Uapi_AecStatsCfg_s# /usr/include/rkaiq/algos/ae/rk_aiq_uapi_ae_int_types_v2.h: 272

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_ae.h: 30
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_ae_setExpSwAttr", "cdecl"):
        continue
    rk_aiq_user_api2_ae_setExpSwAttr = _lib.get("rk_aiq_user_api2_ae_setExpSwAttr", "cdecl")
    rk_aiq_user_api2_ae_setExpSwAttr.argtypes = [POINTER(rk_aiq_sys_ctx_t), Uapi_ExpSwAttrV2_t]
    rk_aiq_user_api2_ae_setExpSwAttr.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_ae.h: 31
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_ae_getExpSwAttr", "cdecl"):
        continue
    rk_aiq_user_api2_ae_getExpSwAttr = _lib.get("rk_aiq_user_api2_ae_getExpSwAttr", "cdecl")
    rk_aiq_user_api2_ae_getExpSwAttr.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(Uapi_ExpSwAttrV2_t)]
    rk_aiq_user_api2_ae_getExpSwAttr.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_ae.h: 32
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_ae_setLinExpAttr", "cdecl"):
        continue
    rk_aiq_user_api2_ae_setLinExpAttr = _lib.get("rk_aiq_user_api2_ae_setLinExpAttr", "cdecl")
    rk_aiq_user_api2_ae_setLinExpAttr.argtypes = [POINTER(rk_aiq_sys_ctx_t), Uapi_LinExpAttrV2_t]
    rk_aiq_user_api2_ae_setLinExpAttr.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_ae.h: 33
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_ae_getLinExpAttr", "cdecl"):
        continue
    rk_aiq_user_api2_ae_getLinExpAttr = _lib.get("rk_aiq_user_api2_ae_getLinExpAttr", "cdecl")
    rk_aiq_user_api2_ae_getLinExpAttr.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(Uapi_LinExpAttrV2_t)]
    rk_aiq_user_api2_ae_getLinExpAttr.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_ae.h: 34
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_ae_setHdrExpAttr", "cdecl"):
        continue
    rk_aiq_user_api2_ae_setHdrExpAttr = _lib.get("rk_aiq_user_api2_ae_setHdrExpAttr", "cdecl")
    rk_aiq_user_api2_ae_setHdrExpAttr.argtypes = [POINTER(rk_aiq_sys_ctx_t), Uapi_HdrExpAttrV2_t]
    rk_aiq_user_api2_ae_setHdrExpAttr.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_ae.h: 35
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_ae_getHdrExpAttr", "cdecl"):
        continue
    rk_aiq_user_api2_ae_getHdrExpAttr = _lib.get("rk_aiq_user_api2_ae_getHdrExpAttr", "cdecl")
    rk_aiq_user_api2_ae_getHdrExpAttr.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(Uapi_HdrExpAttrV2_t)]
    rk_aiq_user_api2_ae_getHdrExpAttr.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_ae.h: 37
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_ae_setLinAeRouteAttr", "cdecl"):
        continue
    rk_aiq_user_api2_ae_setLinAeRouteAttr = _lib.get("rk_aiq_user_api2_ae_setLinAeRouteAttr", "cdecl")
    rk_aiq_user_api2_ae_setLinAeRouteAttr.argtypes = [POINTER(rk_aiq_sys_ctx_t), Uapi_LinAeRouteAttr_t]
    rk_aiq_user_api2_ae_setLinAeRouteAttr.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_ae.h: 38
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_ae_getLinAeRouteAttr", "cdecl"):
        continue
    rk_aiq_user_api2_ae_getLinAeRouteAttr = _lib.get("rk_aiq_user_api2_ae_getLinAeRouteAttr", "cdecl")
    rk_aiq_user_api2_ae_getLinAeRouteAttr.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(Uapi_LinAeRouteAttr_t)]
    rk_aiq_user_api2_ae_getLinAeRouteAttr.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_ae.h: 39
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_ae_setHdrAeRouteAttr", "cdecl"):
        continue
    rk_aiq_user_api2_ae_setHdrAeRouteAttr = _lib.get("rk_aiq_user_api2_ae_setHdrAeRouteAttr", "cdecl")
    rk_aiq_user_api2_ae_setHdrAeRouteAttr.argtypes = [POINTER(rk_aiq_sys_ctx_t), Uapi_HdrAeRouteAttr_t]
    rk_aiq_user_api2_ae_setHdrAeRouteAttr.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_ae.h: 40
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_ae_getHdrAeRouteAttr", "cdecl"):
        continue
    rk_aiq_user_api2_ae_getHdrAeRouteAttr = _lib.get("rk_aiq_user_api2_ae_getHdrAeRouteAttr", "cdecl")
    rk_aiq_user_api2_ae_getHdrAeRouteAttr.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(Uapi_HdrAeRouteAttr_t)]
    rk_aiq_user_api2_ae_getHdrAeRouteAttr.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_ae.h: 42
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_ae_setIrisAttr", "cdecl"):
        continue
    rk_aiq_user_api2_ae_setIrisAttr = _lib.get("rk_aiq_user_api2_ae_setIrisAttr", "cdecl")
    rk_aiq_user_api2_ae_setIrisAttr.argtypes = [POINTER(rk_aiq_sys_ctx_t), Uapi_IrisAttrV2_t]
    rk_aiq_user_api2_ae_setIrisAttr.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_ae.h: 43
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_ae_getIrisAttr", "cdecl"):
        continue
    rk_aiq_user_api2_ae_getIrisAttr = _lib.get("rk_aiq_user_api2_ae_getIrisAttr", "cdecl")
    rk_aiq_user_api2_ae_getIrisAttr.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(Uapi_IrisAttrV2_t)]
    rk_aiq_user_api2_ae_getIrisAttr.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_ae.h: 44
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_ae_setSyncTestAttr", "cdecl"):
        continue
    rk_aiq_user_api2_ae_setSyncTestAttr = _lib.get("rk_aiq_user_api2_ae_setSyncTestAttr", "cdecl")
    rk_aiq_user_api2_ae_setSyncTestAttr.argtypes = [POINTER(rk_aiq_sys_ctx_t), Uapi_AecSyncTest_t]
    rk_aiq_user_api2_ae_setSyncTestAttr.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_ae.h: 45
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_ae_getSyncTestAttr", "cdecl"):
        continue
    rk_aiq_user_api2_ae_getSyncTestAttr = _lib.get("rk_aiq_user_api2_ae_getSyncTestAttr", "cdecl")
    rk_aiq_user_api2_ae_getSyncTestAttr.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(Uapi_AecSyncTest_t)]
    rk_aiq_user_api2_ae_getSyncTestAttr.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_ae.h: 47
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_ae_queryExpResInfo", "cdecl"):
        continue
    rk_aiq_user_api2_ae_queryExpResInfo = _lib.get("rk_aiq_user_api2_ae_queryExpResInfo", "cdecl")
    rk_aiq_user_api2_ae_queryExpResInfo.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(Uapi_ExpQueryInfo_t)]
    rk_aiq_user_api2_ae_queryExpResInfo.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_ae.h: 48
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_ae_setExpWinAttr", "cdecl"):
        continue
    rk_aiq_user_api2_ae_setExpWinAttr = _lib.get("rk_aiq_user_api2_ae_setExpWinAttr", "cdecl")
    rk_aiq_user_api2_ae_setExpWinAttr.argtypes = [POINTER(rk_aiq_sys_ctx_t), Uapi_ExpWin_t]
    rk_aiq_user_api2_ae_setExpWinAttr.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_ae.h: 49
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_ae_getExpWinAttr", "cdecl"):
        continue
    rk_aiq_user_api2_ae_getExpWinAttr = _lib.get("rk_aiq_user_api2_ae_getExpWinAttr", "cdecl")
    rk_aiq_user_api2_ae_getExpWinAttr.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(Uapi_ExpWin_t)]
    rk_aiq_user_api2_ae_getExpWinAttr.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_ae.h: 50
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_ae_setAecStatsCfg", "cdecl"):
        continue
    rk_aiq_user_api2_ae_setAecStatsCfg = _lib.get("rk_aiq_user_api2_ae_setAecStatsCfg", "cdecl")
    rk_aiq_user_api2_ae_setAecStatsCfg.argtypes = [POINTER(rk_aiq_sys_ctx_t), Uapi_AecStatsCfg_t]
    rk_aiq_user_api2_ae_setAecStatsCfg.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_ae.h: 51
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_ae_getAecStatsCfg", "cdecl"):
        continue
    rk_aiq_user_api2_ae_getAecStatsCfg = _lib.get("rk_aiq_user_api2_ae_getAecStatsCfg", "cdecl")
    rk_aiq_user_api2_ae_getAecStatsCfg.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(Uapi_AecStatsCfg_t)]
    rk_aiq_user_api2_ae_getAecStatsCfg.restype = XCamReturn
    break

enum_opMode_e = c_int# /usr/include/rkaiq/uAPI2/rk_aiq_user_api_common.h: 16

OP_AUTO = 0# /usr/include/rkaiq/uAPI2/rk_aiq_user_api_common.h: 16

OP_MANUAL = 1# /usr/include/rkaiq/uAPI2/rk_aiq_user_api_common.h: 16

OP_SEMI_AUTO = 2# /usr/include/rkaiq/uAPI2/rk_aiq_user_api_common.h: 16

OP_REG_MANUAL = 3# /usr/include/rkaiq/uAPI2/rk_aiq_user_api_common.h: 16

OP_INVAL = (OP_REG_MANUAL + 1)# /usr/include/rkaiq/uAPI2/rk_aiq_user_api_common.h: 16

opMode_t = enum_opMode_e# /usr/include/rkaiq/uAPI2/rk_aiq_user_api_common.h: 16

enum_dayNightScene_e = c_int# /usr/include/rkaiq/uAPI2/rk_aiq_user_api_common.h: 28

DAYNIGHT_SCENE_DAY = 0# /usr/include/rkaiq/uAPI2/rk_aiq_user_api_common.h: 28

DAYNIGHT_SCENE_NIGHT = 1# /usr/include/rkaiq/uAPI2/rk_aiq_user_api_common.h: 28

DAYNIGHT_SCENE_INVAL = (DAYNIGHT_SCENE_NIGHT + 1)# /usr/include/rkaiq/uAPI2/rk_aiq_user_api_common.h: 28

dayNightScene_t = enum_dayNightScene_e# /usr/include/rkaiq/uAPI2/rk_aiq_user_api_common.h: 28

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api_common.h: 33
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

paRange_t = struct_paRange_s# /usr/include/rkaiq/uAPI2/rk_aiq_user_api_common.h: 33

enum_awbRange_e = c_int# /usr/include/rkaiq/uAPI2/rk_aiq_user_api_common.h: 39

AWB_RANGE_0 = 0# /usr/include/rkaiq/uAPI2/rk_aiq_user_api_common.h: 39

AWB_RANGE_1 = 1# /usr/include/rkaiq/uAPI2/rk_aiq_user_api_common.h: 39

AWB_RANGE_INVAL = (AWB_RANGE_1 + 1)# /usr/include/rkaiq/uAPI2/rk_aiq_user_api_common.h: 39

awbRange_t = enum_awbRange_e# /usr/include/rkaiq/uAPI2/rk_aiq_user_api_common.h: 39

enum_aeMode_e = c_int# /usr/include/rkaiq/uAPI2/rk_aiq_user_api_common.h: 45

AE_AUTO = 0# /usr/include/rkaiq/uAPI2/rk_aiq_user_api_common.h: 45

AE_IRIS_PRIOR = 1# /usr/include/rkaiq/uAPI2/rk_aiq_user_api_common.h: 45

AE_SHUTTER_PRIOR = 2# /usr/include/rkaiq/uAPI2/rk_aiq_user_api_common.h: 45

aeMode_t = enum_aeMode_e# /usr/include/rkaiq/uAPI2/rk_aiq_user_api_common.h: 45

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api_common.h: 66
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

paRect_t = struct_paRect_s# /usr/include/rkaiq/uAPI2/rk_aiq_user_api_common.h: 66

enum_aeMeasAreaType_e = c_int# /usr/include/rkaiq/uAPI2/rk_aiq_user_api_common.h: 75

AE_MEAS_AREA_AUTO = 0# /usr/include/rkaiq/uAPI2/rk_aiq_user_api_common.h: 75

AE_MEAS_AREA_UP = (AE_MEAS_AREA_AUTO + 1)# /usr/include/rkaiq/uAPI2/rk_aiq_user_api_common.h: 75

AE_MEAS_AREA_BOTTOM = (AE_MEAS_AREA_UP + 1)# /usr/include/rkaiq/uAPI2/rk_aiq_user_api_common.h: 75

AE_MEAS_AREA_LEFT = (AE_MEAS_AREA_BOTTOM + 1)# /usr/include/rkaiq/uAPI2/rk_aiq_user_api_common.h: 75

AE_MEAS_AREA_RIGHT = (AE_MEAS_AREA_LEFT + 1)# /usr/include/rkaiq/uAPI2/rk_aiq_user_api_common.h: 75

AE_MEAS_AREA_CENTER = (AE_MEAS_AREA_RIGHT + 1)# /usr/include/rkaiq/uAPI2/rk_aiq_user_api_common.h: 75

aeMeasAreaType_t = enum_aeMeasAreaType_e# /usr/include/rkaiq/uAPI2/rk_aiq_user_api_common.h: 75

enum_expPwrLineFreq_e = c_int# /usr/include/rkaiq/uAPI2/rk_aiq_user_api_common.h: 81

EXP_PWR_LINE_FREQ_DIS = 0# /usr/include/rkaiq/uAPI2/rk_aiq_user_api_common.h: 81

EXP_PWR_LINE_FREQ_50HZ = 1# /usr/include/rkaiq/uAPI2/rk_aiq_user_api_common.h: 81

EXP_PWR_LINE_FREQ_60HZ = 2# /usr/include/rkaiq/uAPI2/rk_aiq_user_api_common.h: 81

expPwrLineFreq_t = enum_expPwrLineFreq_e# /usr/include/rkaiq/uAPI2/rk_aiq_user_api_common.h: 81

enum_antiFlickerMode_e = c_int# /usr/include/rkaiq/uAPI2/rk_aiq_user_api_common.h: 86

ANTIFLICKER_NORMAL_MODE = 0# /usr/include/rkaiq/uAPI2/rk_aiq_user_api_common.h: 86

ANTIFLICKER_AUTO_MODE = 1# /usr/include/rkaiq/uAPI2/rk_aiq_user_api_common.h: 86

antiFlickerMode_t = enum_antiFlickerMode_e# /usr/include/rkaiq/uAPI2/rk_aiq_user_api_common.h: 86

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api_common.h: 91
class struct_frameRateInfo_s(Structure):
    pass

struct_frameRateInfo_s.__slots__ = [
    'mode',
    'fps',
]
struct_frameRateInfo_s._fields_ = [
    ('mode', opMode_t),
    ('fps', c_uint),
]

frameRateInfo_t = struct_frameRateInfo_s# /usr/include/rkaiq/uAPI2/rk_aiq_user_api_common.h: 91

# /usr/include/rkaiq/iq_parser_v2/af_uapi_head.h: 144
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

rk_tool_customAf_res_t = struct_rk_tool_customAf_res_s# /usr/include/rkaiq/iq_parser_v2/af_uapi_head.h: 144

enum__RKAIQ_AF_MODE = c_int# /usr/include/rkaiq/algos/af/rk_aiq_types_af_algo_int.h: 38

RKAIQ_AF_MODE = enum__RKAIQ_AF_MODE# /usr/include/rkaiq/algos/af/rk_aiq_types_af_algo_int.h: 38

enum__RKAIQ_AF_HWVER = c_int# /usr/include/rkaiq/algos/af/rk_aiq_types_af_algo_int.h: 47

RKAIQ_AF_HWVER = enum__RKAIQ_AF_HWVER# /usr/include/rkaiq/algos/af/rk_aiq_types_af_algo_int.h: 47

# /usr/include/rkaiq/algos/af/rk_aiq_types_af_algo_int.h: 68
class union_anon_157(Union):
    pass

union_anon_157.__slots__ = [
    'manual_meascfg',
    'manual_meascfg_v30',
    'manual_meascfg_v31',
    'manual_meascfg_v32',
]
union_anon_157._fields_ = [
    ('manual_meascfg', rk_aiq_af_algo_meas_v20_t),
    ('manual_meascfg_v30', rk_aiq_af_algo_meas_v30_t),
    ('manual_meascfg_v31', rk_aiq_af_algo_meas_v31_t),
    ('manual_meascfg_v32', rk_aiq_af_algo_meas_v32_t),
]

# /usr/include/rkaiq/algos/af/rk_aiq_types_af_algo_int.h: 74
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
    ('unnamed_1', union_anon_157),
]

rk_aiq_af_attrib_t = struct_rk_aiq_af_attrib_s# /usr/include/rkaiq/algos/af/rk_aiq_types_af_algo_int.h: 74

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_af.h: 30
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_af_SetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_af_SetAttrib = _lib.get("rk_aiq_user_api2_af_SetAttrib", "cdecl")
    rk_aiq_user_api2_af_SetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_af_attrib_t)]
    rk_aiq_user_api2_af_SetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_af.h: 32
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_af_GetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_af_GetAttrib = _lib.get("rk_aiq_user_api2_af_GetAttrib", "cdecl")
    rk_aiq_user_api2_af_GetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_af_attrib_t)]
    rk_aiq_user_api2_af_GetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_af.h: 34
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_af_Lock", "cdecl"):
        continue
    rk_aiq_user_api2_af_Lock = _lib.get("rk_aiq_user_api2_af_Lock", "cdecl")
    rk_aiq_user_api2_af_Lock.argtypes = [POINTER(rk_aiq_sys_ctx_t)]
    rk_aiq_user_api2_af_Lock.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_af.h: 36
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_af_Unlock", "cdecl"):
        continue
    rk_aiq_user_api2_af_Unlock = _lib.get("rk_aiq_user_api2_af_Unlock", "cdecl")
    rk_aiq_user_api2_af_Unlock.argtypes = [POINTER(rk_aiq_sys_ctx_t)]
    rk_aiq_user_api2_af_Unlock.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_af.h: 38
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_af_Oneshot", "cdecl"):
        continue
    rk_aiq_user_api2_af_Oneshot = _lib.get("rk_aiq_user_api2_af_Oneshot", "cdecl")
    rk_aiq_user_api2_af_Oneshot.argtypes = [POINTER(rk_aiq_sys_ctx_t)]
    rk_aiq_user_api2_af_Oneshot.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_af.h: 40
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_af_ManualTriger", "cdecl"):
        continue
    rk_aiq_user_api2_af_ManualTriger = _lib.get("rk_aiq_user_api2_af_ManualTriger", "cdecl")
    rk_aiq_user_api2_af_ManualTriger.argtypes = [POINTER(rk_aiq_sys_ctx_t)]
    rk_aiq_user_api2_af_ManualTriger.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_af.h: 42
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_af_Tracking", "cdecl"):
        continue
    rk_aiq_user_api2_af_Tracking = _lib.get("rk_aiq_user_api2_af_Tracking", "cdecl")
    rk_aiq_user_api2_af_Tracking.argtypes = [POINTER(rk_aiq_sys_ctx_t)]
    rk_aiq_user_api2_af_Tracking.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_af.h: 44
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_af_SetZoomIndex", "cdecl"):
        continue
    rk_aiq_user_api2_af_SetZoomIndex = _lib.get("rk_aiq_user_api2_af_SetZoomIndex", "cdecl")
    rk_aiq_user_api2_af_SetZoomIndex.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_int]
    rk_aiq_user_api2_af_SetZoomIndex.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_af.h: 46
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_af_GetZoomIndex", "cdecl"):
        continue
    rk_aiq_user_api2_af_GetZoomIndex = _lib.get("rk_aiq_user_api2_af_GetZoomIndex", "cdecl")
    rk_aiq_user_api2_af_GetZoomIndex.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(c_int)]
    rk_aiq_user_api2_af_GetZoomIndex.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_af.h: 48
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_af_EndZoomChg", "cdecl"):
        continue
    rk_aiq_user_api2_af_EndZoomChg = _lib.get("rk_aiq_user_api2_af_EndZoomChg", "cdecl")
    rk_aiq_user_api2_af_EndZoomChg.argtypes = [POINTER(rk_aiq_sys_ctx_t)]
    rk_aiq_user_api2_af_EndZoomChg.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_af.h: 50
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_af_StartZoomCalib", "cdecl"):
        continue
    rk_aiq_user_api2_af_StartZoomCalib = _lib.get("rk_aiq_user_api2_af_StartZoomCalib", "cdecl")
    rk_aiq_user_api2_af_StartZoomCalib.argtypes = [POINTER(rk_aiq_sys_ctx_t)]
    rk_aiq_user_api2_af_StartZoomCalib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_af.h: 52
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_af_resetZoom", "cdecl"):
        continue
    rk_aiq_user_api2_af_resetZoom = _lib.get("rk_aiq_user_api2_af_resetZoom", "cdecl")
    rk_aiq_user_api2_af_resetZoom.argtypes = [POINTER(rk_aiq_sys_ctx_t)]
    rk_aiq_user_api2_af_resetZoom.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_af.h: 54
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_af_SetVcmCfg", "cdecl"):
        continue
    rk_aiq_user_api2_af_SetVcmCfg = _lib.get("rk_aiq_user_api2_af_SetVcmCfg", "cdecl")
    rk_aiq_user_api2_af_SetVcmCfg.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_lens_vcmcfg)]
    rk_aiq_user_api2_af_SetVcmCfg.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_af.h: 56
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_af_GetVcmCfg", "cdecl"):
        continue
    rk_aiq_user_api2_af_GetVcmCfg = _lib.get("rk_aiq_user_api2_af_GetVcmCfg", "cdecl")
    rk_aiq_user_api2_af_GetVcmCfg.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_lens_vcmcfg)]
    rk_aiq_user_api2_af_GetVcmCfg.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_af.h: 58
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_af_GetSearchPath", "cdecl"):
        continue
    rk_aiq_user_api2_af_GetSearchPath = _lib.get("rk_aiq_user_api2_af_GetSearchPath", "cdecl")
    rk_aiq_user_api2_af_GetSearchPath.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_af_sec_path_t)]
    rk_aiq_user_api2_af_GetSearchPath.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_af.h: 60
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_af_GetSearchResult", "cdecl"):
        continue
    rk_aiq_user_api2_af_GetSearchResult = _lib.get("rk_aiq_user_api2_af_GetSearchResult", "cdecl")
    rk_aiq_user_api2_af_GetSearchResult.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_af_result_t)]
    rk_aiq_user_api2_af_GetSearchResult.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_af.h: 62
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_af_GetZoomRange", "cdecl"):
        continue
    rk_aiq_user_api2_af_GetZoomRange = _lib.get("rk_aiq_user_api2_af_GetZoomRange", "cdecl")
    rk_aiq_user_api2_af_GetZoomRange.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_af_zoomrange)]
    rk_aiq_user_api2_af_GetZoomRange.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_af.h: 64
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_af_GetFocusRange", "cdecl"):
        continue
    rk_aiq_user_api2_af_GetFocusRange = _lib.get("rk_aiq_user_api2_af_GetFocusRange", "cdecl")
    rk_aiq_user_api2_af_GetFocusRange.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_af_focusrange)]
    rk_aiq_user_api2_af_GetFocusRange.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_af.h: 66
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_af_setAngleZ", "cdecl"):
        continue
    rk_aiq_user_api2_af_setAngleZ = _lib.get("rk_aiq_user_api2_af_setAngleZ", "cdecl")
    rk_aiq_user_api2_af_setAngleZ.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_float]
    rk_aiq_user_api2_af_setAngleZ.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_af.h: 68
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_af_setCustomAfRes", "cdecl"):
        continue
    rk_aiq_user_api2_af_setCustomAfRes = _lib.get("rk_aiq_user_api2_af_setCustomAfRes", "cdecl")
    rk_aiq_user_api2_af_setCustomAfRes.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_tool_customAf_res_t)]
    rk_aiq_user_api2_af_setCustomAfRes.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_af.h: 70
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_af_GetFocusPos", "cdecl"):
        continue
    rk_aiq_user_api2_af_GetFocusPos = _lib.get("rk_aiq_user_api2_af_GetFocusPos", "cdecl")
    rk_aiq_user_api2_af_GetFocusPos.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(c_int)]
    rk_aiq_user_api2_af_GetFocusPos.restype = XCamReturn
    break

# /usr/include/rkaiq/algos/afec/rk_aiq_types_afec_algo_int.h: 12
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

rk_aiq_fec_cfg_t = struct_rk_aiq_fec_cfg_s# /usr/include/rkaiq/algos/afec/rk_aiq_types_afec_algo_int.h: 12

rk_aiq_fec_attrib_t = rk_aiq_fec_cfg_t# /usr/include/rkaiq/algos/afec/rk_aiq_uapi_afec_int.h: 8

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_afec.h: 25
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_afec_SetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_afec_SetAttrib = _lib.get("rk_aiq_user_api2_afec_SetAttrib", "cdecl")
    rk_aiq_user_api2_afec_SetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), rk_aiq_fec_attrib_t]
    rk_aiq_user_api2_afec_SetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_afec.h: 27
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_afec_GetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_afec_GetAttrib = _lib.get("rk_aiq_user_api2_afec_GetAttrib", "cdecl")
    rk_aiq_user_api2_afec_GetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_fec_attrib_t)]
    rk_aiq_user_api2_afec_GetAttrib.restype = XCamReturn
    break

enum_gamma_op_mode_s = c_int# /usr/include/rkaiq/iq_parser_v2/agamma_uapi_compact.h: 28

gamma_op_mode_t = enum_gamma_op_mode_s# /usr/include/rkaiq/iq_parser_v2/agamma_uapi_compact.h: 28

# /usr/include/rkaiq/iq_parser_v2/agamma_uapi_compact.h: 37
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

Agamma_api_Fast_t = struct_Agamma_api_Fast_s# /usr/include/rkaiq/iq_parser_v2/agamma_uapi_compact.h: 37

# /usr/include/rkaiq/iq_parser_v2/agamma_uapi_compact.h: 48
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

Agamma_api_manualV21_t = struct_Agamma_api_manualV21_s# /usr/include/rkaiq/iq_parser_v2/agamma_uapi_compact.h: 48

# /usr/include/rkaiq/iq_parser_v2/agamma_uapi_compact.h: 57
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

Agamma_api_manualV30_t = struct_Agamma_api_manualV30_s# /usr/include/rkaiq/iq_parser_v2/agamma_uapi_compact.h: 57

# /usr/include/rkaiq/iq_parser_v2/agamma_uapi_compact.h: 63
class struct_rk_aiq_gamma_attrV21_s(Structure):
    pass

struct_rk_aiq_gamma_attrV21_s.__slots__ = [
    'mode',
    'stManual',
    'stFast',
]
struct_rk_aiq_gamma_attrV21_s._fields_ = [
    ('mode', gamma_op_mode_t),
    ('stManual', Agamma_api_manualV21_t),
    ('stFast', Agamma_api_Fast_t),
]

rk_aiq_gamma_attrV21_t = struct_rk_aiq_gamma_attrV21_s# /usr/include/rkaiq/iq_parser_v2/agamma_uapi_compact.h: 63

# /usr/include/rkaiq/iq_parser_v2/agamma_uapi_compact.h: 69
class struct_rk_aiq_gamma_attrV30_s(Structure):
    pass

struct_rk_aiq_gamma_attrV30_s.__slots__ = [
    'mode',
    'stManual',
    'stFast',
]
struct_rk_aiq_gamma_attrV30_s._fields_ = [
    ('mode', gamma_op_mode_t),
    ('stManual', Agamma_api_manualV30_t),
    ('stFast', Agamma_api_Fast_t),
]

rk_aiq_gamma_attrV30_t = struct_rk_aiq_gamma_attrV30_s# /usr/include/rkaiq/iq_parser_v2/agamma_uapi_compact.h: 69

# /usr/include/rkaiq/iq_parser_v2/agamma_uapi_compact.h: 76
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

rk_aiq_gamma_attr_t = struct_rk_aiq_gamma_attr_s# /usr/include/rkaiq/iq_parser_v2/agamma_uapi_compact.h: 76

rk_aiq_gamma_attrib_V2_t = rk_aiq_gamma_attr_t# /usr/include/rkaiq/iq_parser_v2/agamma_uapi_compact.h: 78

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_agamma.h: 31
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_agamma_SetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_agamma_SetAttrib = _lib.get("rk_aiq_user_api2_agamma_SetAttrib", "cdecl")
    rk_aiq_user_api2_agamma_SetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), rk_aiq_gamma_attrib_V2_t]
    rk_aiq_user_api2_agamma_SetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_agamma.h: 33
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_agamma_GetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_agamma_GetAttrib = _lib.get("rk_aiq_user_api2_agamma_GetAttrib", "cdecl")
    rk_aiq_user_api2_agamma_GetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_gamma_attrib_V2_t)]
    rk_aiq_user_api2_agamma_GetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_agamma.h: 36
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_agamma_v10_SetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_agamma_v10_SetAttrib = _lib.get("rk_aiq_user_api2_agamma_v10_SetAttrib", "cdecl")
    rk_aiq_user_api2_agamma_v10_SetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_gamma_v10_attr_t)]
    rk_aiq_user_api2_agamma_v10_SetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_agamma.h: 38
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_agamma_v10_GetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_agamma_v10_GetAttrib = _lib.get("rk_aiq_user_api2_agamma_v10_GetAttrib", "cdecl")
    rk_aiq_user_api2_agamma_v10_GetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_gamma_v10_attr_t)]
    rk_aiq_user_api2_agamma_v10_GetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_agamma.h: 40
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_agamma_v11_SetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_agamma_v11_SetAttrib = _lib.get("rk_aiq_user_api2_agamma_v11_SetAttrib", "cdecl")
    rk_aiq_user_api2_agamma_v11_SetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_gamma_v11_attr_t)]
    rk_aiq_user_api2_agamma_v11_SetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_agamma.h: 42
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_agamma_v11_GetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_agamma_v11_GetAttrib = _lib.get("rk_aiq_user_api2_agamma_v11_GetAttrib", "cdecl")
    rk_aiq_user_api2_agamma_v11_GetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_gamma_v11_attr_t)]
    rk_aiq_user_api2_agamma_v11_GetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/iq_parser_v2/aie_uapi_head.h: 30
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

aie_attrib_t = struct_aie_attrib_s# /usr/include/rkaiq/iq_parser_v2/aie_uapi_head.h: 30

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_aie.h: 30
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_aie_SetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_aie_SetAttrib = _lib.get("rk_aiq_user_api2_aie_SetAttrib", "cdecl")
    rk_aiq_user_api2_aie_SetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(aie_attrib_t)]
    rk_aiq_user_api2_aie_SetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_aie.h: 32
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_aie_GetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_aie_GetAttrib = _lib.get("rk_aiq_user_api2_aie_GetAttrib", "cdecl")
    rk_aiq_user_api2_aie_GetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(aie_attrib_t)]
    rk_aiq_user_api2_aie_GetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/algos/aldch/rk_aiq_types_aldch_algo_int.h: 16
class struct_rk_aiq_ldch_cfg_s(Structure):
    pass

struct_rk_aiq_ldch_cfg_s.__slots__ = [
    'sync',
    'en',
    'correct_level',
]
struct_rk_aiq_ldch_cfg_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('en', c_bool),
    ('correct_level', uint8_t),
]

rk_aiq_ldch_cfg_t = struct_rk_aiq_ldch_cfg_s# /usr/include/rkaiq/algos/aldch/rk_aiq_types_aldch_algo_int.h: 16

enum_anon_158 = c_int# /usr/include/rkaiq/algos/aldch/rk_aiq_types_aldch_algo_int.h: 22

rk_aiq_ldch_update_lut_mode_t = enum_anon_158# /usr/include/rkaiq/algos/aldch/rk_aiq_types_aldch_algo_int.h: 22

# /usr/include/rkaiq/algos/aldch/rk_aiq_types_aldch_algo_int.h: 27
class struct_rk_aiq_ldch_lut_external_file_s(Structure):
    pass

struct_rk_aiq_ldch_lut_external_file_s.__slots__ = [
    'config_file_dir',
    'mesh_file_name',
]
struct_rk_aiq_ldch_lut_external_file_s._fields_ = [
    ('config_file_dir', c_char * int(64)),
    ('mesh_file_name', c_char * int(32)),
]

rk_aiq_ldch_lut_external_file_t = struct_rk_aiq_ldch_lut_external_file_s# /usr/include/rkaiq/algos/aldch/rk_aiq_types_aldch_algo_int.h: 27

# /usr/include/rkaiq/algos/aldch/rk_aiq_types_aldch_algo_int.h: 32
class struct_rk_aiq_ldch_lut_external_buffer_s(Structure):
    pass

struct_rk_aiq_ldch_lut_external_buffer_s.__slots__ = [
    'addr',
    'size',
]
struct_rk_aiq_ldch_lut_external_buffer_s._fields_ = [
    ('addr', POINTER(None)),
    ('size', c_size_t),
]

rk_aiq_ldch_lut_external_buffer_t = struct_rk_aiq_ldch_lut_external_buffer_s# /usr/include/rkaiq/algos/aldch/rk_aiq_types_aldch_algo_int.h: 32

# /usr/include/rkaiq/algos/aldch/rk_aiq_types_aldch_algo_int.h: 36
class union_anon_159(Union):
    pass

union_anon_159.__slots__ = [
    'file',
    'buffer',
]
union_anon_159._fields_ = [
    ('file', rk_aiq_ldch_lut_external_file_t),
    ('buffer', rk_aiq_ldch_lut_external_buffer_t),
]

# /usr/include/rkaiq/algos/aldch/rk_aiq_types_aldch_algo_int.h: 40
class struct_rk_aiq_ldch_custom_lut_s(Structure):
    pass

struct_rk_aiq_ldch_custom_lut_s.__slots__ = [
    'update_flag',
    'u',
]
struct_rk_aiq_ldch_custom_lut_s._fields_ = [
    ('update_flag', c_bool),
    ('u', union_anon_159),
]

rk_aiq_ldch_custom_lut_t = struct_rk_aiq_ldch_custom_lut_s# /usr/include/rkaiq/algos/aldch/rk_aiq_types_aldch_algo_int.h: 40

# /usr/include/rkaiq/algos/aldch/rk_aiq_types_aldch_algo_int.h: 56
class struct_rk_aiq_ldch_v21_cfg_s(Structure):
    pass

struct_rk_aiq_ldch_v21_cfg_s.__slots__ = [
    'sync',
    'en',
    'correct_level',
    'bic_mode_en',
    'zero_interp_en',
    'sample_avr_en',
    'bic_weight',
    'update_lut_mode',
    'lut',
]
struct_rk_aiq_ldch_v21_cfg_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('en', c_bool),
    ('correct_level', uint8_t),
    ('bic_mode_en', uint8_t),
    ('zero_interp_en', uint8_t),
    ('sample_avr_en', uint8_t),
    ('bic_weight', uint8_t * int(36)),
    ('update_lut_mode', rk_aiq_ldch_update_lut_mode_t),
    ('lut', rk_aiq_ldch_custom_lut_t),
]

rk_aiq_ldch_v21_cfg_t = struct_rk_aiq_ldch_v21_cfg_s# /usr/include/rkaiq/algos/aldch/rk_aiq_types_aldch_algo_int.h: 56

rk_aiq_ldch_attrib_t = rk_aiq_ldch_cfg_t# /usr/include/rkaiq/algos/aldch/rk_aiq_uapi_aldch_int.h: 8

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_aldch.h: 26
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_aldch_SetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_aldch_SetAttrib = _lib.get("rk_aiq_user_api2_aldch_SetAttrib", "cdecl")
    rk_aiq_user_api2_aldch_SetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_ldch_attrib_t)]
    rk_aiq_user_api2_aldch_SetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_aldch.h: 28
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_aldch_GetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_aldch_GetAttrib = _lib.get("rk_aiq_user_api2_aldch_GetAttrib", "cdecl")
    rk_aiq_user_api2_aldch_GetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_ldch_attrib_t)]
    rk_aiq_user_api2_aldch_GetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/iq_parser_v2/alsc_uapi_head.h: 36
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
    ('lsc_sect_size_x', uint16_t * int(16)),
    ('lsc_sect_size_y', uint16_t * int(16)),
    ('r_data_tbl', c_ushort * int(289)),
    ('gr_data_tbl', c_ushort * int(289)),
    ('gb_data_tbl', c_ushort * int(289)),
    ('b_data_tbl', c_ushort * int(289)),
]

# /usr/include/rkaiq/algos/alsc/rk_aiq_types_alsc_common.h: 20
class struct_lsc_name_s(Structure):
    pass

struct_lsc_name_s.__slots__ = [
    'name',
]
struct_lsc_name_s._fields_ = [
    ('name', c_char * int(32)),
]

lsc_name_t = struct_lsc_name_s# /usr/include/rkaiq/algos/alsc/rk_aiq_types_alsc_common.h: 20

# /usr/include/rkaiq/algos/alsc/rk_aiq_types_alsc_common.h: 40
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

CalibDbV2_LscTableProfile_t = struct_CalibDbV2_LscTableProfile_s# /usr/include/rkaiq/algos/alsc/rk_aiq_types_alsc_common.h: 40

rk_aiq_lsc_mlsc_attrib_t = struct_rk_aiq_lsc_table_s# /usr/include/rkaiq/algos/alsc/rk_aiq_types_alsc_algo_int.h: 59

enum_rk_aiq_lsc_op_mode_s = c_int# /usr/include/rkaiq/algos/alsc/rk_aiq_types_alsc_algo_int.h: 66

rk_aiq_lsc_op_mode_t = enum_rk_aiq_lsc_op_mode_s# /usr/include/rkaiq/algos/alsc/rk_aiq_types_alsc_algo_int.h: 66

# /usr/include/rkaiq/algos/alsc/rk_aiq_types_alsc_algo_int.h: 72
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

Lsc_v2_Resolution_t = struct_Lsc_v2_Resolution_s# /usr/include/rkaiq/algos/alsc/rk_aiq_types_alsc_algo_int.h: 72

# /usr/include/rkaiq/algos/alsc/rk_aiq_types_alsc_algo_int.h: 78
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

CalibDbV2_Lsc_Common_fixed_t = struct_CalibDbV2_Lsc_Common_fixed_s# /usr/include/rkaiq/algos/alsc/rk_aiq_types_alsc_algo_int.h: 78

# /usr/include/rkaiq/algos/alsc/rk_aiq_types_alsc_algo_int.h: 90
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

CalibDbV2_AlscCof_ill_fixed_t = struct_CalibDbV2_AlscCof_ill_fixed_s# /usr/include/rkaiq/algos/alsc/rk_aiq_types_alsc_algo_int.h: 90

# /usr/include/rkaiq/algos/alsc/rk_aiq_types_alsc_algo_int.h: 96
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

CalibDbV2_AlscCof_fixed_t = struct_CalibDbV2_AlscCof_fixed_s# /usr/include/rkaiq/algos/alsc/rk_aiq_types_alsc_algo_int.h: 96

# /usr/include/rkaiq/algos/alsc/rk_aiq_types_alsc_algo_int.h: 101
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

CalibDbV2_LscTable_fixed_t = struct_CalibDbV2_LscTable_fixed_s# /usr/include/rkaiq/algos/alsc/rk_aiq_types_alsc_algo_int.h: 101

# /usr/include/rkaiq/algos/alsc/rk_aiq_types_alsc_algo_int.h: 107
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

rk_aiq_lsc_alsc_attrib_t = struct_rk_aiq_lsc_alsc_attrib_s# /usr/include/rkaiq/algos/alsc/rk_aiq_types_alsc_algo_int.h: 107

# /usr/include/rkaiq/algos/alsc/rk_aiq_types_alsc_algo_int.h: 116
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

rk_aiq_lsc_attrib_t = struct_rk_aiq_lsc_attrib_s# /usr/include/rkaiq/algos/alsc/rk_aiq_types_alsc_algo_int.h: 116

# /usr/include/rkaiq/algos/alsc/rk_aiq_types_alsc_algo_int.h: 125
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

rk_aiq_lsc_querry_info_t = struct_rk_aiq_lsc_querry_info_s# /usr/include/rkaiq/algos/alsc/rk_aiq_types_alsc_algo_int.h: 125

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_alsc.h: 30
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_alsc_SetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_alsc_SetAttrib = _lib.get("rk_aiq_user_api2_alsc_SetAttrib", "cdecl")
    rk_aiq_user_api2_alsc_SetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), rk_aiq_lsc_attrib_t]
    rk_aiq_user_api2_alsc_SetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_alsc.h: 32
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_alsc_GetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_alsc_GetAttrib = _lib.get("rk_aiq_user_api2_alsc_GetAttrib", "cdecl")
    rk_aiq_user_api2_alsc_GetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_lsc_attrib_t)]
    rk_aiq_user_api2_alsc_GetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_alsc.h: 35
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_alsc_QueryLscInfo", "cdecl"):
        continue
    rk_aiq_user_api2_alsc_QueryLscInfo = _lib.get("rk_aiq_user_api2_alsc_QueryLscInfo", "cdecl")
    rk_aiq_user_api2_alsc_QueryLscInfo.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_lsc_querry_info_t)]
    rk_aiq_user_api2_alsc_QueryLscInfo.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_alsc.h: 38
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_alsc_SetAcolorSwInfo", "cdecl"):
        continue
    rk_aiq_user_api2_alsc_SetAcolorSwInfo = _lib.get("rk_aiq_user_api2_alsc_SetAcolorSwInfo", "cdecl")
    rk_aiq_user_api2_alsc_SetAcolorSwInfo.argtypes = [POINTER(rk_aiq_sys_ctx_t), rk_aiq_color_info_t]
    rk_aiq_user_api2_alsc_SetAcolorSwInfo.restype = XCamReturn
    break

enum_merge_OpModeV21_e = c_int# /usr/include/rkaiq/iq_parser_v2/amerge_uapi_compact.h: 32

merge_OpModeV21_t = enum_merge_OpModeV21_e# /usr/include/rkaiq/iq_parser_v2/amerge_uapi_compact.h: 32

mMergeOECurveV21_t = mMergeOECurveV10_t# /usr/include/rkaiq/iq_parser_v2/amerge_uapi_compact.h: 34

mMergeMDCurveV21_t = mMergeMDCurveV10_t# /usr/include/rkaiq/iq_parser_v2/amerge_uapi_compact.h: 35

# /usr/include/rkaiq/iq_parser_v2/amerge_uapi_compact.h: 42
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

mmergeAttrV21_t = struct_mmergeAttrV21_s# /usr/include/rkaiq/iq_parser_v2/amerge_uapi_compact.h: 42

# /usr/include/rkaiq/iq_parser_v2/amerge_uapi_compact.h: 48
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

mergeAttrV21_t = struct_mergeAttrV21_s# /usr/include/rkaiq/iq_parser_v2/amerge_uapi_compact.h: 48

# /usr/include/rkaiq/iq_parser_v2/amerge_uapi_compact.h: 55
class struct_mLongFrameModeDataV30_s(Structure):
    pass

struct_mLongFrameModeDataV30_s.__slots__ = [
    'OECurve',
    'MDCurve',
]
struct_mLongFrameModeDataV30_s._fields_ = [
    ('OECurve', mMergeOECurveV21_t),
    ('MDCurve', mMergeMDCurveV21_t),
]

mLongFrameModeDataV30_t = struct_mLongFrameModeDataV30_s# /usr/include/rkaiq/iq_parser_v2/amerge_uapi_compact.h: 55

mMergeMDCurveV30Short_t = mMergeMDCurveV11Short_t# /usr/include/rkaiq/iq_parser_v2/amerge_uapi_compact.h: 57

# /usr/include/rkaiq/iq_parser_v2/amerge_uapi_compact.h: 64
class struct_mShortFrameModeDataV30_s(Structure):
    pass

struct_mShortFrameModeDataV30_s.__slots__ = [
    'OECurve',
    'MDCurve',
]
struct_mShortFrameModeDataV30_s._fields_ = [
    ('OECurve', mMergeOECurveV21_t),
    ('MDCurve', mMergeMDCurveV30Short_t),
]

mShortFrameModeDataV30_t = struct_mShortFrameModeDataV30_s# /usr/include/rkaiq/iq_parser_v2/amerge_uapi_compact.h: 64

# /usr/include/rkaiq/iq_parser_v2/amerge_uapi_compact.h: 73
class struct_mMergeAttrV30_s(Structure):
    pass

struct_mMergeAttrV30_s.__slots__ = [
    'BaseFrm',
    'LongFrmModeData',
    'ShortFrmModeData',
]
struct_mMergeAttrV30_s._fields_ = [
    ('BaseFrm', MergeBaseFrame_t),
    ('LongFrmModeData', mLongFrameModeDataV30_t),
    ('ShortFrmModeData', mShortFrameModeDataV30_t),
]

mMergeAttrV30_t = struct_mMergeAttrV30_s# /usr/include/rkaiq/iq_parser_v2/amerge_uapi_compact.h: 73

# /usr/include/rkaiq/iq_parser_v2/amerge_uapi_compact.h: 79
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

mergeAttrV30_t = struct_mergeAttrV30_s# /usr/include/rkaiq/iq_parser_v2/amerge_uapi_compact.h: 79

# /usr/include/rkaiq/iq_parser_v2/amerge_uapi_compact.h: 86
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

mergeAttr_t = struct_mergeAttr_s# /usr/include/rkaiq/iq_parser_v2/amerge_uapi_compact.h: 86

amerge_attrib_t = mergeAttr_t# /usr/include/rkaiq/iq_parser_v2/amerge_uapi_compact.h: 88

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_amerge.h: 31
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_amerge_SetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_amerge_SetAttrib = _lib.get("rk_aiq_user_api2_amerge_SetAttrib", "cdecl")
    rk_aiq_user_api2_amerge_SetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), amerge_attrib_t]
    rk_aiq_user_api2_amerge_SetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_amerge.h: 32
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_amerge_GetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_amerge_GetAttrib = _lib.get("rk_aiq_user_api2_amerge_GetAttrib", "cdecl")
    rk_aiq_user_api2_amerge_GetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(amerge_attrib_t)]
    rk_aiq_user_api2_amerge_GetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_amerge.h: 35
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_amerge_v10_SetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_amerge_v10_SetAttrib = _lib.get("rk_aiq_user_api2_amerge_v10_SetAttrib", "cdecl")
    rk_aiq_user_api2_amerge_v10_SetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(mergeAttrV10_t)]
    rk_aiq_user_api2_amerge_v10_SetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_amerge.h: 37
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_amerge_v10_GetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_amerge_v10_GetAttrib = _lib.get("rk_aiq_user_api2_amerge_v10_GetAttrib", "cdecl")
    rk_aiq_user_api2_amerge_v10_GetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(mergeAttrV10_t)]
    rk_aiq_user_api2_amerge_v10_GetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_amerge.h: 39
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_amerge_v11_SetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_amerge_v11_SetAttrib = _lib.get("rk_aiq_user_api2_amerge_v11_SetAttrib", "cdecl")
    rk_aiq_user_api2_amerge_v11_SetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(mergeAttrV11_t)]
    rk_aiq_user_api2_amerge_v11_SetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_amerge.h: 41
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_amerge_v11_GetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_amerge_v11_GetAttrib = _lib.get("rk_aiq_user_api2_amerge_v11_GetAttrib", "cdecl")
    rk_aiq_user_api2_amerge_v11_GetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(mergeAttrV11_t)]
    rk_aiq_user_api2_amerge_v11_GetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_amerge.h: 43
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_amerge_v12_SetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_amerge_v12_SetAttrib = _lib.get("rk_aiq_user_api2_amerge_v12_SetAttrib", "cdecl")
    rk_aiq_user_api2_amerge_v12_SetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(mergeAttrV12_t)]
    rk_aiq_user_api2_amerge_v12_SetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_amerge.h: 45
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_amerge_v12_GetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_amerge_v12_GetAttrib = _lib.get("rk_aiq_user_api2_amerge_v12_GetAttrib", "cdecl")
    rk_aiq_user_api2_amerge_v12_GetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(mergeAttrV12_t)]
    rk_aiq_user_api2_amerge_v12_GetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_anr.h: 35
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_anr_SetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_anr_SetAttrib = _lib.get("rk_aiq_user_api2_anr_SetAttrib", "cdecl")
    rk_aiq_user_api2_anr_SetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_nr_attrib_t)]
    rk_aiq_user_api2_anr_SetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_anr.h: 37
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_anr_GetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_anr_GetAttrib = _lib.get("rk_aiq_user_api2_anr_GetAttrib", "cdecl")
    rk_aiq_user_api2_anr_GetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_nr_attrib_t)]
    rk_aiq_user_api2_anr_GetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_anr.h: 39
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_anr_SetIQPara", "cdecl"):
        continue
    rk_aiq_user_api2_anr_SetIQPara = _lib.get("rk_aiq_user_api2_anr_SetIQPara", "cdecl")
    rk_aiq_user_api2_anr_SetIQPara.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_nr_IQPara_t)]
    rk_aiq_user_api2_anr_SetIQPara.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_anr.h: 41
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_anr_GetIQPara", "cdecl"):
        continue
    rk_aiq_user_api2_anr_GetIQPara = _lib.get("rk_aiq_user_api2_anr_GetIQPara", "cdecl")
    rk_aiq_user_api2_anr_GetIQPara.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_nr_IQPara_t)]
    rk_aiq_user_api2_anr_GetIQPara.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_anr.h: 43
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_anr_SetLumaSFStrength", "cdecl"):
        continue
    rk_aiq_user_api2_anr_SetLumaSFStrength = _lib.get("rk_aiq_user_api2_anr_SetLumaSFStrength", "cdecl")
    rk_aiq_user_api2_anr_SetLumaSFStrength.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_float]
    rk_aiq_user_api2_anr_SetLumaSFStrength.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_anr.h: 45
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_anr_SetLumaTFStrength", "cdecl"):
        continue
    rk_aiq_user_api2_anr_SetLumaTFStrength = _lib.get("rk_aiq_user_api2_anr_SetLumaTFStrength", "cdecl")
    rk_aiq_user_api2_anr_SetLumaTFStrength.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_float]
    rk_aiq_user_api2_anr_SetLumaTFStrength.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_anr.h: 47
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_anr_GetLumaSFStrength", "cdecl"):
        continue
    rk_aiq_user_api2_anr_GetLumaSFStrength = _lib.get("rk_aiq_user_api2_anr_GetLumaSFStrength", "cdecl")
    rk_aiq_user_api2_anr_GetLumaSFStrength.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(c_float)]
    rk_aiq_user_api2_anr_GetLumaSFStrength.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_anr.h: 49
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_anr_GetLumaTFStrength", "cdecl"):
        continue
    rk_aiq_user_api2_anr_GetLumaTFStrength = _lib.get("rk_aiq_user_api2_anr_GetLumaTFStrength", "cdecl")
    rk_aiq_user_api2_anr_GetLumaTFStrength.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(c_float)]
    rk_aiq_user_api2_anr_GetLumaTFStrength.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_anr.h: 51
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_anr_SetChromaSFStrength", "cdecl"):
        continue
    rk_aiq_user_api2_anr_SetChromaSFStrength = _lib.get("rk_aiq_user_api2_anr_SetChromaSFStrength", "cdecl")
    rk_aiq_user_api2_anr_SetChromaSFStrength.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_float]
    rk_aiq_user_api2_anr_SetChromaSFStrength.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_anr.h: 53
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_anr_SetChromaTFStrength", "cdecl"):
        continue
    rk_aiq_user_api2_anr_SetChromaTFStrength = _lib.get("rk_aiq_user_api2_anr_SetChromaTFStrength", "cdecl")
    rk_aiq_user_api2_anr_SetChromaTFStrength.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_float]
    rk_aiq_user_api2_anr_SetChromaTFStrength.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_anr.h: 55
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_anr_GetChromaSFStrength", "cdecl"):
        continue
    rk_aiq_user_api2_anr_GetChromaSFStrength = _lib.get("rk_aiq_user_api2_anr_GetChromaSFStrength", "cdecl")
    rk_aiq_user_api2_anr_GetChromaSFStrength.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(c_float)]
    rk_aiq_user_api2_anr_GetChromaSFStrength.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_anr.h: 57
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_anr_GetChromaTFStrength", "cdecl"):
        continue
    rk_aiq_user_api2_anr_GetChromaTFStrength = _lib.get("rk_aiq_user_api2_anr_GetChromaTFStrength", "cdecl")
    rk_aiq_user_api2_anr_GetChromaTFStrength.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(c_float)]
    rk_aiq_user_api2_anr_GetChromaTFStrength.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_anr.h: 59
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_anr_SetRawnrSFStrength", "cdecl"):
        continue
    rk_aiq_user_api2_anr_SetRawnrSFStrength = _lib.get("rk_aiq_user_api2_anr_SetRawnrSFStrength", "cdecl")
    rk_aiq_user_api2_anr_SetRawnrSFStrength.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_float]
    rk_aiq_user_api2_anr_SetRawnrSFStrength.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_anr.h: 61
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_anr_GetRawnrSFStrength", "cdecl"):
        continue
    rk_aiq_user_api2_anr_GetRawnrSFStrength = _lib.get("rk_aiq_user_api2_anr_GetRawnrSFStrength", "cdecl")
    rk_aiq_user_api2_anr_GetRawnrSFStrength.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(c_float)]
    rk_aiq_user_api2_anr_GetRawnrSFStrength.restype = XCamReturn
    break

enum_Asharp3_OPMode_e = c_int# /usr/include/rkaiq/algos/asharp3/rk_aiq_types_asharp_algo_int_v3.h: 84

Asharp3_OPMode_t = enum_Asharp3_OPMode_e# /usr/include/rkaiq/algos/asharp3/rk_aiq_types_asharp_algo_int_v3.h: 84

# /usr/include/rkaiq/algos/asharp3/rk_aiq_types_asharp_algo_int_v3.h: 146
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

RK_SHARP_Params_V3_t = struct_RK_SHARP_Params_V3_s# /usr/include/rkaiq/algos/asharp3/rk_aiq_types_asharp_algo_int_v3.h: 146

# /usr/include/rkaiq/algos/asharp3/rk_aiq_types_asharp_algo_int_v3.h: 185
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

RK_SHARP_Params_V3_Select_t = struct_RK_SHARP_Params_V3_Select_s# /usr/include/rkaiq/algos/asharp3/rk_aiq_types_asharp_algo_int_v3.h: 185

# /usr/include/rkaiq/algos/asharp3/rk_aiq_types_asharp_algo_int_v3.h: 192
class struct_Asharp_Manual_Attr_V3_s(Structure):
    pass

struct_Asharp_Manual_Attr_V3_s.__slots__ = [
    'stSelect',
]
struct_Asharp_Manual_Attr_V3_s._fields_ = [
    ('stSelect', RK_SHARP_Params_V3_Select_t),
]

Asharp_Manual_Attr_V3_t = struct_Asharp_Manual_Attr_V3_s# /usr/include/rkaiq/algos/asharp3/rk_aiq_types_asharp_algo_int_v3.h: 192

# /usr/include/rkaiq/algos/asharp3/rk_aiq_types_asharp_algo_int_v3.h: 201
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

Asharp_Auto_Attr_V3_t = struct_Asharp_Auto_Attr_V3_s# /usr/include/rkaiq/algos/asharp3/rk_aiq_types_asharp_algo_int_v3.h: 201

# /usr/include/rkaiq/algos/asharp3/rk_aiq_types_asharp_algo_int_v3.h: 226
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

rk_aiq_sharp_attrib_v3_t = struct_rk_aiq_sharp_attrib_v3_s# /usr/include/rkaiq/algos/asharp3/rk_aiq_types_asharp_algo_int_v3.h: 226

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_asharp_v3.h: 31
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_asharpV3_SetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_asharpV3_SetAttrib = _lib.get("rk_aiq_user_api2_asharpV3_SetAttrib", "cdecl")
    rk_aiq_user_api2_asharpV3_SetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_sharp_attrib_v3_t)]
    rk_aiq_user_api2_asharpV3_SetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_asharp_v3.h: 34
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_asharpV3_GetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_asharpV3_GetAttrib = _lib.get("rk_aiq_user_api2_asharpV3_GetAttrib", "cdecl")
    rk_aiq_user_api2_asharpV3_GetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_sharp_attrib_v3_t)]
    rk_aiq_user_api2_asharpV3_GetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_asharp_v3.h: 37
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_asharpV3_SetStrength", "cdecl"):
        continue
    rk_aiq_user_api2_asharpV3_SetStrength = _lib.get("rk_aiq_user_api2_asharpV3_SetStrength", "cdecl")
    rk_aiq_user_api2_asharpV3_SetStrength.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_float]
    rk_aiq_user_api2_asharpV3_SetStrength.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_asharp_v3.h: 40
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_asharpV3_GetStrength", "cdecl"):
        continue
    rk_aiq_user_api2_asharpV3_GetStrength = _lib.get("rk_aiq_user_api2_asharpV3_GetStrength", "cdecl")
    rk_aiq_user_api2_asharpV3_GetStrength.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(c_float)]
    rk_aiq_user_api2_asharpV3_GetStrength.restype = XCamReturn
    break

# /usr/include/rkaiq/iq_parser_v2/sharp_uapi_head_v33.h: 137
class struct_RK_SHARP_Params_V33_Select_s(Structure):
    pass

struct_RK_SHARP_Params_V33_Select_s.__slots__ = [
    'enable',
    'sharp_ratio_seperate_en',
    'kernel_sigma_enable',
    'Center_Mode',
    'exgain_bypass',
    'luma_point',
    'luma_sigma',
    'hf_clip',
    'pbf_gain',
    'pbf_ratio',
    'pbf_add',
    'gaus_ratio',
    'sharp_ratio',
    'sharp_ratio_0',
    'sharp_ratio_1',
    'bf_gain',
    'bf_ratio',
    'bf_add',
    'global_gain',
    'global_gain_alpha',
    'local_gainscale',
    'global_hf_clip_pos',
    'noiseclip_strength',
    'enhance_bit',
    'noiseclip_mode',
    'noise_sigma_clip',
    'gain_adj_sharp_strength',
    'dis_adj_sharp_strength',
    'prefilter_sigma',
    'hfBilateralFilter_sigma',
    'GaussianFilter_sigma',
    'GaussianFilter_radius',
    'GaussianFilter_sigma_0',
    'GaussianFilter_sigma_1',
    'GaussianFilter_radius_0',
    'GaussianFilter_radius_1',
    'prefilter_coeff',
    'GaussianFilter_coeff',
    'hfBilateralFilter_coeff',
    'GaussianFilter_coeff_0',
    'GaussianFilter_coeff_1',
]
struct_RK_SHARP_Params_V33_Select_s._fields_ = [
    ('enable', c_bool),
    ('sharp_ratio_seperate_en', c_bool),
    ('kernel_sigma_enable', c_bool),
    ('Center_Mode', c_bool),
    ('exgain_bypass', c_bool),
    ('luma_point', uint16_t * int(8)),
    ('luma_sigma', uint16_t * int(8)),
    ('hf_clip', uint16_t * int(8)),
    ('pbf_gain', c_float),
    ('pbf_ratio', c_float),
    ('pbf_add', c_float),
    ('gaus_ratio', c_float),
    ('sharp_ratio', c_float),
    ('sharp_ratio_0', c_float),
    ('sharp_ratio_1', c_float),
    ('bf_gain', c_float),
    ('bf_ratio', c_float),
    ('bf_add', c_float),
    ('global_gain', c_float),
    ('global_gain_alpha', c_float),
    ('local_gainscale', c_float),
    ('global_hf_clip_pos', uint8_t),
    ('noiseclip_strength', c_float),
    ('enhance_bit', uint8_t),
    ('noiseclip_mode', c_bool),
    ('noise_sigma_clip', uint16_t),
    ('gain_adj_sharp_strength', c_float * int(14)),
    ('dis_adj_sharp_strength', c_float * int(22)),
    ('prefilter_sigma', c_float),
    ('hfBilateralFilter_sigma', c_float),
    ('GaussianFilter_sigma', c_float),
    ('GaussianFilter_radius', uint8_t),
    ('GaussianFilter_sigma_0', c_float),
    ('GaussianFilter_sigma_1', c_float),
    ('GaussianFilter_radius_0', uint8_t),
    ('GaussianFilter_radius_1', uint8_t),
    ('prefilter_coeff', c_float * int(3)),
    ('GaussianFilter_coeff', c_float * int(6)),
    ('hfBilateralFilter_coeff', c_float * int(3)),
    ('GaussianFilter_coeff_0', c_float * int(6)),
    ('GaussianFilter_coeff_1', c_float * int(6)),
]

RK_SHARP_Params_V33_Select_t = struct_RK_SHARP_Params_V33_Select_s# /usr/include/rkaiq/iq_parser_v2/sharp_uapi_head_v33.h: 137

# /usr/include/rkaiq/iq_parser_v2/sharp_uapi_head_v33.h: 247
class struct_RK_SHARP_Params_V33LT_Select_s(Structure):
    pass

struct_RK_SHARP_Params_V33LT_Select_s.__slots__ = [
    'enable',
    'sharp_ratio_seperate_en',
    'kernel_sigma_enable',
    'Center_Mode',
    'exgain_bypass',
    'clip_hf_mode',
    'add_mode',
    'luma_point',
    'luma_sigma',
    'hf_clip',
    'hf_clip_neg',
    'local_sharp_strength',
    'pbf_gain',
    'pbf_ratio',
    'pbf_add',
    'gaus_ratio',
    'sharp_ratio',
    'sharp_ratio_0',
    'sharp_ratio_1',
    'bf_gain',
    'bf_ratio',
    'bf_add',
    'global_gain',
    'global_gain_alpha',
    'local_gainscale',
    'gain_adj_sharp_strength',
    'dis_adj_sharp_strength',
    'prefilter_sigma',
    'hfBilateralFilter_sigma',
    'GaussianFilter_sigma',
    'GaussianFilter_radius',
    'GaussianFilter_sigma_0',
    'GaussianFilter_sigma_1',
    'GaussianFilter_radius_0',
    'GaussianFilter_radius_1',
    'prefilter_coeff',
    'GaussianFilter_coeff',
    'hfBilateralFilter_coeff',
    'GaussianFilter_coeff_0',
    'GaussianFilter_coeff_1',
]
struct_RK_SHARP_Params_V33LT_Select_s._fields_ = [
    ('enable', c_bool),
    ('sharp_ratio_seperate_en', c_bool),
    ('kernel_sigma_enable', c_bool),
    ('Center_Mode', c_bool),
    ('exgain_bypass', c_bool),
    ('clip_hf_mode', c_bool),
    ('add_mode', c_bool),
    ('luma_point', uint16_t * int(8)),
    ('luma_sigma', uint16_t * int(8)),
    ('hf_clip', uint16_t * int(8)),
    ('hf_clip_neg', uint16_t * int(8)),
    ('local_sharp_strength', c_float * int(8)),
    ('pbf_gain', c_float),
    ('pbf_ratio', c_float),
    ('pbf_add', c_float),
    ('gaus_ratio', c_float),
    ('sharp_ratio', c_float),
    ('sharp_ratio_0', c_float),
    ('sharp_ratio_1', c_float),
    ('bf_gain', c_float),
    ('bf_ratio', c_float),
    ('bf_add', c_float),
    ('global_gain', c_float),
    ('global_gain_alpha', c_float),
    ('local_gainscale', c_float),
    ('gain_adj_sharp_strength', c_float * int(14)),
    ('dis_adj_sharp_strength', c_float * int(22)),
    ('prefilter_sigma', c_float),
    ('hfBilateralFilter_sigma', c_float),
    ('GaussianFilter_sigma', c_float),
    ('GaussianFilter_radius', uint8_t),
    ('GaussianFilter_sigma_0', c_float),
    ('GaussianFilter_sigma_1', c_float),
    ('GaussianFilter_radius_0', uint8_t),
    ('GaussianFilter_radius_1', uint8_t),
    ('prefilter_coeff', c_float * int(3)),
    ('GaussianFilter_coeff', c_float * int(6)),
    ('hfBilateralFilter_coeff', c_float * int(3)),
    ('GaussianFilter_coeff_0', c_float * int(6)),
    ('GaussianFilter_coeff_1', c_float * int(6)),
]

RK_SHARP_Params_V33LT_Select_t = struct_RK_SHARP_Params_V33LT_Select_s# /usr/include/rkaiq/iq_parser_v2/sharp_uapi_head_v33.h: 247

# /usr/include/rkaiq/iq_parser_v2/sharp_uapi_head_v33.h: 278
class struct_Asharp_ExpInfo_V33_s(Structure):
    pass

struct_Asharp_ExpInfo_V33_s.__slots__ = [
    'hdr_mode',
    'snr_mode',
    'arTime',
    'arAGain',
    'arDGain',
    'isp_dgain',
    'blc_ob_predgain',
    'arIso',
    'isoLevelLow',
    'isoLevelHig',
    'rawWidth',
    'rawHeight',
]
struct_Asharp_ExpInfo_V33_s._fields_ = [
    ('hdr_mode', c_int),
    ('snr_mode', c_int),
    ('arTime', c_float * int(3)),
    ('arAGain', c_float * int(3)),
    ('arDGain', c_float * int(3)),
    ('isp_dgain', c_float * int(3)),
    ('blc_ob_predgain', c_float),
    ('arIso', c_int * int(3)),
    ('isoLevelLow', c_int),
    ('isoLevelHig', c_int),
    ('rawWidth', c_int),
    ('rawHeight', c_int),
]

Asharp_ExpInfo_V33_t = struct_Asharp_ExpInfo_V33_s# /usr/include/rkaiq/iq_parser_v2/sharp_uapi_head_v33.h: 278

# /usr/include/rkaiq/iq_parser_v2/sharp_uapi_head_v33.h: 288
class struct_rk_aiq_sharp_info_v33_s(Structure):
    pass

struct_rk_aiq_sharp_info_v33_s.__slots__ = [
    'sync',
    'iso',
    'expo_info',
]
struct_rk_aiq_sharp_info_v33_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('iso', c_int),
    ('expo_info', Asharp_ExpInfo_V33_t),
]

rk_aiq_sharp_info_v33_t = struct_rk_aiq_sharp_info_v33_s# /usr/include/rkaiq/iq_parser_v2/sharp_uapi_head_v33.h: 288

enum_Asharp_OPMode_V33_e = c_int# /usr/include/rkaiq/algos/asharpV33/rk_aiq_types_asharp_algo_int_v33.h: 85

Asharp_OPMode_V33_t = enum_Asharp_OPMode_V33_e# /usr/include/rkaiq/algos/asharpV33/rk_aiq_types_asharp_algo_int_v33.h: 85

# /usr/include/rkaiq/algos/asharpV33/rk_aiq_types_asharp_algo_int_v33.h: 168
class struct_RK_SHARP_Params_V33_s(Structure):
    pass

struct_RK_SHARP_Params_V33_s.__slots__ = [
    'enable',
    'sharp_ratio_seperate_en',
    'kernel_sigma_enable',
    'version',
    'Center_Mode',
    'center_x',
    'center_y',
    'iso',
    'sharpParamsISO',
]
struct_RK_SHARP_Params_V33_s._fields_ = [
    ('enable', c_int),
    ('sharp_ratio_seperate_en', c_int),
    ('kernel_sigma_enable', c_int),
    ('version', c_char * int(64)),
    ('Center_Mode', c_int),
    ('center_x', c_int),
    ('center_y', c_int),
    ('iso', c_int * int(13)),
    ('sharpParamsISO', RK_SHARP_Params_V33_Select_t * int(13)),
]

RK_SHARP_Params_V33_t = struct_RK_SHARP_Params_V33_s# /usr/include/rkaiq/algos/asharpV33/rk_aiq_types_asharp_algo_int_v33.h: 168

# /usr/include/rkaiq/algos/asharpV33/rk_aiq_types_asharp_algo_int_v33.h: 175
class struct_Asharp_Manual_Attr_V33_s(Structure):
    pass

struct_Asharp_Manual_Attr_V33_s.__slots__ = [
    'stSelect',
    'stFix',
]
struct_Asharp_Manual_Attr_V33_s._fields_ = [
    ('stSelect', RK_SHARP_Params_V33_Select_t),
    ('stFix', RK_SHARP_Fix_V33_t),
]

Asharp_Manual_Attr_V33_t = struct_Asharp_Manual_Attr_V33_s# /usr/include/rkaiq/algos/asharpV33/rk_aiq_types_asharp_algo_int_v33.h: 175

# /usr/include/rkaiq/algos/asharpV33/rk_aiq_types_asharp_algo_int_v33.h: 183
class struct_Asharp_Auto_Attr_V33_s(Structure):
    pass

struct_Asharp_Auto_Attr_V33_s.__slots__ = [
    'stParams',
    'stSelect',
]
struct_Asharp_Auto_Attr_V33_s._fields_ = [
    ('stParams', RK_SHARP_Params_V33_t),
    ('stSelect', RK_SHARP_Params_V33_Select_t),
]

Asharp_Auto_Attr_V33_t = struct_Asharp_Auto_Attr_V33_s# /usr/include/rkaiq/algos/asharpV33/rk_aiq_types_asharp_algo_int_v33.h: 183

# /usr/include/rkaiq/algos/asharpV33/rk_aiq_types_asharp_algo_int_v33.h: 199
class struct_RK_SHARP_Params_V33LT_s(Structure):
    pass

struct_RK_SHARP_Params_V33LT_s.__slots__ = [
    'enable',
    'sharp_ratio_seperate_en',
    'kernel_sigma_enable',
    'version',
    'Center_Mode',
    'center_x',
    'center_y',
    'iso',
    'sharpParamsISO',
]
struct_RK_SHARP_Params_V33LT_s._fields_ = [
    ('enable', c_int),
    ('sharp_ratio_seperate_en', c_int),
    ('kernel_sigma_enable', c_int),
    ('version', c_char * int(64)),
    ('Center_Mode', c_int),
    ('center_x', c_int),
    ('center_y', c_int),
    ('iso', c_int * int(13)),
    ('sharpParamsISO', RK_SHARP_Params_V33LT_Select_t * int(13)),
]

RK_SHARP_Params_V33LT_t = struct_RK_SHARP_Params_V33LT_s# /usr/include/rkaiq/algos/asharpV33/rk_aiq_types_asharp_algo_int_v33.h: 199

# /usr/include/rkaiq/algos/asharpV33/rk_aiq_types_asharp_algo_int_v33.h: 206
class struct_Asharp_Manual_Attr_V33LT_s(Structure):
    pass

struct_Asharp_Manual_Attr_V33LT_s.__slots__ = [
    'stSelect',
    'stFix',
]
struct_Asharp_Manual_Attr_V33LT_s._fields_ = [
    ('stSelect', RK_SHARP_Params_V33LT_Select_t),
    ('stFix', RK_SHARP_Fix_V33_t),
]

Asharp_Manual_Attr_V33LT_t = struct_Asharp_Manual_Attr_V33LT_s# /usr/include/rkaiq/algos/asharpV33/rk_aiq_types_asharp_algo_int_v33.h: 206

# /usr/include/rkaiq/algos/asharpV33/rk_aiq_types_asharp_algo_int_v33.h: 214
class struct_Asharp_Auto_Attr_V33LT_s(Structure):
    pass

struct_Asharp_Auto_Attr_V33LT_s.__slots__ = [
    'stParams',
    'stSelect',
]
struct_Asharp_Auto_Attr_V33LT_s._fields_ = [
    ('stParams', RK_SHARP_Params_V33LT_t),
    ('stSelect', RK_SHARP_Params_V33LT_Select_t),
]

Asharp_Auto_Attr_V33LT_t = struct_Asharp_Auto_Attr_V33LT_s# /usr/include/rkaiq/algos/asharpV33/rk_aiq_types_asharp_algo_int_v33.h: 214

# /usr/include/rkaiq/algos/asharpV33/rk_aiq_types_asharp_algo_int_v33.h: 243
class struct_rk_aiq_sharp_attrib_v33_s(Structure):
    pass

struct_rk_aiq_sharp_attrib_v33_s.__slots__ = [
    'sync',
    'eMode',
    'stAuto',
    'stManual',
]
struct_rk_aiq_sharp_attrib_v33_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('eMode', Asharp_OPMode_V33_t),
    ('stAuto', Asharp_Auto_Attr_V33_t),
    ('stManual', Asharp_Manual_Attr_V33_t),
]

rk_aiq_sharp_attrib_v33_t = struct_rk_aiq_sharp_attrib_v33_s# /usr/include/rkaiq/algos/asharpV33/rk_aiq_types_asharp_algo_int_v33.h: 243

# /usr/include/rkaiq/algos/asharpV33/rk_aiq_types_asharp_algo_int_v33.h: 251
class struct_rk_aiq_sharp_attrib_v33LT_s(Structure):
    pass

struct_rk_aiq_sharp_attrib_v33LT_s.__slots__ = [
    'sync',
    'eMode',
    'stAuto',
    'stManual',
]
struct_rk_aiq_sharp_attrib_v33LT_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('eMode', Asharp_OPMode_V33_t),
    ('stAuto', Asharp_Auto_Attr_V33LT_t),
    ('stManual', Asharp_Manual_Attr_V33LT_t),
]

rk_aiq_sharp_attrib_v33LT_t = struct_rk_aiq_sharp_attrib_v33LT_s# /usr/include/rkaiq/algos/asharpV33/rk_aiq_types_asharp_algo_int_v33.h: 251

# /usr/include/rkaiq/algos/asharpV33/rk_aiq_types_asharp_algo_int_v33.h: 258
class struct_rk_aiq_sharp_strength_v33_s(Structure):
    pass

struct_rk_aiq_sharp_strength_v33_s.__slots__ = [
    'sync',
    'percent',
    'strength_enable',
]
struct_rk_aiq_sharp_strength_v33_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('percent', c_float),
    ('strength_enable', c_bool),
]

rk_aiq_sharp_strength_v33_t = struct_rk_aiq_sharp_strength_v33_s# /usr/include/rkaiq/algos/asharpV33/rk_aiq_types_asharp_algo_int_v33.h: 258

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_asharp_v33.h: 29
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_asharpV33_SetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_asharpV33_SetAttrib = _lib.get("rk_aiq_user_api2_asharpV33_SetAttrib", "cdecl")
    rk_aiq_user_api2_asharpV33_SetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_sharp_attrib_v33_t)]
    rk_aiq_user_api2_asharpV33_SetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_asharp_v33.h: 32
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_asharpV33_GetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_asharpV33_GetAttrib = _lib.get("rk_aiq_user_api2_asharpV33_GetAttrib", "cdecl")
    rk_aiq_user_api2_asharpV33_GetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_sharp_attrib_v33_t)]
    rk_aiq_user_api2_asharpV33_GetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_asharp_v33.h: 35
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_asharpV33Lite_SetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_asharpV33Lite_SetAttrib = _lib.get("rk_aiq_user_api2_asharpV33Lite_SetAttrib", "cdecl")
    rk_aiq_user_api2_asharpV33Lite_SetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_sharp_attrib_v33LT_t)]
    rk_aiq_user_api2_asharpV33Lite_SetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_asharp_v33.h: 38
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_asharpV33Lite_GetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_asharpV33Lite_GetAttrib = _lib.get("rk_aiq_user_api2_asharpV33Lite_GetAttrib", "cdecl")
    rk_aiq_user_api2_asharpV33Lite_GetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_sharp_attrib_v33LT_t)]
    rk_aiq_user_api2_asharpV33Lite_GetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_asharp_v33.h: 41
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_asharpV33_SetStrength", "cdecl"):
        continue
    rk_aiq_user_api2_asharpV33_SetStrength = _lib.get("rk_aiq_user_api2_asharpV33_SetStrength", "cdecl")
    rk_aiq_user_api2_asharpV33_SetStrength.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_sharp_strength_v33_t)]
    rk_aiq_user_api2_asharpV33_SetStrength.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_asharp_v33.h: 44
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_asharpV33_GetStrength", "cdecl"):
        continue
    rk_aiq_user_api2_asharpV33_GetStrength = _lib.get("rk_aiq_user_api2_asharpV33_GetStrength", "cdecl")
    rk_aiq_user_api2_asharpV33_GetStrength.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_sharp_strength_v33_t)]
    rk_aiq_user_api2_asharpV33_GetStrength.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_asharp_v33.h: 46
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_asharpV33_GetInfo", "cdecl"):
        continue
    rk_aiq_user_api2_asharpV33_GetInfo = _lib.get("rk_aiq_user_api2_asharpV33_GetInfo", "cdecl")
    rk_aiq_user_api2_asharpV33_GetInfo.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_sharp_info_v33_t)]
    rk_aiq_user_api2_asharpV33_GetInfo.restype = XCamReturn
    break

# /usr/include/rkaiq/iq_parser_v2/sharp_uapi_head_v4.h: 101
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

RK_SHARP_Params_V4_Select_t = struct_RK_SHARP_Params_V4_Select_s# /usr/include/rkaiq/iq_parser_v2/sharp_uapi_head_v4.h: 101

# /usr/include/rkaiq/iq_parser_v2/sharp_uapi_head_v4.h: 130
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

Asharp4_ExpInfo_t = struct_Asharp4_ExpInfo_s# /usr/include/rkaiq/iq_parser_v2/sharp_uapi_head_v4.h: 130

# /usr/include/rkaiq/iq_parser_v2/sharp_uapi_head_v4.h: 139
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

rk_aiq_sharp_info_v4_t = struct_rk_aiq_sharp_info_v4_s# /usr/include/rkaiq/iq_parser_v2/sharp_uapi_head_v4.h: 139

enum_Asharp4_OPMode_e = c_int# /usr/include/rkaiq/algos/asharp4/rk_aiq_types_asharp_algo_int_v4.h: 87

Asharp4_OPMode_t = enum_Asharp4_OPMode_e# /usr/include/rkaiq/algos/asharp4/rk_aiq_types_asharp_algo_int_v4.h: 87

# /usr/include/rkaiq/algos/asharp4/rk_aiq_types_asharp_algo_int_v4.h: 130
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

RK_SHARP_Params_V4_t = struct_RK_SHARP_Params_V4_s# /usr/include/rkaiq/algos/asharp4/rk_aiq_types_asharp_algo_int_v4.h: 130

# /usr/include/rkaiq/algos/asharp4/rk_aiq_types_asharp_algo_int_v4.h: 169
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

Asharp_Manual_Attr_V4_t = struct_Asharp_Manual_Attr_V4_s# /usr/include/rkaiq/algos/asharp4/rk_aiq_types_asharp_algo_int_v4.h: 169

# /usr/include/rkaiq/algos/asharp4/rk_aiq_types_asharp_algo_int_v4.h: 178
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

Asharp_Auto_Attr_V4_t = struct_Asharp_Auto_Attr_V4_s# /usr/include/rkaiq/algos/asharp4/rk_aiq_types_asharp_algo_int_v4.h: 178

# /usr/include/rkaiq/algos/asharp4/rk_aiq_types_asharp_algo_int_v4.h: 205
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

rk_aiq_sharp_attrib_v4_t = struct_rk_aiq_sharp_attrib_v4_s# /usr/include/rkaiq/algos/asharp4/rk_aiq_types_asharp_algo_int_v4.h: 205

# /usr/include/rkaiq/algos/asharp4/rk_aiq_types_asharp_algo_int_v4.h: 213
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

rk_aiq_sharp_strength_v4_t = struct_rk_aiq_sharp_strength_v4_s# /usr/include/rkaiq/algos/asharp4/rk_aiq_types_asharp_algo_int_v4.h: 213

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_asharp_v4.h: 31
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_asharpV4_SetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_asharpV4_SetAttrib = _lib.get("rk_aiq_user_api2_asharpV4_SetAttrib", "cdecl")
    rk_aiq_user_api2_asharpV4_SetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_sharp_attrib_v4_t)]
    rk_aiq_user_api2_asharpV4_SetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_asharp_v4.h: 34
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_asharpV4_GetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_asharpV4_GetAttrib = _lib.get("rk_aiq_user_api2_asharpV4_GetAttrib", "cdecl")
    rk_aiq_user_api2_asharpV4_GetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_sharp_attrib_v4_t)]
    rk_aiq_user_api2_asharpV4_GetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_asharp_v4.h: 37
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_asharpV4_SetStrength", "cdecl"):
        continue
    rk_aiq_user_api2_asharpV4_SetStrength = _lib.get("rk_aiq_user_api2_asharpV4_SetStrength", "cdecl")
    rk_aiq_user_api2_asharpV4_SetStrength.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_sharp_strength_v4_t)]
    rk_aiq_user_api2_asharpV4_SetStrength.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_asharp_v4.h: 40
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_asharpV4_GetStrength", "cdecl"):
        continue
    rk_aiq_user_api2_asharpV4_GetStrength = _lib.get("rk_aiq_user_api2_asharpV4_GetStrength", "cdecl")
    rk_aiq_user_api2_asharpV4_GetStrength.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_sharp_strength_v4_t)]
    rk_aiq_user_api2_asharpV4_GetStrength.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_asharp_v4.h: 43
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_asharpV4_GetInfo", "cdecl"):
        continue
    rk_aiq_user_api2_asharpV4_GetInfo = _lib.get("rk_aiq_user_api2_asharpV4_GetInfo", "cdecl")
    rk_aiq_user_api2_asharpV4_GetInfo.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_sharp_info_v4_t)]
    rk_aiq_user_api2_asharpV4_GetInfo.restype = XCamReturn
    break

atmo_attrib_t = tmoAttr_t# /usr/include/rkaiq/algos/atmo/rk_aiq_uapi_atmo_int.h: 13

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_atmo.h: 31
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_atmo_SetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_atmo_SetAttrib = _lib.get("rk_aiq_user_api2_atmo_SetAttrib", "cdecl")
    rk_aiq_user_api2_atmo_SetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), atmo_attrib_t]
    rk_aiq_user_api2_atmo_SetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_atmo.h: 33
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_atmo_GetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_atmo_GetAttrib = _lib.get("rk_aiq_user_api2_atmo_GetAttrib", "cdecl")
    rk_aiq_user_api2_atmo_GetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(atmo_attrib_t)]
    rk_aiq_user_api2_atmo_GetAttrib.restype = XCamReturn
    break

enum_CalibDbV2_Awb_Down_Scale_Mode_e = c_int# /usr/include/rkaiq/iq_parser_v2/awb_head.h: 46

CalibDbV2_Awb_Down_Scale_Mode_t = enum_CalibDbV2_Awb_Down_Scale_Mode_e# /usr/include/rkaiq/iq_parser_v2/awb_head.h: 46

enum_CalibDbV2_Awb_Blk_Stat_V21_e = c_int# /usr/include/rkaiq/iq_parser_v2/awb_head.h: 52

CalibDbV2_Awb_Blk_Stat_V21_t = enum_CalibDbV2_Awb_Blk_Stat_V21_e# /usr/include/rkaiq/iq_parser_v2/awb_head.h: 52

enum_CalibDbV2_Awb_Ext_Range_Dom_e = c_int# /usr/include/rkaiq/iq_parser_v2/awb_head.h: 64

CalibDbV2_Awb_Ext_Range_Dom_t = enum_CalibDbV2_Awb_Ext_Range_Dom_e# /usr/include/rkaiq/iq_parser_v2/awb_head.h: 64

enum_CalibDbV2_Awb_Ext_Range_Mode_s = c_int# /usr/include/rkaiq/iq_parser_v2/awb_head.h: 69

CalibDbV2_Awb_Ext_Range_Mode_t = enum_CalibDbV2_Awb_Ext_Range_Mode_s# /usr/include/rkaiq/iq_parser_v2/awb_head.h: 69

# /usr/include/rkaiq/iq_parser_v2/awb_head.h: 108
class struct_CalibDbV2_Yuv3D_2_Range_Ill_s(Structure):
    pass

struct_CalibDbV2_Yuv3D_2_Range_Ill_s.__slots__ = [
    'thcurve_u',
    'thcure_th',
    'lineVector',
    'disP1P2',
]
struct_CalibDbV2_Yuv3D_2_Range_Ill_s._fields_ = [
    ('thcurve_u', c_float * int(6)),
    ('thcure_th', c_float * int(6)),
    ('lineVector', c_float * int(6)),
    ('disP1P2', c_ubyte),
]

CalibDbV2_Yuv3D_2_Range_Ill_t = struct_CalibDbV2_Yuv3D_2_Range_Ill_s# /usr/include/rkaiq/iq_parser_v2/awb_head.h: 108

# /usr/include/rkaiq/iq_parser_v2/awb_head.h: 124
class struct_CalibDbV2_Tcs_Range_Ill2_s(Structure):
    pass

struct_CalibDbV2_Tcs_Range_Ill2_s.__slots__ = [
    'normal',
    'big',
]
struct_CalibDbV2_Tcs_Range_Ill2_s._fields_ = [
    ('normal', c_float * int(4)),
    ('big', c_float * int(4)),
]

CalibDbV2_Tcs_Range_Ill2_t = struct_CalibDbV2_Tcs_Range_Ill2_s# /usr/include/rkaiq/iq_parser_v2/awb_head.h: 124

# /usr/include/rkaiq/iq_parser_v2/awb_head.h: 131
class struct_CalibDbV2_Uv_Range_Ill_s(Structure):
    pass

struct_CalibDbV2_Uv_Range_Ill_s.__slots__ = [
    'u',
    'v',
]
struct_CalibDbV2_Uv_Range_Ill_s._fields_ = [
    ('u', c_float * int(4)),
    ('v', c_float * int(4)),
]

CalibDbV2_Uv_Range_Ill_t = struct_CalibDbV2_Uv_Range_Ill_s# /usr/include/rkaiq/iq_parser_v2/awb_head.h: 131

enum_CalibDbV2_Awb_DoorType_e = c_int# /usr/include/rkaiq/iq_parser_v2/awb_head.h: 137

CalibDbV2_Awb_DoorType_t = enum_CalibDbV2_Awb_DoorType_e# /usr/include/rkaiq/iq_parser_v2/awb_head.h: 137

enum_CalibDb_Window_Mode_e = c_int# /usr/include/rkaiq/iq_parser_v2/awb_head.h: 167

CalibDb_Window_Mode_t = enum_CalibDb_Window_Mode_e# /usr/include/rkaiq/iq_parser_v2/awb_head.h: 167

# /usr/include/rkaiq/iq_parser_v2/awb_head.h: 174
class struct_CalibDbV2_StatWindow_s(Structure):
    pass

struct_CalibDbV2_StatWindow_s.__slots__ = [
    'mode',
    'window',
]
struct_CalibDbV2_StatWindow_s._fields_ = [
    ('mode', CalibDb_Window_Mode_t),
    ('window', c_float * int(4)),
]

CalibDbV2_StatWindow_t = struct_CalibDbV2_StatWindow_s# /usr/include/rkaiq/iq_parser_v2/awb_head.h: 174

# /usr/include/rkaiq/iq_parser_v2/awb_head.h: 195
class struct_CalibDbV2_Awb_DaylgtClip_Cfg_s(Structure):
    pass

struct_CalibDbV2_Awb_DaylgtClip_Cfg_s.__slots__ = [
    'enable',
    'outdoor_cct_min',
]
struct_CalibDbV2_Awb_DaylgtClip_Cfg_s._fields_ = [
    ('enable', c_bool),
    ('outdoor_cct_min', c_float),
]

CalibDbV2_Awb_DaylgtClip_Cfg_t = struct_CalibDbV2_Awb_DaylgtClip_Cfg_s# /usr/include/rkaiq/iq_parser_v2/awb_head.h: 195

# /usr/include/rkaiq/iq_parser_v2/awb_head.h: 232
class struct_CalibDbV2_Rgb2Tcs_s(Structure):
    pass

struct_CalibDbV2_Rgb2Tcs_s.__slots__ = [
    'pseudoLuminanceWeight',
    'rotationMat',
]
struct_CalibDbV2_Rgb2Tcs_s._fields_ = [
    ('pseudoLuminanceWeight', c_float * int(3)),
    ('rotationMat', c_float * int(9)),
]

CalibDbV2_Rgb2Tcs_t = struct_CalibDbV2_Rgb2Tcs_s# /usr/include/rkaiq/iq_parser_v2/awb_head.h: 232

# /usr/include/rkaiq/iq_parser_v2/awb_head.h: 241
class struct_CalibDbV2_Awb_Sgc_Cblk_s(Structure):
    pass

struct_CalibDbV2_Awb_Sgc_Cblk_s.__slots__ = [
    'index',
    'meanC',
    'meanH',
]
struct_CalibDbV2_Awb_Sgc_Cblk_s._fields_ = [
    ('index', c_ushort),
    ('meanC', c_float),
    ('meanH', c_float),
]

CalibDbV2_Awb_Sgc_Cblk_t = struct_CalibDbV2_Awb_Sgc_Cblk_s# /usr/include/rkaiq/iq_parser_v2/awb_head.h: 241

enum_CalibDbV2_Awb_Mul_Win_Mode_e = c_int# /usr/include/rkaiq/iq_parser_v2/awb_head.h: 281

CalibDbV2_Awb_Mul_Win_Mode_t = enum_CalibDbV2_Awb_Mul_Win_Mode_e# /usr/include/rkaiq/iq_parser_v2/awb_head.h: 281

# /usr/include/rkaiq/iq_parser_v2/awb_head.h: 292
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

CalibDbV2_Awb_Mul_Win_t = struct_CalibDbV2_Awb_Mul_Win_s# /usr/include/rkaiq/iq_parser_v2/awb_head.h: 292

# /usr/include/rkaiq/iq_parser_v2/awb_head.h: 333
class struct_CalibDbV2_Wb_Awb_Prob_Calc_Dt_s(Structure):
    pass

struct_CalibDbV2_Wb_Awb_Prob_Calc_Dt_s.__slots__ = [
    'proDis_THH',
    'proDis_THL',
]
struct_CalibDbV2_Wb_Awb_Prob_Calc_Dt_s._fields_ = [
    ('proDis_THH', c_float),
    ('proDis_THL', c_float),
]

CalibDbV2_Wb_Awb_Prob_Calc_Dt_t = struct_CalibDbV2_Wb_Awb_Prob_Calc_Dt_s# /usr/include/rkaiq/iq_parser_v2/awb_head.h: 333

# /usr/include/rkaiq/iq_parser_v2/awb_head.h: 340
class struct_CalibDbV2_Wb_Awb_Prob_Calc_Lv_s(Structure):
    pass

struct_CalibDbV2_Wb_Awb_Prob_Calc_Lv_s.__slots__ = [
    'outdoorLumaValThLow',
    'outdoorLumaValThHigh',
]
struct_CalibDbV2_Wb_Awb_Prob_Calc_Lv_s._fields_ = [
    ('outdoorLumaValThLow', c_uint),
    ('outdoorLumaValThHigh', c_uint),
]

CalibDbV2_Wb_Awb_Prob_Calc_Lv_t = struct_CalibDbV2_Wb_Awb_Prob_Calc_Lv_s# /usr/include/rkaiq/iq_parser_v2/awb_head.h: 340

# /usr/include/rkaiq/iq_parser_v2/awb_head.h: 347
class struct_CalibDbV2_Wb_Awb_Prob_Calc_Wp_s(Structure):
    pass

struct_CalibDbV2_Wb_Awb_Prob_Calc_Wp_s.__slots__ = [
    'wpNumPercTh',
    'wpNumPercTh2',
]
struct_CalibDbV2_Wb_Awb_Prob_Calc_Wp_s._fields_ = [
    ('wpNumPercTh', c_float),
    ('wpNumPercTh2', c_float),
]

CalibDbV2_Wb_Awb_Prob_Calc_Wp_t = struct_CalibDbV2_Wb_Awb_Prob_Calc_Wp_s# /usr/include/rkaiq/iq_parser_v2/awb_head.h: 347

# /usr/include/rkaiq/iq_parser_v2/awb_head.h: 354
class struct_CalibDbV2_Wb_Awb_Convg_s(Structure):
    pass

struct_CalibDbV2_Wb_Awb_Convg_s.__slots__ = [
    'varThforUnDamp',
    'varThforDamp',
]
struct_CalibDbV2_Wb_Awb_Convg_s._fields_ = [
    ('varThforUnDamp', c_float),
    ('varThforDamp', c_float),
]

CalibDbV2_Wb_Awb_Convg_t = struct_CalibDbV2_Wb_Awb_Convg_s# /usr/include/rkaiq/iq_parser_v2/awb_head.h: 354

# /usr/include/rkaiq/iq_parser_v2/awb_head.h: 385
class struct_CalibDbV2_Awb_DampFactor_s(Structure):
    pass

struct_CalibDbV2_Awb_DampFactor_s.__slots__ = [
    'dFStep',
    'dFMin',
    'dFMax',
    'lvIIRsize',
    'lvVarTh',
]
struct_CalibDbV2_Awb_DampFactor_s._fields_ = [
    ('dFStep', c_float),
    ('dFMin', c_float),
    ('dFMax', c_float),
    ('lvIIRsize', c_int),
    ('lvVarTh', c_float),
]

CalibDbV2_Awb_DampFactor_t = struct_CalibDbV2_Awb_DampFactor_s# /usr/include/rkaiq/iq_parser_v2/awb_head.h: 385

# /usr/include/rkaiq/iq_parser_v2/awb_head.h: 426
class struct_CalibDbV2_Awb_Cct_Lut_Cfg_Lv2_s(Structure):
    pass

struct_CalibDbV2_Awb_Cct_Lut_Cfg_Lv2_s.__slots__ = [
    'ctlData',
    'rgct_in_ds',
    'bgcri_in_ds',
    'rgct_lut_out',
    'bgcri_lut_out',
]
struct_CalibDbV2_Awb_Cct_Lut_Cfg_Lv2_s._fields_ = [
    ('ctlData', c_float),
    ('rgct_in_ds', c_float * int(9)),
    ('bgcri_in_ds', c_float * int(11)),
    ('rgct_lut_out', c_float * int((9 * 11))),
    ('bgcri_lut_out', c_float * int((9 * 11))),
]

CalibDbV2_Awb_Cct_Lut_Cfg_Lv2_t = struct_CalibDbV2_Awb_Cct_Lut_Cfg_Lv2_s# /usr/include/rkaiq/iq_parser_v2/awb_head.h: 426

enum_CalibDbV2_Awb_Ctrl_Dat_Selt_e = c_int# /usr/include/rkaiq/iq_parser_v2/awb_head.h: 432

CalibDbV2_Awb_Ctrl_Dat_Selt_t = enum_CalibDbV2_Awb_Ctrl_Dat_Selt_e# /usr/include/rkaiq/iq_parser_v2/awb_head.h: 432

enum_CalibDbV2_Awb_Gain_Adj_Dat_Sl_e = c_int# /usr/include/rkaiq/iq_parser_v2/awb_head.h: 437

CalibDbV2_Awb_Gain_Adj_Dat_Sl_t = enum_CalibDbV2_Awb_Gain_Adj_Dat_Sl_e# /usr/include/rkaiq/iq_parser_v2/awb_head.h: 437

# /usr/include/rkaiq/iq_parser_v2/awb_head.h: 489
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

CalibDbV2_Awb_gain_offset_cfg_t = struct_CalibDbV2_Awb_gain_offset_cfg_s# /usr/include/rkaiq/iq_parser_v2/awb_head.h: 489

# /usr/include/rkaiq/iq_parser_v2/awb_head.h: 579
class struct_CalibDbV2_Awb_Ava_Site_Rec_s(Structure):
    pass

struct_CalibDbV2_Awb_Ava_Site_Rec_s.__slots__ = [
    'enable',
    'frameNum',
    'fullFileName',
    'avaEnable',
    'wbgainTh',
    'lvValueTh',
]
struct_CalibDbV2_Awb_Ava_Site_Rec_s._fields_ = [
    ('enable', c_bool),
    ('frameNum', c_uint),
    ('fullFileName', c_char * int(100)),
    ('avaEnable', c_bool),
    ('wbgainTh', c_float),
    ('lvValueTh', c_float),
]

CalibDbV2_Awb_Ava_Site_Rec_t = struct_CalibDbV2_Awb_Ava_Site_Rec_s# /usr/include/rkaiq/iq_parser_v2/awb_head.h: 579

# /usr/include/rkaiq/iq_parser_v2/awb_head.h: 675
class struct_CalibDbV2_Awb_Lu_Wgt_En_Th_s(Structure):
    pass

struct_CalibDbV2_Awb_Lu_Wgt_En_Th_s.__slots__ = [
    'wpDiffWeiNoTh',
    'wpDiffWeiLvValueTh',
]
struct_CalibDbV2_Awb_Lu_Wgt_En_Th_s._fields_ = [
    ('wpDiffWeiNoTh', c_float),
    ('wpDiffWeiLvValueTh', c_uint),
]

CalibDbV2_Awb_Lu_Wgt_En_Th_t = struct_CalibDbV2_Awb_Lu_Wgt_En_Th_s# /usr/include/rkaiq/iq_parser_v2/awb_head.h: 675

# /usr/include/rkaiq/iq_parser_v2/awb_head.h: 682
class struct_CalibDbV2_Awb_Lum_Wgt_Lv_Rto_s(Structure):
    pass

struct_CalibDbV2_Awb_Lum_Wgt_Lv_Rto_s.__slots__ = [
    'ratioValue',
    'weight',
]
struct_CalibDbV2_Awb_Lum_Wgt_Lv_Rto_s._fields_ = [
    ('ratioValue', c_float),
    ('weight', c_float * int(9)),
]

CalibDbV2_Awb_Lum_Wgt_Lv_Rto_t = struct_CalibDbV2_Awb_Lum_Wgt_Lv_Rto_s# /usr/include/rkaiq/iq_parser_v2/awb_head.h: 682

enum_CalibDbV2_Awb_Raw_Select_Mode_s = c_int# /usr/include/rkaiq/iq_parser_v2/awb_head.h: 864

CalibDbV2_Awb_Raw_Select_Mode_e = enum_CalibDbV2_Awb_Raw_Select_Mode_s# /usr/include/rkaiq/iq_parser_v2/awb_head.h: 864

# /usr/include/rkaiq/iq_parser_v2/awb_head.h: 871
class struct_CalibDbV2_Awb_Raw_Select_s(Structure):
    pass

struct_CalibDbV2_Awb_Raw_Select_s.__slots__ = [
    'frameChooseMode',
    'frameChoose',
]
struct_CalibDbV2_Awb_Raw_Select_s._fields_ = [
    ('frameChooseMode', CalibDbV2_Awb_Raw_Select_Mode_e),
    ('frameChoose', c_ubyte),
]

CalibDbV2_Awb_Raw_Select_t = struct_CalibDbV2_Awb_Raw_Select_s# /usr/include/rkaiq/iq_parser_v2/awb_head.h: 871

enum_CalibDbV2_Wb_Awb_EarlAct_mdoe_e = c_int# /usr/include/rkaiq/iq_parser_v2/awb_head.h: 943

CalibDbV2_Wb_Awb_EarlAct_mdoe_t = enum_CalibDbV2_Wb_Awb_EarlAct_mdoe_e# /usr/include/rkaiq/iq_parser_v2/awb_head.h: 943

# /usr/include/rkaiq/iq_parser_v2/awb_head.h: 950
class struct_CalibDbV2_Tcs_Range_Ill3_s(Structure):
    pass

struct_CalibDbV2_Tcs_Range_Ill3_s.__slots__ = [
    'normal',
    'big',
]
struct_CalibDbV2_Tcs_Range_Ill3_s._fields_ = [
    ('normal', c_int * int(4)),
    ('big', c_int * int(4)),
]

CalibDbV2_Tcs_Range_Ill3_t = struct_CalibDbV2_Tcs_Range_Ill3_s# /usr/include/rkaiq/iq_parser_v2/awb_head.h: 950

# /usr/include/rkaiq/iq_parser_v2/awb_head.h: 959
class struct_CalibDbV2_Wb_Awb_EarlAct_s(Structure):
    pass

struct_CalibDbV2_Wb_Awb_EarlAct_s.__slots__ = [
    'enable',
    'mode',
    'xyRegion',
]
struct_CalibDbV2_Wb_Awb_EarlAct_s._fields_ = [
    ('enable', c_bool),
    ('mode', CalibDbV2_Wb_Awb_EarlAct_mdoe_t),
    ('xyRegion', CalibDbV2_Tcs_Range_Ill3_t * int(4)),
]

CalibDbV2_Wb_Awb_EarlAct_t = struct_CalibDbV2_Wb_Awb_EarlAct_s# /usr/include/rkaiq/iq_parser_v2/awb_head.h: 959

# /usr/include/rkaiq/iq_parser_v2/awb_uapi_head.h: 127
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

rk_tool_awb_measure_wp_res_fl_t = struct_rk_tool_awb_measure_wp_res_fl_s# /usr/include/rkaiq/iq_parser_v2/awb_uapi_head.h: 127

# /usr/include/rkaiq/iq_parser_v2/awb_uapi_head.h: 134
class struct_rk_tool_awb_blk_res2_fl_s(Structure):
    pass

struct_rk_tool_awb_blk_res2_fl_s.__slots__ = [
    'WpNo',
    'gain',
]
struct_rk_tool_awb_blk_res2_fl_s._fields_ = [
    ('WpNo', c_uint),
    ('gain', c_float * int(4)),
]

rk_tool_awb_blk_res2_fl_t = struct_rk_tool_awb_blk_res2_fl_s# /usr/include/rkaiq/iq_parser_v2/awb_uapi_head.h: 134

# /usr/include/rkaiq/iq_parser_v2/awb_uapi_head.h: 139
class struct_rk_tool_awb_wp_res_light_fl_s(Structure):
    pass

struct_rk_tool_awb_wp_res_light_fl_s.__slots__ = [
    'xYType',
]
struct_rk_tool_awb_wp_res_light_fl_s._fields_ = [
    ('xYType', rk_tool_awb_measure_wp_res_fl_t * int(2)),
]

rk_tool_awb_wp_res_light_fl_t = struct_rk_tool_awb_wp_res_light_fl_s# /usr/include/rkaiq/iq_parser_v2/awb_uapi_head.h: 139

# /usr/include/rkaiq/iq_parser_v2/awb_uapi_head.h: 148
class struct_rk_tool_awb_blk_res_fl_s(Structure):
    pass

struct_rk_tool_awb_blk_res_fl_s.__slots__ = [
    'R',
    'G',
    'B',
]
struct_rk_tool_awb_blk_res_fl_s._fields_ = [
    ('R', c_float),
    ('G', c_float),
    ('B', c_float),
]

rk_tool_awb_blk_res_fl_t = struct_rk_tool_awb_blk_res_fl_s# /usr/include/rkaiq/iq_parser_v2/awb_uapi_head.h: 148

# /usr/include/rkaiq/iq_parser_v2/awb_uapi_head.h: 153
class struct_rk_tool_awb_effect_para1_s(Structure):
    pass

struct_rk_tool_awb_effect_para1_s.__slots__ = [
    'hdrFrameChoose',
]
struct_rk_tool_awb_effect_para1_s._fields_ = [
    ('hdrFrameChoose', c_int),
]

rk_tool_awb_effect_para1_t = struct_rk_tool_awb_effect_para1_s# /usr/include/rkaiq/iq_parser_v2/awb_uapi_head.h: 153

# /usr/include/rkaiq/iq_parser_v2/awb_uapi_head.h: 188
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
    ('light', rk_tool_awb_wp_res_light_fl_t * int(14)),
    ('lightWpResVaLidIll', c_bool * int(14)),
    ('lightWpResVaLid', c_bool),
    ('WpNo', c_int * int(2)),
    ('WpNo2', c_int * int(14)),
    ('blkGwResValid', c_bool),
    ('blkSgcResVaLid', c_bool),
    ('blkSgcResult', rk_tool_awb_blk_res_fl_t * int(225)),
    ('blkWpResVaLid', c_bool),
    ('blkWpResult', rk_tool_awb_blk_res2_fl_t * int(225)),
    ('excWpResValid', c_bool),
    ('excWpRangeResult', rk_tool_awb_measure_wp_res_fl_t * int(4)),
    ('extraLightResult', rk_tool_awb_measure_wp_res_fl_t),
    ('WpNoHist', c_uint * int(8)),
    ('effectHwPara', rk_tool_awb_effect_para1_t),
]

rk_tool_awb_stat_res_full_t = struct_rk_tool_awb_stat_res_full_s# /usr/include/rkaiq/iq_parser_v2/awb_uapi_head.h: 188

# /usr/include/rkaiq/iq_parser_v2/awb_uapi_head.h: 209
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
    ('statisticsStable', c_ubyte),
    ('forceRunAwbFlag', c_bool),
    ('samrtRunAwbFlag2', c_bool),
    ('wbgainMean', (c_float * int(4)) * int(4)),
    ('algMethodStable', c_bool),
]

rk_tool_awb_smart_run_res_t = struct_rk_tool_awb_smart_run_res_s# /usr/include/rkaiq/iq_parser_v2/awb_uapi_head.h: 209

# /usr/include/rkaiq/iq_parser_v2/awb_uapi_head.h: 232
class struct_rk_tool_awb_illInf_s(Structure):
    pass

struct_rk_tool_awb_illInf_s.__slots__ = [
    'illName',
    'gainValue',
    'prob_total',
    'prob_dis',
    'prob_LV',
    'weight',
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
    ('weight', c_float),
    ('spatialGainValue', c_float * int(4)),
    ('prob_WPNO', c_float),
    ('staWeight', c_float),
    ('xyType2Weight', c_float),
]

rk_tool_awb_illInf_t = struct_rk_tool_awb_illInf_s# /usr/include/rkaiq/iq_parser_v2/awb_uapi_head.h: 232

# /usr/include/rkaiq/iq_parser_v2/awb_uapi_head.h: 241
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

rk_tool_color_tempture_info_t = struct_rk_tool_color_tempture_info_s# /usr/include/rkaiq/iq_parser_v2/awb_uapi_head.h: 241

# /usr/include/rkaiq/iq_parser_v2/awb_uapi_head.h: 340
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
    'dsRateWh',
    'dsRateHt',
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
    'wbGainAdjustIn',
    'wbGainAdjust',
    'cctAdjustIn',
    'cctAdjustOut',
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
    ('dsRateWh', uint8_t),
    ('dsRateHt', uint8_t),
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
    ('wbGainAdjustIn', c_float * int(4)),
    ('wbGainAdjust', c_float * int(4)),
    ('cctAdjustIn', rk_tool_color_tempture_info_t),
    ('cctAdjustOut', rk_tool_color_tempture_info_t),
    ('wbGainOffset', c_float * int(4)),
    ('wbGainSmooth', c_float * int(4)),
    ('stat3aAwbLastGainOut', c_float * int(4)),
    ('stat3aAwbGainOut', c_float * int(4)),
    ('algMethod', c_int),
]

rk_tool_awb_strategy_result_t = struct_rk_tool_awb_strategy_result_s# /usr/include/rkaiq/iq_parser_v2/awb_uapi_head.h: 340

enum_rk_aiq_wb_scene_e = c_int# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 42

rk_aiq_wb_scene_t = enum_rk_aiq_wb_scene_e# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 42

# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 47
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

rk_aiq_wb_cct_t = struct_rk_aiq_wb_cct_s# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 47

enum_rk_aiq_wb_mwb_mode_e = c_int# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 66

rk_aiq_wb_mwb_mode_t = enum_rk_aiq_wb_mwb_mode_e# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 66

# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 72
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

# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 77
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

rk_aiq_wb_mwb_attrib_t = struct_rk_aiq_wb_mwb_attrib_s# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 77

enum_rk_aiq_wb_awb_alg_method_s = c_int# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 85

rk_aiq_wb_awb_alg_method_t = enum_rk_aiq_wb_awb_alg_method_s# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 85

enum_rk_aiq_wb_op_mode_s = c_int# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 123

rk_aiq_wb_op_mode_t = enum_rk_aiq_wb_op_mode_s# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 123

# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 129
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

rk_aiq_uapiV2_wb_opMode_t = struct_rk_aiq_uapiV2_wb_opMode_s# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 129

# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 145
class struct_rk_aiq_wb_querry_info_s(Structure):
    pass

struct_rk_aiq_wb_querry_info_s.__slots__ = [
    'gain',
    'cctGloabl',
    'awbConverged',
    'LVValue',
    'stat_gain_glb',
    'stat_gain_blk',
]
struct_rk_aiq_wb_querry_info_s._fields_ = [
    ('gain', rk_aiq_wb_gain_t),
    ('cctGloabl', rk_aiq_wb_cct_t),
    ('awbConverged', c_bool),
    ('LVValue', uint32_t),
    ('stat_gain_glb', rk_aiq_wb_gain_t),
    ('stat_gain_blk', rk_aiq_wb_gain_t),
]

rk_aiq_wb_querry_info_t = struct_rk_aiq_wb_querry_info_s# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 145

# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 185
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

rk_aiq_uapiV2_wb_awb_wbGainAdjustLut_t = struct_rk_aiq_uapiV2_wb_awb_wbGainAdjustLut_s# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 185

# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 195
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

rk_aiq_uapiV2_wb_awb_wbGainAdjust_t = struct_rk_aiq_uapiV2_wb_awb_wbGainAdjust_s# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 195

# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 201
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

rk_aiq_uapiV2_wb_awb_wbGainOffset_t = struct_rk_aiq_uapiV2_wb_awb_wbGainOffset_s# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 201

# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 208
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

rk_aiq_uapiV2_wb_awb_mulWindow_t = struct_rk_aiq_uapiV2_wb_awb_mulWindow_s# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 208

# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 214
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

rk_aiq_uapiV2_wbV30_awb_attrib_t = struct_rk_aiq_uapiV2_wbV21_awb_attrib_s# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 214

# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 229
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

rk_aiq_uapiV2_wbV21_attrib_t = struct_rk_aiq_uapiV2_wbV21_attrib_s# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 229

rk_aiq_uapiV2_wbV30_attrib_t = rk_aiq_uapiV2_wbV21_attrib_t# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 238

# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 244
class struct_rk_aiq_uapiV2_wbV32_awb_mulWindow_s(Structure):
    pass

struct_rk_aiq_uapiV2_wbV32_awb_mulWindow_s.__slots__ = [
    'sync',
    'enable',
    'window',
]
struct_rk_aiq_uapiV2_wbV32_awb_mulWindow_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('enable', c_bool),
    ('window', (c_float * int(4)) * int(4)),
]

rk_aiq_uapiV2_wbV32_awb_mulWindow_t = struct_rk_aiq_uapiV2_wbV32_awb_mulWindow_s# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 244

# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 252
class struct_rk_aiq_uapiV2_wb_awb_cctClipCfg_s(Structure):
    pass

struct_rk_aiq_uapiV2_wb_awb_cctClipCfg_s.__slots__ = [
    'enable',
    'cct',
    'cct_len',
    'cri_bound_up',
    'cri_bound_low',
]
struct_rk_aiq_uapiV2_wb_awb_cctClipCfg_s._fields_ = [
    ('enable', c_bool),
    ('cct', c_float * int(15)),
    ('cct_len', c_int),
    ('cri_bound_up', c_float * int(15)),
    ('cri_bound_low', c_float * int(15)),
]

rk_aiq_uapiV2_wb_awb_cctClipCfg_t = struct_rk_aiq_uapiV2_wb_awb_cctClipCfg_s# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 252

# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 260
class struct_rk_aiq_uapiV2_wbV32_awb_gainAdjust_s(Structure):
    pass

struct_rk_aiq_uapiV2_wbV32_awb_gainAdjust_s.__slots__ = [
    'enable',
    'ctrlDataSelt',
    'adjDataSelt',
    'lutAll',
    'lutAll_len',
]
struct_rk_aiq_uapiV2_wbV32_awb_gainAdjust_s._fields_ = [
    ('enable', c_bool),
    ('ctrlDataSelt', CalibDbV2_Awb_Ctrl_Dat_Selt_t),
    ('adjDataSelt', CalibDbV2_Awb_Gain_Adj_Dat_Sl_t),
    ('lutAll', CalibDbV2_Awb_Cct_Lut_Cfg_Lv2_t * int(8)),
    ('lutAll_len', c_int),
]

rk_aiq_uapiV2_wbV32_awb_gainAdjust_t = struct_rk_aiq_uapiV2_wbV32_awb_gainAdjust_s# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 260

# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 266
class struct_rk_aiq_uapiV2_wb_awb_dampFactor_s(Structure):
    pass

struct_rk_aiq_uapiV2_wb_awb_dampFactor_s.__slots__ = [
    'dFStep',
    'dFMin',
    'dFMax',
]
struct_rk_aiq_uapiV2_wb_awb_dampFactor_s._fields_ = [
    ('dFStep', c_float),
    ('dFMin', c_float),
    ('dFMax', c_float),
]

rk_aiq_uapiV2_wb_awb_dampFactor_t = struct_rk_aiq_uapiV2_wb_awb_dampFactor_s# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 266

# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 284
class struct_rk_aiq_uapiV2_wbV32_awb_attrib_s(Structure):
    pass

struct_rk_aiq_uapiV2_wbV32_awb_attrib_s.__slots__ = [
    'algMtdTp',
    'algMtdTp_valid',
    'dampFactor',
    'dampFactor_valid',
    'wbGainOffset',
    'wbGainOffset_valid',
    'multiWindow',
    'multiWindow_valid',
    'wbGainDaylightClip',
    'wbGainDaylightClip_valid',
    'wbGainClip',
    'wbGainClip_valid',
    'wbGainAdjust',
    'wbGainAdjust_valid',
]
struct_rk_aiq_uapiV2_wbV32_awb_attrib_s._fields_ = [
    ('algMtdTp', rk_aiq_wb_awb_alg_method_t),
    ('algMtdTp_valid', c_bool),
    ('dampFactor', rk_aiq_uapiV2_wb_awb_dampFactor_t),
    ('dampFactor_valid', c_bool),
    ('wbGainOffset', CalibDbV2_Awb_gain_offset_cfg_t),
    ('wbGainOffset_valid', c_bool),
    ('multiWindow', rk_aiq_uapiV2_wbV32_awb_mulWindow_t),
    ('multiWindow_valid', c_bool),
    ('wbGainDaylightClip', CalibDbV2_Awb_DaylgtClip_Cfg_t),
    ('wbGainDaylightClip_valid', c_bool),
    ('wbGainClip', rk_aiq_uapiV2_wb_awb_cctClipCfg_t),
    ('wbGainClip_valid', c_bool),
    ('wbGainAdjust', rk_aiq_uapiV2_wbV32_awb_gainAdjust_t),
    ('wbGainAdjust_valid', c_bool),
]

rk_aiq_uapiV2_wbV32_awb_attrib_t = struct_rk_aiq_uapiV2_wbV32_awb_attrib_s# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 284

# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 293
class struct_rk_aiq_uapiV2_wbV32_attrib_t(Structure):
    pass

struct_rk_aiq_uapiV2_wbV32_attrib_t.__slots__ = [
    'sync',
    'byPass',
    'mode',
    'stManual',
    'stAuto',
]
struct_rk_aiq_uapiV2_wbV32_attrib_t._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('byPass', c_bool),
    ('mode', rk_aiq_wb_op_mode_t),
    ('stManual', rk_aiq_wb_mwb_attrib_t),
    ('stAuto', rk_aiq_uapiV2_wbV32_awb_attrib_t),
]

rk_aiq_uapiV2_wbV32_attrib_t = struct_rk_aiq_uapiV2_wbV32_attrib_t# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 293

# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 301
class struct_rk_aiq_uapiV2_awb_wrtIn_attr_s(Structure):
    pass

struct_rk_aiq_uapiV2_awb_wrtIn_attr_s.__slots__ = [
    'sync',
    'en',
    'mode',
    'path',
    'call_cnt',
]
struct_rk_aiq_uapiV2_awb_wrtIn_attr_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('en', c_bool),
    ('mode', c_int),
    ('path', c_char * int(100)),
    ('call_cnt', c_int),
]

rk_aiq_uapiV2_awb_wrtIn_attr_t = struct_rk_aiq_uapiV2_awb_wrtIn_attr_s# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 301

# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 306
class struct_rk_aiq_uapiV2_awb_ffwbgain_attr_s(Structure):
    pass

struct_rk_aiq_uapiV2_awb_ffwbgain_attr_s.__slots__ = [
    'sync',
    'wggain',
]
struct_rk_aiq_uapiV2_awb_ffwbgain_attr_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('wggain', rk_aiq_wb_gain_t),
]

rk_aiq_uapiV2_awb_ffwbgain_attr_t = struct_rk_aiq_uapiV2_awb_ffwbgain_attr_s# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 306

# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 313
class struct_rk_aiq_uapiV2_awb_ExtR_Wei_V32_s(Structure):
    pass

struct_rk_aiq_uapiV2_awb_ExtR_Wei_V32_s.__slots__ = [
    'lumaValue',
    'lumaValue_len',
    'weight',
    'weight_len',
]
struct_rk_aiq_uapiV2_awb_ExtR_Wei_V32_s._fields_ = [
    ('lumaValue', c_float * int(16)),
    ('lumaValue_len', c_int),
    ('weight', c_float * int(16)),
    ('weight_len', c_int),
]

rk_aiq_uapiV2_awb_ExtR_Wei_V32_t = struct_rk_aiq_uapiV2_awb_ExtR_Wei_V32_s# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 313

# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 324
class struct_rk_aiq_uapiV2_awb_Gain_Lut_Cfg_s(Structure):
    pass

struct_rk_aiq_uapiV2_awb_Gain_Lut_Cfg_s.__slots__ = [
    'ct_grid_num',
    'cri_grid_num',
    'rgct_in_ds',
    'bgcri_in_ds',
    'rgct_lut_out',
    'bgcri_lut_out',
]
struct_rk_aiq_uapiV2_awb_Gain_Lut_Cfg_s._fields_ = [
    ('ct_grid_num', c_int),
    ('cri_grid_num', c_int),
    ('rgct_in_ds', POINTER(c_float)),
    ('bgcri_in_ds', POINTER(c_float)),
    ('rgct_lut_out', POINTER(c_float)),
    ('bgcri_lut_out', POINTER(c_float)),
]

rk_aiq_uapiV2_awb_Gain_Lut_Cfg_t = struct_rk_aiq_uapiV2_awb_Gain_Lut_Cfg_s# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 324

# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 330
class struct_rk_aiq_uapiV2_awb_CamMain_info_s(Structure):
    pass

struct_rk_aiq_uapiV2_awb_CamMain_info_s.__slots__ = [
    'wbgain',
    'fLV',
    'fLV_valid',
]
struct_rk_aiq_uapiV2_awb_CamMain_info_s._fields_ = [
    ('wbgain', rk_aiq_wb_gain_t),
    ('fLV', c_float),
    ('fLV_valid', c_bool),
]

rk_aiq_uapiV2_awb_CamMain_info_t = struct_rk_aiq_uapiV2_awb_CamMain_info_s# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 330

# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 336
class struct_rk_aiq_uapiV2_awb_Slave2Main_Cfg_s(Structure):
    pass

struct_rk_aiq_uapiV2_awb_Slave2Main_Cfg_s.__slots__ = [
    'enable',
    'cct_lut_cfg',
    'camM',
]
struct_rk_aiq_uapiV2_awb_Slave2Main_Cfg_s._fields_ = [
    ('enable', c_bool),
    ('cct_lut_cfg', rk_aiq_uapiV2_awb_Gain_Lut_Cfg_t),
    ('camM', rk_aiq_uapiV2_awb_CamMain_info_t),
]

rk_aiq_uapiV2_awb_Slave2Main_Cfg_t = struct_rk_aiq_uapiV2_awb_Slave2Main_Cfg_s# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 336

# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 343
class struct_rk_aiq_uapiV2_ExtRange_V32_s(Structure):
    pass

struct_rk_aiq_uapiV2_ExtRange_V32_s.__slots__ = [
    'domain',
    'mode',
    'region',
    'weightInculde',
]
struct_rk_aiq_uapiV2_ExtRange_V32_s._fields_ = [
    ('domain', CalibDbV2_Awb_Ext_Range_Dom_t),
    ('mode', CalibDbV2_Awb_Ext_Range_Mode_t),
    ('region', c_int * int(4)),
    ('weightInculde', rk_aiq_uapiV2_awb_ExtR_Wei_V32_t),
]

rk_aiq_uapiV2_ExtRange_V32_t = struct_rk_aiq_uapiV2_ExtRange_V32_s# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 343

# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 349
class struct_rk_aiq_uapiV2_Awb_Luma_Weight_Lv_s(Structure):
    pass

struct_rk_aiq_uapiV2_Awb_Luma_Weight_Lv_s.__slots__ = [
    'LvValue',
    'ratioSet',
    'ratioSet_len',
]
struct_rk_aiq_uapiV2_Awb_Luma_Weight_Lv_s._fields_ = [
    ('LvValue', c_float),
    ('ratioSet', CalibDbV2_Awb_Lum_Wgt_Lv_Rto_t * int(8)),
    ('ratioSet_len', c_int),
]

rk_aiq_uapiV2_Awb_Luma_Weight_Lv_t = struct_rk_aiq_uapiV2_Awb_Luma_Weight_Lv_s# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 349

# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 358
class struct_rk_aiq_uapiV2_Awb_Luma_Weight_s(Structure):
    pass

struct_rk_aiq_uapiV2_Awb_Luma_Weight_s.__slots__ = [
    'enable',
    'wpDiffWeiEnableTh',
    'wpDiffwei_y',
    'perfectBin',
    'wpDiffWeightLvSet',
    'wpDiffWeightLvSet_len',
]
struct_rk_aiq_uapiV2_Awb_Luma_Weight_s._fields_ = [
    ('enable', c_bool),
    ('wpDiffWeiEnableTh', CalibDbV2_Awb_Lu_Wgt_En_Th_t),
    ('wpDiffwei_y', c_ubyte * int(9)),
    ('perfectBin', c_ubyte * int(8)),
    ('wpDiffWeightLvSet', rk_aiq_uapiV2_Awb_Luma_Weight_Lv_t * int(16)),
    ('wpDiffWeightLvSet_len', c_int),
]

rk_aiq_uapiV2_Awb_Luma_Weight_t = struct_rk_aiq_uapiV2_Awb_Luma_Weight_s# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 358

# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 373
class struct_rk_aiq_uapiV2_Awb_Light_V32_s(Structure):
    pass

struct_rk_aiq_uapiV2_Awb_Light_V32_s.__slots__ = [
    'name',
    'doorType',
    'standardGainValue',
    'uvRegion',
    'xyRegion',
    'rtYuvRegion',
    'staWeight',
    'dayGainLvThSet',
    'defaultDayGainLow',
    'defaultDayGainHigh',
    'weight',
]
struct_rk_aiq_uapiV2_Awb_Light_V32_s._fields_ = [
    ('name', c_char * int(20)),
    ('doorType', CalibDbV2_Awb_DoorType_t),
    ('standardGainValue', c_float * int(4)),
    ('uvRegion', CalibDbV2_Uv_Range_Ill_t),
    ('xyRegion', CalibDbV2_Tcs_Range_Ill2_t),
    ('rtYuvRegion', CalibDbV2_Yuv3D_2_Range_Ill_t),
    ('staWeight', c_ubyte * int(16)),
    ('dayGainLvThSet', c_uint * int(2)),
    ('defaultDayGainLow', c_float * int(4)),
    ('defaultDayGainHigh', c_float * int(4)),
    ('weight', rk_aiq_uapiV2_awb_ExtR_Wei_V32_t),
]

rk_aiq_uapiV2_Awb_Light_V32_t = struct_rk_aiq_uapiV2_Awb_Light_V32_s# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 373

# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 387
class struct_rk_aiq_uapiV2_Awb_offset_data_s(Structure):
    pass

struct_rk_aiq_uapiV2_Awb_offset_data_s.__slots__ = [
    'ISO',
    'ISO_len',
    'R_Channel',
    'R_Channel_len',
    'Gr_Channel',
    'Gr_Channel_len',
    'Gb_Channel',
    'Gb_Channel_len',
    'B_Channel',
    'B_Channel_len',
]
struct_rk_aiq_uapiV2_Awb_offset_data_s._fields_ = [
    ('ISO', c_float * int(13)),
    ('ISO_len', c_int),
    ('R_Channel', c_float * int(13)),
    ('R_Channel_len', c_int),
    ('Gr_Channel', c_float * int(13)),
    ('Gr_Channel_len', c_int),
    ('Gb_Channel', c_float * int(13)),
    ('Gb_Channel_len', c_int),
    ('B_Channel', c_float * int(13)),
    ('B_Channel_len', c_int),
]

rk_aiq_uapiV2_Awb_offset_data_t = struct_rk_aiq_uapiV2_Awb_offset_data_s# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 387

# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 392
class struct_rk_aiq_uapiV2_Awb_Blc_s(Structure):
    pass

struct_rk_aiq_uapiV2_Awb_Blc_s.__slots__ = [
    'enable',
    'offset',
]
struct_rk_aiq_uapiV2_Awb_Blc_s._fields_ = [
    ('enable', c_bool),
    ('offset', rk_aiq_uapiV2_Awb_offset_data_t),
]

rk_aiq_uapiV2_Awb_Blc_t = struct_rk_aiq_uapiV2_Awb_Blc_s# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 392

# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 413
class struct_rk_aiq_uapiV2_Awb_Limit_Range_V32_s(Structure):
    pass

struct_rk_aiq_uapiV2_Awb_Limit_Range_V32_s.__slots__ = [
    'lumaValue',
    'lumaValue_len',
    'maxR',
    'maxR_len',
    'minR',
    'minR_len',
    'maxG',
    'maxG_len',
    'minG',
    'minG_len',
    'maxB',
    'maxB_len',
    'minB',
    'minB_len',
    'maxY',
    'maxY_len',
    'minY',
    'minY_len',
]
struct_rk_aiq_uapiV2_Awb_Limit_Range_V32_s._fields_ = [
    ('lumaValue', c_float * int(16)),
    ('lumaValue_len', c_int),
    ('maxR', c_float * int(16)),
    ('maxR_len', c_int),
    ('minR', c_float * int(16)),
    ('minR_len', c_int),
    ('maxG', c_float * int(16)),
    ('maxG_len', c_int),
    ('minG', c_float * int(16)),
    ('minG_len', c_int),
    ('maxB', c_float * int(16)),
    ('maxB_len', c_int),
    ('minB', c_float * int(16)),
    ('minB_len', c_int),
    ('maxY', c_float * int(16)),
    ('maxY_len', c_int),
    ('minY', c_float * int(16)),
    ('minY_len', c_int),
]

rk_aiq_uapiV2_Awb_Limit_Range_V32_t = struct_rk_aiq_uapiV2_Awb_Limit_Range_V32_s# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 413

# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 437
class struct_rk_aiq_uapiV2_Wb_Awb_IqAtPa_V32_s(Structure):
    pass

struct_rk_aiq_uapiV2_Wb_Awb_IqAtPa_V32_s.__slots__ = [
    'rawSelectPara',
    'blc2ForAwb',
    'lscBypass',
    'uvDetectionEnable',
    'xyDetectionEnable',
    'yuvDetectionEnable',
    'blkStatisticsEnable',
    'downScaleMode',
    'blkMeasureMode',
    'mainWindow',
    'limitRange',
    'rgb2TcsPara',
    'rgb2RotationYuvMat',
    'extraWpRange',
    'wpDiffLumaWeight',
    'wpDiffBlkWeiEnable',
    'wpDiffBlkWeight',
    'lightSources',
    'lightSources_len',
    'earlierAwbAct',
]
struct_rk_aiq_uapiV2_Wb_Awb_IqAtPa_V32_s._fields_ = [
    ('rawSelectPara', CalibDbV2_Awb_Raw_Select_t),
    ('blc2ForAwb', rk_aiq_uapiV2_Awb_Blc_t),
    ('lscBypass', c_bool),
    ('uvDetectionEnable', c_bool),
    ('xyDetectionEnable', c_bool),
    ('yuvDetectionEnable', c_bool),
    ('blkStatisticsEnable', c_bool),
    ('downScaleMode', CalibDbV2_Awb_Down_Scale_Mode_t),
    ('blkMeasureMode', CalibDbV2_Awb_Blk_Stat_V21_t),
    ('mainWindow', CalibDbV2_StatWindow_t),
    ('limitRange', rk_aiq_uapiV2_Awb_Limit_Range_V32_t),
    ('rgb2TcsPara', CalibDbV2_Rgb2Tcs_t),
    ('rgb2RotationYuvMat', c_float * int(16)),
    ('extraWpRange', rk_aiq_uapiV2_ExtRange_V32_t * int(7)),
    ('wpDiffLumaWeight', rk_aiq_uapiV2_Awb_Luma_Weight_t),
    ('wpDiffBlkWeiEnable', c_bool),
    ('wpDiffBlkWeight', c_ushort * int(225)),
    ('lightSources', rk_aiq_uapiV2_Awb_Light_V32_t * int(14)),
    ('lightSources_len', c_int),
    ('earlierAwbAct', CalibDbV2_Wb_Awb_EarlAct_t),
]

rk_aiq_uapiV2_Wb_Awb_IqAtPa_V32_t = struct_rk_aiq_uapiV2_Wb_Awb_IqAtPa_V32_s# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 437

# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 446
class struct_rk_aiq_uapiV2_Awb_xyRg_stb_WpTh_s(Structure):
    pass

struct_rk_aiq_uapiV2_Awb_xyRg_stb_WpTh_s.__slots__ = [
    'lumaValue',
    'lumaValue_len',
    'forBigType',
    'forBigType_len',
    'forExtraType',
    'forExtraType_len',
]
struct_rk_aiq_uapiV2_Awb_xyRg_stb_WpTh_s._fields_ = [
    ('lumaValue', c_float * int(16)),
    ('lumaValue_len', c_int),
    ('forBigType', c_float * int(16)),
    ('forBigType_len', c_int),
    ('forExtraType', c_float * int(16)),
    ('forExtraType_len', c_int),
]

rk_aiq_uapiV2_Awb_xyRg_stb_WpTh_t = struct_rk_aiq_uapiV2_Awb_xyRg_stb_WpTh_s# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 446

# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 453
class struct_rk_aiq_uapiV2_Awb_xyRegion_stable_s(Structure):
    pass

struct_rk_aiq_uapiV2_Awb_xyRegion_stable_s.__slots__ = [
    'enable',
    'wpNumTh',
    'xyTypeListSize',
    'varianceLumaTh',
]
struct_rk_aiq_uapiV2_Awb_xyRegion_stable_s._fields_ = [
    ('enable', c_bool),
    ('wpNumTh', rk_aiq_uapiV2_Awb_xyRg_stb_WpTh_t),
    ('xyTypeListSize', c_int),
    ('varianceLumaTh', c_float),
]

rk_aiq_uapiV2_Awb_xyRegion_stable_t = struct_rk_aiq_uapiV2_Awb_xyRegion_stable_s# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 453

# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 459
class struct_rk_aiq_uapiV2_Awb_Sgc_Ls_s(Structure):
    pass

struct_rk_aiq_uapiV2_Awb_Sgc_Ls_s.__slots__ = [
    'name',
    'RGain',
    'BGain',
]
struct_rk_aiq_uapiV2_Awb_Sgc_Ls_s._fields_ = [
    ('name', c_char * int(20)),
    ('RGain', c_float),
    ('BGain', c_float),
]

rk_aiq_uapiV2_Awb_Sgc_Ls_t = struct_rk_aiq_uapiV2_Awb_Sgc_Ls_s# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 459

# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 468
class struct_rk_aiq_uapiV2_Awb_Sgc_s(Structure):
    pass

struct_rk_aiq_uapiV2_Awb_Sgc_s.__slots__ = [
    'enable',
    'colorBlock',
    'colorBlock_len',
    'lsUsedForEstimation',
    'lsUsedForEstimation_len',
    'alpha',
]
struct_rk_aiq_uapiV2_Awb_Sgc_s._fields_ = [
    ('enable', c_bool),
    ('colorBlock', CalibDbV2_Awb_Sgc_Cblk_t * int(16)),
    ('colorBlock_len', c_int),
    ('lsUsedForEstimation', rk_aiq_uapiV2_Awb_Sgc_Ls_t * int(14)),
    ('lsUsedForEstimation_len', c_int),
    ('alpha', c_float),
]

rk_aiq_uapiV2_Awb_Sgc_t = struct_rk_aiq_uapiV2_Awb_Sgc_s# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 468

# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 477
class struct_rk_aiq_uapiV2_Wb_Awb_Div_WpTh_s(Structure):
    pass

struct_rk_aiq_uapiV2_Wb_Awb_Div_WpTh_s.__slots__ = [
    'lumaValue',
    'lumaValue_len',
    'low',
    'low_len',
    'high',
    'high_len',
]
struct_rk_aiq_uapiV2_Wb_Awb_Div_WpTh_s._fields_ = [
    ('lumaValue', c_float * int(16)),
    ('lumaValue_len', c_int),
    ('low', c_float * int(16)),
    ('low_len', c_int),
    ('high', c_float * int(16)),
    ('high_len', c_int),
]

rk_aiq_uapiV2_Wb_Awb_Div_WpTh_t = struct_rk_aiq_uapiV2_Wb_Awb_Div_WpTh_s# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 477

# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 485
class struct_rk_aiq_uapiV2_Wb_Awb_Div_s(Structure):
    pass

struct_rk_aiq_uapiV2_Wb_Awb_Div_s.__slots__ = [
    'lumaValThLow',
    'lumaValThLow2',
    'lumaValThHigh',
    'lumaValThHigh2',
    'wpNumTh',
]
struct_rk_aiq_uapiV2_Wb_Awb_Div_s._fields_ = [
    ('lumaValThLow', c_uint),
    ('lumaValThLow2', c_uint),
    ('lumaValThHigh', c_uint),
    ('lumaValThHigh2', c_uint),
    ('wpNumTh', rk_aiq_uapiV2_Wb_Awb_Div_WpTh_t),
]

rk_aiq_uapiV2_Wb_Awb_Div_t = struct_rk_aiq_uapiV2_Wb_Awb_Div_s# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 485

# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 493
class struct_rk_aiq_uapiV2_Awb_Tolerance_s(Structure):
    pass

struct_rk_aiq_uapiV2_Awb_Tolerance_s.__slots__ = [
    'lumaValue',
    'lumaValue_len',
    'toleranceValue',
    'toleranceValue_len',
]
struct_rk_aiq_uapiV2_Awb_Tolerance_s._fields_ = [
    ('lumaValue', c_float * int(16)),
    ('lumaValue_len', c_int),
    ('toleranceValue', c_float * int(16)),
    ('toleranceValue_len', c_int),
]

rk_aiq_uapiV2_Awb_Tolerance_t = struct_rk_aiq_uapiV2_Awb_Tolerance_s# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 493

# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 500
class struct_rk_aiq_uapiV2_Awb_runinterval_s(Structure):
    pass

struct_rk_aiq_uapiV2_Awb_runinterval_s.__slots__ = [
    'lumaValue',
    'lumaValue_len',
    'intervalValue',
    'intervalValue_len',
]
struct_rk_aiq_uapiV2_Awb_runinterval_s._fields_ = [
    ('lumaValue', c_float * int(16)),
    ('lumaValue_len', c_int),
    ('intervalValue', c_float * int(16)),
    ('intervalValue_len', c_int),
]

rk_aiq_uapiV2_Awb_runinterval_t = struct_rk_aiq_uapiV2_Awb_runinterval_s# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 500

# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 511
class struct_rk_aiq_uapiV2_Awb_SmartRun_cfg_s(Structure):
    pass

struct_rk_aiq_uapiV2_Awb_SmartRun_cfg_s.__slots__ = [
    'lumaValue',
    'lumaValue_len',
    'lvVarTh',
    'lvVarTh_len',
    'wbgainAlgDiffTh',
    'wbgainAlgDiffTh_len',
    'wbgainHwDiffTh',
    'wbgainHwDiffTh_len',
]
struct_rk_aiq_uapiV2_Awb_SmartRun_cfg_s._fields_ = [
    ('lumaValue', c_float * int(16)),
    ('lumaValue_len', c_int),
    ('lvVarTh', c_float * int(16)),
    ('lvVarTh_len', c_int),
    ('wbgainAlgDiffTh', c_float * int(16)),
    ('wbgainAlgDiffTh_len', c_int),
    ('wbgainHwDiffTh', c_float * int(16)),
    ('wbgainHwDiffTh_len', c_int),
]

rk_aiq_uapiV2_Awb_SmartRun_cfg_t = struct_rk_aiq_uapiV2_Awb_SmartRun_cfg_s# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 511

# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 516
class struct_rk_aiq_uapiV2_Awb_SmartRun_s(Structure):
    pass

struct_rk_aiq_uapiV2_Awb_SmartRun_s.__slots__ = [
    'enable',
    'cfg',
]
struct_rk_aiq_uapiV2_Awb_SmartRun_s._fields_ = [
    ('enable', c_bool),
    ('cfg', rk_aiq_uapiV2_Awb_SmartRun_cfg_t),
]

rk_aiq_uapiV2_Awb_SmartRun_t = struct_rk_aiq_uapiV2_Awb_SmartRun_s# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 516

# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 543
class struct_rk_aiq_uapiV2_Wb_Awb_IqAtExtPa_V32_s(Structure):
    pass

struct_rk_aiq_uapiV2_Wb_Awb_IqAtExtPa_V32_s.__slots__ = [
    'lightSourceForFirstFrame',
    'smartRun',
    'tolerance',
    'runInterval',
    'dampFactor',
    'wbGainAdjust',
    'wbGainDaylightClip',
    'wbGainClip',
    'division',
    'defaultNightGain',
    'lumaValueMatrix',
    'defaultNightGainWeight',
    'probCalcDis',
    'probCalcLv',
    'probCalcWp',
    'converged',
    'xyRegionStableSelection',
    'weightForNightGainCalc',
    'weightForNightGainCalc_len',
    'singleColorProces',
    'lineRgBg',
    'lineRgProjCCT',
    'wbGainOffset',
    'avaSiteRec',
]
struct_rk_aiq_uapiV2_Wb_Awb_IqAtExtPa_V32_s._fields_ = [
    ('lightSourceForFirstFrame', c_char * int(20)),
    ('smartRun', rk_aiq_uapiV2_Awb_SmartRun_t),
    ('tolerance', rk_aiq_uapiV2_Awb_Tolerance_t),
    ('runInterval', rk_aiq_uapiV2_Awb_runinterval_t),
    ('dampFactor', CalibDbV2_Awb_DampFactor_t),
    ('wbGainAdjust', rk_aiq_uapiV2_wbV32_awb_gainAdjust_t),
    ('wbGainDaylightClip', CalibDbV2_Awb_DaylgtClip_Cfg_t),
    ('wbGainClip', rk_aiq_uapiV2_wb_awb_cctClipCfg_t),
    ('division', rk_aiq_uapiV2_Wb_Awb_Div_t),
    ('defaultNightGain', c_float * int(4)),
    ('lumaValueMatrix', c_uint * int(16)),
    ('defaultNightGainWeight', c_ubyte * int(16)),
    ('probCalcDis', CalibDbV2_Wb_Awb_Prob_Calc_Dt_t),
    ('probCalcLv', CalibDbV2_Wb_Awb_Prob_Calc_Lv_t),
    ('probCalcWp', CalibDbV2_Wb_Awb_Prob_Calc_Wp_t),
    ('converged', CalibDbV2_Wb_Awb_Convg_t),
    ('xyRegionStableSelection', rk_aiq_uapiV2_Awb_xyRegion_stable_t),
    ('weightForNightGainCalc', c_ubyte * int(16)),
    ('weightForNightGainCalc_len', c_int),
    ('singleColorProces', rk_aiq_uapiV2_Awb_Sgc_t),
    ('lineRgBg', c_float * int(3)),
    ('lineRgProjCCT', c_float * int(3)),
    ('wbGainOffset', CalibDbV2_Awb_gain_offset_cfg_t),
    ('avaSiteRec', CalibDbV2_Awb_Ava_Site_Rec_t),
]

rk_aiq_uapiV2_Wb_Awb_IqAtExtPa_V32_t = struct_rk_aiq_uapiV2_Wb_Awb_IqAtExtPa_V32_s# /usr/include/rkaiq/algos/awb/rk_aiq_types_awb_algo_int.h: 543

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_awb.h: 30
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_awbV21_SetAllAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_awbV21_SetAllAttrib = _lib.get("rk_aiq_user_api2_awbV21_SetAllAttrib", "cdecl")
    rk_aiq_user_api2_awbV21_SetAllAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), rk_aiq_uapiV2_wbV21_attrib_t]
    rk_aiq_user_api2_awbV21_SetAllAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_awb.h: 32
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_awbV21_GetAllAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_awbV21_GetAllAttrib = _lib.get("rk_aiq_user_api2_awbV21_GetAllAttrib", "cdecl")
    rk_aiq_user_api2_awbV21_GetAllAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_uapiV2_wbV21_attrib_t)]
    rk_aiq_user_api2_awbV21_GetAllAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_awb.h: 34
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_awbV30_SetAllAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_awbV30_SetAllAttrib = _lib.get("rk_aiq_user_api2_awbV30_SetAllAttrib", "cdecl")
    rk_aiq_user_api2_awbV30_SetAllAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), rk_aiq_uapiV2_wbV30_attrib_t]
    rk_aiq_user_api2_awbV30_SetAllAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_awb.h: 36
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_awbV30_GetAllAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_awbV30_GetAllAttrib = _lib.get("rk_aiq_user_api2_awbV30_GetAllAttrib", "cdecl")
    rk_aiq_user_api2_awbV30_GetAllAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_uapiV2_wbV30_attrib_t)]
    rk_aiq_user_api2_awbV30_GetAllAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_awb.h: 38
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_awbV32_SetAllAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_awbV32_SetAllAttrib = _lib.get("rk_aiq_user_api2_awbV32_SetAllAttrib", "cdecl")
    rk_aiq_user_api2_awbV32_SetAllAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), rk_aiq_uapiV2_wbV32_attrib_t]
    rk_aiq_user_api2_awbV32_SetAllAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_awb.h: 40
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_awbV32_GetAllAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_awbV32_GetAllAttrib = _lib.get("rk_aiq_user_api2_awbV32_GetAllAttrib", "cdecl")
    rk_aiq_user_api2_awbV32_GetAllAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_uapiV2_wbV32_attrib_t)]
    rk_aiq_user_api2_awbV32_GetAllAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_awb.h: 42
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_awb_GetCCT", "cdecl"):
        continue
    rk_aiq_user_api2_awb_GetCCT = _lib.get("rk_aiq_user_api2_awb_GetCCT", "cdecl")
    rk_aiq_user_api2_awb_GetCCT.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_wb_cct_t)]
    rk_aiq_user_api2_awb_GetCCT.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_awb.h: 44
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_awb_QueryWBInfo", "cdecl"):
        continue
    rk_aiq_user_api2_awb_QueryWBInfo = _lib.get("rk_aiq_user_api2_awb_QueryWBInfo", "cdecl")
    rk_aiq_user_api2_awb_QueryWBInfo.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_wb_querry_info_t)]
    rk_aiq_user_api2_awb_QueryWBInfo.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_awb.h: 46
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_awb_Lock", "cdecl"):
        continue
    rk_aiq_user_api2_awb_Lock = _lib.get("rk_aiq_user_api2_awb_Lock", "cdecl")
    rk_aiq_user_api2_awb_Lock.argtypes = [POINTER(rk_aiq_sys_ctx_t)]
    rk_aiq_user_api2_awb_Lock.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_awb.h: 48
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_awb_Unlock", "cdecl"):
        continue
    rk_aiq_user_api2_awb_Unlock = _lib.get("rk_aiq_user_api2_awb_Unlock", "cdecl")
    rk_aiq_user_api2_awb_Unlock.argtypes = [POINTER(rk_aiq_sys_ctx_t)]
    rk_aiq_user_api2_awb_Unlock.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_awb.h: 50
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_awb_SetWpModeAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_awb_SetWpModeAttrib = _lib.get("rk_aiq_user_api2_awb_SetWpModeAttrib", "cdecl")
    rk_aiq_user_api2_awb_SetWpModeAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), rk_aiq_uapiV2_wb_opMode_t]
    rk_aiq_user_api2_awb_SetWpModeAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_awb.h: 52
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_awb_GetWpModeAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_awb_GetWpModeAttrib = _lib.get("rk_aiq_user_api2_awb_GetWpModeAttrib", "cdecl")
    rk_aiq_user_api2_awb_GetWpModeAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_uapiV2_wb_opMode_t)]
    rk_aiq_user_api2_awb_GetWpModeAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_awb.h: 54
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_awb_SetMwbAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_awb_SetMwbAttrib = _lib.get("rk_aiq_user_api2_awb_SetMwbAttrib", "cdecl")
    rk_aiq_user_api2_awb_SetMwbAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), rk_aiq_wb_mwb_attrib_t]
    rk_aiq_user_api2_awb_SetMwbAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_awb.h: 56
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_awb_GetMwbAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_awb_GetMwbAttrib = _lib.get("rk_aiq_user_api2_awb_GetMwbAttrib", "cdecl")
    rk_aiq_user_api2_awb_GetMwbAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_wb_mwb_attrib_t)]
    rk_aiq_user_api2_awb_GetMwbAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_awb.h: 58
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_awb_SetWbGainAdjustAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_awb_SetWbGainAdjustAttrib = _lib.get("rk_aiq_user_api2_awb_SetWbGainAdjustAttrib", "cdecl")
    rk_aiq_user_api2_awb_SetWbGainAdjustAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), rk_aiq_uapiV2_wb_awb_wbGainAdjust_t]
    rk_aiq_user_api2_awb_SetWbGainAdjustAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_awb.h: 60
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_awb_GetWbGainAdjustAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_awb_GetWbGainAdjustAttrib = _lib.get("rk_aiq_user_api2_awb_GetWbGainAdjustAttrib", "cdecl")
    rk_aiq_user_api2_awb_GetWbGainAdjustAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_uapiV2_wb_awb_wbGainAdjust_t)]
    rk_aiq_user_api2_awb_GetWbGainAdjustAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_awb.h: 62
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_awb_SetWbGainOffsetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_awb_SetWbGainOffsetAttrib = _lib.get("rk_aiq_user_api2_awb_SetWbGainOffsetAttrib", "cdecl")
    rk_aiq_user_api2_awb_SetWbGainOffsetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), rk_aiq_uapiV2_wb_awb_wbGainOffset_t]
    rk_aiq_user_api2_awb_SetWbGainOffsetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_awb.h: 64
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_awb_GetWbGainOffsetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_awb_GetWbGainOffsetAttrib = _lib.get("rk_aiq_user_api2_awb_GetWbGainOffsetAttrib", "cdecl")
    rk_aiq_user_api2_awb_GetWbGainOffsetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_uapiV2_wb_awb_wbGainOffset_t)]
    rk_aiq_user_api2_awb_GetWbGainOffsetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_awb.h: 66
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_awb_SetMultiWindowAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_awb_SetMultiWindowAttrib = _lib.get("rk_aiq_user_api2_awb_SetMultiWindowAttrib", "cdecl")
    rk_aiq_user_api2_awb_SetMultiWindowAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), rk_aiq_uapiV2_wb_awb_mulWindow_t]
    rk_aiq_user_api2_awb_SetMultiWindowAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_awb.h: 68
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_awb_GetMultiWindowAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_awb_GetMultiWindowAttrib = _lib.get("rk_aiq_user_api2_awb_GetMultiWindowAttrib", "cdecl")
    rk_aiq_user_api2_awb_GetMultiWindowAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_uapiV2_wb_awb_mulWindow_t)]
    rk_aiq_user_api2_awb_GetMultiWindowAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_awb.h: 70
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_awb_getStrategyResult", "cdecl"):
        continue
    rk_aiq_user_api2_awb_getStrategyResult = _lib.get("rk_aiq_user_api2_awb_getStrategyResult", "cdecl")
    rk_aiq_user_api2_awb_getStrategyResult.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_tool_awb_strategy_result_t)]
    rk_aiq_user_api2_awb_getStrategyResult.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_awb.h: 72
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_awb_getAlgoSta", "cdecl"):
        continue
    rk_aiq_user_api2_awb_getAlgoSta = _lib.get("rk_aiq_user_api2_awb_getAlgoSta", "cdecl")
    rk_aiq_user_api2_awb_getAlgoSta.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_tool_awb_stat_res_full_t)]
    rk_aiq_user_api2_awb_getAlgoSta.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_awb.h: 74
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_awbV32_SetMultiWindowAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_awbV32_SetMultiWindowAttrib = _lib.get("rk_aiq_user_api2_awbV32_SetMultiWindowAttrib", "cdecl")
    rk_aiq_user_api2_awbV32_SetMultiWindowAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), rk_aiq_uapiV2_wbV32_awb_mulWindow_t]
    rk_aiq_user_api2_awbV32_SetMultiWindowAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_awb.h: 76
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_awbV32_GetMultiWindowAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_awbV32_GetMultiWindowAttrib = _lib.get("rk_aiq_user_api2_awbV32_GetMultiWindowAttrib", "cdecl")
    rk_aiq_user_api2_awbV32_GetMultiWindowAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_uapiV2_wbV32_awb_mulWindow_t)]
    rk_aiq_user_api2_awbV32_GetMultiWindowAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_awb.h: 78
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_awb_WriteAwbIn", "cdecl"):
        continue
    rk_aiq_user_api2_awb_WriteAwbIn = _lib.get("rk_aiq_user_api2_awb_WriteAwbIn", "cdecl")
    rk_aiq_user_api2_awb_WriteAwbIn.argtypes = [POINTER(rk_aiq_sys_ctx_t), rk_aiq_uapiV2_awb_wrtIn_attr_t]
    rk_aiq_user_api2_awb_WriteAwbIn.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_awb.h: 80
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_awb_SetFFWbgainAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_awb_SetFFWbgainAttrib = _lib.get("rk_aiq_user_api2_awb_SetFFWbgainAttrib", "cdecl")
    rk_aiq_user_api2_awb_SetFFWbgainAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), rk_aiq_uapiV2_awb_ffwbgain_attr_t]
    rk_aiq_user_api2_awb_SetFFWbgainAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_awb.h: 82
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_awbV32_SetIQAutoExtPara", "cdecl"):
        continue
    rk_aiq_user_api2_awbV32_SetIQAutoExtPara = _lib.get("rk_aiq_user_api2_awbV32_SetIQAutoExtPara", "cdecl")
    rk_aiq_user_api2_awbV32_SetIQAutoExtPara.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_uapiV2_Wb_Awb_IqAtExtPa_V32_t)]
    rk_aiq_user_api2_awbV32_SetIQAutoExtPara.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_awb.h: 84
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_awbV32_GetIQAutoExtPara", "cdecl"):
        continue
    rk_aiq_user_api2_awbV32_GetIQAutoExtPara = _lib.get("rk_aiq_user_api2_awbV32_GetIQAutoExtPara", "cdecl")
    rk_aiq_user_api2_awbV32_GetIQAutoExtPara.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_uapiV2_Wb_Awb_IqAtExtPa_V32_t)]
    rk_aiq_user_api2_awbV32_GetIQAutoExtPara.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_awb.h: 86
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_awbV32_SetIQAutoPara", "cdecl"):
        continue
    rk_aiq_user_api2_awbV32_SetIQAutoPara = _lib.get("rk_aiq_user_api2_awbV32_SetIQAutoPara", "cdecl")
    rk_aiq_user_api2_awbV32_SetIQAutoPara.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_uapiV2_Wb_Awb_IqAtPa_V32_t)]
    rk_aiq_user_api2_awbV32_SetIQAutoPara.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_awb.h: 88
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_awbV32_GetIQAutoPara", "cdecl"):
        continue
    rk_aiq_user_api2_awbV32_GetIQAutoPara = _lib.get("rk_aiq_user_api2_awbV32_GetIQAutoPara", "cdecl")
    rk_aiq_user_api2_awbV32_GetIQAutoPara.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_uapiV2_Wb_Awb_IqAtPa_V32_t)]
    rk_aiq_user_api2_awbV32_GetIQAutoPara.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_awb.h: 90
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_awb_setAwbPreWbgain", "cdecl"):
        continue
    rk_aiq_user_api2_awb_setAwbPreWbgain = _lib.get("rk_aiq_user_api2_awb_setAwbPreWbgain", "cdecl")
    rk_aiq_user_api2_awb_setAwbPreWbgain.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_float * int(4)]
    rk_aiq_user_api2_awb_setAwbPreWbgain.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_awb.h: 92
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_awb_IqMap2Main", "cdecl"):
        continue
    rk_aiq_user_api2_awb_IqMap2Main = _lib.get("rk_aiq_user_api2_awb_IqMap2Main", "cdecl")
    rk_aiq_user_api2_awb_IqMap2Main.argtypes = [POINTER(rk_aiq_sys_ctx_t), rk_aiq_uapiV2_awb_Slave2Main_Cfg_t]
    rk_aiq_user_api2_awb_IqMap2Main.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_awb.h: 94
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_awb_freeConvertLut", "cdecl"):
        continue
    rk_aiq_user_api2_awb_freeConvertLut = _lib.get("rk_aiq_user_api2_awb_freeConvertLut", "cdecl")
    rk_aiq_user_api2_awb_freeConvertLut.argtypes = [POINTER(rk_aiq_uapiV2_awb_Gain_Lut_Cfg_t)]
    rk_aiq_user_api2_awb_freeConvertLut.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_awb.h: 96
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_awb_loadConvertLut", "cdecl"):
        continue
    rk_aiq_user_api2_awb_loadConvertLut = _lib.get("rk_aiq_user_api2_awb_loadConvertLut", "cdecl")
    rk_aiq_user_api2_awb_loadConvertLut.argtypes = [POINTER(rk_aiq_uapiV2_awb_Gain_Lut_Cfg_t), String]
    rk_aiq_user_api2_awb_loadConvertLut.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_awb.h: 98
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_awb_wbgainConvert2", "cdecl"):
        continue
    rk_aiq_user_api2_awb_wbgainConvert2 = _lib.get("rk_aiq_user_api2_awb_wbgainConvert2", "cdecl")
    rk_aiq_user_api2_awb_wbgainConvert2.argtypes = [rk_aiq_wb_gain_t, POINTER(rk_aiq_uapiV2_awb_Gain_Lut_Cfg_t), POINTER(rk_aiq_wb_gain_t)]
    rk_aiq_user_api2_awb_wbgainConvert2.restype = XCamReturn
    break

enum_Aynr_OPMode_e = c_int# /usr/include/rkaiq/algos/aynr2/rk_aiq_types_aynr_algo_int_v2.h: 69

Aynr_OPMode_t = enum_Aynr_OPMode_e# /usr/include/rkaiq/algos/aynr2/rk_aiq_types_aynr_algo_int_v2.h: 69

# /usr/include/rkaiq/algos/aynr2/rk_aiq_types_aynr_algo_int_v2.h: 126
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

RK_YNR_Params_V2_Select_t = struct_RK_YNR_Params_V2_Select_s# /usr/include/rkaiq/algos/aynr2/rk_aiq_types_aynr_algo_int_v2.h: 126

# /usr/include/rkaiq/algos/aynr2/rk_aiq_types_aynr_algo_int_v2.h: 137
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

RK_YNR_Params_V2_t = struct_RK_YNR_Params_V2_s# /usr/include/rkaiq/algos/aynr2/rk_aiq_types_aynr_algo_int_v2.h: 137

# /usr/include/rkaiq/algos/aynr2/rk_aiq_types_aynr_algo_int_v2.h: 145
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

Aynr_Manual_Attr_V2_t = struct_Aynr_Manual_Attr_V2_s# /usr/include/rkaiq/algos/aynr2/rk_aiq_types_aynr_algo_int_v2.h: 145

# /usr/include/rkaiq/algos/aynr2/rk_aiq_types_aynr_algo_int_v2.h: 155
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

Aynr_Auto_Attr_V2_t = struct_Aynr_Auto_Attr_V2_s# /usr/include/rkaiq/algos/aynr2/rk_aiq_types_aynr_algo_int_v2.h: 155

# /usr/include/rkaiq/algos/aynr2/rk_aiq_types_aynr_algo_int_v2.h: 180
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

rk_aiq_ynr_attrib_v2_t = struct_rk_aiq_ynr_attrib_v2_s# /usr/include/rkaiq/algos/aynr2/rk_aiq_types_aynr_algo_int_v2.h: 180

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_aynr_v2.h: 31
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_aynrV2_SetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_aynrV2_SetAttrib = _lib.get("rk_aiq_user_api2_aynrV2_SetAttrib", "cdecl")
    rk_aiq_user_api2_aynrV2_SetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_ynr_attrib_v2_t)]
    rk_aiq_user_api2_aynrV2_SetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_aynr_v2.h: 34
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_aynrV2_GetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_aynrV2_GetAttrib = _lib.get("rk_aiq_user_api2_aynrV2_GetAttrib", "cdecl")
    rk_aiq_user_api2_aynrV2_GetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_ynr_attrib_v2_t)]
    rk_aiq_user_api2_aynrV2_GetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_aynr_v2.h: 37
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_aynrV2_SetStrength", "cdecl"):
        continue
    rk_aiq_user_api2_aynrV2_SetStrength = _lib.get("rk_aiq_user_api2_aynrV2_SetStrength", "cdecl")
    rk_aiq_user_api2_aynrV2_SetStrength.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_float]
    rk_aiq_user_api2_aynrV2_SetStrength.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_aynr_v2.h: 40
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_aynrV2_GetStrength", "cdecl"):
        continue
    rk_aiq_user_api2_aynrV2_GetStrength = _lib.get("rk_aiq_user_api2_aynrV2_GetStrength", "cdecl")
    rk_aiq_user_api2_aynrV2_GetStrength.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(c_float)]
    rk_aiq_user_api2_aynrV2_GetStrength.restype = XCamReturn
    break

# /usr/include/rkaiq/iq_parser_v2/ynr_uapi_head_v22.h: 143
class struct_RK_YNR_Params_V22_Select_s(Structure):
    pass

struct_RK_YNR_Params_V22_Select_s.__slots__ = [
    'enable',
    'ynr_bft3x3_bypass',
    'ynr_lbft5x5_bypass',
    'ynr_lgft3x3_bypass',
    'ynr_flt1x1_bypass',
    'ynr_nlm11x11_bypass',
    'ynr_thumb_mix_cur_en',
    'lumaPoint',
    'sigma',
    'lo_lumaPoint',
    'lo_ratio',
    'hi_lumaPoint',
    'hi_ratio',
    'lci',
    'hci',
    'ynr_global_gain_alpha',
    'ynr_global_gain',
    'ynr_adjust_thresh',
    'ynr_adjust_scale',
    'rnr_strength',
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
    'hi_bf_scale',
    'hi_gain_alpha',
    'hi_center_weight',
    'hi_weight_offset',
    'hi_min_sigma',
    'hi_nr_weight',
    'hi_filter_coeff1_1',
    'hi_filter_coeff1_2',
    'hi_filter_coeff1_3',
    'hi_filter_coeff2_1',
    'hi_filter_coeff2_2',
    'hi_filter_coeff2_3',
]
struct_RK_YNR_Params_V22_Select_s._fields_ = [
    ('enable', c_bool),
    ('ynr_bft3x3_bypass', c_bool),
    ('ynr_lbft5x5_bypass', c_bool),
    ('ynr_lgft3x3_bypass', c_bool),
    ('ynr_flt1x1_bypass', c_bool),
    ('ynr_nlm11x11_bypass', c_bool),
    ('ynr_thumb_mix_cur_en', c_bool),
    ('lumaPoint', uint16_t * int(((1 << 4) + 1))),
    ('sigma', c_float * int(((1 << 4) + 1))),
    ('lo_lumaPoint', uint16_t * int(6)),
    ('lo_ratio', c_float * int(6)),
    ('hi_lumaPoint', uint16_t * int(6)),
    ('hi_ratio', c_float * int(6)),
    ('lci', c_float),
    ('hci', c_float),
    ('ynr_global_gain_alpha', c_float),
    ('ynr_global_gain', c_float),
    ('ynr_adjust_thresh', c_float),
    ('ynr_adjust_scale', c_float),
    ('rnr_strength', c_float * int(17)),
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
    ('hi_bf_scale', c_float),
    ('hi_gain_alpha', c_float),
    ('hi_center_weight', c_float),
    ('hi_weight_offset', c_float),
    ('hi_min_sigma', c_float),
    ('hi_nr_weight', c_float),
    ('hi_filter_coeff1_1', uint8_t),
    ('hi_filter_coeff1_2', uint8_t),
    ('hi_filter_coeff1_3', uint8_t),
    ('hi_filter_coeff2_1', uint8_t),
    ('hi_filter_coeff2_2', uint8_t),
    ('hi_filter_coeff2_3', uint8_t),
]

RK_YNR_Params_V22_Select_t = struct_RK_YNR_Params_V22_Select_s# /usr/include/rkaiq/iq_parser_v2/ynr_uapi_head_v22.h: 143

# /usr/include/rkaiq/iq_parser_v2/ynr_uapi_head_v22.h: 175
class struct_Aynr_ExpInfo_V22_s(Structure):
    pass

struct_Aynr_ExpInfo_V22_s.__slots__ = [
    'hdr_mode',
    'snr_mode',
    'arTime',
    'arAGain',
    'arDGain',
    'isp_dgain',
    'blc_ob_predgain',
    'arIso',
    'isoLevelLow',
    'isoLevelHig',
    'rawWidth',
    'rawHeight',
]
struct_Aynr_ExpInfo_V22_s._fields_ = [
    ('hdr_mode', c_int),
    ('snr_mode', c_int),
    ('arTime', c_float * int(3)),
    ('arAGain', c_float * int(3)),
    ('arDGain', c_float * int(3)),
    ('isp_dgain', c_float * int(3)),
    ('blc_ob_predgain', c_float),
    ('arIso', c_int * int(3)),
    ('isoLevelLow', c_int),
    ('isoLevelHig', c_int),
    ('rawWidth', c_int),
    ('rawHeight', c_int),
]

Aynr_ExpInfo_V22_t = struct_Aynr_ExpInfo_V22_s# /usr/include/rkaiq/iq_parser_v2/ynr_uapi_head_v22.h: 175

# /usr/include/rkaiq/iq_parser_v2/ynr_uapi_head_v22.h: 185
class struct_rk_aiq_ynr_info_v22_s(Structure):
    pass

struct_rk_aiq_ynr_info_v22_s.__slots__ = [
    'sync',
    'iso',
    'expo_info',
]
struct_rk_aiq_ynr_info_v22_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('iso', c_int),
    ('expo_info', Aynr_ExpInfo_V22_t),
]

rk_aiq_ynr_info_v22_t = struct_rk_aiq_ynr_info_v22_s# /usr/include/rkaiq/iq_parser_v2/ynr_uapi_head_v22.h: 185

enum_Aynr_OPMode_V22_e = c_int# /usr/include/rkaiq/algos/aynrV22/rk_aiq_types_aynr_algo_int_v22.h: 72

Aynr_OPMode_V22_t = enum_Aynr_OPMode_V22_e# /usr/include/rkaiq/algos/aynrV22/rk_aiq_types_aynr_algo_int_v22.h: 72

# /usr/include/rkaiq/algos/aynrV22/rk_aiq_types_aynr_algo_int_v22.h: 151
class struct_RK_YNR_Params_V22_s(Structure):
    pass

struct_RK_YNR_Params_V22_s.__slots__ = [
    'enable',
    'version',
    'iso',
    'arYnrParamsISO',
]
struct_RK_YNR_Params_V22_s._fields_ = [
    ('enable', c_int),
    ('version', c_char * int(64)),
    ('iso', c_float * int(13)),
    ('arYnrParamsISO', RK_YNR_Params_V22_Select_t * int(13)),
]

RK_YNR_Params_V22_t = struct_RK_YNR_Params_V22_s# /usr/include/rkaiq/algos/aynrV22/rk_aiq_types_aynr_algo_int_v22.h: 151

# /usr/include/rkaiq/algos/aynrV22/rk_aiq_types_aynr_algo_int_v22.h: 160
class struct_Aynr_Manual_Attr_V22_s(Structure):
    pass

struct_Aynr_Manual_Attr_V22_s.__slots__ = [
    'stSelect',
    'stFix',
]
struct_Aynr_Manual_Attr_V22_s._fields_ = [
    ('stSelect', RK_YNR_Params_V22_Select_t),
    ('stFix', RK_YNR_Fix_V22_t),
]

Aynr_Manual_Attr_V22_t = struct_Aynr_Manual_Attr_V22_s# /usr/include/rkaiq/algos/aynrV22/rk_aiq_types_aynr_algo_int_v22.h: 160

# /usr/include/rkaiq/algos/aynrV22/rk_aiq_types_aynr_algo_int_v22.h: 169
class struct_Aynr_Auto_Attr_V22_s(Structure):
    pass

struct_Aynr_Auto_Attr_V22_s.__slots__ = [
    'stParams',
    'stSelect',
]
struct_Aynr_Auto_Attr_V22_s._fields_ = [
    ('stParams', RK_YNR_Params_V22_t),
    ('stSelect', RK_YNR_Params_V22_Select_t),
]

Aynr_Auto_Attr_V22_t = struct_Aynr_Auto_Attr_V22_s# /usr/include/rkaiq/algos/aynrV22/rk_aiq_types_aynr_algo_int_v22.h: 169

# /usr/include/rkaiq/algos/aynrV22/rk_aiq_types_aynr_algo_int_v22.h: 205
class struct_rk_aiq_ynr_attrib_v22_s(Structure):
    pass

struct_rk_aiq_ynr_attrib_v22_s.__slots__ = [
    'sync',
    'eMode',
    'stAuto',
    'stManual',
]
struct_rk_aiq_ynr_attrib_v22_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('eMode', Aynr_OPMode_V22_t),
    ('stAuto', Aynr_Auto_Attr_V22_t),
    ('stManual', Aynr_Manual_Attr_V22_t),
]

rk_aiq_ynr_attrib_v22_t = struct_rk_aiq_ynr_attrib_v22_s# /usr/include/rkaiq/algos/aynrV22/rk_aiq_types_aynr_algo_int_v22.h: 205

# /usr/include/rkaiq/algos/aynrV22/rk_aiq_types_aynr_algo_int_v22.h: 220
class struct_rk_aiq_ynr_strength_v22_s(Structure):
    pass

struct_rk_aiq_ynr_strength_v22_s.__slots__ = [
    'sync',
    'percent',
    'strength_enable',
]
struct_rk_aiq_ynr_strength_v22_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('percent', c_float),
    ('strength_enable', c_bool),
]

rk_aiq_ynr_strength_v22_t = struct_rk_aiq_ynr_strength_v22_s# /usr/include/rkaiq/algos/aynrV22/rk_aiq_types_aynr_algo_int_v22.h: 220

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_aynr_v22.h: 28
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_aynrV22_SetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_aynrV22_SetAttrib = _lib.get("rk_aiq_user_api2_aynrV22_SetAttrib", "cdecl")
    rk_aiq_user_api2_aynrV22_SetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_ynr_attrib_v22_t)]
    rk_aiq_user_api2_aynrV22_SetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_aynr_v22.h: 31
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_aynrV22_GetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_aynrV22_GetAttrib = _lib.get("rk_aiq_user_api2_aynrV22_GetAttrib", "cdecl")
    rk_aiq_user_api2_aynrV22_GetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_ynr_attrib_v22_t)]
    rk_aiq_user_api2_aynrV22_GetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_aynr_v22.h: 34
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_aynrV22_SetStrength", "cdecl"):
        continue
    rk_aiq_user_api2_aynrV22_SetStrength = _lib.get("rk_aiq_user_api2_aynrV22_SetStrength", "cdecl")
    rk_aiq_user_api2_aynrV22_SetStrength.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_ynr_strength_v22_t)]
    rk_aiq_user_api2_aynrV22_SetStrength.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_aynr_v22.h: 37
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_aynrV22_GetStrength", "cdecl"):
        continue
    rk_aiq_user_api2_aynrV22_GetStrength = _lib.get("rk_aiq_user_api2_aynrV22_GetStrength", "cdecl")
    rk_aiq_user_api2_aynrV22_GetStrength.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_ynr_strength_v22_t)]
    rk_aiq_user_api2_aynrV22_GetStrength.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_aynr_v22.h: 40
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_aynrV22_GetInfo", "cdecl"):
        continue
    rk_aiq_user_api2_aynrV22_GetInfo = _lib.get("rk_aiq_user_api2_aynrV22_GetInfo", "cdecl")
    rk_aiq_user_api2_aynrV22_GetInfo.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_ynr_info_v22_t)]
    rk_aiq_user_api2_aynrV22_GetInfo.restype = XCamReturn
    break

# /usr/include/rkaiq/iq_parser_v2/ynr_uapi_head_v3.h: 123
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

RK_YNR_Params_V3_Select_t = struct_RK_YNR_Params_V3_Select_s# /usr/include/rkaiq/iq_parser_v2/ynr_uapi_head_v3.h: 123

# /usr/include/rkaiq/iq_parser_v2/ynr_uapi_head_v3.h: 150
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

Aynr_ExpInfo_V3_t = struct_Aynr_ExpInfo_V3_s# /usr/include/rkaiq/iq_parser_v2/ynr_uapi_head_v3.h: 150

# /usr/include/rkaiq/iq_parser_v2/ynr_uapi_head_v3.h: 161
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

rk_aiq_ynr_info_v3_t = struct_rk_aiq_ynr_info_v3_s# /usr/include/rkaiq/iq_parser_v2/ynr_uapi_head_v3.h: 161

enum_Aynr_OPMode_V3_e = c_int# /usr/include/rkaiq/algos/aynr3/rk_aiq_types_aynr_algo_int_v3.h: 72

Aynr_OPMode_V3_t = enum_Aynr_OPMode_V3_e# /usr/include/rkaiq/algos/aynr3/rk_aiq_types_aynr_algo_int_v3.h: 72

# /usr/include/rkaiq/algos/aynr3/rk_aiq_types_aynr_algo_int_v3.h: 139
class struct_RK_YNR_Sigma_formula_s(Structure):
    pass

struct_RK_YNR_Sigma_formula_s.__slots__ = [
    'sigma_curve',
]
struct_RK_YNR_Sigma_formula_s._fields_ = [
    ('sigma_curve', c_double * int(5)),
]

RK_YNR_Sigma_formula_t = struct_RK_YNR_Sigma_formula_s# /usr/include/rkaiq/algos/aynr3/rk_aiq_types_aynr_algo_int_v3.h: 139

# /usr/include/rkaiq/algos/aynr3/rk_aiq_types_aynr_algo_int_v3.h: 149
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

RK_YNR_Params_V3_t = struct_RK_YNR_Params_V3_s# /usr/include/rkaiq/algos/aynr3/rk_aiq_types_aynr_algo_int_v3.h: 149

# /usr/include/rkaiq/algos/aynr3/rk_aiq_types_aynr_algo_int_v3.h: 158
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

Aynr_Manual_Attr_V3_t = struct_Aynr_Manual_Attr_V3_s# /usr/include/rkaiq/algos/aynr3/rk_aiq_types_aynr_algo_int_v3.h: 158

# /usr/include/rkaiq/algos/aynr3/rk_aiq_types_aynr_algo_int_v3.h: 167
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

Aynr_Auto_Attr_V3_t = struct_Aynr_Auto_Attr_V3_s# /usr/include/rkaiq/algos/aynr3/rk_aiq_types_aynr_algo_int_v3.h: 167

# /usr/include/rkaiq/algos/aynr3/rk_aiq_types_aynr_algo_int_v3.h: 200
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

rk_aiq_ynr_attrib_v3_t = struct_rk_aiq_ynr_attrib_v3_s# /usr/include/rkaiq/algos/aynr3/rk_aiq_types_aynr_algo_int_v3.h: 200

# /usr/include/rkaiq/algos/aynr3/rk_aiq_types_aynr_algo_int_v3.h: 215
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

rk_aiq_ynr_strength_v3_t = struct_rk_aiq_ynr_strength_v3_s# /usr/include/rkaiq/algos/aynr3/rk_aiq_types_aynr_algo_int_v3.h: 215

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_aynr_v3.h: 31
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_aynrV3_SetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_aynrV3_SetAttrib = _lib.get("rk_aiq_user_api2_aynrV3_SetAttrib", "cdecl")
    rk_aiq_user_api2_aynrV3_SetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_ynr_attrib_v3_t)]
    rk_aiq_user_api2_aynrV3_SetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_aynr_v3.h: 34
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_aynrV3_GetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_aynrV3_GetAttrib = _lib.get("rk_aiq_user_api2_aynrV3_GetAttrib", "cdecl")
    rk_aiq_user_api2_aynrV3_GetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_ynr_attrib_v3_t)]
    rk_aiq_user_api2_aynrV3_GetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_aynr_v3.h: 37
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_aynrV3_SetStrength", "cdecl"):
        continue
    rk_aiq_user_api2_aynrV3_SetStrength = _lib.get("rk_aiq_user_api2_aynrV3_SetStrength", "cdecl")
    rk_aiq_user_api2_aynrV3_SetStrength.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_ynr_strength_v3_t)]
    rk_aiq_user_api2_aynrV3_SetStrength.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_aynr_v3.h: 40
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_aynrV3_GetStrength", "cdecl"):
        continue
    rk_aiq_user_api2_aynrV3_GetStrength = _lib.get("rk_aiq_user_api2_aynrV3_GetStrength", "cdecl")
    rk_aiq_user_api2_aynrV3_GetStrength.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_ynr_strength_v3_t)]
    rk_aiq_user_api2_aynrV3_GetStrength.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_aynr_v3.h: 43
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_aynrV3_GetInfo", "cdecl"):
        continue
    rk_aiq_user_api2_aynrV3_GetInfo = _lib.get("rk_aiq_user_api2_aynrV3_GetInfo", "cdecl")
    rk_aiq_user_api2_aynrV3_GetInfo.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_ynr_info_v3_t)]
    rk_aiq_user_api2_aynrV3_GetInfo.restype = XCamReturn
    break

# /usr/include/rkaiq/iq_parser_v2/gain_uapi_head_v2.h: 36
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

RK_GAIN_Select_V2_t = struct_RK_GAIN_Select_V2_s# /usr/include/rkaiq/iq_parser_v2/gain_uapi_head_v2.h: 36

# /usr/include/rkaiq/iq_parser_v2/gain_uapi_head_v2.h: 60
class struct_Again_ExpInfo_V2_s(Structure):
    pass

struct_Again_ExpInfo_V2_s.__slots__ = [
    'hdr_mode',
    'snr_mode',
    'arTime',
    'arAGain',
    'arDGain',
    'isp_dgain',
    'arIso',
    'isoLevelLow',
    'isoLevelHig',
]
struct_Again_ExpInfo_V2_s._fields_ = [
    ('hdr_mode', c_int),
    ('snr_mode', c_int),
    ('arTime', c_float * int(3)),
    ('arAGain', c_float * int(3)),
    ('arDGain', c_float * int(3)),
    ('isp_dgain', c_float * int(3)),
    ('arIso', c_int * int(3)),
    ('isoLevelLow', c_int),
    ('isoLevelHig', c_int),
]

Again_ExpInfo_V2_t = struct_Again_ExpInfo_V2_s# /usr/include/rkaiq/iq_parser_v2/gain_uapi_head_v2.h: 60

# /usr/include/rkaiq/iq_parser_v2/gain_uapi_head_v2.h: 69
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

rk_aiq_gain_info_v2_t = struct_rk_aiq_gain_info_v2_s# /usr/include/rkaiq/iq_parser_v2/gain_uapi_head_v2.h: 69

enum_Again_OPMode_V2_e = c_int# /usr/include/rkaiq/algos/again2/rk_aiq_types_again_algo_int_v2.h: 78

Again_OPMode_V2_t = enum_Again_OPMode_V2_e# /usr/include/rkaiq/algos/again2/rk_aiq_types_again_algo_int_v2.h: 78

# /usr/include/rkaiq/algos/again2/rk_aiq_types_again_algo_int_v2.h: 104
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

RK_GAIN_Params_V2_t = struct_RK_GAIN_Params_V2_s# /usr/include/rkaiq/algos/again2/rk_aiq_types_again_algo_int_v2.h: 104

# /usr/include/rkaiq/algos/again2/rk_aiq_types_again_algo_int_v2.h: 111
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

Again_Manual_Attr_V2_t = struct_Again_Manual_Attr_V2_s# /usr/include/rkaiq/algos/again2/rk_aiq_types_again_algo_int_v2.h: 111

# /usr/include/rkaiq/algos/again2/rk_aiq_types_again_algo_int_v2.h: 120
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

Again_Auto_Attr_V2_t = struct_AgainV2_Auto_Attr_V2_s# /usr/include/rkaiq/algos/again2/rk_aiq_types_again_algo_int_v2.h: 120

# /usr/include/rkaiq/algos/again2/rk_aiq_types_again_algo_int_v2.h: 143
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

rk_aiq_gain_attrib_v2_t = struct_rk_aiq_gain_attrib_v2_s# /usr/include/rkaiq/algos/again2/rk_aiq_types_again_algo_int_v2.h: 143

# /usr/include/rkaiq/algos/again2/rk_aiq_types_again_algo_int_v2.h: 151
class struct_rk_aiq_uapiV2_again_wrtIn_attr_s(Structure):
    pass

struct_rk_aiq_uapiV2_again_wrtIn_attr_s.__slots__ = [
    'sync',
    'enable',
    'mode',
    'path',
    'call_cnt',
]
struct_rk_aiq_uapiV2_again_wrtIn_attr_s._fields_ = [
    ('sync', rk_aiq_uapi_sync_t),
    ('enable', c_bool),
    ('mode', c_int),
    ('path', c_char * int(100)),
    ('call_cnt', c_int),
]

rk_aiq_uapiV2_again_wrtIn_attr_t = struct_rk_aiq_uapiV2_again_wrtIn_attr_s# /usr/include/rkaiq/algos/again2/rk_aiq_types_again_algo_int_v2.h: 151

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_again_v2.h: 31
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_againV2_SetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_againV2_SetAttrib = _lib.get("rk_aiq_user_api2_againV2_SetAttrib", "cdecl")
    rk_aiq_user_api2_againV2_SetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_gain_attrib_v2_t)]
    rk_aiq_user_api2_againV2_SetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_again_v2.h: 34
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_againV2_GetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_againV2_GetAttrib = _lib.get("rk_aiq_user_api2_againV2_GetAttrib", "cdecl")
    rk_aiq_user_api2_againV2_GetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_gain_attrib_v2_t)]
    rk_aiq_user_api2_againV2_GetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_again_v2.h: 37
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_againV2_GetInfo", "cdecl"):
        continue
    rk_aiq_user_api2_againV2_GetInfo = _lib.get("rk_aiq_user_api2_againV2_GetInfo", "cdecl")
    rk_aiq_user_api2_againV2_GetInfo.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_gain_info_v2_t)]
    rk_aiq_user_api2_againV2_GetInfo.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_again_v2.h: 40
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_againV2_WriteInput", "cdecl"):
        continue
    rk_aiq_user_api2_againV2_WriteInput = _lib.get("rk_aiq_user_api2_againV2_WriteInput", "cdecl")
    rk_aiq_user_api2_againV2_WriteInput.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_uapiV2_again_wrtIn_attr_t), c_bool]
    rk_aiq_user_api2_againV2_WriteInput.restype = XCamReturn
    break

rk_aiq_ldch_v21_attrib_t = rk_aiq_ldch_v21_cfg_t# /usr/include/rkaiq/algos/aldch/rk_aiq_uapi_aldch_v21_int.h: 8

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_aldch_v21.h: 26
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_aldch_v21_SetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_aldch_v21_SetAttrib = _lib.get("rk_aiq_user_api2_aldch_v21_SetAttrib", "cdecl")
    rk_aiq_user_api2_aldch_v21_SetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_ldch_v21_attrib_t)]
    rk_aiq_user_api2_aldch_v21_SetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_aldch_v21.h: 28
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_aldch_v21_GetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_aldch_v21_GetAttrib = _lib.get("rk_aiq_user_api2_aldch_v21_GetAttrib", "cdecl")
    rk_aiq_user_api2_aldch_v21_GetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_ldch_v21_attrib_t)]
    rk_aiq_user_api2_aldch_v21_GetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_ablc_v32.h: 28
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_ablcV32_SetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_ablcV32_SetAttrib = _lib.get("rk_aiq_user_api2_ablcV32_SetAttrib", "cdecl")
    rk_aiq_user_api2_ablcV32_SetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_blc_attrib_V32_t)]
    rk_aiq_user_api2_ablcV32_SetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_ablc_v32.h: 30
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_ablcV32_GetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_ablcV32_GetAttrib = _lib.get("rk_aiq_user_api2_ablcV32_GetAttrib", "cdecl")
    rk_aiq_user_api2_ablcV32_GetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_blc_attrib_V32_t)]
    rk_aiq_user_api2_ablcV32_GetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_ablc_v32.h: 32
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_ablcV32_GetInfo", "cdecl"):
        continue
    rk_aiq_user_api2_ablcV32_GetInfo = _lib.get("rk_aiq_user_api2_ablcV32_GetInfo", "cdecl")
    rk_aiq_user_api2_ablcV32_GetInfo.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_blc_info_v32_t)]
    rk_aiq_user_api2_ablcV32_GetInfo.restype = XCamReturn
    break

# /usr/include/rkaiq/algos/acsm/rk_aiq_uapi_acsm_int.h: 37
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

rk_aiq_uapi_acsm_attrib_t = struct_rk_aiq_uapi_acsm_attrib_s# /usr/include/rkaiq/algos/acsm/rk_aiq_uapi_acsm_int.h: 37

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_acsm.h: 31
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_acsm_SetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_acsm_SetAttrib = _lib.get("rk_aiq_user_api2_acsm_SetAttrib", "cdecl")
    rk_aiq_user_api2_acsm_SetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_uapi_acsm_attrib_t)]
    rk_aiq_user_api2_acsm_SetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_acsm.h: 33
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_acsm_GetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_acsm_GetAttrib = _lib.get("rk_aiq_user_api2_acsm_GetAttrib", "cdecl")
    rk_aiq_user_api2_acsm_GetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_uapi_acsm_attrib_t)]
    rk_aiq_user_api2_acsm_GetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/algos/acgc/rk_aiq_uapi_acgc_int.h: 38
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

rk_aiq_uapi_acgc_attrib_t = struct_rk_aiq_uapi_acgc_attrib_s# /usr/include/rkaiq/algos/acgc/rk_aiq_uapi_acgc_int.h: 38

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_acgc.h: 28
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_acgc_SetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_acgc_SetAttrib = _lib.get("rk_aiq_user_api2_acgc_SetAttrib", "cdecl")
    rk_aiq_user_api2_acgc_SetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_uapi_acgc_attrib_t)]
    rk_aiq_user_api2_acgc_SetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_acgc.h: 30
for _lib in _libs.values():
    if not _lib.has("rk_aiq_user_api2_acgc_GetAttrib", "cdecl"):
        continue
    rk_aiq_user_api2_acgc_GetAttrib = _lib.get("rk_aiq_user_api2_acgc_GetAttrib", "cdecl")
    rk_aiq_user_api2_acgc_GetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_uapi_acgc_attrib_t)]
    rk_aiq_user_api2_acgc_GetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 78
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_setAeLock", "cdecl"):
        continue
    rk_aiq_uapi2_setAeLock = _lib.get("rk_aiq_uapi2_setAeLock", "cdecl")
    rk_aiq_uapi2_setAeLock.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_bool]
    rk_aiq_uapi2_setAeLock.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 89
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_setExpMode", "cdecl"):
        continue
    rk_aiq_uapi2_setExpMode = _lib.get("rk_aiq_uapi2_setExpMode", "cdecl")
    rk_aiq_uapi2_setExpMode.argtypes = [POINTER(rk_aiq_sys_ctx_t), opMode_t]
    rk_aiq_uapi2_setExpMode.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 90
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_getExpMode", "cdecl"):
        continue
    rk_aiq_uapi2_getExpMode = _lib.get("rk_aiq_uapi2_getExpMode", "cdecl")
    rk_aiq_uapi2_getExpMode.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(opMode_t)]
    rk_aiq_uapi2_getExpMode.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 104
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_setExpGainRange", "cdecl"):
        continue
    rk_aiq_uapi2_setExpGainRange = _lib.get("rk_aiq_uapi2_setExpGainRange", "cdecl")
    rk_aiq_uapi2_setExpGainRange.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(paRange_t)]
    rk_aiq_uapi2_setExpGainRange.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 105
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_getExpGainRange", "cdecl"):
        continue
    rk_aiq_uapi2_getExpGainRange = _lib.get("rk_aiq_uapi2_getExpGainRange", "cdecl")
    rk_aiq_uapi2_getExpGainRange.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(paRange_t)]
    rk_aiq_uapi2_getExpGainRange.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 118
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_setExpTimeRange", "cdecl"):
        continue
    rk_aiq_uapi2_setExpTimeRange = _lib.get("rk_aiq_uapi2_setExpTimeRange", "cdecl")
    rk_aiq_uapi2_setExpTimeRange.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(paRange_t)]
    rk_aiq_uapi2_setExpTimeRange.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 119
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_getExpTimeRange", "cdecl"):
        continue
    rk_aiq_uapi2_getExpTimeRange = _lib.get("rk_aiq_uapi2_getExpTimeRange", "cdecl")
    rk_aiq_uapi2_getExpTimeRange.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(paRange_t)]
    rk_aiq_uapi2_getExpTimeRange.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 132
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_setBLCMode", "cdecl"):
        continue
    rk_aiq_uapi2_setBLCMode = _lib.get("rk_aiq_uapi2_setBLCMode", "cdecl")
    rk_aiq_uapi2_setBLCMode.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_bool, aeMeasAreaType_t]
    rk_aiq_uapi2_setBLCMode.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 142
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_setBLCStrength", "cdecl"):
        continue
    rk_aiq_uapi2_setBLCStrength = _lib.get("rk_aiq_uapi2_setBLCStrength", "cdecl")
    rk_aiq_uapi2_setBLCStrength.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_int]
    rk_aiq_uapi2_setBLCStrength.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 154
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_setHLCMode", "cdecl"):
        continue
    rk_aiq_uapi2_setHLCMode = _lib.get("rk_aiq_uapi2_setHLCMode", "cdecl")
    rk_aiq_uapi2_setHLCMode.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_bool]
    rk_aiq_uapi2_setHLCMode.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 164
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_setHLCStrength", "cdecl"):
        continue
    rk_aiq_uapi2_setHLCStrength = _lib.get("rk_aiq_uapi2_setHLCStrength", "cdecl")
    rk_aiq_uapi2_setHLCStrength.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_int]
    rk_aiq_uapi2_setHLCStrength.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 175
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_setAntiFlickerEn", "cdecl"):
        continue
    rk_aiq_uapi2_setAntiFlickerEn = _lib.get("rk_aiq_uapi2_setAntiFlickerEn", "cdecl")
    rk_aiq_uapi2_setAntiFlickerEn.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_bool]
    rk_aiq_uapi2_setAntiFlickerEn.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 176
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_getAntiFlickerEn", "cdecl"):
        continue
    rk_aiq_uapi2_getAntiFlickerEn = _lib.get("rk_aiq_uapi2_getAntiFlickerEn", "cdecl")
    rk_aiq_uapi2_getAntiFlickerEn.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(c_bool)]
    rk_aiq_uapi2_getAntiFlickerEn.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 187
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_setAntiFlickerMode", "cdecl"):
        continue
    rk_aiq_uapi2_setAntiFlickerMode = _lib.get("rk_aiq_uapi2_setAntiFlickerMode", "cdecl")
    rk_aiq_uapi2_setAntiFlickerMode.argtypes = [POINTER(rk_aiq_sys_ctx_t), antiFlickerMode_t]
    rk_aiq_uapi2_setAntiFlickerMode.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 188
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_getAntiFlickerMode", "cdecl"):
        continue
    rk_aiq_uapi2_getAntiFlickerMode = _lib.get("rk_aiq_uapi2_getAntiFlickerMode", "cdecl")
    rk_aiq_uapi2_getAntiFlickerMode.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(antiFlickerMode_t)]
    rk_aiq_uapi2_getAntiFlickerMode.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 205
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_setWBMode", "cdecl"):
        continue
    rk_aiq_uapi2_setWBMode = _lib.get("rk_aiq_uapi2_setWBMode", "cdecl")
    rk_aiq_uapi2_setWBMode.argtypes = [POINTER(rk_aiq_sys_ctx_t), opMode_t]
    rk_aiq_uapi2_setWBMode.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 206
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_getWBMode", "cdecl"):
        continue
    rk_aiq_uapi2_getWBMode = _lib.get("rk_aiq_uapi2_getWBMode", "cdecl")
    rk_aiq_uapi2_getWBMode.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(opMode_t)]
    rk_aiq_uapi2_getWBMode.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 218
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_lockAWB", "cdecl"):
        continue
    rk_aiq_uapi2_lockAWB = _lib.get("rk_aiq_uapi2_lockAWB", "cdecl")
    rk_aiq_uapi2_lockAWB.argtypes = [POINTER(rk_aiq_sys_ctx_t)]
    rk_aiq_uapi2_lockAWB.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 219
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_unlockAWB", "cdecl"):
        continue
    rk_aiq_uapi2_unlockAWB = _lib.get("rk_aiq_uapi2_unlockAWB", "cdecl")
    rk_aiq_uapi2_unlockAWB.argtypes = [POINTER(rk_aiq_sys_ctx_t)]
    rk_aiq_uapi2_unlockAWB.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 230
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_setMWBScene", "cdecl"):
        continue
    rk_aiq_uapi2_setMWBScene = _lib.get("rk_aiq_uapi2_setMWBScene", "cdecl")
    rk_aiq_uapi2_setMWBScene.argtypes = [POINTER(rk_aiq_sys_ctx_t), rk_aiq_wb_scene_t]
    rk_aiq_uapi2_setMWBScene.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 231
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_getMWBScene", "cdecl"):
        continue
    rk_aiq_uapi2_getMWBScene = _lib.get("rk_aiq_uapi2_getMWBScene", "cdecl")
    rk_aiq_uapi2_getMWBScene.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_wb_scene_t)]
    rk_aiq_uapi2_getMWBScene.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 243
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_setMWBGain", "cdecl"):
        continue
    rk_aiq_uapi2_setMWBGain = _lib.get("rk_aiq_uapi2_setMWBGain", "cdecl")
    rk_aiq_uapi2_setMWBGain.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_wb_gain_t)]
    rk_aiq_uapi2_setMWBGain.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 244
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_getWBGain", "cdecl"):
        continue
    rk_aiq_uapi2_getWBGain = _lib.get("rk_aiq_uapi2_getWBGain", "cdecl")
    rk_aiq_uapi2_getWBGain.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_wb_gain_t)]
    rk_aiq_uapi2_getWBGain.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 255
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_setMWBCT", "cdecl"):
        continue
    rk_aiq_uapi2_setMWBCT = _lib.get("rk_aiq_uapi2_setMWBCT", "cdecl")
    rk_aiq_uapi2_setMWBCT.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_uint]
    rk_aiq_uapi2_setMWBCT.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 256
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_getWBCT", "cdecl"):
        continue
    rk_aiq_uapi2_getWBCT = _lib.get("rk_aiq_uapi2_getWBCT", "cdecl")
    rk_aiq_uapi2_getWBCT.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(c_uint)]
    rk_aiq_uapi2_getWBCT.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 267
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_setAwbGainOffsetAttrib", "cdecl"):
        continue
    rk_aiq_uapi2_setAwbGainOffsetAttrib = _lib.get("rk_aiq_uapi2_setAwbGainOffsetAttrib", "cdecl")
    rk_aiq_uapi2_setAwbGainOffsetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), rk_aiq_uapiV2_wb_awb_wbGainOffset_t]
    rk_aiq_uapi2_setAwbGainOffsetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 268
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_getAwbGainOffsetAttrib", "cdecl"):
        continue
    rk_aiq_uapi2_getAwbGainOffsetAttrib = _lib.get("rk_aiq_uapi2_getAwbGainOffsetAttrib", "cdecl")
    rk_aiq_uapi2_getAwbGainOffsetAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_uapiV2_wb_awb_wbGainOffset_t)]
    rk_aiq_uapi2_getAwbGainOffsetAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 279
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_setAwbGainAdjustAttrib", "cdecl"):
        continue
    rk_aiq_uapi2_setAwbGainAdjustAttrib = _lib.get("rk_aiq_uapi2_setAwbGainAdjustAttrib", "cdecl")
    rk_aiq_uapi2_setAwbGainAdjustAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), rk_aiq_uapiV2_wb_awb_wbGainAdjust_t]
    rk_aiq_uapi2_setAwbGainAdjustAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 280
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_getAwbGainAdjustAttrib", "cdecl"):
        continue
    rk_aiq_uapi2_getAwbGainAdjustAttrib = _lib.get("rk_aiq_uapi2_getAwbGainAdjustAttrib", "cdecl")
    rk_aiq_uapi2_getAwbGainAdjustAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_uapiV2_wb_awb_wbGainAdjust_t)]
    rk_aiq_uapi2_getAwbGainAdjustAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 291
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_setAwbMultiWindowAttrib", "cdecl"):
        continue
    rk_aiq_uapi2_setAwbMultiWindowAttrib = _lib.get("rk_aiq_uapi2_setAwbMultiWindowAttrib", "cdecl")
    rk_aiq_uapi2_setAwbMultiWindowAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), rk_aiq_uapiV2_wb_awb_mulWindow_t]
    rk_aiq_uapi2_setAwbMultiWindowAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 292
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_getAwbMultiWindowAttrib", "cdecl"):
        continue
    rk_aiq_uapi2_getAwbMultiWindowAttrib = _lib.get("rk_aiq_uapi2_getAwbMultiWindowAttrib", "cdecl")
    rk_aiq_uapi2_getAwbMultiWindowAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_uapiV2_wb_awb_mulWindow_t)]
    rk_aiq_uapi2_getAwbMultiWindowAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 304
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_setAwbV30AllAttrib", "cdecl"):
        continue
    rk_aiq_uapi2_setAwbV30AllAttrib = _lib.get("rk_aiq_uapi2_setAwbV30AllAttrib", "cdecl")
    rk_aiq_uapi2_setAwbV30AllAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), rk_aiq_uapiV2_wbV30_attrib_t]
    rk_aiq_uapi2_setAwbV30AllAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 305
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_getAwbV30AllAttrib", "cdecl"):
        continue
    rk_aiq_uapi2_getAwbV30AllAttrib = _lib.get("rk_aiq_uapi2_getAwbV30AllAttrib", "cdecl")
    rk_aiq_uapi2_getAwbV30AllAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_uapiV2_wbV30_attrib_t)]
    rk_aiq_uapi2_getAwbV30AllAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 317
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_setAwbV21AllAttrib", "cdecl"):
        continue
    rk_aiq_uapi2_setAwbV21AllAttrib = _lib.get("rk_aiq_uapi2_setAwbV21AllAttrib", "cdecl")
    rk_aiq_uapi2_setAwbV21AllAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), rk_aiq_uapiV2_wbV21_attrib_t]
    rk_aiq_uapi2_setAwbV21AllAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 318
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_getAwbV21AllAttrib", "cdecl"):
        continue
    rk_aiq_uapi2_getAwbV21AllAttrib = _lib.get("rk_aiq_uapi2_getAwbV21AllAttrib", "cdecl")
    rk_aiq_uapi2_getAwbV21AllAttrib.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_uapiV2_wbV21_attrib_t)]
    rk_aiq_uapi2_getAwbV21AllAttrib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 331
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_setExpPwrLineFreqMode", "cdecl"):
        continue
    rk_aiq_uapi2_setExpPwrLineFreqMode = _lib.get("rk_aiq_uapi2_setExpPwrLineFreqMode", "cdecl")
    rk_aiq_uapi2_setExpPwrLineFreqMode.argtypes = [POINTER(rk_aiq_sys_ctx_t), expPwrLineFreq_t]
    rk_aiq_uapi2_setExpPwrLineFreqMode.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 332
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_getExpPwrLineFreqMode", "cdecl"):
        continue
    rk_aiq_uapi2_getExpPwrLineFreqMode = _lib.get("rk_aiq_uapi2_getExpPwrLineFreqMode", "cdecl")
    rk_aiq_uapi2_getExpPwrLineFreqMode.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(expPwrLineFreq_t)]
    rk_aiq_uapi2_getExpPwrLineFreqMode.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 344
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_setGammaCoef", "cdecl"):
        continue
    rk_aiq_uapi2_setGammaCoef = _lib.get("rk_aiq_uapi2_setGammaCoef", "cdecl")
    rk_aiq_uapi2_setGammaCoef.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_float, c_float]
    rk_aiq_uapi2_setGammaCoef.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 356
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_setDarkAreaBoostStrth", "cdecl"):
        continue
    rk_aiq_uapi2_setDarkAreaBoostStrth = _lib.get("rk_aiq_uapi2_setDarkAreaBoostStrth", "cdecl")
    rk_aiq_uapi2_setDarkAreaBoostStrth.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_uint]
    rk_aiq_uapi2_setDarkAreaBoostStrth.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 357
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_getDarkAreaBoostStrth", "cdecl"):
        continue
    rk_aiq_uapi2_getDarkAreaBoostStrth = _lib.get("rk_aiq_uapi2_getDarkAreaBoostStrth", "cdecl")
    rk_aiq_uapi2_getDarkAreaBoostStrth.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(c_uint)]
    rk_aiq_uapi2_getDarkAreaBoostStrth.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 369
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_setMHDRStrth", "cdecl"):
        continue
    rk_aiq_uapi2_setMHDRStrth = _lib.get("rk_aiq_uapi2_setMHDRStrth", "cdecl")
    rk_aiq_uapi2_setMHDRStrth.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_bool, c_uint]
    rk_aiq_uapi2_setMHDRStrth.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 370
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_getMHDRStrth", "cdecl"):
        continue
    rk_aiq_uapi2_getMHDRStrth = _lib.get("rk_aiq_uapi2_getMHDRStrth", "cdecl")
    rk_aiq_uapi2_getMHDRStrth.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(c_bool), POINTER(c_uint)]
    rk_aiq_uapi2_getMHDRStrth.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 380
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_setDehazeModuleEnable", "cdecl"):
        continue
    rk_aiq_uapi2_setDehazeModuleEnable = _lib.get("rk_aiq_uapi2_setDehazeModuleEnable", "cdecl")
    rk_aiq_uapi2_setDehazeModuleEnable.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_bool]
    rk_aiq_uapi2_setDehazeModuleEnable.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 390
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_setDehazeEnable", "cdecl"):
        continue
    rk_aiq_uapi2_setDehazeEnable = _lib.get("rk_aiq_uapi2_setDehazeEnable", "cdecl")
    rk_aiq_uapi2_setDehazeEnable.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_bool]
    rk_aiq_uapi2_setDehazeEnable.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 402
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_setMDehazeStrth", "cdecl"):
        continue
    rk_aiq_uapi2_setMDehazeStrth = _lib.get("rk_aiq_uapi2_setMDehazeStrth", "cdecl")
    rk_aiq_uapi2_setMDehazeStrth.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_uint]
    rk_aiq_uapi2_setMDehazeStrth.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 403
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_getMDehazeStrth", "cdecl"):
        continue
    rk_aiq_uapi2_getMDehazeStrth = _lib.get("rk_aiq_uapi2_getMDehazeStrth", "cdecl")
    rk_aiq_uapi2_getMDehazeStrth.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(c_uint)]
    rk_aiq_uapi2_getMDehazeStrth.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 413
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_setEnhanceEnable", "cdecl"):
        continue
    rk_aiq_uapi2_setEnhanceEnable = _lib.get("rk_aiq_uapi2_setEnhanceEnable", "cdecl")
    rk_aiq_uapi2_setEnhanceEnable.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_bool]
    rk_aiq_uapi2_setEnhanceEnable.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 425
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_setMEnhanceStrth", "cdecl"):
        continue
    rk_aiq_uapi2_setMEnhanceStrth = _lib.get("rk_aiq_uapi2_setMEnhanceStrth", "cdecl")
    rk_aiq_uapi2_setMEnhanceStrth.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_uint]
    rk_aiq_uapi2_setMEnhanceStrth.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 426
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_getMEnhanceStrth", "cdecl"):
        continue
    rk_aiq_uapi2_getMEnhanceStrth = _lib.get("rk_aiq_uapi2_getMEnhanceStrth", "cdecl")
    rk_aiq_uapi2_getMEnhanceStrth.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(c_uint)]
    rk_aiq_uapi2_getMEnhanceStrth.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 438
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_setMEnhanceChromeStrth", "cdecl"):
        continue
    rk_aiq_uapi2_setMEnhanceChromeStrth = _lib.get("rk_aiq_uapi2_setMEnhanceChromeStrth", "cdecl")
    rk_aiq_uapi2_setMEnhanceChromeStrth.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_uint]
    rk_aiq_uapi2_setMEnhanceChromeStrth.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 439
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_getMEnhanceChromeStrth", "cdecl"):
        continue
    rk_aiq_uapi2_getMEnhanceChromeStrth = _lib.get("rk_aiq_uapi2_getMEnhanceChromeStrth", "cdecl")
    rk_aiq_uapi2_getMEnhanceChromeStrth.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(c_uint)]
    rk_aiq_uapi2_getMEnhanceChromeStrth.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 454
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_setDrcLocalTMO", "cdecl"):
        continue
    rk_aiq_uapi2_setDrcLocalTMO = _lib.get("rk_aiq_uapi2_setDrcLocalTMO", "cdecl")
    rk_aiq_uapi2_setDrcLocalTMO.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_float, c_float, c_float]
    rk_aiq_uapi2_setDrcLocalTMO.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 455
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_getDrcLocalTMO", "cdecl"):
        continue
    rk_aiq_uapi2_getDrcLocalTMO = _lib.get("rk_aiq_uapi2_getDrcLocalTMO", "cdecl")
    rk_aiq_uapi2_getDrcLocalTMO.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(c_float), POINTER(c_float), POINTER(c_float)]
    rk_aiq_uapi2_getDrcLocalTMO.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 472
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_setDrcLocalData", "cdecl"):
        continue
    rk_aiq_uapi2_setDrcLocalData = _lib.get("rk_aiq_uapi2_setDrcLocalData", "cdecl")
    rk_aiq_uapi2_setDrcLocalData.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_float, c_float, c_float, c_int, c_float]
    rk_aiq_uapi2_setDrcLocalData.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 473
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_getDrcLocalData", "cdecl"):
        continue
    rk_aiq_uapi2_getDrcLocalData = _lib.get("rk_aiq_uapi2_getDrcLocalData", "cdecl")
    rk_aiq_uapi2_getDrcLocalData.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(c_float), POINTER(c_float), POINTER(c_float), POINTER(c_int), POINTER(c_float)]
    rk_aiq_uapi2_getDrcLocalData.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 486
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_setDrcHiLit", "cdecl"):
        continue
    rk_aiq_uapi2_setDrcHiLit = _lib.get("rk_aiq_uapi2_setDrcHiLit", "cdecl")
    rk_aiq_uapi2_setDrcHiLit.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_float]
    rk_aiq_uapi2_setDrcHiLit.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 487
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_getDrcHiLit", "cdecl"):
        continue
    rk_aiq_uapi2_getDrcHiLit = _lib.get("rk_aiq_uapi2_getDrcHiLit", "cdecl")
    rk_aiq_uapi2_getDrcHiLit.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(c_float)]
    rk_aiq_uapi2_getDrcHiLit.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 502
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_setDrcGain", "cdecl"):
        continue
    rk_aiq_uapi2_setDrcGain = _lib.get("rk_aiq_uapi2_setDrcGain", "cdecl")
    rk_aiq_uapi2_setDrcGain.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_float, c_float, c_float]
    rk_aiq_uapi2_setDrcGain.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 503
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_getDrcGain", "cdecl"):
        continue
    rk_aiq_uapi2_getDrcGain = _lib.get("rk_aiq_uapi2_getDrcGain", "cdecl")
    rk_aiq_uapi2_getDrcGain.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(c_float), POINTER(c_float), POINTER(c_float)]
    rk_aiq_uapi2_getDrcGain.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 521
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_setNRMode", "cdecl"):
        continue
    rk_aiq_uapi2_setNRMode = _lib.get("rk_aiq_uapi2_setNRMode", "cdecl")
    rk_aiq_uapi2_setNRMode.argtypes = [POINTER(rk_aiq_sys_ctx_t), opMode_t]
    rk_aiq_uapi2_setNRMode.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 522
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_getNRMode", "cdecl"):
        continue
    rk_aiq_uapi2_getNRMode = _lib.get("rk_aiq_uapi2_getNRMode", "cdecl")
    rk_aiq_uapi2_getNRMode.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(opMode_t)]
    rk_aiq_uapi2_getNRMode.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 533
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_setANRStrth", "cdecl"):
        continue
    rk_aiq_uapi2_setANRStrth = _lib.get("rk_aiq_uapi2_setANRStrth", "cdecl")
    rk_aiq_uapi2_setANRStrth.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_uint]
    rk_aiq_uapi2_setANRStrth.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 534
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_getANRStrth", "cdecl"):
        continue
    rk_aiq_uapi2_getANRStrth = _lib.get("rk_aiq_uapi2_getANRStrth", "cdecl")
    rk_aiq_uapi2_getANRStrth.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(c_uint)]
    rk_aiq_uapi2_getANRStrth.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 547
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_setMSpaNRStrth", "cdecl"):
        continue
    rk_aiq_uapi2_setMSpaNRStrth = _lib.get("rk_aiq_uapi2_setMSpaNRStrth", "cdecl")
    rk_aiq_uapi2_setMSpaNRStrth.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_bool, c_uint]
    rk_aiq_uapi2_setMSpaNRStrth.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 548
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_getMSpaNRStrth", "cdecl"):
        continue
    rk_aiq_uapi2_getMSpaNRStrth = _lib.get("rk_aiq_uapi2_getMSpaNRStrth", "cdecl")
    rk_aiq_uapi2_getMSpaNRStrth.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(c_bool), POINTER(c_uint)]
    rk_aiq_uapi2_getMSpaNRStrth.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 560
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_setMTNRStrth", "cdecl"):
        continue
    rk_aiq_uapi2_setMTNRStrth = _lib.get("rk_aiq_uapi2_setMTNRStrth", "cdecl")
    rk_aiq_uapi2_setMTNRStrth.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_bool, c_uint]
    rk_aiq_uapi2_setMTNRStrth.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 562
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_getMTNRStrth", "cdecl"):
        continue
    rk_aiq_uapi2_getMTNRStrth = _lib.get("rk_aiq_uapi2_getMTNRStrth", "cdecl")
    rk_aiq_uapi2_getMTNRStrth.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(c_bool), POINTER(c_uint)]
    rk_aiq_uapi2_getMTNRStrth.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 572
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_setSharpness", "cdecl"):
        continue
    rk_aiq_uapi2_setSharpness = _lib.get("rk_aiq_uapi2_setSharpness", "cdecl")
    rk_aiq_uapi2_setSharpness.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_uint]
    rk_aiq_uapi2_setSharpness.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 573
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_getSharpness", "cdecl"):
        continue
    rk_aiq_uapi2_getSharpness = _lib.get("rk_aiq_uapi2_getSharpness", "cdecl")
    rk_aiq_uapi2_getSharpness.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(c_uint)]
    rk_aiq_uapi2_getSharpness.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 590
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_setFocusMode", "cdecl"):
        continue
    rk_aiq_uapi2_setFocusMode = _lib.get("rk_aiq_uapi2_setFocusMode", "cdecl")
    rk_aiq_uapi2_setFocusMode.argtypes = [POINTER(rk_aiq_sys_ctx_t), opMode_t]
    rk_aiq_uapi2_setFocusMode.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 591
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_getFocusMode", "cdecl"):
        continue
    rk_aiq_uapi2_getFocusMode = _lib.get("rk_aiq_uapi2_getFocusMode", "cdecl")
    rk_aiq_uapi2_getFocusMode.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(opMode_t)]
    rk_aiq_uapi2_getFocusMode.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 601
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_setFocusPosition", "cdecl"):
        continue
    rk_aiq_uapi2_setFocusPosition = _lib.get("rk_aiq_uapi2_setFocusPosition", "cdecl")
    rk_aiq_uapi2_setFocusPosition.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_short]
    rk_aiq_uapi2_setFocusPosition.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 602
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_getFocusPosition", "cdecl"):
        continue
    rk_aiq_uapi2_getFocusPosition = _lib.get("rk_aiq_uapi2_getFocusPosition", "cdecl")
    rk_aiq_uapi2_getFocusPosition.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(c_short)]
    rk_aiq_uapi2_getFocusPosition.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 612
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_setFocusWin", "cdecl"):
        continue
    rk_aiq_uapi2_setFocusWin = _lib.get("rk_aiq_uapi2_setFocusWin", "cdecl")
    rk_aiq_uapi2_setFocusWin.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(paRect_t)]
    rk_aiq_uapi2_setFocusWin.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 613
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_getFocusWin", "cdecl"):
        continue
    rk_aiq_uapi2_getFocusWin = _lib.get("rk_aiq_uapi2_getFocusWin", "cdecl")
    rk_aiq_uapi2_getFocusWin.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(paRect_t)]
    rk_aiq_uapi2_getFocusWin.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 624
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_lockFocus", "cdecl"):
        continue
    rk_aiq_uapi2_lockFocus = _lib.get("rk_aiq_uapi2_lockFocus", "cdecl")
    rk_aiq_uapi2_lockFocus.argtypes = [POINTER(rk_aiq_sys_ctx_t)]
    rk_aiq_uapi2_lockFocus.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 625
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_unlockFocus", "cdecl"):
        continue
    rk_aiq_uapi2_unlockFocus = _lib.get("rk_aiq_uapi2_unlockFocus", "cdecl")
    rk_aiq_uapi2_unlockFocus.argtypes = [POINTER(rk_aiq_sys_ctx_t)]
    rk_aiq_uapi2_unlockFocus.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 636
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_oneshotFocus", "cdecl"):
        continue
    rk_aiq_uapi2_oneshotFocus = _lib.get("rk_aiq_uapi2_oneshotFocus", "cdecl")
    rk_aiq_uapi2_oneshotFocus.argtypes = [POINTER(rk_aiq_sys_ctx_t)]
    rk_aiq_uapi2_oneshotFocus.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 647
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_manualTrigerFocus", "cdecl"):
        continue
    rk_aiq_uapi2_manualTrigerFocus = _lib.get("rk_aiq_uapi2_manualTrigerFocus", "cdecl")
    rk_aiq_uapi2_manualTrigerFocus.argtypes = [POINTER(rk_aiq_sys_ctx_t)]
    rk_aiq_uapi2_manualTrigerFocus.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 658
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_trackingFocus", "cdecl"):
        continue
    rk_aiq_uapi2_trackingFocus = _lib.get("rk_aiq_uapi2_trackingFocus", "cdecl")
    rk_aiq_uapi2_trackingFocus.argtypes = [POINTER(rk_aiq_sys_ctx_t)]
    rk_aiq_uapi2_trackingFocus.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 669
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_getSearchPath", "cdecl"):
        continue
    rk_aiq_uapi2_getSearchPath = _lib.get("rk_aiq_uapi2_getSearchPath", "cdecl")
    rk_aiq_uapi2_getSearchPath.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_af_sec_path_t)]
    rk_aiq_uapi2_getSearchPath.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 680
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_getSearchResult", "cdecl"):
        continue
    rk_aiq_uapi2_getSearchResult = _lib.get("rk_aiq_uapi2_getSearchResult", "cdecl")
    rk_aiq_uapi2_getSearchResult.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_af_result_t)]
    rk_aiq_uapi2_getSearchResult.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 691
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_setOpZoomPosition", "cdecl"):
        continue
    rk_aiq_uapi2_setOpZoomPosition = _lib.get("rk_aiq_uapi2_setOpZoomPosition", "cdecl")
    rk_aiq_uapi2_setOpZoomPosition.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_int]
    rk_aiq_uapi2_setOpZoomPosition.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 692
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_getOpZoomPosition", "cdecl"):
        continue
    rk_aiq_uapi2_getOpZoomPosition = _lib.get("rk_aiq_uapi2_getOpZoomPosition", "cdecl")
    rk_aiq_uapi2_getOpZoomPosition.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(c_int)]
    rk_aiq_uapi2_getOpZoomPosition.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 693
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_endOpZoomChange", "cdecl"):
        continue
    rk_aiq_uapi2_endOpZoomChange = _lib.get("rk_aiq_uapi2_endOpZoomChange", "cdecl")
    rk_aiq_uapi2_endOpZoomChange.argtypes = [POINTER(rk_aiq_sys_ctx_t)]
    rk_aiq_uapi2_endOpZoomChange.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 704
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_getZoomRange", "cdecl"):
        continue
    rk_aiq_uapi2_getZoomRange = _lib.get("rk_aiq_uapi2_getZoomRange", "cdecl")
    rk_aiq_uapi2_getZoomRange.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_af_zoomrange)]
    rk_aiq_uapi2_getZoomRange.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 705
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_getFocusRange", "cdecl"):
        continue
    rk_aiq_uapi2_getFocusRange = _lib.get("rk_aiq_uapi2_getFocusRange", "cdecl")
    rk_aiq_uapi2_getFocusRange.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_af_focusrange)]
    rk_aiq_uapi2_getFocusRange.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 716
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_startZoomCalib", "cdecl"):
        continue
    rk_aiq_uapi2_startZoomCalib = _lib.get("rk_aiq_uapi2_startZoomCalib", "cdecl")
    rk_aiq_uapi2_startZoomCalib.argtypes = [POINTER(rk_aiq_sys_ctx_t)]
    rk_aiq_uapi2_startZoomCalib.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 717
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_resetZoom", "cdecl"):
        continue
    rk_aiq_uapi2_resetZoom = _lib.get("rk_aiq_uapi2_resetZoom", "cdecl")
    rk_aiq_uapi2_resetZoom.argtypes = [POINTER(rk_aiq_sys_ctx_t)]
    rk_aiq_uapi2_resetZoom.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 728
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_setAngleZ", "cdecl"):
        continue
    rk_aiq_uapi2_setAngleZ = _lib.get("rk_aiq_uapi2_setAngleZ", "cdecl")
    rk_aiq_uapi2_setAngleZ.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_float]
    rk_aiq_uapi2_setAngleZ.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 741
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_setAcolorSwInfo", "cdecl"):
        continue
    rk_aiq_uapi2_setAcolorSwInfo = _lib.get("rk_aiq_uapi2_setAcolorSwInfo", "cdecl")
    rk_aiq_uapi2_setAcolorSwInfo.argtypes = [POINTER(rk_aiq_sys_ctx_t), rk_aiq_color_info_t]
    rk_aiq_uapi2_setAcolorSwInfo.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 762
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_setCCMMode", "cdecl"):
        continue
    rk_aiq_uapi2_setCCMMode = _lib.get("rk_aiq_uapi2_setCCMMode", "cdecl")
    rk_aiq_uapi2_setCCMMode.argtypes = [POINTER(rk_aiq_sys_ctx_t), opMode_t]
    rk_aiq_uapi2_setCCMMode.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 763
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_getCCMMode", "cdecl"):
        continue
    rk_aiq_uapi2_getCCMMode = _lib.get("rk_aiq_uapi2_getCCMMode", "cdecl")
    rk_aiq_uapi2_getCCMMode.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(opMode_t)]
    rk_aiq_uapi2_getCCMMode.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 778
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_setMCcCoef", "cdecl"):
        continue
    rk_aiq_uapi2_setMCcCoef = _lib.get("rk_aiq_uapi2_setMCcCoef", "cdecl")
    rk_aiq_uapi2_setMCcCoef.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_ccm_matrix_t)]
    rk_aiq_uapi2_setMCcCoef.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 779
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_getMCcCoef", "cdecl"):
        continue
    rk_aiq_uapi2_getMCcCoef = _lib.get("rk_aiq_uapi2_getMCcCoef", "cdecl")
    rk_aiq_uapi2_getMCcCoef.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_ccm_matrix_t)]
    rk_aiq_uapi2_getMCcCoef.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 791
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_getACcmSat", "cdecl"):
        continue
    rk_aiq_uapi2_getACcmSat = _lib.get("rk_aiq_uapi2_getACcmSat", "cdecl")
    rk_aiq_uapi2_getACcmSat.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(c_float)]
    rk_aiq_uapi2_getACcmSat.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 803
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_getACcmMatrixName", "cdecl"):
        continue
    rk_aiq_uapi2_getACcmMatrixName = _lib.get("rk_aiq_uapi2_getACcmMatrixName", "cdecl")
    rk_aiq_uapi2_getACcmMatrixName.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(POINTER(c_char))]
    rk_aiq_uapi2_getACcmMatrixName.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 821
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_setLut3dMode", "cdecl"):
        continue
    rk_aiq_uapi2_setLut3dMode = _lib.get("rk_aiq_uapi2_setLut3dMode", "cdecl")
    rk_aiq_uapi2_setLut3dMode.argtypes = [POINTER(rk_aiq_sys_ctx_t), opMode_t]
    rk_aiq_uapi2_setLut3dMode.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 822
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_getLut3dMode", "cdecl"):
        continue
    rk_aiq_uapi2_getLut3dMode = _lib.get("rk_aiq_uapi2_getLut3dMode", "cdecl")
    rk_aiq_uapi2_getLut3dMode.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(opMode_t)]
    rk_aiq_uapi2_getLut3dMode.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 838
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_setM3dLut", "cdecl"):
        continue
    rk_aiq_uapi2_setM3dLut = _lib.get("rk_aiq_uapi2_setM3dLut", "cdecl")
    rk_aiq_uapi2_setM3dLut.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_lut3d_table_t)]
    rk_aiq_uapi2_setM3dLut.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 839
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_getM3dLut", "cdecl"):
        continue
    rk_aiq_uapi2_getM3dLut = _lib.get("rk_aiq_uapi2_getM3dLut", "cdecl")
    rk_aiq_uapi2_getM3dLut.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(rk_aiq_lut3d_table_t)]
    rk_aiq_uapi2_getM3dLut.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 851
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_getA3dLutStrth", "cdecl"):
        continue
    rk_aiq_uapi2_getA3dLutStrth = _lib.get("rk_aiq_uapi2_getA3dLutStrth", "cdecl")
    rk_aiq_uapi2_getA3dLutStrth.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(c_float)]
    rk_aiq_uapi2_getA3dLutStrth.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 863
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_getA3dLutName", "cdecl"):
        continue
    rk_aiq_uapi2_getA3dLutName = _lib.get("rk_aiq_uapi2_getA3dLutName", "cdecl")
    rk_aiq_uapi2_getA3dLutName.argtypes = [POINTER(rk_aiq_sys_ctx_t), String]
    rk_aiq_uapi2_getA3dLutName.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 872
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_setLdchEn", "cdecl"):
        continue
    rk_aiq_uapi2_setLdchEn = _lib.get("rk_aiq_uapi2_setLdchEn", "cdecl")
    rk_aiq_uapi2_setLdchEn.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_bool]
    rk_aiq_uapi2_setLdchEn.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 880
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_setLdchCorrectLevel", "cdecl"):
        continue
    rk_aiq_uapi2_setLdchCorrectLevel = _lib.get("rk_aiq_uapi2_setLdchCorrectLevel", "cdecl")
    rk_aiq_uapi2_setLdchCorrectLevel.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_int]
    rk_aiq_uapi2_setLdchCorrectLevel.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 889
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_setFecEn", "cdecl"):
        continue
    rk_aiq_uapi2_setFecEn = _lib.get("rk_aiq_uapi2_setFecEn", "cdecl")
    rk_aiq_uapi2_setFecEn.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_bool]
    rk_aiq_uapi2_setFecEn.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 898
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_setFecCorrectDirection", "cdecl"):
        continue
    rk_aiq_uapi2_setFecCorrectDirection = _lib.get("rk_aiq_uapi2_setFecCorrectDirection", "cdecl")
    rk_aiq_uapi2_setFecCorrectDirection.argtypes = [POINTER(rk_aiq_sys_ctx_t), fec_correct_direction_t]
    rk_aiq_uapi2_setFecCorrectDirection.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 907
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_setFecBypass", "cdecl"):
        continue
    rk_aiq_uapi2_setFecBypass = _lib.get("rk_aiq_uapi2_setFecBypass", "cdecl")
    rk_aiq_uapi2_setFecBypass.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_bool]
    rk_aiq_uapi2_setFecBypass.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 916
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_setFecCorrectLevel", "cdecl"):
        continue
    rk_aiq_uapi2_setFecCorrectLevel = _lib.get("rk_aiq_uapi2_setFecCorrectLevel", "cdecl")
    rk_aiq_uapi2_setFecCorrectLevel.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_int]
    rk_aiq_uapi2_setFecCorrectLevel.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 925
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_setFecCorrectMode", "cdecl"):
        continue
    rk_aiq_uapi2_setFecCorrectMode = _lib.get("rk_aiq_uapi2_setFecCorrectMode", "cdecl")
    rk_aiq_uapi2_setFecCorrectMode.argtypes = [POINTER(rk_aiq_sys_ctx_t), fec_correct_mode_t]
    rk_aiq_uapi2_setFecCorrectMode.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 935
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_setMirrorFlip", "cdecl"):
        continue
    rk_aiq_uapi2_setMirrorFlip = _lib.get("rk_aiq_uapi2_setMirrorFlip", "cdecl")
    rk_aiq_uapi2_setMirrorFlip.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_bool, c_bool, c_int]
    rk_aiq_uapi2_setMirrorFlip.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 945
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_getMirrorFlip", "cdecl"):
        continue
    rk_aiq_uapi2_getMirrorFlip = _lib.get("rk_aiq_uapi2_getMirrorFlip", "cdecl")
    rk_aiq_uapi2_getMirrorFlip.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(c_bool), POINTER(c_bool)]
    rk_aiq_uapi2_getMirrorFlip.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 961
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_setContrast", "cdecl"):
        continue
    rk_aiq_uapi2_setContrast = _lib.get("rk_aiq_uapi2_setContrast", "cdecl")
    rk_aiq_uapi2_setContrast.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_uint]
    rk_aiq_uapi2_setContrast.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 963
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_getContrast", "cdecl"):
        continue
    rk_aiq_uapi2_getContrast = _lib.get("rk_aiq_uapi2_getContrast", "cdecl")
    rk_aiq_uapi2_getContrast.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(c_uint)]
    rk_aiq_uapi2_getContrast.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 973
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_setBrightness", "cdecl"):
        continue
    rk_aiq_uapi2_setBrightness = _lib.get("rk_aiq_uapi2_setBrightness", "cdecl")
    rk_aiq_uapi2_setBrightness.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_uint]
    rk_aiq_uapi2_setBrightness.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 975
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_getBrightness", "cdecl"):
        continue
    rk_aiq_uapi2_getBrightness = _lib.get("rk_aiq_uapi2_getBrightness", "cdecl")
    rk_aiq_uapi2_getBrightness.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(c_uint)]
    rk_aiq_uapi2_getBrightness.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 985
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_setSaturation", "cdecl"):
        continue
    rk_aiq_uapi2_setSaturation = _lib.get("rk_aiq_uapi2_setSaturation", "cdecl")
    rk_aiq_uapi2_setSaturation.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_uint]
    rk_aiq_uapi2_setSaturation.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 987
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_getSaturation", "cdecl"):
        continue
    rk_aiq_uapi2_getSaturation = _lib.get("rk_aiq_uapi2_getSaturation", "cdecl")
    rk_aiq_uapi2_getSaturation.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(c_uint)]
    rk_aiq_uapi2_getSaturation.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 997
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_setHue", "cdecl"):
        continue
    rk_aiq_uapi2_setHue = _lib.get("rk_aiq_uapi2_setHue", "cdecl")
    rk_aiq_uapi2_setHue.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_uint]
    rk_aiq_uapi2_setHue.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 999
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_getHue", "cdecl"):
        continue
    rk_aiq_uapi2_getHue = _lib.get("rk_aiq_uapi2_getHue", "cdecl")
    rk_aiq_uapi2_getHue.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(c_uint)]
    rk_aiq_uapi2_getHue.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 1023
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_setColorMode", "cdecl"):
        continue
    rk_aiq_uapi2_setColorMode = _lib.get("rk_aiq_uapi2_setColorMode", "cdecl")
    rk_aiq_uapi2_setColorMode.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_uint]
    rk_aiq_uapi2_setColorMode.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 1025
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_getColorMode", "cdecl"):
        continue
    rk_aiq_uapi2_getColorMode = _lib.get("rk_aiq_uapi2_getColorMode", "cdecl")
    rk_aiq_uapi2_getColorMode.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(c_uint)]
    rk_aiq_uapi2_getColorMode.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 1045
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_setColorSpace", "cdecl"):
        continue
    rk_aiq_uapi2_setColorSpace = _lib.get("rk_aiq_uapi2_setColorSpace", "cdecl")
    rk_aiq_uapi2_setColorSpace.argtypes = [POINTER(rk_aiq_sys_ctx_t), c_int]
    rk_aiq_uapi2_setColorSpace.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 1046
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_getColorSpace", "cdecl"):
        continue
    rk_aiq_uapi2_getColorSpace = _lib.get("rk_aiq_uapi2_getColorSpace", "cdecl")
    rk_aiq_uapi2_getColorSpace.argtypes = [POINTER(rk_aiq_sys_ctx_t), POINTER(c_int)]
    rk_aiq_uapi2_getColorSpace.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 1055
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_setGrayMode", "cdecl"):
        continue
    rk_aiq_uapi2_setGrayMode = _lib.get("rk_aiq_uapi2_setGrayMode", "cdecl")
    rk_aiq_uapi2_setGrayMode.argtypes = [POINTER(rk_aiq_sys_ctx_t), rk_aiq_gray_mode_t]
    rk_aiq_uapi2_setGrayMode.restype = XCamReturn
    break

# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_imgproc.h: 1063
for _lib in _libs.values():
    if not _lib.has("rk_aiq_uapi2_getGrayMode", "cdecl"):
        continue
    rk_aiq_uapi2_getGrayMode = _lib.get("rk_aiq_uapi2_getGrayMode", "cdecl")
    rk_aiq_uapi2_getGrayMode.argtypes = [POINTER(rk_aiq_sys_ctx_t)]
    rk_aiq_uapi2_getGrayMode.restype = rk_aiq_gray_mode_t
    break

rk_aiq_sys_ctx_s = struct_rk_aiq_sys_ctx_s# /usr/include/rkaiq/uAPI2/rk_aiq_user_api2_a3dlut.h: 24

paRange_s = struct_paRange_s# /usr/include/rkaiq/uAPI2/rk_aiq_user_api_common.h: 33

paRect_s = struct_paRect_s# /usr/include/rkaiq/uAPI2/rk_aiq_user_api_common.h: 66

frameRateInfo_s = struct_frameRateInfo_s# /usr/include/rkaiq/uAPI2/rk_aiq_user_api_common.h: 91

# No inserted files

# No prefix-stripping

