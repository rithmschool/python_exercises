class Snack():

    count = 1
    snack_list = []

    def __init__ (self, name, image_url):
        self.name = name
        self.image_url = image_url
        self.id = Snack.count
        Snack.count +=1
        Snack.snack_list.append(self)


    @classmethod
    def find(cls, snack_id):
        return next(snack for snack in cls.snack_list if snack.id == snack_id)




