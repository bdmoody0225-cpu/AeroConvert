"""
Tests for AeroConvert conversion engine.

Author: Braden Moody
Version: 0.3.0
"""

import pytest

from converters.conversion_engine import convert


# ==========================================================
# LENGTH TESTS
# ==========================================================

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


def test_feet_to_meter():
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


# ==========================================================
# MASS TESTS
# ==========================================================

def test_kilogram_to_pound():
    """
    Test conversion from kilograms to pounds.
    """

    result = convert(
        1,
        "mass",
        "kg",
        "lb"
    )

    assert round(result, 5) == 2.20462


def test_pound_to_kilogram():
    """
    Test conversion from pounds to kilograms.
    """

    result = convert(
        2.20462,
        "mass",
        "lb",
        "kg"
    )

    assert round(result, 5) == 1.0


def test_metric_ton_to_kilogram():
    """
    Test conversion from metric tons to kilograms.
    """

    result = convert(
        2,
        "mass",
        "t",
        "kg"
    )

    assert result == 2000.0


# ==========================================================
# FORCE TESTS
# ==========================================================

def test_newton_to_pound_force():
    """
    Test conversion from newtons to pound-force.
    """

    result = convert(
        1,
        "force",
        "n",
        "lbf"
    )

    assert round(result, 5) == 0.22481


def test_pound_force_to_newton():
    """
    Test conversion from pound-force to newtons.
    """

    result = convert(
        1,
        "force",
        "lbf",
        "n"
    )

    assert round(result, 5) == 4.44822


def test_kilonewton_to_newton():
    """
    Test conversion from kilonewtons to newtons.
    """

    result = convert(
        5,
        "force",
        "kn",
        "n"
    )

    assert result == 5000.0


# ==========================================================
# ERROR HANDLING TESTS
# ==========================================================

def test_invalid_unit():
    """
    Test that an invalid unit raises a ValueError.
    """

    with pytest.raises(ValueError):

        convert(
            10,
            "length",
            "banana",
            "m"
        )


def test_invalid_category():
    """
    Test that an invalid category raises a ValueError.
    """

    with pytest.raises(ValueError):

        convert(
            10,
            "pizza",
            "kg",
            "lb"
        )