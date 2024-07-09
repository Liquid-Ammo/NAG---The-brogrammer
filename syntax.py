print("NAG - The Brogramming Language  |  Interactive Mode ")

var = {}

while True:

  a = str(input(">>>"))
  a.strip()
  b = a.split(" ")
  var_error = True
  
  if b[0] == "let":
    if b[1][0] not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      for i in b[1]:
        var_error = True
        if i.isalpha() or i.isdigit() or i == "_":
          var_error = False
    else:
      var_error = True

    expression = ""
    
    if not var_error:
      for i in b[1:]:
        expression += i.strip()
      variable,value = expression.split("=")
      print(value,type(value))
      if (value[0] == '\"' and value[-1] == '\"') or (value[0] == '\'' and value[-1] == '\'') :
        var[variable] = str(value[1:-1])
      elif value.isdigit():
        var[variable] = int(value[1:-1])
    else:
      print("Error: Invalid Variable Name")
  elif b[0] == "show" and len(b) == 2:
    print(var[b[1]])

  else:
    print("Syntax error")
