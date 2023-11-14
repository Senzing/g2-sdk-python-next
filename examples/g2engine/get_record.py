#! /usr/bin/env python3

import json

from senzing import g2engine
from senzing.g2exception import G2Exception

ini_params_dict = {
    "PIPELINE": {
        "CONFIGPATH": "/etc/opt/senzing",
        "RESOURCEPATH": "/opt/senzing/g2/resources",
        "SUPPORTPATH": "/opt/senzing/data",
    },
    "SQL": {"CONNECTION": "sqlite3://na:na@/tmp/sqlite/G2C.db"},
}
# Const should be at top
# TODO Change this to use truthset data?
MODULE_NAME = "Example"
data_source_code = "TEST"
record_id = "Example-1"

try:
    g2_engine = g2engine.G2Engine(MODULE_NAME, json.dumps(ini_params_dict))
    result = g2_engine.get_record(data_source_code, record_id)
    print(result)
except G2Exception as err:
    print(err)
