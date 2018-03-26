import characters
import items
import locations
import effects
from random import randint


class Battle():
    def __innit__(self, hero, foes):
        self.hero = hero
        self.foes = foes
        self.turn = 1

    def Battle_start(self):  # {{{
        print('*' * 54 + '\n')
        if len(foes) > 1:
            print("{} foes!\n".format(len(foes)))
            for i in foes:
                print(i.name)
        else:
            print("A {} attacks!".format(self.foes[0].name))
        print()  # }}}

    def Dots(self):  # {{{
        if not hero.effect:
            pass
        else:
            for i in hero.effect:
                if i.type == "Dot":
                        i.proc(hero)
                else:
                    pass
            for x in foes:
                if not x.effect:
                    pass
                else:
                    for j in x.effect:
                        if j.type == "Dot":
                            j.proc(x)
                        else:
                            pass  # }}}

    def Battle_engine(self):
        while hero.is_alive() and len(foes) > 0:
            self.Dots()
            print()
            run = self.Player_options()
            if run is True:
                break

    def Player_options(self):
        while True:
            print()
            for i in foes:
                i.check_status()
            print('\n' + '-' * 54)
            print('\n1. Attack\t\t\t2. {}'.format(hero.special))
            print('\n3. Use Item\t\t\t4. Flee')
            choice = input('> ')
            if choice == '1':
                target = self.Choose_target()
                dmg = hero.attack(foes[target])
                foes[target].hp -= dmg
            elif choice == '2':
                pass
            elif choice == '3':
                check = self.Use_item_option()
                if check is False:
                    continue
            elif choice == '4':
                run = self.Flee()
                if run is True:
                    return True
            else:
                print("\nInvalid Input\n")
                continue
            for num, i in enumerate(foes):
                if i.hp < 1:
                    print("{} dies!".format(i.name))
                    hero.zenny += i.bounty
                    del(foes[num])
                else:
                    pass
            break

    def Flee(self):
        print('\nYou attempt to run!')
        roll = randint(1, 100)
        if roll in range(1, 36):
            print('And get away!')
            return True
        else:
            print('And fail!')
            return False

    def Use_item_option(self):  # {{{
        hero.show_inventory()
        print('\nWhich Item?')
        choice = int(input())
        for num, i in enumerate(hero.inventory):
            if choice - 1 == num:
                if i.useable is True:
                    if i.type == 'on self':
                        print(i.descrip)
                        confirm = input('Use? (y/n)').lower()
                        if confirm == 'y':
                            i.Use(hero)
                        else:
                            return False
                    elif i.type == 'on target':
                        target = self.Choose_target()
                        i.Use(foes[target])
                else:
                    print("That items not useable right now.")
                    return False
            else:
                pass  # }}}

    def Choose_target(self):  # {{{
            print()
            for num, i in enumerate(foes):
                print('{}. {}'.format(num + 1, i.name))
            try:
                target = int(input("Which target? "))
                if target < len(foes) - 1 or target > len(foes):
                    print("\nInvalid target\n")
                else:
                    return target - 1
            except ValueError:
                print("\nInvalid input\n")  # }}}

town = locations.Town()
hero = characters.Hero(50)
hero.weapon = items.Sword()
foes = [characters.Goblin(10), characters.Goblin(10)]
hero.Add_effect(effects.Poison(2))
hero.add_item(items.Potion(), 3)
hero.add_item(items.Longsword(), 1)
fight = Battle()
fight.Battle_start()
fight.Battle_engine()
