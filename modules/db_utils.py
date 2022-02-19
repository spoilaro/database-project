from random import randint
import sqlite3
from sqlite3 import Error
import names
import random
from bokeh.plotting import figure, show, output_file, save


def create_connection(db_path: str):

    try:
        connection = sqlite3.connect(db_path)
        print(sqlite3.version)
        return connection

    except Error as e:
        print(e)


def initialize_users(connection, user_count):
    cursor = connection.cursor()

    cursor.execute("delete from Users")
    cursor.execute("delete from sqlite_sequence where name='Users'")
    for _ in range(user_count-1):
        owner = names.get_first_name()
        cursor.execute("insert into Users (username) values (?)", (owner,))
        connection.commit()
    cursor.execute("insert into Users (username) values (?)", ("Tester",))
    connection.commit()


def initilize_use_cases(connection):
    cursor = connection.cursor()

    cursor.execute("delete from UseCases")
    cursor.execute("delete from sqlite_sequence where name='UseCases'")
    cursor.execute("""
        insert into UseCases (place) values
        ('School'),
        ('Mining'),
        ('Office'),
        ('Gaming'),
        ('Unknown')
    """)
    connection.commit()


def initilize_manufacturers(connection):
    cursor = connection.cursor()
    cursor.execute("delete from Manufacturers")
    cursor.execute("delete from sqlite_sequence where name='Manufacturers'")
    cursor.execute("""
        insert into Manufacturers (name) values
        ('Nvidia'),
        ('AMD')
    """)
    connection.commit()


def initilize_specs(connection, gpu, index):

    try:
        num = int(gpu.split(" ")[2][2:])

        if num > 70:
            grade = 3
        elif num <= 70 and num > 50:
            grade = 2
        else:
            grade = 1

        cursor = connection.cursor()

        cursor.execute(
            "insert into Specs (gpu_id, model, grade) values (?, ?, ?)", (index, gpu, grade))
        connection.commit()

    except:
        return


def initialize_user_use_cases(connection):
    # TODO Implement
    pass


def initilize_db(connection):
    RANDOM_USER_COUNT = 50
    cursor = connection.cursor()

    initialize_users(connection, RANDOM_USER_COUNT)
    initilize_use_cases(connection)
    initilize_manufacturers(connection)

    cursor.execute("delete from GraphicCards")
    cursor.execute("delete from sqlite_sequence where name='GraphicCards'")
    with open("gpu.csv", "r") as f:
        lines = f.readlines()

    gpus = [
        line.strip() for line in lines
        if line.startswith("GeForce") or line.startswith("Radeon")
    ]

    for index, gpu in enumerate(gpus):
        manufacturer = 1 if gpu.startswith("GeForce") else 2
        data = (gpu, random.randint(1, RANDOM_USER_COUNT), manufacturer)

        cursor.execute(
            "insert into GraphicCards (name, owner_id, manufacturer_id) values (?, ?, ?)", data)
        initilize_specs(connection, gpu, index)

        connection.commit()
    # Adding a couple of gpus for the test user "Tester, ID 50"
    cursor.execute("insert into GraphicCards (name, owner_id, manufacturer_id) values ('GeForce GTX 750', 50, 1)")
    cursor.execute("insert into GraphicCards (name, owner_id, manufacturer_id) values ('GeForce GTX 780', 50, 1)")
    connection.commit()


def get_user_id(connection, username):
    query = "select id from Users where username = ?"
    cursor = connection.cursor()
    cursor.execute(query, (username,))
    res = cursor.fetchone()
    return res[0]


def get_specs(connection):
    cursor = connection.cursor()

    query = "select * from Specs"
    cursor.execute(query)

    res = cursor.fetchall()

    if len(res) == 0:
        print("Specs is empty!\n")

    for r in res:
        print(r)


def get_use_cases(connection, username):
    cursor = connection.cursor()

    q = """select UseCases.place from UseCases
            inner join User_UseCases on UseCases.id=User_UseCases.use_case_id
            inner join Users on User_UseCases.user_id=Users.id where Users.username = ?
    """
    cursor.execute(q, (username,))

    res = cursor.fetchall()

    for r in res:
        print(r[0])


def add_new_use_case(connection, usecase_name):
    sql = "insert into UseCases (place) values (?)"
    cursor = connection.cursor()

    cursor.execute(sql, (usecase_name,))
    connection.commit()

    print("New use case added")
    print()

def get_graphiccards(connection, username):
    cursor = connection.cursor()

    u_id = get_user_id(connection, username)
    print(u_id)

    query = "select name from GraphicCards where owner_id = ?"
    cursor.execute(query, (u_id,))

    res = cursor.fetchall()

    for r in res:
        print(r[0])


def get_the_highest_grade(connection, username):
    cursor = connection.cursor()
    u_id = get_user_id(connection, username)

    query = """select GraphicCards.name, Specs.grade from GraphicCards
                inner join Specs on GraphicCards.id = Specs.gpu_id where GraphicCards.owner_id = ?
                order by Specs.grade limit 1
                """

    cursor.execute(query, (u_id,))

    res = cursor.fetchall()

    for r in res:
        print(r)


def update_name(connection, username, new_name):
    cursor = connection.cursor()
    u_id = get_user_id(connection, username)

    q = "update Users set username = ? where id = ?"
    cursor.execute(q, (new_name, u_id))

    connection.commit()
    print("Name updated succesfully")

def spec_graph(connection):
    cursor = connection.cursor()

    cursor.execute("select grade, model from Specs")
    res = cursor.fetchall()

    y = [row[0] for row in res]
    x = [row[1] for row in res]

    print(y)
    print(x)

    output_file(filename="Specs.html", title="Specs")

    p = figure(title="Spec Graph", x_axis_label="Card Name", y_axis_label="Card Grade", x_range=x)
    p.vbar(top=y_test, legend_label="Specs", width=0.5, bottom=0, color="red")

    save(p)





