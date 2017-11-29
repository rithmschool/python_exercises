# from the flask library import a class named Flask
from flask import Flask
import math
app = Flask(__name__)


@app.route('/math/<int:num>/<string:op>/<int:num2>')
def nums(num, op, num2):
    if op == '+':
        return f"{num + num2}"
    if op == '-':
        return f"{num - num2}"
    if op == '*':
        return f"{num * num2}" 
    if op == '%':
        return f"{math.floor(num / num2)}"
# I tried assigning the math operators to a dictionary,
# but it didn't work for some reason
# Also, I don't know how to escape a backslash, so I used '%' instead

if __name__ == "__main__":
    app.run(port=3000)