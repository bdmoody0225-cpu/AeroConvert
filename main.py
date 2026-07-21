"""
AeroConvert
-----------

A professional aerospace engineering toolkit.

Author: Braden Moody
Version: 0.1.0
"""

APP_NAME = "AeroConvert"
VERSION = "0.1.0"
AUTHOR = "Braden Moody"

from cli.menus import (print_header, print_menu, handle_menu_choice)

def main() -> None:
    """
    Start AeroConvert
    """

    print_header()

    print_menu()

    choice = input("Select an option:")

    handle_menu_choice(choice)


if __name__ == "__main__":

    main()
