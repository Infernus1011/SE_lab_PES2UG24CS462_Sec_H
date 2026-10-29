import pytest
from train_fare import base_fare, concession, tatkal_charge


def test_sleeper_fare():
    assert base_fare("SL", 500) == 500


def test_base_fare_invalid_class():
    with pytest.raises(ValueError, match="unknown class"):
        base_fare("AC", 500)


def test_base_fare_invalid_distance():
    with pytest.raises(ValueError, match="invalid distance"):
        base_fare("SL", 0)
    with pytest.raises(ValueError, match="invalid distance"):
        base_fare("SL", -10)


def test_base_fare_minimum_value_applies():
    assert base_fare("SL", 10) == 50
    assert base_fare("3A", 1) == 50


@pytest.mark.parametrize(
    ("age", "gender", "is_tatkal", "expected"),
    [
        (2, "M", False, 100),
        (5, "M", False, 50),
        (12, "F", False, 50),
        (18, "M", False, 0),
        (60, "M", False, 40),
        (60, "F", False, 50),
        (70, "F", True, 0),
    ],
)
def test_concession_cases(age, gender, is_tatkal, expected):
    assert concession(age, gender, is_tatkal) == expected


def test_tatkal_charge_cases():
    assert tatkal_charge("SL", 500) == 100
    assert tatkal_charge("2A", 500) == 150
    assert tatkal_charge("3A", 2000) == 400
