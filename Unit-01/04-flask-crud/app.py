from flask import Flask, render_template, request, redirect, url_for
from flask_modus import Modus

app = Flask(__name__)
modus = Modus(app)

@app.route("/")
def root():
	return redirect(url_for('index'))

#To read items (GET /items)
#To create item (POST /items)
@app.route("/items", methods=["GET", "POST"])
def index():
	if(request.method == "POST")
		pass
		return redirect("url_for('index')")
	return render_template("index.html")

#To read form to create item(GET /items/new)
@app.route("/items/new")
def new():
	return render_template("new.html")

#To read item (GET /items/<int:id>)
#To edit item (PUT /items/<int:id>)
#To delete item (DELETE /items/<int:id>)
@app.route("/items/<int:id>", methods=["GET", "PUT", "DELETE"])
def show(id):
	if(request.method == "PUT")
		pass
		return redirect("url_for('show')")
	if(request.method == b"DELETE")
		pass
		return redirect("url_for('show')")
	return render_template("show.html")

#To read form to edit/delete item (GET /items/<int:id>/edit)
@app.route("/items/<int:id>/edit")
def edit_item():
	return render_template("edit.html")


if __name__ == "__main__":
	app.run(debug=True)