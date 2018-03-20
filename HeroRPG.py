import characters
import items
import locations
import effects


class Battle():
    def __innit__(self, hero, foes):
        self.hero = hero
        self.foes = foes
        self.turn = 1

    def Battle_engine(self):
        while hero.is_alive() and len(foes) > 0:
            pass

hero = characters.Hero(12)
hero.add_item(items.Longsword(), 1)
hero.add_item(items.Chainmail(), 1)
hero.add_item(items.Leather(), 0)
hero.show_inventory()
hero.hp -= 5
print(hero.hp)
town = locations.Town()
town.rest_at_inn(hero, 2)
print(hero.hp)
foes = [characters.Goblin(10), characters.Goblin(10)]
print("Enemy attack!")
if len(foes) > 1:
    print("{} foes!".format(len(foes)))
else:
    print("A {}!".format(foes[0].name))
for i in foes:
    i.check_status()
fight = Battle()
fight.Battle_engine()
