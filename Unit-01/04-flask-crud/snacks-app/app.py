from flask import Flask, render_template, url_for, request, redirect
from snack import Snack
from flask_modus import Modus

pb = Snack('Peanut Butter','http://peanutbutterlovers.com/wp-content/uploads/2015/10/pb_hero.jpg')
print(pb)

snacks = [pb]

app = Flask(__name__)
modus = Modus(app)

@app.route('/snacks', methods=["GET", "POST"])
def index():
  if request.method == "POST":
    snacks.append(Snack(request.form['name'], request.form['image_url']))
    return redirect(url_for('index'))

  return render_template('index.html', snacks=snacks)

@app.route('/snacks/new')
def new():
  return render_template('new.html')



if __name__ == '__main__':
  app.run(port=3000, debug=True)