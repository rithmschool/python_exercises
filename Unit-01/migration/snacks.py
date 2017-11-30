class Snack():

	count = 1

	def __init__(self, name, kind):
		self.name = name
		self.kind = kind
		self.id = Snack.count 
		Snack.count += 1

	def __repr__(self):
		return "{} {} {}".format(self.id, self.name, self.kind)