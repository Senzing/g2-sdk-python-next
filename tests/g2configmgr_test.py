import json

import pytest
from pytest_schema import Or, schema

from senzing import g2config, g2configmgr, g2exception

# -----------------------------------------------------------------------------
# G2ConfigMgr fixtures
# -----------------------------------------------------------------------------


@pytest.fixture(name="g2_config", scope="module")
def g2config_fixture(engine_vars):
    """
    Single engine object to use for all tests.
    engine_vars is returned from conftest.py.
    """

    result = g2config.G2Config(
        engine_vars["MODULE_NAME"],
        engine_vars["INI_PARAMS"],
    )
    return result


@pytest.fixture(name="g2_configmgr", scope="module")
def g2configmgr_instance_fixture(engine_vars):
    """Single engine object to use for all tests.
    build_engine_vars is returned from conftest.pys"""

    result = g2configmgr.G2ConfigMgr(
        engine_vars["MODULE_NAME"],
        engine_vars["INI_PARAMS"],
    )
    return result


# -----------------------------------------------------------------------------
# G2ConfigMgr schemas
# -----------------------------------------------------------------------------


config_list_schema = {
    "CONFIGS": [{"CONFIG_ID": int, "CONFIG_COMMENTS": str, "SYS_CREATE_DT": str}]
}

