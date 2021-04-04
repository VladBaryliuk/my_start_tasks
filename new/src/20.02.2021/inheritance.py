import random
class Warior:
    def __init__(self, health, stamina):
        self.__health = health
        self.__stamina = stamina

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, new_health):
        if self.__health > 60:
            self.__health = 60
        if self.__health < 0:
            self.__health = 0
        else:
            self.__health = new_health
    def introduces(self):
        print("-----------")
        print(f'Class: {self.__class__.__name__}',
              f'\nHealth: {self.health}',
              f'\nStamina: {self.stamina}')
        print('-----------')

    def healWarior(self, target):
        print('-----------')
        print(f'{self.__class__.__name__} bandage with herbs on '
              f'{target.__class__.__name__}')
        target.health += 10
        self.stamina -= 20
        print(f'Health of {target.__class__.__name__} upgraded to {target.health}',
              f'\nNow {self.__class__.__name__} have only {self.stamina} stamina')
        print('------------')
    def attacks(self, target):
        print('-----------')
        print(f'{self.__class__.__name__} attack {target.__class__.__name__} with sword ')
        target.health -= 3
        print(f'Health of {target.__class__.__name__} lowed to {target.health}')
        print('------------')


class Mage:
    def __init__(self, health, mana):
        self.health = health
        self.mana = mana

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, new_health):
        if self.__health > 60:
            self.__health = 60
        if self.__health < 0:
            self.__health = 0
        else:
            self.__health = new_health

    def introducesMage(self):
        print("-----------")
        print(f'Class: {self.__class__.__name__}',
              f'\nHealth: {self.health}',
              f'\nmana: {self.mana}')
        print('-----------')

    def heal(self, target):
        print('-----------')
        print(f'{self.__class__.__name__} casts a heal spell on '
              f'{target.__class__.__name__}')
        target.health += 10
        self.mana -= 20
        print(f'Health of {target.__class__.__name__} upgraded to {target.health}',
              f'\nNow {self.__class__.__name__} have only {self.mana} mana')
        print('------------')

    def attacksMage(self, target):
        print('-----------')
        print(f'{self.__class__.__name__} attack {target.__class__.__name__} with magic ')
        target.health -= 3
        print(f'Health of {target.__class__.__name__} lowed to {target.health}')
        print('------------')


class Archer(Warior):
    def __init__(self, __health=100, __stamina=100, arrows=20):
        super().__init__(__health, __stamina)
        self.arrows = arrows

    @stamina.setter
    def stamina(self, new_stamina):
        if self.__stamina > 100:
            self.__stamina = 100
        if self.__stamina < 0:
            self.__stamina = 0
        else:
            self.__stamina = new_stamina

    def attacs(self, target):
        chance = random.randint(1, 100)
        if chance <= 30:
            print('-----------')
            print(f'{self.__class__.__name__} attack {target.__class__.__name__} with sword and makes critical hit ')
            target.health -= 10
            if target.__class__.__name__ == 'Wizard':
                print(f'Health of {target.__class__.__name__} lowed to {target.health()}')
            print(f'Health of {target.__class__.__name__} lowed to {target.health()}')
            print('------------')
        elif chance >= 41:
            print('-----------')
            print(f'{self.__class__.__name__} attack {target.__class__.__name__} with sword ')
            target._set_health(-3)
            if target.__class__.__name__ == 'Wizard':
                print(f'Health of {target.__class__.__name__} lowed to {target._get_health()}')
            print(f'Health of {target.__class__.__name__} lowed to {target._get_health()}')
            print('------------')
        else:
            print(self.__class__.__name__, "makes final punch and kills", target.__class__.__name__)

    def sniper_shot(self, target):
        print('-----------')
        print(f'{self.__class__.__name__} make a sniper shot '
              f'{target.__class__.__name__}')
        target.health -= 15
        self.stamina -= 30
        print(f'Health of {target.__class__.__name__} lowed to {target.health}',
              f'\nNow {self.__class__.__name__} have only {self.stamina} stamina')
        print('------------')


    def introduces(self):
        super().introduces()
        print("------------")
        print(f'Arrows: {self.arrows}')
        print("------------")


class Alchemist(Mage):
    def __init__(self, health=100, stamina=100, fire_bottle=10):
        super().__init__(health, stamina)
        self.fire_bottles = fire_bottle

    def attacks(self, target):
        print('-----------')
        print(f'{self.__class__.__name__} shoot a bow on {target.__class__.__name__}')
        self.health -= 3
        target.health -= 10
        self.fire_bottles -= 1
        print(f'Health of {target.__class__.__name__} lowed to {target.health}')
        print(f'Health of {self.__class__.__name__} lowed to {self.health}')
        print('------------')
        print(f'Now {self.__class__.__name__} have {self.fire_bottles} bottles with fire')
        print('------------')

        def introduces(self):
            super().introduces()
            print("------------")
            print(f'Fire bottles: {self.fire_bottles}')
            print("------------")


unit1 = Archer()
unit2 = Archer()
unit1.sniper_shot(unit2)
unit3 = Alchemist()
unit3.attacks(unit2)
