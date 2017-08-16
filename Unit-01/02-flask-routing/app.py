from flask import Flask
app  = Flask(__name__)

@app.route('/add/<int:num>/<int:num2>')
def my_add(num, num2):
    return str(num + num2)

@app.route('/subtract/<int:num>/<int:num2>')
def my_sub(num, num2):
    return str(num - num2)

@app.route('/multi/<int:num>/<int:num2>')
def my_multi(num,num2):
    return str(num * num2)

@app.route('/divi/<int:num>/<int:num2>')
def my_divi(num, num2):
    return str(num / num2)

@app.route('/math/<int:num>/<int:num2>')
def my_math(num, num2):
    pass
if __name__ == '__main__':
    app.run(port=3000, debug=True)
