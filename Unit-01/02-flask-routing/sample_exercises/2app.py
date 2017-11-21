from flask import Flask, render_template
from random import random
app = Flask(__name__)



@app.route("/")
def say_hi():
    return render_template("index.html")


@app.route("/bye")
def say_bye():
    return render_template("bye.html")

@app.route("/sweet")
def sweet():
    return render_template("sweet.html")


@app.route("/feeling_lucky")
def coin_fip():
    return render_template("random.html", num=random())

@app.rout("/fruits")
def fruits():
    fruits = ["apples", "bananas", "cherries", "durians"]
    return render_template("fruits.html", fruits=fruits)






if __name__ == "__main__":
    app.run(debug=True)
