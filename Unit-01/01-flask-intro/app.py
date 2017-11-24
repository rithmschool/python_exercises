from flask import Flask

app = Flask(__name__)

@app.route("/")
def greet():
    return "Welcome!"

@app.route("/home")
def greetHome():
    return "Welcome Home!"

@app.route("/back")
def greetBack():
    return "Welcome Back!"

@app.route("/sum/<int:x>/<int:y>")
def sum(x, y):
    return x + y


if __name__ == "__main__":
    app.run(port=5000, debug=True)
