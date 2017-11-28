# Add a class for a snack here!

class Snack():

	id = 1

	def __init__(self, name, kind):
		self.name = name
		self.kind = kind
		self.id = Snack.id
		Snack.id += 1

	def __repr__(self):
		return f"Snack #{self.id}; Name: {self.name}; Kind: {self.kind}"