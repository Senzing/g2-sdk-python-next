#! /usr/bin/env python3

# -----------------------------------------------------------------------------
# G2Engine.py
# -----------------------------------------------------------------------------

# Import from standard library. https://docs.python.org/3/library/

from ctypes import *
import functools
import json
import os
import threading
import warnings

# Import from https://pypi.org/

# Import from Senzing.

from .G2Exception import TranslateG2ModuleException, G2ModuleNotInitialized, G2ModuleGenericException
from .G2EngineFlags import G2EngineFlags

# Metadata

__all__ = ['G2Engine']
__version__ = "0.0.1"  # See https://www.python.org/dev/peps/pep-0396/
__date__ = '2023-10-30'
__updated__ = '2023-10-30'


SENZING_PRODUCT_ID = "5043"  # See https://github.com/Senzing/knowledge-base/blob/main/lists/senzing-component-ids.md
