from flask import Flask, render_template
import jinja2

app = Flask(__name__)

app.jinja_env.undefined = jinja2.StrictUndefined
app.jinja_env.auto_reload = True

@app.route('/add/<int:a>/<int:b>')
def add(a,b):
    return str(a+b)

@app.route('/subtract/<int:a>/<int:b>')
def subtract(a,b):
    return str(a-b)

@app.route('/multiply/<int:a>/<int:b>')
def multiply(a,b):
    return str(a*b)

@app.route('/divide/<int:a>/<int:b>')
def divide(a,b):
    return str(a/b)

@app.route('/math/<type>/<int:a>/<int:b>')
def math(type,a,b):
    if type == "add":
        return str(a+b)
    if type == "subtract":
        return str(a-b)
    if type == "multiply":
        return str(a*b)
    if type == "divide":
        return str(a/b)

if __name__ == '__main__':
    app.run(debug=True)