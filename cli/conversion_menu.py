"""
AeroConvert Conversion Menu

Handles user interaction for unit conversions.

Author: Braden Moody
Version: 0.3.0
"""

from converters.conversion_engine import convert
from converters.conversion_engine import convert_temperature

UNIT_DISPLAY = {
    "length": {
        "m": "Meter",
        "km": "Kilometer",
        "cm": "Centimeter",
        "mm": "Millimeter",
        "ft": "Foot",
        "yd": "Yard",
        "mi": "Mile",
        "nmi": "Nautical Mile",
    },

    "mass": {
        "kg": "Kilogram",
        "g": "Gram",
        "mg": "Milligram",
        "lb": "Pound",
        "oz": "Ounce",
        "slug": "Slug",
        "t": "Metric Ton",
    },

    "force": {
        "n": "Newton",
        "kn": "Kilonewton",
        "mn": "Meganewton",
        "lbf": "Pound Force",
        "dyn": "Dyne",
    },

    "temperature": {
        "c": "Celsius",
        "f": "Farenheit",
        "k": "Kelvin"
    },

    "pressure": {
        "pa": "Pascal",
        "kpa": "Kilopascal",
        "mpa": "Megapascal",
        "bar": "Bar",
        "atm": "Standard Atmosphere",
        "psi": "Pounds per Square Inch"
    },

    "velocity": {
        "m/s": "Meters per Second",
        "km/h": "Kilometers per Hour",
        "ft/s": "Feet per Second",
        "mph": "Miles per Hour",
        "kt": "Knots"
    }

}


def conversion_menu() -> None:
    """
    Display the unit conversion menu.
    """

    while True:

        print()
        print("=" * 40)
        print("UNIT CONVERSIONS".center(40))
        print("=" * 40)

        print("[1] Length")
        print("[2] Mass")
        print("[3] Force")
        print("[4] Temperature")
        print("[5] Pressure")
        print("[6] Velocity")
        print("[0] Back")
        print()

        choice = input("Select a category: ").strip()

        if choice == "1":
            conversion_screen(
                "LENGTH CONVERTER",
                "length"
            )

        elif choice == "2":
            conversion_screen(
                "MASS CONVERTER",
                "mass"
            )

        elif choice == "3":
            conversion_screen(
                "FORCE CONVERTER",
                "force"
            )

        elif choice == "4":
            conversion_screen(
                "TEMPERATURE CONVERTER",
                "temperature"
            )

        elif choice == "5":
            conversion_screen(
                "PRESSURE CONVERTER",
                "pressure"
            )

        elif choice == "6":
            conversion_screen(
                "VELOCITY CONVERTER",
                "velocity"
            )
        
        elif choice == "0":
            break

        else:
            print("\nInvalid selection.")


def conversion_screen(title: str, category: str) -> None:
    """
    Generic conversion interface.
    """

    print()
    print("=" * 40)
    print(title.center(40))
    print("=" * 40)

    print("\nAvailable Units")
    print("----------------")

    for unit, name in UNIT_DISPLAY[category].items():

        print(f"{unit:<5} - {name}")

    print()

    value = float(input("Enter value: "))

    from_unit = input("From unit: ").strip().lower()

    to_unit = input("To unit: ").strip().lower()

    if category == "temperature":

        result = convert_temperature(
            value,
            from_unit,
            to_unit
        )

    else:
        result = convert(
            value,
            category,
            from_unit,
            to_unit
        )

    print()
    print("Result:")
    print(f"{value} {from_unit} = {result:.4f} {to_unit}")

    input("\nPress Enter to continue...")



