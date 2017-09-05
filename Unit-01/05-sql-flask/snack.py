class Snack():
	count = 1
	def __init__(self, name, type, deliciousness):
		self.name = name
		self.type = type
		self.deliciousness = deliciousness
		self.id = Snack.count
		Snack.count += 1