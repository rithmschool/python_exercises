from flask import Flask, render_template

app = Flask(__name__)

# @app.route("/fruit_form")
# def fruit_form():
#     return render_template("fruit_form.html") 
@app.route('/')
# when this route is reached (through the browser bar or someone clicking a link, run the following function)
def hello():
    # this `return` is the response from our server. We are responding with the text "Hello World"
    return "Hello World!"
#what url should trigger our 
#the route() decorator is used to bind a function to a URL. 
#The function is given a name which is also used to generate URLs for that 
#particular function, and returns the message we want to display in the user’s browser.
@app.route("/person/<name>/<age>")
def display(name, age):
    name.capitalize()
    return render_template("person_info.html", name=name, age=age)

# @app.route('/user/<username>')
# def profile(username): pass	

# If it can match URLs, can Flask also generate them? Of course it can. To build a URL 
# o a specific function you can use the url_for() function. It accepts the name of the 
# unction as first argument and a number of keyword arguments, each corresponding to 
# the variable part of the URL rule.	

# @app.route('/user/<username>')
# ... def profile(username): pass
# ...
# >>> with app.test_request_context():
# ...  print url_for('index')
# ...  print url_for('login')
# ...  print url_for('login', next='/')
# ...  print url_for('profile', username='John Doe')


#We will separate code and User Interface using a technique called Templates. 
#We make the directory called /templates/ and create the template:		


if __name__ == "__main__":
	app.run(port=8080, debug=True)  

