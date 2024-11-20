from flask import Flask, render_template, request
from Ai import chatbot, startai

if True:
    import mysql.connector as sqltor

    connector12 = sqltor.connect(host="localhost", user="root", passwd="")
    jelly = connector12.cursor()
    if connector12.is_connected():
        print()
        print()
        print()
        print()
        print("Connection Secure")
        print()
        print()
        print()
        print()
    else:
        print("Connection Error")

app = Flask(__name__)
user_select = None

startai()


@app.route("/")
def index():
    return render_template("login.html")


@app.route("/", methods=["POST", "GET"])
def login():
    user = request.form["username"]
    passwd = request.form["password"]
    a = open("User.txt", "r")
    b = a.read()
    b = b.split("\n")
    a.close()

    for i in b:
        i = str(i)
        if eval(i)["User"] == user:
            if eval(i)["Passwd"] == passwd:
                global user_select
                user_select = eval(i)
                print("Login Successful")
                return render_template("index.html")
            else:
                return render_template("login.html", msg="Invalid Password.")


@app.route("/reg")
def ind():
    return render_template("register.html")


@app.route("/register", methods=["POST", "GET"])
def register():
    user = request.form["username"]
    passwd = request.form["password"]
    a = open("User.txt", "r")
    b = a.read()
    b = b.split("\n")
    a.close()
    c = True
    for i in b:
        i = eval(str(i))
        if i["User"] != user and c:
            pass
        else:
            c = False
    if not c:
        return render_template(
            "register.html", msg="Username in use use a different one or login."
        )
    elif c:
        a1 = open("User.txt", "a")
        b1 = {"User": user, "Passwd": passwd, "Databases": []}
        a1.write("\n" + str(b1))
        global user_select
        user_select = dict(b1)
        a1.close()
        print("User Added Successfully.")
        print("Login Successful")
        return render_template("index.html")


his = ""


@app.route("/input", methods=["POST", "GET"])
def Generate():
    global user_select
    if user_select == None:
        return "Error Not Loged In"

    print(user_select)
    global his

    if True:

        user_name = user_select["User"]
        a = open("User.txt", "r")
        b = (a.read()).split("\n")
        for i in b:
            x = eval(i)
            if x["User"] == user_name:
                user_select = x
        a.close()

        sub = request.form["inp"]
        sub1 = chatbot(sub)
        sub2 = sub1.split(" ")
        out = ""
        if sub2[0].lower() == "use":
            if sub2[1].lower() not in user_select["Databases"]:
                out = "Access Restricted to Database."
            elif sub2[1].lower() in user_select["Databases"]:
                jelly.execute(sub1)
                # out = "sql return left to insert use"

        elif sub2[0].lower() == "create":
            if sub2[2].lower() not in user_select["Databases"]:
                jelly.execute(sub1)
                print("ADiinng DAtabase")
                a = open("User.txt", "r")
                b = a.read()
                b = b.split("\n")
                a.close()
                c = ""
                for i in b:
                    i = eval(str(i))
                    if i["User"] == user_select["User"]:
                        i["Databases"] += [sub2[2]]
                        c = c + str(i)
                    else:
                        c = c + str(i) + "\n"

                a = open("User.txt", "w")
                a.write(c)
                a.close()
                # out = "sql return left to insert create"

        elif sub2[0].lower() == "drop":
            if sub2[1].lower() not in user_select["Databases"]:
                out = "Access Restricted to Database."
            elif sub2[1].lower() in user_select["Databases"]:
                jelly.execute(sub1)
                # out = "sql return left to insert drop"

        else:
            jelly.execute(sub1)
            try:
                x = jelly.fetchall()
                out = ""
                for i in x:
                    out += str(i)
            except:
                pass

                # out = "sql return left to insert else"
        print(type(his), type(sub), type(sub1), type(out))
        his = his + str(
            '<p class="prompt">'
            + ">>> "
            + sub
            + "<p>"
            + '<p class="statement">'
            + sub1
            + "<p>"
            + '<p class="statement">'
            + str(out)
            + "<p>"
        )
        print(his)
        return render_template("index.html", his=his)


app.run(host="0.0.0.0", port=5020)