class Snack():

	snack_list = []
	count = 1

	def __init__(self, name, kind):
		self.name = name
		self.kind = kind
		self.id = Snack.count
		Snack.snack_list.append(self)
		Snack.count += 1

	def __repr__(self):
		return "Toy: {} Kind: {} ID: {}".format(self.name, self.kind, self.id)

	@classmethod
	def snack_by_id(cls, id):
		# return [snack for snack in cls.snack_list if snack.id == id][0]
		return next(snack for snack in cls.snack_list if snack.id ==id)