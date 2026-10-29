import pytest

from train_fare import concession, tatkal_charge


@pytest.mark.parametrize(
    ("age", "gender", "is_tatkal", "expected"),
    [
        (2, "M", False, 100),
        (5, "M", False, 50),
        (12, "F", False, 50),
        (18, "M", False, 0),
        (60, "M", False, 40),
        (60, "F", False, 50),
        (80, "F", True, 0),
    ],
)
def test_concession_branches(age, gender, is_tatkal, expected):
    assert concession(age, gender, is_tatkal) == expected


def test_tatkal_charge_ceiling_and_floor():
    assert tatkal_charge("SL", 50) == 100
    assert tatkal_charge("2A", 1000) == 300
    assert tatkal_charge("3A", 5000) == 400
