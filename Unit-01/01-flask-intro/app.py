from flask import Flask, render_template
import jinja2

app = Flask(__name__)

app.jinja_env.undefined = jinja2.StrictUndefined
app.jinja_env.auto_reload = True

@app.route('/welcome')
def welcome():
    return "welcome"

@app.route('/welcome/home')
def welcome_home():
    return "welcome home"

@app.route('/welcome/back')
def welcome_back():
    return "welcome back!"

@app.route('/sum')
def sum():
    sum = 5 + 5
    return str(sum)

if __name__ == '__main__':
    app.run(debug=True)