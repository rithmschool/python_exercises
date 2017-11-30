class Snack():

    count = 1

    def __init__(self,name):
        self.name = name
        self.id = Snack.count
        Snack.count += 1
