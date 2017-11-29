from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Magic Calculator!"


@app.route('/add/<int:num1>/<int:num2>')
def add(num1,num2):
    return "The sum is {}".format(num1 + num2)

@app.route('/name/<int:num1>/<int:num2>')
def favorite_number(num1,num2):
    return "Your sum is {}, which is made of {} and {}".format(num1 + num2, num1, num2)


app.run(debug=True)
