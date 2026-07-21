"""
AeroConvert Conversion Menu

Handles user interaction for unit conversions.

Author: Braden Moody
Version: 0.3.0
"""

from converters.conversion_engine import convert


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
        print("[0] Back")
        print()

        choice = input("Select a category: ").strip()

        if choice == "1":
            length_conversion_menu()

        elif choice == "2":
            mass_conversion_menu()

        elif choice == "3":
            force_conversion_menu()

        elif choice == "0":
            break

        else:
            print("\nInvalid selection.")


def length_conversion_menu() -> None:
    """
    Display the length conversion menu.
    """

    print()
    print("=" * 40)
    print("LENGTH CONVERTER".center(40))
    print("=" * 40)

    print("\nAvailable Units")
    print("----------------")
    print("m    - Meter")
    print("km   - Kilometer")
    print("cm   - Centimeter")
    print("mm   - Millimeter")
    print("ft   - Foot")
    print("in   - Inch")
    print("yd   - Yard")
    print("mi   - Mile")
    print("nmi  - Nautical Mile")

    print()

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

    input("\nPress Enter to continue...")


def mass_conversion_menu() -> None:
    """
    Display the mass conversion menu.
    """

    print()
    print("=" * 40)
    print("MASS CONVERTER".center(40))
    print("=" * 40)

    print("\nAvailable Units")
    print("----------------")
    print("kg   - Kilogram")
    print("g    - Gram")
    print("mg   - Milligram")
    print("lb   - Pound")
    print("oz   - Ounce")
    print("slug - Slug")
    print("t    - Metric Ton")

    print()

    value = float(input("Enter value: "))
    from_unit = input("From unit: ").strip().lower()
    to_unit = input("To unit: ").strip().lower()

    result = convert(
        value,
        "mass",
        from_unit,
        to_unit
    )

    print()
    print(f"Result:")
    print(f"{value} {from_unit} = {result:.4f} {to_unit}")

    input("\nPress Enter to continue...")


def force_conversion_menu() -> None:
    """
    Display the force conversion menu.
    """

    print()
    print("=" * 40)
    print("FORCE CONVERTER".center(40))
    print("=" * 40)

    print("\nAvailable Units")
    print("----------------")
    print("n    - Newton")
    print("kn   - Kilonewton")
    print("mn   - Meganewton")
    print("lbf  - Pound Force")
    print("dyn  - Dyne")

    print()

    value = float(input("Enter value: "))
    from_unit = input("From unit: ").strip().lower()
    to_unit = input("To unit: ").strip().lower()

    result = convert(
        value,
        "force",
        from_unit,
        to_unit
    )

    print()
    print(f"Result:")
    print(f"{value} {from_unit} = {result:.4f} {to_unit}")

    input("\nPress Enter to continue...")