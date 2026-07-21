"""
Tests for AeroConvert conversion engine.

Author: Braden Moody
Version: 0.1.0
"""

from converters.conversion_engine import convert

import pytest

def test_meter_to_feet():
    """
    Test conversion from meters to feet.
    """

    result = convert(
        1,
        "length",
        "m",
        "ft"
    )

    assert round(result, 5) == 3.28084


def test_feet_to_meters():
    """
    Test conversion from feet to meters.
    """

    result = convert(
        3.28084,
        "length",
        "ft",
        "m"
    )

    assert round(result, 5) == 1.0


def test_kilometer_to_meter():
    """
    Test conversion from kilometers to meters.
    """

    result = convert(
        1,
        "length",
        "km",
        "m"
    )

    assert result == 1000.0


def test_invalid_unit():
    """
    Test that invalid units raise an error.
    """

    with pytest.raises(ValueError):

        convert(
            10,
            "length",
            "banana",
            "m"
        )


def test_kilogram_to_pound():

    result = convert(
        1,
        "mass",
        "kg",
        "lb"
    )

    assert round(result, 5) == 2.20462


def test_pound_to_kilogram():

    result = convert(
        2.20462,
        "mass",
        "lb",
        "kg"
    )

    assert round(result, 5) == 1.0