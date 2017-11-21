from flask import Flask

app = Flask(__name__)



@app.route("/add/<int:x>/<int:y>")
def add():
    return "<int:x>" + "<int:y>"

@app.route("/sub/<int:x>/<int:y>")
def sub(x, y):
    return x - y

@app.route("/mult/<int:x>/<int:y>")
def mult(x, y):
    return x * y


@app.route("/div/<int:x>/<int:y>")
def div(x, y):
    return x / y











if __name__ == "__main__":
    app.run(port=8080, debug=True)
