class Snack():
    count = 1

    def __init__(self, name, image_url):
        self.name = name
        self.image_url = image_url
        self.id = Snack.count
        Snack.count += 1

    def __repr__(self):
        return "Snack #{}: {}".format(self.id, self.name)
