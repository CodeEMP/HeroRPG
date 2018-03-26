from random import randint


class Item:
    def __init__(self):
        self.price = 0
        self.number = 1
        self.descrip = ''

    def description(self):
        print(self.descrip)


# Weapons
class Weapon(Item):  # {{{
    def __init__(self):
        super().__init__()
        self.equipable = True
        self.useable = False
        self.weapdmgmin = 0
        self.weapdmgmax = 0

    def weapdmg(self):
        return randint(self.weapdmgmin, self.weapdmgmax)  # }}}


class Sword(Weapon):  # {{{
    def __init__(self):
        super().__init__()
        self.name = "Sword"
        self.price = 25
        self.descrip = """
        A quality sword according to some black smith.
        Deals 3-5 damage."""
        self.weapdmgmin = 3
        self.weapdmgmax = 5
        self.equipable = True
        self.useable = False  # }}}


class Dagger(Weapon):  # {{{
    def __init__(self):
        super().__init__()
        self.name = 'Dagger'
        self.equipable = True
        self.useable = False
        self.price = 10
        self.descrip = """\tA sharp dagger. Used for stabbing presumably.
        \nDeals 1-2 damage."""
        self.weapdmgmin = 1
        self.weapdmgmax = 5  # }}}


class Shortsword(Weapon):  # {{{
    def __init__(self):
        super().__init__()
        self.name = "Shortsword"
        self.equipable = True
        self.useable = False
        self.weapdmgmin = 2
        self.price = 15
        self.weapdmgmax = 4
        self.descrip = """
        A short sword. Good thing size isn't everything.\n
        Deals 2-4 damage."""  # }}}


class Longsword(Weapon):  # {{{
    def __init__(self):
        super().__init__()
        self.name = "Longsword"
        self.equipable = True
        self.useable = False
        self.price = 35
        self.descrip = """
        Quite a long sword. Whoever said size isn't everything
        didn't have one of these.\n
        Deals 4-6 damage."""
        self.weapdmgmin = 4
        self.weapdmgmax = 6  # }}}


# Armor
class Armor(Item):  # {{{
    def __init__(self):
        super().__init__()
        self.useable = False
        self.equipable = True
        self.armor = 0

    def armorrate(self):
        return self.armor  # }}}


class Unarmored(Armor):  # {{{
    def __init__(self):
        super().__init__()
        self.name = 'Unarmored'
        self.useable = False
        self.equipable = True  # }}}


class Leather(Armor):  # {{{
    def __init__(self):
        super().__init__()
        self.name = 'Leather'
        self.price = 20
        self.armor = 1
        self.descrip = '''\tLeather armor. Maybe a little too tight.
        \nProvides 1 armor.'''  # }}}


class Chainmail(Armor):  # {{{
    def __init__(self):
        super().__init__()
        self.name = 'Chainmail'
        self.price = 35
        self.armor = 2
        self.descrip = '''\tChainmail armor. If only it would stop pinching.
        \nProvides 2 armor.'''  # }}}


# Consumables
class Potion(Item):  # {{{
    def __init__(self):
        super().__init__()
        self.useable = True
        self.price = 5
        self.name = "Potion"
        self.number = 3
        self.type = 'on self'
        self.descrip = """\tA vial of red liquid. There's a tag attached to the cork.
        "No hooved animals were harmed in the making of this potion."
        I'm sure that's nothing to be concerned about.
        Heals for 10-13 HP."""

    def Use(self, target):
        print('\nYou Chug the Potion.')
        heal = randint(10, 13)
        print('It heals you for {}.'.format(heal))
        target.hp += heal
        if target.hp > target.maxhp:
            target.hp = target.maxhp  # }}}
