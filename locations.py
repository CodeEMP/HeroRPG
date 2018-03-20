class Location:
    places = []
    descrip = ""

    def list_places(self):
        for num, i in enumerate(self.places):
            print("{}. {}".format(num, i))


class Town(Location):
    def rest_at_inn(self, hero, price):
        hero.hp = hero.maxhp
        hero.zenny -= price
