from flask import Flask , render_template, request
from Ai import chatbot
import pathlib
import pprint
import mimetypes

app = Flask (__name__)

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

app.run(host="0.0.0.0",port=5020)







'''


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/input", methods=["POST", "GET"])
def Generate():
    while True:
        subject = request.form["firstField"]
        chapter = request.form["secondField"]
        question_type = request.form["thirdField"]
        output = chatbot(subject, chapter, question_type)
        global outpu
        out = output[2]
        outpu = output[1]
        return render_template("index.html", out=out)


@app.route("/download", methods=["POST", "GET"])
def download_name():
    return send_file(outpu, as_attachment=True)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000)
    '''