config_schema = {
    "G2_CONFIG": {
        "CFG_ATTR": [
            {
                "ATTR_ID": int,
                "ATTR_CODE": str,
                "ATTR_CLASS": str,
                "FTYPE_CODE": Or(str, None),
                "FELEM_CODE": Or(str, None),
                "FELEM_REQ": str,
                "DEFAULT_VALUE": Or(str, None),
                "ADVANCED": str,
                "INTERNAL": str,
            },
        ],
        "CFG_CFBOM": [
            {
                "CFCALL_ID": int,
                "FTYPE_ID": int,
                "FELEM_ID": int,
                "EXEC_ORDER": int,
            },
        ],
        "CFG_CFCALL": [
            {
                "CFCALL_ID": int,
                "FTYPE_ID": int,
                "CFUNC_ID": int,
                "EXEC_ORDER": int,
            },
        ],
        "CFG_CFRTN": [
            {
                "CFRTN_ID": int,
                "CFUNC_ID": int,
                "FTYPE_ID": int,
                "CFUNC_RTNVAL": str,
                "EXEC_ORDER": int,
                "SAME_SCORE": int,
                "CLOSE_SCORE": int,
                "LIKELY_SCORE": int,
                "PLAUSIBLE_SCORE": int,
                "UN_LIKELY_SCORE": int,
            },
        ],
        "CFG_CFUNC": [
            {
                "CFUNC_ID": int,
                "CFUNC_CODE": str,
                "CFUNC_DESC": str,
                "FUNC_LIB": str,
                "FUNC_VER": str,
                "CONNECT_STR": str,
                "ANON_SUPPORT": str,
                "LANGUAGE": Or(str, None),
                "JAVA_CLASS_NAME": Or(str, None),
            },
        ],
        "CFG_DFBOM": [
            {
                "DFCALL_ID": int,
                "FTYPE_ID": int,
                "FELEM_ID": int,
                "EXEC_ORDER": int,
            },
        ],
        "CFG_DFCALL": [
            {
                "DFCALL_ID": int,
                "FTYPE_ID": int,
                "DFUNC_ID": int,
                "EXEC_ORDER": int,
            },
        ],
        "CFG_DFUNC": [
            {
                "DFUNC_ID": int,
                "DFUNC_CODE": str,
                "DFUNC_DESC": str,
                "FUNC_LIB": str,
                "FUNC_VER": str,
                "CONNECT_STR": str,
                "ANON_SUPPORT": str,
                "LANGUAGE": Or(str, None),
                "JAVA_CLASS_NAME": Or(str, None),
            },
        ],
        "CFG_DSRC": [
            {
                "DSRC_ID": int,
                "DSRC_CODE": str,
                "DSRC_DESC": str,
                "DSRC_RELY": int,
                "RETENTION_LEVEL": str,
                "CONVERSATIONAL": str,
            },
        ],
        "CFG_DSRC_INTEREST": [],
        "CFG_ECLASS": [
            {
                "ECLASS_ID": int,
                "ECLASS_CODE": str,
                "ECLASS_DESC": str,
                "RESOLVE": str,
            },
        ],
        "CFG_EFBOM": [
            {
                "EFCALL_ID": int,
                "FTYPE_ID": int,
                "FELEM_ID": int,
                "EXEC_ORDER": int,
                "FELEM_REQ": str,
            },
        ],
        "CFG_EFCALL": [
            {
                "EFCALL_ID": int,
                "FTYPE_ID": int,
                "FELEM_ID": int,
                "EFUNC_ID": int,
                "EXEC_ORDER": int,
                "EFEAT_FTYPE_ID": int,
                "IS_VIRTUAL": str,
            },
        ],
        "CFG_EFUNC": [
            {
                "EFUNC_ID": int,
                "EFUNC_CODE": str,
                "EFUNC_DESC": str,
                "FUNC_LIB": str,
                "FUNC_VER": str,
                "CONNECT_STR": str,
                "LANGUAGE": Or(str, None),
                "JAVA_CLASS_NAME": Or(str, None),
            },
        ],
        "CFG_ERFRAG": [
            {
                "ERFRAG_ID": int,
                "ERFRAG_CODE": str,
                "ERFRAG_DESC": str,
                "ERFRAG_SOURCE": str,
                "ERFRAG_DEPENDS": Or(str, None),
            },
        ],
        "CFG_ERRULE": [
            {
                "ERRULE_ID": int,
                "ERRULE_CODE": str,
                "ERRULE_DESC": str,
                "RESOLVE": str,
                "RELATE": str,
                "REF_SCORE": int,
                "RTYPE_ID": int,
                "QUAL_ERFRAG_CODE": str,
                "DISQ_ERFRAG_CODE": Or(str, None),
                "ERRULE_TIER": Or(int, None),
            },
        ],
        "CFG_ETYPE": [
            {
                "ETYPE_ID": int,
                "ETYPE_CODE": str,
                "ETYPE_DESC": str,
                "ECLASS_ID": int,
            },
        ],
        "CFG_FBOM": [
            {
                "FTYPE_ID": int,
                "FELEM_ID": int,
                "EXEC_ORDER": int,
                "DISPLAY_LEVEL": int,
                "DISPLAY_DELIM": Or(str, None),
                "DERIVED": str,
            },
        ],
        "CFG_FBOVR": [
            {
                "FTYPE_ID": int,
                "ECLASS_ID": int,
                "UTYPE_CODE": str,
                "FTYPE_FREQ": str,
                "FTYPE_EXCL": str,
                "FTYPE_STAB": str,
            },
        ],
        "CFG_FCLASS": [
            {
                "FCLASS_ID": int,
                "FCLASS_CODE": str,
                "FCLASS_DESC": str,
            },
        ],
        "CFG_FELEM": [
            {
                "FELEM_ID": int,
                "FELEM_CODE": str,
                "FELEM_DESC": str,
                "TOKENIZE": str,
                "DATA_TYPE": str,
            },
        ],
        "CFG_FTYPE": [
            {
                "FTYPE_ID": int,
                "FTYPE_CODE": Or(str, None),
                "FTYPE_DESC": str,
                "FCLASS_ID": int,
                "FTYPE_FREQ": str,
                "FTYPE_EXCL": str,
                "FTYPE_STAB": str,
                "PERSIST_HISTORY": str,
                "USED_FOR_CAND": str,
                "DERIVED": str,
                "DERIVATION": Or(str, None),
                "RTYPE_ID": int,
                "ANONYMIZE": str,
                "VERSION": int,
                "SHOW_IN_MATCH_KEY": str,
            },
        ],
        "CFG_GENERIC_THRESHOLD": [
            {
                "GPLAN_ID": int,
                "BEHAVIOR": str,
                "FTYPE_ID": int,
                "CANDIDATE_CAP": int,
                "SCORING_CAP": int,
                "SEND_TO_REDO": str,
            },
        ],
        "CFG_GPLAN": [
            {
                "GPLAN_ID": int,
                "GPLAN_CODE": str,
                "GPLAN_DESC": str,
            },
        ],
        "CFG_LENS": [
            {
                "LENS_ID": int,
                "LENS_CODE": str,
                "LENS_DESC": str,
            },
        ],
        "CFG_LENSRL": [],
        "CFG_RCLASS": [
            {
                "RCLASS_ID": int,
                "RCLASS_CODE": str,
                "RCLASS_DESC": str,
                "IS_DISCLOSED": str,
            },
        ],
        "CFG_RTYPE": [
            {
                "RTYPE_ID": int,
                "RTYPE_CODE": str,
                "RTYPE_DESC": str,
                "RCLASS_ID": int,
                "REL_STRENGTH": int,
                "BREAK_RES": str,
            },
        ],
        "CFG_SFCALL": [
            {
                "SFCALL_ID": int,
                "FTYPE_ID": int,
                "FELEM_ID": int,
                "SFUNC_ID": int,
                "EXEC_ORDER": int,
            },
        ],
        "CFG_SFUNC": [
            {
                "SFUNC_ID": int,
                "SFUNC_CODE": str,
                "SFUNC_DESC": str,
                "FUNC_LIB": str,
                "FUNC_VER": str,
                "CONNECT_STR": str,
                "LANGUAGE": Or(str, None),
                "JAVA_CLASS_NAME": Or(str, None),
            },
        ],
        "SYS_OOM": [
            {
                "OOM_TYPE": str,
                "OOM_LEVEL": str,
                "LENS_ID": int,
                "FTYPE_ID": int,
                "LIB_FEAT_ID": int,
                "FELEM_ID": int,
                "LIB_FELEM_ID": int,
                "THRESH1_CNT": int,
                "THRESH1_OOM": int,
                "NEXT_THRESH": int,
            },
        ],
        "CONFIG_BASE_VERSION": {
            "VERSION": str,
            "BUILD_VERSION": str,
            "BUILD_DATE": str,
            "BUILD_NUMBER": str,
            "COMPATIBILITY_VERSION": {
                "CONFIG_VERSION": str,
            },
        },
    },
}


