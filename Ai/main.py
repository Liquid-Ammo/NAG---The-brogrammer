from flask import Flask, render_template, request
from Ai import chatbot
import pathlib
import pprint
import mimetypes

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/input", methods=["POST", "GET"])
def Generate():
    global output
    while True:
        sub = request.form["inp"]
        print(sub)
        sub = chatbot(sub)
        return render_template("index.html", out=sub)


app.run(host="0.0.0.0", port=5020)
