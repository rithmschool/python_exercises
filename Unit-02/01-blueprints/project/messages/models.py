from project import db

class Message(db.Model):

    __tablename__ = "messages"

    #create the essential columns for our table
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.Text)
    user_id = db.Column(db.Integer)

    def __init__(self, message, user_id):
        self.message = message
        self.user_id = user_id

    def __repr__(self):
        return "Message by user {}: {}".format(self.user_id, self.message)