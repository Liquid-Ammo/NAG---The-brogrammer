from flask import Flask, render_template, request
from Ai import chatbot
from execute import execute

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


his = ""


@app.route("/input", methods=["POST", "GET"])
def Generate():
    global his
    while True:
        sub = request.form["inp"]
        cu = his
        sub1 = chatbot(sub)
        out = execute(sub1)
        his = (
            cu
            + '<p class="prompt">'
            + ">>> "
            + sub
            + "<p>"
            + '<p class="statement">'
            + sub1
            + "<p>"
            + '<p class="statement">'
            + out
            + "<p>"
        )
        print(his)
        return render_template("index.html", his=his)


app.run(host="0.0.0.0", port=5020)
