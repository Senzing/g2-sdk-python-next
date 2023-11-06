#! /usr/bin/env python3

import json

from senzing import g2config
from senzing.g2exception import G2Exception

INI_PARAMS_DICT = {
    "PIPELINE": {
        "CONFIGPATH": "/etc/opt/senzing",
        "RESOURCEPATH": "/opt/senzing/g2/resources",
        "SUPPORTPATH": "/opt/senzing/data",
    },
    "SQL": {"CONNECTION": "sqlite3://na:na@/tmp/sqlite/G2C.db"},
}
MODULE_NAME = "Example"

try:
    G2_CONFIG = g2config.G2Config()
    G2_CONFIG.init(MODULE_NAME, json.dumps(INI_PARAMS_DICT))

    # Do work.

    G2_CONFIG.destroy()
except G2Exception as err:
    print(err)
