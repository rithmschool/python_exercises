# Add a class for a snack here!
class Snack():
    id = 1
    def __init__(self, name, kind):
        self.name = name
        self.id = Snack.id
        self.kind = kind
        Snack.id += 1
