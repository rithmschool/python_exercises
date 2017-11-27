from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/person/<name>/<age")
def display():
    name = request.args['name'].title()
    age = request.args['age'].title()
    return render_template("base.html", name=name, age=age)
