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
    equipable = True
    useable = False


class Dagger(Weapon):
    name = 'Dagger'
    equipable = True
    useable = False
    price = 10
    descrip = """A sharp dagger. Used for stabbing presumably.
    \nDeals 1-2 damage."""
    weapdmgmin = 1
    weapdmgmax = 5


class Shortsword(Weapon):
    name = "Shortsword"
    equipable = True
    useable = False
    weapdmgmin = 2
    price = 15
    weapdmgmax = 4
    descrip = """
    A short sword. Good thing size isn't everything.\n
    Deals 2-4 damage."""


class Longsword(Weapon):
    name = "Longsword"
    equipable = True
    useable = False
    price = 35
    descrip = """
    Quite a long sword. Whoever said size isn't everything
    didn't have one of these.\n
    Deals 4-6 damage."""
    weapdmgmin = 4
    weapdmgmax = 6


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


# Consumables
class Potion(Item):
    price = 5
    name = "Potion"
    number = 3
    descrip = """A vial of red liquid. There's a tag attached to the cork.
    'No animals were harmed in the making of this potion.'
    I'm sure that's nothing to be concerned about.
    Heals for 5-8 HP."""
