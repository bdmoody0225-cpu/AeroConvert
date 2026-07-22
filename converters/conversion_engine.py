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

FORCE_UNITS = {
    "n": 1.0,
    "kn": 1000.0,
    "mn": 1_000_000.0,
    "lbf": 4.4482216152605,
    "dyn": 0.00001
}

PRESSURE_UNITS = {
    "pa": 1.0,
    "kpa": 1000.0,
    "mpa": 1000000.0,
    "bar": 100000.0,
    "atm": 101325.0,
    "psi": 6894.757293168
}

VELOCITY_UNITS = {
    "m/s": 1.0,
    "km/h": 0.2777777778,
    "ft/s": 0.3048,
    "mph": 0.44704,
    "kt": 0.5144444444
}

AREA_UNITS = {
    "m2": 1.0,
    "cm2": 0.0001,
    "mm2": 0.000001,
    "ft2": 0.09290304,
    "in2": 0.00064516,
    "yd2": 0.83612736,
    "acre": 4046.8564224
}

VOLUME_UNITS = {
    "m3": 1.0,
    "cm3": 0.000001,
    "L": 0.001,
    "mL": 0.000001,
    "ft3": 0.283168466,
    "in3": 0.000016387064,
    "gal": 0.003785411784
}

DENSITY_UNITS = {
    "kg/m3": 1.0,
    "g/cm3": 1000.0,
    "lb/ft3": 16.01846337,
    "slug/ft3": 515.378818
}

UNIT_DATABASE = {
    "length": LENGTH_UNITS,
    "mass": MASS_UNITS,
    "force": FORCE_UNITS,
    "pressure": PRESSURE_UNITS,
    "velocity": VELOCITY_UNITS,
    "area": AREA_UNITS,
    "volume": VOLUME_UNITS,
    "density": DENSITY_UNITS
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

    if category == "temperature":
        return convert_temperature(
            value,
            from_unit,
            to_unit
        )

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

def convert_temperature(
        value: float,
        from_unit: str,
        to_unit: str
) -> float:
    
    """
    Convert temperature between Celsius,
    Farenheit, and Kelvin
    """

    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    if from_unit == "c":
        celsius = value

    elif from_unit == "f":
        celsius = (value - 32) * 5 / 9

    elif from_unit == "k":
        celsius = value - 273.15

    else:
        raise ValueError(f"Unsupported temperature unit: {from_unit}")
    

    if to_unit == "c":
        return celsius
    
    elif to_unit == "f":
        return (celsius * 9 / 5) + 32
    
    elif to_unit == "k":
        return celsius + 273.15
    
    else: 
        raise ValueError(f"Unsupported temperature unit: {to_unit}")


if __name__ == "__main__":

    result = convert(
        10,
        "length",
        "m",
        "ft"
    )

    print(result)