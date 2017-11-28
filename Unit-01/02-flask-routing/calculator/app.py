from flask import Flask

app = Flask(__name__)


@app.route('/math/<oper>/<int:num1>/<int:num2>')
def math(oper,num1,num2):
    if format(oper) == "add":
        return format(num1 + num2)
    if format(oper) == "subtract":
        return format(num1 - num2)
    if format(oper) == "multiply":
        return format(num1 * num2)
    if format(oper) == "divide":
        return format(num1 / num2)
    

if __name__ == ('__main__'):
    app.run(debug=True)
