from typing import Any
from simple_term_menu import TerminalMenu


def menu() -> Any:
    options = [
        "[0] Quit",
        "[1] Initilize Database",
        "[2] Preview Specs",
        "[3] See My Use Cases",
        "[4] Add a new use case",
        "[5] See my Graphic Cards",
        "[6] See my best Card",
        "[7] Update my name",
        "[8] Spec Graph",

    ]

    terminal_main_menu = TerminalMenu(options, title="Menu")

    index = terminal_main_menu.show()

    return index
