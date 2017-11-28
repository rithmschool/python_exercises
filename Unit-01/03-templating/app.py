from flask import Flask, render_template

app = Flask(__name__)

@app.route("/person")
def person():
	return 
render_template("person.html")

@app.route("/name")
def name():
	return
render_template("name.html")

@app.route("/age")
def age():
	return
render_template("age.html")

if __name__ == '__main__':
    app.run(debug=True)

