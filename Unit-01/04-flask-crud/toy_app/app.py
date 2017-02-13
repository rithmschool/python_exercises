from toy import Toy 
from flask import Flask, render_template, request, redirect, url_for
from flask_modus import Modus

app = Flask(__name__)
modus = Modus(app)

lego = Toy('lego','https://mi-od-live-s.legocdn.com/r/www/r/catalogs/-/media/catalogs/characters/star%20wars/new%20full%20body/updated/75088_senate-commando-captain_mugshot_672x896.png?l.r2=-1758278976')
blocks = Toy('blocks', 'https://www.getfilecloud.com/blog/wp-content/uploads/2014/01/building-blocks.jpg')
tank = Toy('tank','http://nationalinterest.org/files/main_images/t-90s_0032_copy_0.jpg')
micro_machine = Toy('micro machine', 'http://m2museum.com/Cars/Chevrolet/Blazer/IMG_20141118_203556_347.jpg')

toys = [lego,blocks,tank,micro_machine]
# List toys, if POST modify DB and then list toys
@app.route('/toys', methods=["GET","POST"])
def index():
	if request.method == "POST":
		new_toy = Toy(request.form['toy'], request.form['image_url'])
		toys.append(new_toy)
		return redirect(url_for('index'))
	else:
		return render_template('index.html', toys=toys)

@app.route('/toys/new')
def new_toy():
	return render_template('new_toy.html')

@app.route('/toys/<int:id>', methods=["GET", "PATCH", "DELETE"])
def toy_id(id):
	if request.method == b'PATCH':
		toy_by_id = [toy for toy in toys if toy.id == id][0]
		toy_by_id.name = request.form['toy']
		toy_by_id.image_url = request.form['image_url']
		return redirect(url_for('index'))
	if request.method == b'DELETE':
		toy_by_id = [toy for toy in toys if toy.id == id][0]
		toy_to_delete_idx = toys.index(toy_by_id)
		toys.pop(toy_to_delete_idx)	
		return redirect(url_for('index'))
	else:
		return render_template('toy_id.html', toys = toys, id=id)

@app.route('/toys/<int:id>/edit')
def edit_toy(id):
	toy_by_id = [toy for toy in toys if toy.id == id][0]
	return render_template('edit.html', id=id, toy=toy_by_id)


if __name__ == '__main__':
	app.run(port=3000,debug=True)