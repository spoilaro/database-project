# Modules
from modules.header import render_header
from modules.menu import menu
from modules.db_utils import *

def main() -> None:
    connection = create_connection("./gpu_system.db")

    username = input("Username: ")

    render_header()

    run = True

    while (run):
        choice = menu()

        if choice == 0:
            quit()
        elif choice == 1:
            initilize_db(connection)
        elif choice == 2:
            get_specs(connection)
        elif choice == 3:
            get_use_cases(connection, username)
        elif choice == 4:
            add_new_use_case(connection, "Personal")
        elif choice == 5:
            get_graphiccards(connection, username)
        elif choice == 6:
            get_the_highest_grade(connection, username)
        elif choice == 7:
            new_name = input("Give a new name: ")
            update_name(connection, username, new_name)
        elif choice == 8:
            spec_graph(connection)


if __name__ == "__main__":
    main()
