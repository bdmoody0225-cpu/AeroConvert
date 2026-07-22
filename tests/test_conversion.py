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
# TEMPERATURE TESTS
# ==========================================================

def test_celsius_to_farenheit():
    """
    Test conversion from celsius to farenheit.
    """

    result = convert(
        0,
        "temperature",
        "c",
        "f"
    )

    assert result == 32.0


def test_farenheit_to_celsius():
    """
    Test conversion from farenheit to celsius.
    """

    result = convert(
        32,
        "temperature",
        "f",
        "c"
    )

    assert result == 0.0

def test_celsius_to_kelvin():
    """
    Test conversion from celsius to kelvin.
    """

    result = convert(
        100,
        "temperature",
        "c",
        "k"
    )

    assert result == 373.15

def test_kelvin_to_celsius():
    """
    Test conversion from kelvin to celsius.
    """

    result = convert(
        273.15,
        "temperature",
        "k",
        "c"
    )

    assert result == 0.0

# ==========================================================
# PRESSURE TESTS
# ==========================================================

def test_pascal_to_kilopascal():
    """
    Test conversion from pascals to kilopascals.
    """

    result = convert(
        1000,
        "pressure",
        "pa",
        "kpa"
    )

    assert result == 1.0

def test_bar_to_pascal():
    """
    Test conversion from bar to pascal.
    """

    result = convert(
        1,
        "pressure",
        "bar",
        "pa"
    )

    assert result == 100000.0

def test_atm_to_psi():
    """
    Test conversion from atmospheres to psi.
    """

    result = convert(
        1,
        "pressure",
        "atm",
        "psi"
    )

    assert round(result, 4) == 14.6959

def test_psi_to_pascal():
    """
    Test conversion from psi to pascals.
    """

    result = convert(
        1,
        "pressure",
        "psi",
        "pa"
    )

    assert round(result, 3) == 6894.757

# ==========================================================
# VELOCITY TESTS
# ==========================================================

def test_mph_to_kph():
    """
    Test conversion from meters per second to kilometers per hour.
    """

    result = convert(
        10,
        "velocity",
        "m/s",
        "km/h"
    )

    assert round(result, 1) == 36.0

def test_kph_to_mps():
    """
    Test conversion from kilometers per hour ro meters per second.
    """

    result = convert(
        36,
        "velocity",
        "km/h",
        "m/s"
    )

    assert round(result, 1) == 10.0

def test_mph_to_knots():
    """
    Test conversion from miles per hour to knots.
    """

    result = convert(
        100,
        "velocity",
        "mph",
        "kt"
    )

    assert round(result, 2) == 86.90

def test_knots_to_mps():
    """
    Test conversion from knots to meters per second.
    """

    result = convert(
        100,
        "velocity",
        "kt",
        "m/s"
    )

    assert round(result, 3) == 51.444

# ==========================================================
# AREA TESTS
# ==========================================================

def test_square_meter_to_square_centimeter():
    """
    Test conversion from square meters to square centimeters.
    """

    result = convert(
        1,
        "area",
        "m2",
        "cm2"
    )

    assert result == 10000.0


def test_square_foot_to_square_meter():
    """
    Test conversion from square feet to square meters.
    """

    result = convert(
        1,
        "area",
        "ft2",
        "m2"
    )

    assert round(result, 8) == 0.09290304


def test_acre_to_square_meter():
    """
    Test conversion from acres to square meters.
    """

    result = convert(
        1,
        "area",
        "acre",
        "m2"
    )

    assert round(result, 4) == 4046.8564

# ==========================================================
# VOLUME TESTS
# ==========================================================

def test_cubic_meter_to_liter():
    """
    Test conversion from cubic meters to liters.
    """

    result = convert(
        1,
        "volume",
        "m3",
        "L"
    )

    assert result == 1000.0


def test_liter_to_milliliter():
    """
    Test conversion from liters to milliliters.
    """

    result = convert(
        1,
        "volume",
        "L",
        "mL"
    )

    assert round(result, 6) == 1000.0


def test_gallon_to_liter():
    """
    Test conversion from gallons to liters.
    """

    result = convert(
        1,
        "volume",
        "gal",
        "L"
    )

    assert round(result, 6) == 3.785412

# ==========================================================
# DENSITY TESTS
# ==========================================================

def test_g_cm3_to_kg_m3():
    """
    Test conversion from grams per cubic centimeter
    to kilograms per cubic meter.
    """

    result = convert(
        1,
        "density",
        "g/cm3",
        "kg/m3"
    )

    assert result == 1000.0


def test_kg_m3_to_g_cm3():
    """
    Test conversion from kilograms per cubic meter
    to grams per cubic centimeter.
    """

    result = convert(
        1000,
        "density",
        "kg/m3",
        "g/cm3"
    )

    assert result == 1.0


def test_lb_ft3_to_kg_m3():
    """
    Test conversion from pounds per cubic foot
    to kilograms per cubic meter.
    """

    result = convert(
        1,
        "density",
        "lb/ft3",
        "kg/m3"
    )

    assert round(result, 5) == 16.01846


def test_slug_ft3_to_kg_m3():
    """
    Test conversion from slugs per cubic foot
    to kilograms per cubic meter.
    """

    result = convert(
        1,
        "density",
        "slug/ft3",
        "kg/m3"
    )

    assert round(result, 3) == 515.379

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