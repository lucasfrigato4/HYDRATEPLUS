import pytest
from src.app import add_water, set_goal

def test_add_water():
    result = add_water(500)
    assert result["consumed"] >= 500

def test_invalid_water():
    with pytest.raises(ValueError):
        add_water(-100)

def test_set_goal():
    set_goal(3000)