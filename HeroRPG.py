import characters
import items
import locations
import effects


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
            self.Player_options()

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
                pass
            elif choice == '4':
                pass
            else:
                print("\nInvalid Input\n")
                continue
            for num, i in enumerate(foes):
                if i.hp < 1:
                    print("{} dies!".format(i.name))
                    del(foes[num])
                else:
                    pass
            break

    def Choose_target(self):  # {{{
        while True:
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
fight = Battle()
hero.Add_effect(effects.Poison(2))
fight.Battle_start()
fight.Battle_engine()
