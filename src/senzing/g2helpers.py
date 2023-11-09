"""
TODO: g2helpers.py
"""

import os
from ctypes import POINTER, c_char_p, c_uint, c_void_p, cast
from typing import Any

uintptr_type = POINTER(c_uint)

# -----------------------------------------------------------------------------
# Helpers for working with C
# -----------------------------------------------------------------------------


# TODO: Figure out better return type hint (e.g. POINTER[c_uint], _Pointer[c_uint])
def as_uintptr_t(candidate_value: int) -> Any:
    """
    Internal processing function.
    This converts many types of values to an integer.

    :meta private:
    """

    result = cast(candidate_value, POINTER(c_uint))
    return result


def as_c_int(candidate_value: Any) -> int:
    """
    Internal processing function.
    This converts many types of values to an integer.

    :meta private:
    """

    if candidate_value is None:  # handle null string
        return int(0)
    if isinstance(candidate_value, str):  # if string is unicode, transcode to utf-8 str
        return int(candidate_value.encode("utf-8"))
    if isinstance(
        candidate_value, bytearray
    ):  # if input is bytearray, assumt utf-8 and convert to str
        return int(candidate_value)
    if isinstance(candidate_value, bytes):
        return int(candidate_value)
    # input is already an int
    return int(candidate_value)


def as_c_char_p(candidate_value: Any) -> Any:
    """
    Internal processing function.

    :meta private:
    """

    if candidate_value is None:  # handle null string
        return b""
    if isinstance(candidate_value, str):  # if string is unicode, transcode to utf-8 str
        return candidate_value.encode("utf-8")
    if isinstance(
        candidate_value, bytearray
    ):  # if input is bytearray, assumt utf-8 and convert to str
        return candidate_value.decode().encode("utf-8")
    if isinstance(candidate_value, bytes):
        return str(candidate_value).encode("utf-8")
    # input is already a str
    return candidate_value


def as_python_int(candidate_value: Any) -> int:
    """
    From a c_void_p, return a true python int.

    Args:
        candidate_value (Any): A c_void_p to be transformed.

    Returns:
        int: The python int representation

    :meta private:
    """

    result = cast(candidate_value, c_void_p).value
    if result is None:
        result = 0
    return result


def as_python_str(candidate_value: Any) -> str:
    """
    From a c_char_p, return a true python str,

    Args:
        candidate_value (Any): A c_char_p value to be transformed.

    Returns:
        str: The python string representation.

    :meta private:
    """
    result_raw = cast(candidate_value, c_char_p).value
    result = result_raw.decode() if result_raw else ""
    return result


# ---------------------w----------------------------------------------------
# Helpers for working with files and directories.
# -----------------------------------------------------------------------------


def find_file_in_path(filename: str) -> str:
    """
    Find a file in the PATH environment variable.

    :meta private:
    """
    path_dirs = os.environ["PATH"].split(os.pathsep)
    for path_dir in path_dirs:
        file_path = os.path.join(path_dir, filename)
        if os.path.exists(file_path):
            return file_path
    return ""
