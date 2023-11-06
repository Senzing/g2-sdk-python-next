"""
The `g2configmgr` package is used to modify Senzing configurations in the Senzing database.
It is a wrapper over Senzing's G2Configmgr C binding.
It conforms to the interface specified in
`g2configmgr_abstract.py <https://github.com/Senzing/g2-sdk-python-next/blob/main/src/senzing/g2configmgr_abstract.py>`_


To use g2configmgr,
the LD_LIBRARY_PATH environment variable must include a path to Senzing's libraries.

Example:

.. code-block:: bash

    export LD_LIBRARY_PATH=/opt/senzing/g2/lib
"""

import ctypes
import os
from typing import Any

from .g2configmgr_abstract import G2ConfigMgrAbstract
from .g2exception import G2Exception, new_g2exception
from .g2helpers import find_file_in_path

# Metadata

__all__ = ["G2ConfigMgr"]
__version__ = "0.0.1"  # See https://www.python.org/dev/peps/pep-0396/
__date__ = "2023-10-30"
__updated__ = "2023-10-30"

SENZING_PRODUCT_ID = "5041"  # See https://github.com/Senzing/knowledge-base/blob/main/lists/senzing-component-ids.md
CALLER_SKIP = 6

# -----------------------------------------------------------------------------
# Classes that are result structures from calls to Senzing
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# G2ConfigMgr class
# -----------------------------------------------------------------------------


class G2ConfigMgr(G2ConfigMgrAbstract):
    """
    The `init` method initializes the Senzing G2ConfigMgr object.
    It must be called prior to any other calls.

    **Note:** If the G2ConfigMr constructor is called with parameters,
    the constructor will automatically call the `init()` method.

    Example:

    .. code-block:: python

        g2_configmgr = g2configmgr.G2ConfigMgr(MODULE_NAME, INI_PARAMS)


    If the G2ConfigMgr constructor is called without parameters,
    the `init()` method must be called to initialize the use of G2Product.

    Example:

    .. code-block:: python

        g2_configmgr = g2configmgr.G2ConfigMgr()
        g2_configmgr.init(MODULE_NAME, INI_PARAMS)

    Either `module_name` and `ini_params` must both be specified or neither must be specified.
    Just specifying one or the other results in a **G2Exception**.

    Parameters:
        module_name:
            `Optional:` A name for the auditing node, to help identify it within system logs. Default: ""
        ini_params:
            `Optional:` A JSON string containing configuration parameters. Default: ""
        init_config_id:
            `Optional:` Specify the ID of a specific Senzing configuration. Default: 0 - Use current Senzing configuration
        verbose_logging:
            `Optional:` A flag to enable deeper logging of the G2 processing. 0 for no Senzing logging; 1 for logging. Default: 0

    Raises:
        G2Exception: Raised when input parameters are incorrect.

    .. collapse:: Example:

        .. literalinclude:: ../../examples/g2configmgr_constructor.py
            :linenos:
            :language: python
    """

    # -------------------------------------------------------------------------
    # Python dunder/magic methods
    # -------------------------------------------------------------------------

    def __init__(
        self,
        *args: Any,
        module_name: str = "",
        ini_params: str = "",
        init_config_id: int = 0,
        verbose_logging: int = 0,
        **kwargs: Any,
    ) -> None:
        """
        Constructor

        For return value of -> None, see https://peps.python.org/pep-0484/#the-meaning-of-annotations
        """

        self.ini_params = ini_params
        self.module_name = module_name
        self.noop = ""
        self.verbose_logging = verbose_logging

        try:
            if os.name == "nt":
                self.library_handle = ctypes.cdll.LoadLibrary(
                    find_file_in_path("G2.dll")
                )
            else:
                self.library_handle = ctypes.cdll.LoadLibrary("libG2.so")
        except OSError as err:
            raise G2Exception("Failed to load the G2 library") from err

        # Initialize C function input parameters and results.
        # Must be synchronized with g2/sdk/c/libg2configmgr.h

        self.library_handle.G2ConfigMgr_clearLastException.argtypes = []
        self.library_handle.G2ConfigMgr_clearLastException.restype = None
        self.library_handle.G2ConfigMgr_getLastException.argtypes = [
            ctypes.POINTER(ctypes.c_char),
            ctypes.c_size_t,
        ]
        self.library_handle.G2ConfigMgr_getLastException.restype = ctypes.c_longlong
        self.library_handle.G2GoHelper_free.argtypes = [ctypes.c_char_p]

        # Initialize Senzing engine.

        self.init(self.module_name, self.ini_params, self.verbose_logging)

    def __del__(self) -> None:
        """Destructor"""
        self.destroy()

    # -------------------------------------------------------------------------
    # Development methods - to be removed after initial development
    # -------------------------------------------------------------------------

    def fake_g2configmgr(self, *args: Any, **kwargs: Any) -> None:
        """
        TODO: Remove once SDK methods have been implemented.

        :meta private:
        """
        if len(args) + len(kwargs) > 2000:
            print(self.noop)

    # -------------------------------------------------------------------------
    # Exception helpers
    # -------------------------------------------------------------------------

    def new_exception(self, error_id: int, *args: Any) -> Exception:
        """
        Generate a new exception based on the error_id.

        :meta private:
        """
        return new_g2exception(
            self.library_handle.G2ConfigMgr_getLastException,
            self.library_handle.G2ConfigMgr_clearLastException,
            SENZING_PRODUCT_ID,
            error_id,
            self.ID_MESSAGES,
            CALLER_SKIP,
            *args,
        )

    # -------------------------------------------------------------------------
    # G2ConfigMgr methods
    # -------------------------------------------------------------------------

    def add_config(
        self, config_str: str, config_comments: str, *args: Any, **kwargs: Any
    ) -> int:
        self.fake_g2configmgr(config_str, config_comments)
        return 0

    def destroy(self, *args: Any, **kwargs: Any) -> None:
        self.fake_g2configmgr()

    def get_config(self, config_id: int, *args: Any, **kwargs: Any) -> str:
        self.fake_g2configmgr(config_id)
        return "string"

    def get_config_list(self, *args: Any, **kwargs: Any) -> str:
        self.fake_g2configmgr()
        return "string"

    def get_default_config_id(self, *args: Any, **kwargs: Any) -> int:
        self.fake_g2configmgr()
        return 0

    def init(
        self,
        module_name: str,
        ini_params: str,
        *args: Any,
        verbose_logging: int = 0,
        **kwargs: Any,
    ) -> None:
        self.fake_g2configmgr(module_name, ini_params, verbose_logging)

    def replace_default_config_id(
        self, old_config_id: int, new_config_id: int, *args: Any, **kwargs: Any
    ) -> None:
        self.fake_g2configmgr(old_config_id, new_config_id)

    def set_default_config_id(self, config_id: int, *args: Any, **kwargs: Any) -> None:
        self.fake_g2configmgr(config_id)
