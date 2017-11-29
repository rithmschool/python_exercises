from flask import Flask, render_template
from snack import Snack


app = Flask(__name__)

snickers = Snack(name = "snickers", kind = "candy bar")
cheetos = Snack(name = 'cheetos', kind = 'chips')
skittles = Snack(name = 'skittles', kind = 'candy')
peanuts = Snack(name = 'peanuts', kind = 'nuts')

snack_list = [snickers, cheetos, skittles, peanuts]

@app.route('/snacks')
def index():
    return render_template('index.html', snacks=snack_list)

@app.route('/snacks/new')
def new():
    return render_template('new.html')

if __name__ == ("__main__"):
    app.run(debug=True, port=5000)
