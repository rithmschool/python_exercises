from project import db

class History(db.Model):
    __tablename__ = 'histories'

    id = db.Column(db.Integer, primary_key=True)
    city_lived_in = db.Column(db.Text)
    owner_id = db.Column(db.Integer, db.ForeignKey("owners.id"))

    def __init__(self, city_lived_in, owner_id):
        self.city_lived_in = city_lived_in
        self.owner_id = owner_id