# -----------------------------------------------------------------------------
# G2ConfigMgr testcases
# -----------------------------------------------------------------------------


def test_exception(g2_configmgr):
    """Test exceptions."""
    actual = g2_configmgr.new_exception(0)
    assert isinstance(actual, Exception)


def test_constructor(engine_vars):
    """Test constructor."""
    actual = g2configmgr.G2ConfigMgr(
        engine_vars["MODULE_NAME"],
        engine_vars["INI_PARAMS"],
    )
    assert isinstance(actual, g2configmgr.G2ConfigMgr)


def test_constructor_dict(engine_vars):
    """Test constructor."""
    actual = g2configmgr.G2ConfigMgr(
        engine_vars["MODULE_NAME"],
        engine_vars["INI_PARAMS_DICT"],
    )
    assert isinstance(actual, g2configmgr.G2ConfigMgr)


def test_constructor_bad_module_name(engine_vars):
    """Test constructor."""
    bad_module_name = ""
    with pytest.raises(g2exception.G2Exception):
        actual = g2configmgr.G2ConfigMgr(
            bad_module_name,
            engine_vars["INI_PARAMS"],
        )
        assert isinstance(actual, g2configmgr.G2ConfigMgr)


def test_constructor_bad_ini_params(engine_vars):
    """Test constructor."""
    bad_ini_params = ""
    with pytest.raises(g2exception.G2Exception):
        actual = g2configmgr.G2ConfigMgr(
            engine_vars["MODULE_NAME"],
            bad_ini_params,
        )
        assert isinstance(actual, g2configmgr.G2ConfigMgr)


