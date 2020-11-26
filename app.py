from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")



@app.route("/hello")
def hello():
    return render_template("hello.html")

@app.route("/images")
def images():
    return render_template("images.html")

@app.route("/mathew")
def mathew():
    return render_template("mathew.html")
