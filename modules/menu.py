from typing import Any
from simple_term_menu import TerminalMenu


def menu() -> Any:
    options = [
        "[0] Quit",
        "[1] Add example data",
        "[2] Preview Specs",
        "[3] See My Use Cases",
        "[4] Add a new use case",
        "[5] See my Graphics Cards",
        "[6] See my best Card",
        "[7] Update my name",
        "[8] Save Specs as graph",

    ]

    terminal_main_menu = TerminalMenu(options, title="Menu")

    index = terminal_main_menu.show()

    return index
