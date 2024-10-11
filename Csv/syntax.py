import csv

from Up import create_table, var_assign, show_tables

import os

print("NAG - The Brogramming Language  |  Interactive Mode ")

var = {}

while True:

    a = str(input(">>> "))
    a = a.strip()
    b = a.split(" ")

    if b[0] == "let":
        var_assign(var, b)

    elif b[0] == "show" and len(b) == 2:

        if b[1] in var:
            print(var[b[1]], type(var[b[1]]))

        else:
            print("Variable not found")

    elif b[0] == "list" and b[1] == "tables" and len(b) == 2:
        show_tables()

    elif b[0] == "create" and b[1] == "table" and len(b) == 3:
        create_table(b[2])

    elif b[0] == "list" and b[1] == "var":

        if len(var) == 0:
            print(">", "Empty")

        else:
            for i in var:
                print(">", i, " : ", var[i], type(var[i]))

    elif b[0] == "clear" and len(b) == 1:
        os.system("clear")
        print("NAG - The Brogramming Language  |  Interactive Mode ")

    elif b[0] == "var" and b[1] == "clear" and len(b) == 2:
        var = {}

    else:
        print("Error: Invalid Syntax")
