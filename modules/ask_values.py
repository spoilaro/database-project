
def ask_for_new():

    data = {}
    data["name"] = input("Name of the fun: ")
    data["fun_type"]= input("Fun type: ")
    data["author"]= input("Author: ")
    data["published"]= input("Year published: ")

    return data
