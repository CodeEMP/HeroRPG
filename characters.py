import items
from random import randint


class Character:
    def __init__(self, hp):
        self.maxhp = hp
        self.hp = self.maxhp
    power = 0
    armor = 0
    weapon = None

    def check_status(self):
        print("{} has {} HP.".format(self.name, self.hp))

    def attack(self, target):
        weapdmg = weapon.weapdmg()
        dmg = weapdmg + self.power
        print("{} attacks with a {},", end = " ")
        if target.Dodge() is True:
            print("the {} dodges!".format(target.name))
        else:
            dmg = self.weapon.weapdmg()
            dmg += self.power
            critroll = randint(1,20)
            if critroll == 20:
                dmg *= 2
                print("and CRITS the {} for {} damage!".format(target.name, dmg))
