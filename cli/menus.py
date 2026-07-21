"""
AeroConvert Main Menu

Handles the main application navigation.

Author: Braden Moody
Version: 0.3.0
"""

from cli.conversion_menu import conversion_menu


def print_header() -> None:
    """
    Display application header.
    """

    print("=" * 50)
    print("AeroConvert".center(50))
    print("Version 0.3.0".center(50))
    print("=" * 50)


def print_menu() -> None:
    """
    Display main menu options.
    """

    print()
    print("[1] Unit Conversions")
    print("[2] Aircraft Performance")
    print("[3] Rocket Propulsion")
    print("[4] Orbital Mechanics")
    print("[5] Standard Atmosphere")
    print("[6] Engineering Database")
    print("[7] About")
    print("[0] Exit")
    print()


def handle_menu_choice(choice: str) -> None:
    """
    Handle user menu selections.
    """

    if choice == "1":

        conversion_menu()


    elif choice == "2":

        print("Aircraft Performance coming soon!")


    elif choice == "3":

        print("Rocket Propulsion coming soon!")


    elif choice == "4":

        print("Orbital Mechanics coming soon!")


    elif choice == "5":

        print("Standard Atmosphere coming soon!")


    elif choice == "6":

        print("Engineering Database coming soon!")


    elif choice == "7":

        print("AeroConvert created by Braden Moody")


    elif choice == "0":

        print("Exiting AeroConvert...")


    else:

        print("Invalid selection.")