"""
AeroConvert Conversion Menu

Handles user interaction for unit conversions.

Author: Braden Moody
Version: 0.1.0
"""

from converters.conversion_engine import convert

def length_conversion_menu() -> None:
    """
    Display the length conversion menu.
    """

    print()
    print("=" * 40)
    print("LENGTH CONVERTER".center(40))
    print("=" * 40)

    value = float(input("Enter value: "))

    from_unit = input("From unit: ").strip().lower()

    to_unit = input("To unit: ").strip().lower()

    result = convert(
        value,
        "length",
        from_unit,
        to_unit
    )

    print()
    print(f"Result:")
    print(f"{value} {from_unit} = {result:.4f} {to_unit}")


if __name__ == "__main__":

    length_conversion_menu()