from flask import Flask, render_template, redirect, url_for, request
from flask_modus import Modus
from snack import Snack
import jinja2

app = Flask(__name__)
modus = Modus(app)

app.jinja_env.undefined = jinja2.StrictUndefined
app.jinja_env.auto_reload = True


# mm = Snack(name='chocolate chip cookies', kind='cookies')
# doritos = Snack(name='doritos', kind='chips')
# apple = Snack(name='apple', kind='fruit')

# snack_list = [mm, doritos, apple]
snack_list = []

@app.route('/snacks', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        snack_list.append(Snack(request.form['name'], request.form['kind']))
        return redirect(url_for('index'))
    return render_template('index.html', snacks=snack_list) # GET method -> return index.html

@app.route('/snacks/new')
def new():
    return render_template('new.html')

@app.route('/snacks/<int:id>', methods=["GET", "PATCH", "DELETE"])
def show(id):
    # for snack in snack_list:
    #     if snack.id == id:
    #         found_snack = snack
    found_snack = next(snack for snack in snack_list if snack.id == id) # refactored

    if request.method == "PATCH": # NOT bytes literal here
        found_snack.name = request.form['name']
        found_snack.kind = request.form['kind']
        return redirect(url_for('index'))
    
    if request.method == "DELETE": # NOT bytes literal here
        snack_list.remove(found_snack)
        return redirect(url_for('index'))

    return render_template('show.html', snack=found_snack)

@app.route('/snacks/<int:id>/edit')
def edit(id):
    # found_snack = [snack for snack in snack_list if snack.id == id][0]
    found_snack = next(snack for snack in snack_list if snack.id == id) # refactored
    return render_template('edit.html', snack=found_snack)

if __name__ == '__main__':
    app.run(port=3000)