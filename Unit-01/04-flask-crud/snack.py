class Snack():

    count = 1

    def __init__(self, snack_type, calories):
        self.snack_type = snack_type
        self.calories = calories
        self.id = Snack.count
        Snack.count += 1