"""
AeroConvert Command Line Interface

Handles user menus and interaction.

Author: Braden Moody
Version: 0.1.0
"""

APP_NAME = "AeroConvert"
VERSION = "0.1.0"
AUTHOR = "Braden Moody"

def print_header() -> None:
    """
    Display the AeroConvert application header.
    """

    print("=" * 50)
    print(APP_NAME.center(50))
    print(f"Version {VERSION}".center(50))
    print("=" * 50)


def print_menu() -> None:
    """
    Display the main menu.
    """

    print()
    print("MAIN MENU".center(50))
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
    Process the user's menu selection.
    """

    if choice == "1":
        print("\nOpening Unit Conversions...")

    elif choice == "2":
        print("\nOpening Aircraft Performance...")

    elif choice == "3":
        print("\nOpening Rocket Propulsion...")

    elif choice == "4":
        print("\nOpening Orbital Mechanics...")

    elif choice == "5":
        print("\nOpening Standard Atmosphere")

    elif choice == "6":
        print("\nOpening Engineering Database")

    elif choice == "7":
        print("\nAeroConvert")
        print(f"Version : {VERSION}")
        print(f"Author: {AUTHOR}")

    elif choice == "0":
        print("\nThank you for using AeroConvert!")

    else:
        print("\nInvalid Selection.")