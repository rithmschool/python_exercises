# Add a class for a snack here!
class Snack():

    counter = 1

    def __init__(self, name, kind):
	    self.name = name
	    self.kind = kind
	    self.id = Snack.counter
	    Snack.counter += 1

    def __repr__(self):
	    return self.namels
	    	