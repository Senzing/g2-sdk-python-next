# import json

import pytest

from senzing import g2engine

# from pytest_schema import schema

# -----------------------------------------------------------------------------
# G2Engine fixtures
# -----------------------------------------------------------------------------


@pytest.fixture(name="g2engine_instance", scope="module")
def g2engine_instance_fixture(engine_vars):
    """Single engine object to use for all tests.
    engine_vars is returned from conftest.pys"""
    result = g2engine.G2Engine(
        engine_vars["MODULE_NAME"],
        engine_vars["INI_PARAMS"],
    )
    return result


# -----------------------------------------------------------------------------
# G2Engine schemas
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# G2Engine testcases
# -----------------------------------------------------------------------------


def test_init_and_destroy_01(engine_vars):
    """Test G2Engine().init() and G2Engine.destroy()."""
    g2_engine = g2engine.G2Engine()
    g2_engine.init(engine_vars["MODULE_NAME"], engine_vars["INI_PARAMS"], 0)
    g2_engine.destroy()


def test_init_and_destroy_02(engine_vars):
    """Test G2Engine().init() and G2Engine.destroy()."""
    g2_engine_2 = g2engine.G2Engine()
    g2_engine_2.init(engine_vars["MODULE_NAME"], engine_vars["INI_PARAMS"], 0)
    g2_engine_2.destroy()
