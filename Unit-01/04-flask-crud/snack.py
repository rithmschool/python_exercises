# Add a class for a snack here!
class Snack():
	id = 1
	def __init__(self, name, kind):
		self._name = name
		self._kind = kind
		self.id = Snack.id
		Snack.id += 1
	def __repr__(self):
		return "Name: {self.name}; Kind: {self.kind}"	
	@property
	def name(self):
		return self._name
	@name.setter
	def name(self, value):
		self._name = value

	@property
	def kind(self):
		return self._kind
	@kind.setter
	def kind(self, value):
		self._kind = value				
