import items
from random import randint
import effects


class Character:
    def __init__(self, hp):
        self.maxhp = hp
        self.hp = self.maxhp
    power = 0
    armor = 0
    weapon = items.Dagger()
    evasion = 0
    effect = None
    powermod = 0
    evasionmod = 0

    def check_status(self):
        print("{} has {} HP.".format(self.name, self.hp))

    def attack(self, target):
        weapdmg = self.weapon.weapdmg()
        dmg = weapdmg + self.power
        print("{} attacks with a {},", end=" ")
        if target.Dodge() is True:
            print("the {} dodges!".format(target.name))
            return 0
        else:
            dmg = self.weapon.weapdmg()
            dmg += self.power + self.powermod
            critroll = randint(1, 20)
            if critroll == 20:
                dmg *= 2
                print("""and CRITS the {} for {} damage!
                      """.format(target.name, dmg))
                return dmg
            else:
                print("""and hits the {} for {} damage!
                      """.format(target.name, dmg))

    def dodge(self):
        try:
            dodg = self.evasion + self.evasionmod
            miss = (dodg*40)/(dodg*40)+dodg-1
        except ZeroDivisionError:
            miss = 0
        miss = round(miss)
        roll = randint(1, 100)
        if roll in range(0, miss + 1):
            return True
        else:
            return False

    def is_alive(self):
        if self.hp > 0:
            return True
        else:
            return False


class Hero(Character):
    weapon = items.Shortsword()
    starting_power = 0
    starting_evasion = 0
    inventory = [items.Potion()]
    zenny = 1

    def show_inventory(self):
        for i in self.inventory:
            if i.number > 0:
                print("{}: {}".format(i.name, i.number))
            else:
                pass

    def check_for_item(self, item):
        for i in self.inventory:
            if i.name == item.name:
                return True
            else:
                pass
            return False

    def add_item(self, item, num):
        check = self.check_for_item(item)
        if check is True:
            for i in self.inventory:
                if i.name == item.name:
                    i.number += num
                else:
                    pass
        else:
            self.inventory.append(item)
            for i in self.inventory:
                if i.name == item.name:
                    i.number += num
                else:
                    pass

    def remove_item(self, item, num):
        for i in self.inventory:
            if i.name == item.name:
                i.number -= num


class Enemy(Character):
    descrip = ''
    special = None
    hurt = ''
    unhurt = ''

    def check_status(self):
        if self.hp/self.maxhp * 100 <= 50:
            print(self.hurt)
        else:
            print(self.unhurt)

    def attack(self, target):
        spec = False
        if self.special is not None:
            spec = self.roll_for_special()
        else:
            pass
        if spec is True:
            self.special(target)
        else:
            print("{} attacks with it's {},".format(self.name,
                  self.weapon.name), end=" ")
            dmg = self.weapon.weapdmg()
            dmg += self.power
            if target.dodge() is True:
                print("and you dodge it!")
                return 0
            else:
                print("and deals {} damage!".format(dmg))
                return dmg

    def special(self, target):
        pass

    def roll_for_special(self):
        pass


class Goblin(Enemy):
    weapon = items.Dagger()
    hurt = 'The Goblins looking rough.'
    unhurt = 'The Goblin glares menacingly.'
