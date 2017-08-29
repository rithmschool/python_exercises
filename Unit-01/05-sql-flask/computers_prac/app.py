from flask import Flask, render_template
from flask_modus import Modus  
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# tell SQLAlch where the database is
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/computers-db'
# make it faster
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
# assign the DB an object
db = SQLAlchemy(app)
# interpret headers
modus = Modus(app)
# inherit the magic to connect and play in the DB 


class Computer(db.Model):
    __tablename__ = "computers"
    # tell POSTGRES what the columns are
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)
    memory = db.Column(db.Integer)
    # tell POSTGRES what the rows are for each item

    def __init__(self, name, memory):
        self.name = name
        self.memory = memory

    def __repr__(self):
        return "{}, {}".format(self.name, self.memory)


@app.route('/computers', methods = ['GET'])
def index():
    computers = Computer.query.all()
    return render_template('index.html', computers=computers)


from IPython import embed; embed()
if __name__ == '__main__':
    app.run(port=3000,debug=True)

