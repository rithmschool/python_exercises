from flask import Flask, render_template, request
from random import random
app = Flask(__name__)

#see a list of all fruits
#form to add a fruits
    # -when you submit the form, add the new fruit to
    # the list
    # send you to the original form
fruits = ["apple", "banana", "oranges", "pears"]

@app.route("/greet")
def greet():
    first_name = request.args['first_name'].title()
    last_name = request.args['last_name'].title()
    return render_template(
        "greet.html",
        first_name=first_name,
        last_name=last_name
    )

# @app.route("/greet")
# def greet():
#     from IPython import embed; embed()
#     return render_template("greet.html")

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
def coin_flip():
    return render_template("random.html", num=random())

@app.route("/fruit_list")
def fruit_list():
    fruit_name_form = request.args['fruit_name']
    fruits.append(fruit_name_form)
    return render_template("fruit_list.html", fruits=fruits)

@app.route("/fruit_form")
def fruit_form():
    return render_template("fruit_form.html")

# @app.route("/greet")
# def greet():
#     first_name = request.args['first_name'].title()
#     last_name = request.args['last_name'].title()
#     return render_template(
#         "greet.html",
#         first_name=first_name,
#         last_name=last_name
#     )




if __name__ == "__main__":
    app.run(port=5000, debug=True)