def test_add_config(g2_configmgr, g2_config):
    """Test G2ConfigMgr().add_config()."""
    config_handle = g2_config.create()
    config_str = g2_config.save(config_handle)
    config_comments = "Test"
    actual = g2_configmgr.add_config(config_str, config_comments)
    assert isinstance(actual, int)
    assert actual > 0


def test_add_config_dict(g2_configmgr, g2_config):
    """Test G2ConfigMgr().add_config()."""
    config_handle = g2_config.create()
    config_str = g2_config.save(config_handle)
    config_str_dict = json.loads(config_str)
    config_comments = "Test"
    actual = g2_configmgr.add_config(config_str_dict, config_comments)
    assert isinstance(actual, int)
    assert actual > 0


def test_add_config_bad_config_str_type(g2_configmgr):
    """Test G2ConfigMgr().add_config()."""
    bad_config_str = 0
    config_comments = "Test"
    with pytest.raises(TypeError):
        g2_configmgr.add_config(bad_config_str, config_comments)


def test_add_config_bad_config_str_value(g2_configmgr):
    """Test G2ConfigMgr().add_config()."""
    config_str_dict = {"just": "junk"}
    config_comments = "Test"
    actual = g2_configmgr.add_config(config_str_dict, config_comments)
    assert isinstance(actual, int)
    assert actual > 0


def test_add_config_bad_config_comments_type(g2_configmgr, g2_config):
    """Test G2ConfigMgr().add_config()."""
    config_handle = g2_config.create()
    config_str = g2_config.save(config_handle)
    bad_config_comments = 0
    with pytest.raises(TypeError):
        g2_configmgr.add_config(config_str, bad_config_comments)


def test_get_config(g2_configmgr):
    """Test G2ConfigMgr().get_default_config_id()."""
    config_id = g2_configmgr.get_default_config_id()
    actual = g2_configmgr.get_config(config_id)
    actual_json = json.loads(actual)
    assert schema(config_schema) == actual_json


def test_get_config_bad_config_id_type(g2_configmgr):
    """Test G2ConfigMgr().get_default_config_id()."""
    bad_config_id = "string"
    with pytest.raises(TypeError):
        g2_configmgr.get_config(bad_config_id)


def test_get_config_bad_config_id_value(g2_configmgr):
    """Test G2ConfigMgr().get_default_config_id()."""
    bad_config_id = 1234
    with pytest.raises(g2exception.G2ConfigurationError):
        g2_configmgr.get_config(bad_config_id)


def test_get_config_list(g2_configmgr):
    """Test G2ConfigMgr().get_default_config_id()."""
    actual = g2_configmgr.get_config_list()
    actual_json = json.loads(actual)
    assert schema(config_list_schema) == actual_json


def test_get_default_config_id(g2_configmgr):
    """Test G2ConfigMgr().get_default_config_id()."""
    actual = g2_configmgr.get_default_config_id()
    assert isinstance(actual, int)


def test_replace_default_config_id(g2_configmgr, g2_config):
    """Test G2ConfigMgr().get_default_config_id()."""
    old_config_id = g2_configmgr.get_default_config_id()
    config_handle = g2_config.create()
    input_json_dict = {"DSRC_CODE": "REPLACE_DEFAULT_CONFIG_ID"}
    g2_config.add_data_source(config_handle, json.dumps(input_json_dict))
    json_config = g2_config.save(config_handle)
    new_config_id = g2_configmgr.add_config(json_config, "Test")
    assert old_config_id != new_config_id
    g2_configmgr.replace_default_config_id(old_config_id, new_config_id)
    actual = g2_configmgr.get_default_config_id()
    assert actual == new_config_id


