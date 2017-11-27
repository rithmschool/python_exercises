from flask import Flask, render_template

app = Flask(__name__)



@app.route("/person/<name>/<age>")
def display(name, age):
    name.capitalize()
    return render_template("person_info.html", name=name, age=age)



if __name__ == "__main__":
	app.run(port=8080, debug=True)  

