# Add a class for a snack here!
class Snack:

	snack_id = 1

	def __init__(self, name, kind):
		self.name = name
		self.kind = kind
		self.id = Snack.snack_id
		Snack.snack_id +=1