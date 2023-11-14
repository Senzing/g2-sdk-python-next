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
# Consts should be at top
MODULE_NAME = "Example"

data_source_code = "TEST"
record_id_1 = "Example-1"
record_id_2 = "Example-2"
record = {
    "RECORD_TYPE": "PERSON",
    "PRIMARY_NAME_LAST": "Smith",
    "PRIMARY_NAME_FIRST": "Robert",
    "DATE_OF_BIRTH": "12/11/1978",
    "ADDR_TYPE": "MAILING",
    "ADDR_LINE1": "123 Main Street, Las Vegas NV 89132",
    "PHONE_TYPE": "HOME",
    "PHONE_NUMBER": "702-919-1300",
    "EMAIL_ADDRESS": "bsmith@work.com",
    "DATE": "1/2/18",
    "STATUS": "Active",
    "AMOUNT": "100",
}

try:
    g2_engine = g2engine.G2Engine(MODULE_NAME, json.dumps(ini_params_dict))
    g2_engine.add_record(data_source_code, record_id_1, json.dumps(record))
except G2Exception as err:
    print(err)

try:
    g2_engine = g2engine.G2Engine(MODULE_NAME, json.dumps(ini_params_dict))
    result = g2_engine.add_record(
        data_source_code, record_id_2, json.dumps(record), with_info=True
    )
    print(result)
except G2Exception as err:
    print(err)
