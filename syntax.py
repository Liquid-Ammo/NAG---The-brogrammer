from Up import create_table
import csv

print("NAG - The Brogramming Language  |  Interactive Mode ")

var = {}

while True:

  a = str(input(">>> "))
  a.strip()
  b = a.split(" ")
  var_error = True

  if b[0] == "let":

    expression = ""
    for i in b[1:]:
      expression += i.strip()

    variable, value = expression.split("=")

    if variable[0] not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      for i in variable:
        var_error = True
        if i.isalpha() or i.isdigit() or i == "_":
          var_error = False
    else:
      var_error = True

    if not var_error:

      if (value[0] == '\"' and value[-1] == '\"') or (value[0] == '\'' and value[-1] == '\''):
        var[variable] = str(value[1:-1])

      elif value.isdigit():
        var[variable] = int(value)

      elif value == "True":
        value = True
        var[variable] = value

      elif value == "False":
        value = False
        var[variable] = value

      elif value.split(".")[0].isdigit() and value.split(".")[1].isdigit():
        var[variable] = float(value)
        
      else:
        print("Error: Invalid Value")

    else:
      print("Error: Invalid Variable Name")

  elif b[0] == "show" and len(b) == 2:
    print(var[b[1]], type(var[b[1]]))


  elif b[0] == "list" and b[1] == "tables" and len(b) == 2:
    pass

  elif b[0] == "create" and b[1] == "table" and len(b) == 3:
    a = create_table(b[2])
    file = open("csv_data//csvdata.csv", "a+")
    wri = csv.writer(file)    
    wri.writerow([b[2], list(a[0]), list(a[1]), list(a[2])])
    file.close()

  else:
    print("Error: Invalid Syntax")
