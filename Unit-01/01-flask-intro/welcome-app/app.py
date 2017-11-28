from flask import Flask

app = Flask(__name__)

@app.route("/welcome")
def index():
    return "<h1>Welcome</h1>"

@app.route("/welcome/home")
def home():
    return "<h1>Welcome Home</h1>"

@app.route("/welcome/back")
def back():
    return "<h1>Welcome Back</h1>"

@app.route("/sum")
def sum():
    sum = 5 + 5 
    return format(sum)

if __name__ == "__main__":
    app.run(debug=True)
