from flask import Flask

app = Flask (__name__)

@app.route('/welcome')
def welcome():
    return "welcome"

@app.route('/welcome/home')
def welcome_home():
    return "Welcome Home"

@app.route('/welcome/back')
def welcome_back():
    return "Welcome back"

@app.route("/sum")
def sum():
    sum = 5 + 5
    return str(sum)

if __name__ == '__main__':
    app.run(port=3000, debug=True)