def test_replace_default_config_id_bad_new_id_type(g2_configmgr):
    """Test G2ConfigMgr().get_default_config_id()."""
    old_config_id = g2_configmgr.get_default_config_id()
    bad_new_config_id = "string"
    with pytest.raises(TypeError):
        g2_configmgr.replace_default_config_id(old_config_id, bad_new_config_id)


def test_replace_default_config_id_bad_new_id_value(g2_configmgr):
    """Test G2ConfigMgr().get_default_config_id()."""
    old_config_id = g2_configmgr.get_default_config_id()
    bad_new_config_id = 1234
    with pytest.raises(g2exception.G2ConfigurationError):
        g2_configmgr.replace_default_config_id(old_config_id, bad_new_config_id)


def test_replace_default_config_id_bad_old_id_type(g2_configmgr, g2_config):
    """Test G2ConfigMgr().get_default_config_id()."""
    bad_old_config_id = "string"
    config_handle = g2_config.create()
    input_json_dict = {"DSRC_CODE": "REPLACE_DEFAULT_CONFIG_ID"}
    g2_config.add_data_source(config_handle, json.dumps(input_json_dict))
    json_config = g2_config.save(config_handle)
    new_config_id = g2_configmgr.add_config(json_config, "Test")
    with pytest.raises(TypeError):
        g2_configmgr.replace_default_config_id(bad_old_config_id, new_config_id)


def test_replace_default_config_id_bad_old_id_value(g2_configmgr, g2_config):
    """Test G2ConfigMgr().get_default_config_id()."""
    bad_old_config_id = 1234
    config_handle = g2_config.create()
    input_json_dict = {"DSRC_CODE": "REPLACE_DEFAULT_CONFIG_ID"}
    g2_config.add_data_source(config_handle, json.dumps(input_json_dict))
    json_config = g2_config.save(config_handle)
    new_config_id = g2_configmgr.add_config(json_config, "Test")
    with pytest.raises(g2exception.G2ConfigurationError):
        g2_configmgr.replace_default_config_id(bad_old_config_id, new_config_id)


def test_set_default_config_id(g2_configmgr, g2_config):
    """Test G2ConfigMgr().get_default_config_id()."""
    old_config_id = g2_configmgr.get_default_config_id()
    config_handle = g2_config.create()
    input_json_dict = {"DSRC_CODE": "SET_DEFAULT_CONFIG_ID"}
    g2_config.add_data_source(config_handle, json.dumps(input_json_dict))
    json_config = g2_config.save(config_handle)
    new_config_id = g2_configmgr.add_config(json_config, "Test")
    assert old_config_id != new_config_id
    g2_configmgr.set_default_config_id(new_config_id)
    actual = g2_configmgr.get_default_config_id()
    assert actual == new_config_id


def test_set_default_config_id_bad_config_id_type(g2_configmgr):
    """Test G2ConfigMgr().get_default_config_id()."""
    bad_config_id = "string"
    with pytest.raises(TypeError):
        g2_configmgr.set_default_config_id(bad_config_id)


def test_set_default_config_id_bad_config_id_value(g2_configmgr):
    """Test G2ConfigMgr().set_default_config_id()."""
    bad_config_id = 1
    with pytest.raises(g2exception.G2ConfigurationError):
        g2_configmgr.set_default_config_id(bad_config_id)


def test_init_and_destroy(g2_configmgr):
    """Test G2ConfigMgr().init() and G2ConfigMgr.destroy()."""
    g2_configmgr.init("Example", "{}", 0)
    g2_configmgr.destroy()


def test_init_and_destroy_again(g2_configmgr):
    """Test G2ConfigMgr().init() and G2ConfigMgr.destroy()."""
    g2_configmgr.init("Example", "{}", 0)
    g2_configmgr.destroy()
