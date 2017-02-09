from flask import Flask, render_template, request, redirect, url_for
from flask_modus import Modus
from snack import Snack





app = Flask(__name__)
modus = Modus(app)

@app.route('/')
def hello():
    return "HELLO WORRRRRRRRLD"

@app.route('/snacks', methods=["GET","POST"])
def index():
    if request.method == "POST":
        Snack(request.form['name'], request.form['image_url'])
        return redirect(url_for('index'))
    return render_template('index.html', snacks=Snack.snack_list)


@app.route('/snacks/new')
def new():
    return render_template('new.html', snacks=Snack.snack_list)

@app.route('/snacks/<int:id>',methods=["GET","PATCH"])
def show(id):
    if request.method == b"PATCH":
        Snack.find(id).name = request.form['name']
        return redirect(url_for('index'))
    return render_template('show.html', snack=Snack.find(id))

@app.route('/snacks/<int:id>/edit')
def edit(id):

    return render_template('edit.html', snack=Snack.find(id))


#Snack('snack','sndsaf')
#print(Snack.find(1).name)












if __name__ == '__main__':
   app.run(port=3000, debug = True)
   #—never use debug true in production. Use only in development
