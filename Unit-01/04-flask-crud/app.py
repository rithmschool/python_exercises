from flask import Flask, render_template
from snack import Snack

app = Flask(__name__)

pringles = Snack(name='pringles', kind='chips')
cake = Snack(name='cake', kind='baked goods')
cupcakes = Snack(name='cupcakes', kind='baked goods')
rice krispies = Snack(name='rice krispies', kind='baked goods')
cheetos = Snack(name='cheetos', kind='chips')

snack_list = [pringles, cake, cupcakes, rice krispies, cheetos]

@app.route('/snacks')
def index():
    return render_template('index.html', snacks=snacks)

if __name__ == '__main__':
    app.run(debug=True,port=3000)      
