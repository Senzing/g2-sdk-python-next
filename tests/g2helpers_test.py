import json

from senzing import g2helpers

# -----------------------------------------------------------------------------
# G2Config testcases
# -----------------------------------------------------------------------------


def test_as_str():
    """Test as_str."""
    a_dict = {
        "test1": "Fred",
        "test2": 5,
        "test3": {"test3.1": "Wilma"},
    }
    actual = json.dumps(a_dict)
    result1 = g2helpers.as_str(a_dict)
    assert isinstance(result1, str)
    assert result1 == actual
    result2 = g2helpers.as_str(actual)
    assert isinstance(result2, str)
    assert result2 == actual
