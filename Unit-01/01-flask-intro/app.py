from flask import Flask
app = Flask(__name__)

@app.route("/")
def root():
    return "hi everyone!"

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
    total = 5+5
    return str(total)

@app.route("/numbers/<num1>/<int:num2>") # if <arg> is used def must have arg
def show_numbers(num1, num2):
  return 'type num1 {}, type num2 {}'.format(num1 + num1 , num2)



if __name__ == '__main__':
  app.run(port=5000, debug=True)