class Toy():

	count = 1

	def __init__(self, name, image_url):
		self.name = name
		self.image_url = image_url
		self.id = Toy.count + 1
		Toy.count += 1

	def __repr__(self):
		return "Toy {}, ID: {}".format(self.name, self.id)