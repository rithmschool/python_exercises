class Snack():

	count = 1

	def __init__(self, name, taste):
		self.name = name
		self.taste = taste
		self.id = Snack.count
		Snack.count += 1

	def __repr__(self):
		return "{} {} {}".format(self.id, self.name, self.taste)