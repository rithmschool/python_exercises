from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
  return "You are in the right place"

@app.route("/welcome")
def welcome():
  return "welcome"

@app.route("/welcome/home")
def welcome_home():
  return "welcome home"

@app.route("/welcome/back")
def welcome_back():
  return "welcome back"

@app.route("/sum")
def sum():
  return str(5+5)

if __name__ == "__main__":
  app.run(debug=True)