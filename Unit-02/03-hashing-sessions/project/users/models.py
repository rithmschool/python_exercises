from project import db, bcrypt

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, unique=True )
    password = db.Column(db.Text)

    def __init__(self, username, password):
        self.username = username
        #UTF-8 used by Python, otherwise it would be a bytes literal
        self.password = bcrypt.generate_password_hash(password).decode('UTF-8') 

    # this is a class method so decorate it to get access to cls <class> as a first parameter
    @classmethod
    def authenticate(cls, username, password):
        found_user = cls.query.filter_by(username = username).first()
        if found_user:
            authenticated_user = bcrypt.check_password_hash(found_user.password, password)
            if authenticated_user:
                return found_user   # return the user so they can be logged in
        return False