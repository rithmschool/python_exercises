# Add a class for a snack here!

class Snack():

    count = 1

    def __init__(self, name, kind):
        self.name = name
        self.kind = kind
        self.id = Snack.count
        Snack.count += 1