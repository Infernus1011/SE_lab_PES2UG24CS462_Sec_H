import pytest

from train_fare import base_fare, tatkal_charge


def test_base_fare_valid_class_and_distance():
    assert base_fare("SL", 500) == 500
    assert base_fare("2A", 10) == 50


def test_base_fare_invalid_class():
    with pytest.raises(ValueError, match="unknown class"):
        base_fare("AC", 500)


def test_base_fare_invalid_distance():
    with pytest.raises(ValueError, match="invalid distance"):
        base_fare("SL", 0)
    with pytest.raises(ValueError, match="invalid distance"):
        base_fare("SL", -5)


def test_base_fare_floor_to_minimum():
    assert base_fare("SL", 10) == 50
    assert base_fare("3A", 1) == 50


def test_tatkal_charge_sl_case():
    assert tatkal_charge("SL", 500) == 100


def test_tatkal_charge_non_sl_case():
    assert tatkal_charge("2A", 500) == 150
    assert tatkal_charge("3A", 2500) == 400
