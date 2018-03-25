import items
from random import randint
import effects


class Character:
    def __init__(self, hp):
        self.maxhp = hp
        self.hp = self.maxhp
        self.power = 0
        self.armor = 0
        self.weapon = items.Dagger()
        self.evasion = 0
        self.effect = []
        self.powermod = 0
        self.evasionmod = 0

    def check_status(self):
        print("{} has {} HP.".format(self.name, self.hp))

    def attack(self, target):
        weapdmg = self.weapon.weapdmg()
        dmg = weapdmg + self.power
        print("{} attacks with a {},"
              .format(self.name, self.weapon.name), end=' ')
        if target.Dodge() is True:
            print("the {} dodges!".format(target.name))
            return 0
        else:
            dmg = self.weapon.weapdmg()
            dmg += self.power + self.powermod
            critroll = randint(1, 20)
            if critroll == 20:
                dmg *= 2
                dmg -= target.armor.armorrate()
                if dmg < 1:
                    dmg = 1
                print("""and CRITS the {} for {} damage!
                      """.format(target.name, dmg))
                return dmg
            else:
                dmg -= target.armor.armorrate()
                if dmg < 1:
                    dmg = 1
                print("""and hits the {} for {} damage!
                      """.format(target.name, dmg))
                return dmg

    def Dodge(self):  # {{{
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
            return False  # }}}

    def is_alive(self):  # {{{
        if self.hp > 0:
            return True
        else:
            return False  # }}}

    def check_for_effect(self, effect):  # {{{
        for i in self.effect:
            if i.name == effect.name:
                return True
            else:
                pass
        return False

    def Add_effect(self, effec):
        self.effect.append(effec)  # }}}


class Hero(Character):
    def __init__(self, hp):
        super().__init__(hp)
        self.weapon = items.Shortsword()
        self.starting_power = 0
        self.starting_evasion = 0
        self.inventory = [items.Potion()]
        self.zenny = 1
        self.special = 'special'
        self.name = 'Hero'
        self.armor = items.Unarmored()

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
    def __init__(self, hp):
        super().__init__(hp)
        self.descrip = ''
        self.special = None
        self.hurt = ''
        self.unhurt = ''

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
                dmg -= target.armor.armorrate()
                if dmg < 1:
                    dmg = 1
                print("and deals {} damage!".format(dmg))
                return dmg

    def special(self, target):
        pass

    def roll_for_special(self):
        return False


class Goblin(Enemy):  # {{{
    def __init__(self, hp):
        super().__init__(hp)
        self.name = "Goblin"
        self.weapon = items.Dagger()
        self.hurt = 'The Goblins looking rough.'
        self.unhurt = 'The Goblin glares menacingly.'
        self.armor = items.Unarmored()  # }}}


class Viper(Enemy):
    def __init__(self, hp):
        super().__init__(hp)
        self.name = "Viper"
        self.weapon = items.Dagger()
        self.weapon.name = 'Bite'
        self.special = "Poison Bite"
        self.armor = items.Unarmored()

    def roll_for_special(self):
        return True

    def special(self, target):
        print("Viper lunges for a {},".format(self.special), end=' ')
        if target.dodge() is True:
            print("and you dodge it!")
            return 0
        else:
            dmg = self.weapon.weapdmg()
            dmg += self.power
            print("and deals {} damage!".format(dmg))
            print("You are poisoned!")
            check = target.check_for_effect(effects.Poison())
            if check is True:
                for i in target.effect:
                    if i.name == 'Poison':
                        i.duration = 3
                    else:
                        target.Add_effect(effects.Poison(3))
