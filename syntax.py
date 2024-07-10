from Up import create_table , var_assign , show_tables

print("NAG - The Brogramming Language  |  Interactive Mode ")

var = {}

while True:

  a = str(input(">>> "))
  a.strip()
  b = a.split(" ")

  if b[0] == "let":
    var_assign(var , b)    

  elif b[0] == "show" and len(b) == 2:
    print(var[b[1]], type(var[b[1]]))


  elif b[0] == "list" and b[1] == "tables" and len(b) == 2:
    show_tables()

  elif b[0] == "create" and b[1] == "table" and len(b) == 3:
    create_table(b[2])

  else:
    print("Error: Invalid Syntax")
