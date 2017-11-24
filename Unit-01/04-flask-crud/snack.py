# Add a class for a snack here!

class Snacks():

	count = 1

	def __init__(self, name, kind):
		self.name = name
		self.kind = kind
		self.id = Snacks.count 
		Snacks.count += 1

