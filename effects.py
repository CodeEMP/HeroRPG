class Effect:
    def __init__(self, duration):
        self.duration = duration
        self.name = ''
        self.descrip = ''

    def check_duration(self):
        if self.duration > 0:
            return True
        else:
            return False


class Boon(Effect):  # {{{
    type = 'Boon'  # }}}


class Dot(Effect):  # {{{
    type = 'Dot'  # }}}


class DeBuff(Effect):  # {{{
    type = 'Debuff'  # }}}


class Poison(Dot):
    def __init__(self, duration):
        super().__init__(duration)
        self.name = "Poison"
        self.descrip = "Deals 1 damage per turn."

    def proc(self, target):
        target.hp -= 1
        print("{} takes 1 poison damage.".format(target.name))


class Empower(Boon):
    def __init__(self, duration):
        super().__init__(duration)
        self.name = "Empower"
        self.descrip = "Increases power by 2."

    def buff(self, target):
        target.powermod += 2

    def cycle(self, target):
        if self.duration < 1:
            print("Your extra strength fades")
            target.powermod -= 2
            return True
        else:
            return False
