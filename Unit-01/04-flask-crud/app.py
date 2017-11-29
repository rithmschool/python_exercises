from flask import Flask, render_template
from snack import Snack

app = Flask(__name__)

doritos = Snack(name = "doritos", kind = "chips")
snickers = Snack(name = "snickers", kind = "candy bar")
peanuts = Snack(name = "peanuts", kind = "nuts")

snack_list = [doritos, snickers, peanuts]

@app.route("/snacks")
def index():
    return render_template('index.html', snacks=snack_list)



if __name__ == ("__main__"):
    app.run(debug=True, port=3000)

