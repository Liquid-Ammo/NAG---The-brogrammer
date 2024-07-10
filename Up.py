def create_table(name):

  import csv
  column_name = []
  column_datatype = []
  column_key = []

  while True:
    a = str(input("  : "))
    a.strip()
    b = a.split(" ")

    if b[0] == ";":
      break

    elif len(b) == 2:

      if b[0] not in column_name:
        column_name.append(b[0])
      else:
        print("Error: Repeated Attribute Name")

      column_datatype.append(b[1])
      column_key.append(False)

    elif len(b) == 3:
      column_name.append(b[0])
      column_datatype.append(b[1])

      if b[2] == "primary":
        column_key.append(True)
      else:
        print("Error: Invalid Key")

    else:
      print("Error: Invalid Syntax")

    z = "csv_data//" + name + ".csv"

    aq = open(z, "w")
    bq = csv.writer(aq)
    bq.writerow(column_name)
    aq.close()

  a = [column_name, column_datatype, column_key]
  file = open("csv_data//csvdata.csv", "a+")
  wri = csv.writer(file)    
  wri.writerow([name,list(a[0]), list(a[1]), list(a[2])])
  file.close()
  file = open("csv_data//tables.csv", "a+")
  wri = csv.writer(file)
  wri.writerow([name])
  file.close()




def var_assign(var , b) :

  var_error = True
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


def show_tables():
  import csv
  a = open ( "csv_data//tables.csv" , "r" )
  wri = csv.reader(a)
  for i in wri:
    print(i[0])