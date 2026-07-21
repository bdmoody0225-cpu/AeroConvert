"""
AeroConvert Conversion Engine

Provides a universal unit conversion system.

Author: Braden Moody
Version: 0.1.0
"""

LENGTH_UNITS = {
    "m": 1.0,
    "km": 1000.0,
    "cm": 0.01,
    "mm": 0.001,
    "ft": 0.3048,
    "in": 0.0254,
    "yd": 0.9144,
    "mi": 1609.344,
    "nmi": 1852.0
}

MASS_UNITS = {
    "kg": 1.0,
    "g": 0.001,
    "mg": 0.000001,
    "lb": 0.45359237,
    "oz": 0.028349523125,
    "slug": 14.59390294,
    "t": 1000.0
}

UNIT_DATABASE = {
    "length": LENGTH_UNITS,
    "mass": MASS_UNITS
}

def convert_length(value: float, from_unit: str, to_unit: str) -> float:

    """
    Convert a length value between supported units.

    Parameters:
        Value:
            The numerical value to convert.

        from_unit:
            Original Unit.

        to_unit:
            Desired unit.

    Returns:
        Converted value.
    """

    if from_unit not in LENGTH_UNITS:
        raise ValueError(f"Unsupported unit: {from_unit}")
    
    if to_unit not in LENGTH_UNITS:
        raise ValueError(f"Unsupported unit: {to_unit}")
    
    meters = value * LENGTH_UNITS[from_unit]

    converted = meters / LENGTH_UNITS[to_unit]

    return converted

def convert(
        value: float,
        category: str,
        from_unit: str,
        to_unit: str
) -> float:
    
    """
    Universal unit conversion function.
    """

    if category not in UNIT_DATABASE:
        raise ValueError(f"Unsupported category: {category}")
    
    units = UNIT_DATABASE[category]

    if from_unit not in units:
        raise ValueError(f"Unsupported unit: {from_unit}")
    
    if to_unit not in units:
        raise ValueError(f"Unsupported unit: {to_unit}")
    
    base_value = value * units[from_unit]

    converted_value = base_value / units[to_unit]

    return converted_value


if __name__ == "__main__":

    result = convert(
        10,
        "length",
        "m",
        "ft"
    )

    print(result)