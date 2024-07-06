print("Legit - The Brogramming Language  |  Interactive Mode ")

var = {}

while True :

    a = str ( input ( ">>>" ) )
    b = a.split(" ")

    if b[0] == "let" and b[2] == "be" and len(b) == 4 :
        var [b[1]] = b[3]

    elif b[0] == "show" and len(b) == 2 :
        print(var[b[1]])
        
    else:
        break