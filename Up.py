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

  return column_name, column_datatype, column_key
