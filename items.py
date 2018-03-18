from random import randint


class Item:
    price = 0
    number = 0
    name = ''
    descrip = ''
    useable = True
    equipable = False

    def description(self):
        print(self.descrip)


# Weapons
class Weapon(Item):
    equipable = True
    useable = False
    weapdmgmin = 0
    weapdmgmax = 0

    def weapdmg(self):
        return randint(self.weapdmgmin, self.weapdmgmax)


class Sword(Weapon):
    name = "Sword"
    price = 25
    descrip = """
    A quality sword according to some black smith.
    Deals 3-5 damage."""
    weapdmgmin = 3
    weapdmgmax = 5


class Dagger(Weapon):
    name = 'Dagger'
    price = 10
    descrip = """A sharp dagger. Used for stabbing presumably.
    \nDeals 1-2 damage."""
    weapdmgmin = 1
    weapdmgmax = 5


# Armor
class Armor(Item):
    useable = False
    equipable = True
    armor = 0

    def armorrate(self):
        return self.armor


class Unarmored(Armor):
    name = 'Unarmored'
    useable = False
    equipable = True


class Leather(Armor):
    name = 'Leather'
    price = 20
    armor = 1
    descrip = '''Leather armor. Maybe a little too tight.
    \nProvides 1 armor.'''


class Chainmail(Armor):
    name = 'Chainmail'
    price = 35
    armor = 2
    descrip = '''Chainmail armor. If only it would stop pinching.
    \nProvides 2 armor.'''
