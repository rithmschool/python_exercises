from flask import Flask, render_template
import jinja2

app = Flask(__name__)

app.jinja_env.undefined = jinja2.StrictUndefined
app.jinja_env.auto_reload = True

@app.route('/add/<int:a>/<int:b>')
def add(a, b):
    return str(a + b)

@app.route('/subtract/<int:a>/<int:b>')
def subtract(a, b):
    return str(a - b)

@app.route('/multiply/<int:a>/<int:b>')
def multiply(a, b):
    return str(a * b)

@app.route('/divide/<int:a>/<int:b>')
def divide(a, b):
    return str(a / b)

@app.route('/math/<operation>/<int:a>/<int:b>')
def op(operation, a, b):
    if operation == "add":
        return add(a, b)
    if operation == "subtract":
        return subtract(a, b)
    if operation == "multiply":
        return multiply(a, b)
    if operation == "divide":
        return divide(a, b)

if __name__ == '__main__':
    app.run(port=3000)
