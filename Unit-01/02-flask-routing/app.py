from flask import Flask

app = Flask(__name__)

@app.route('/math')
def math_functions():
    return "Math is Fun 🎠 !"

@app.route('/add/<int:num>/<int:num>')
def add(num_1, num_2):
    sum = num_1 + num_2
    return str(sum)

@app.route('/subtract/<int:num>/<int:num>')
def subtract(num_1, num_2):
    subtraction = num_1 - num_2
    return str(subtraction)

@app.route('/multiply/<int:num>/<int:num>')
def name(num_1, num_2):
    multiplication = num_1 * num_2
    return str()

@app.route('/divide/<int:num>/<int:num>')
def name(num_1, num_2):
    division = num_1 / num_2
    return str()

if __name__ == '__main__':
    app.run(port=3000, debug=True)
