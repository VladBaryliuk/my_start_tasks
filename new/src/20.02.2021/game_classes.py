class Warior:
    def __init__(self, health, stamina):
        self.health = health
        self.stamina = stamina

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
    def attacksWarior(self, target):
        print('-----------')
        print(f'{self.__class__.__name__} attack {target.__class__.__name__} with sword ')
        target.health -= 3
        print(f'Health of {target.__class__.__name__} lowed to {target.health}')
        print('------------')


unit1 = Warior(100, 100)
unit2 = Warior(85, 110)
unit1.introduces()


class Mage:
    def __init__(self, health, mana):
        self.health = health
        self.mana = mana

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


unit3 = Mage(health=60, mana=100)
unit4 = Mage(health=50, mana=110)
unit3.introducesMage()
unit3.heal(unit1)
unit1.healWarior(unit3)
unit1.attacksWarior(unit4)
unit3.attacksMage(unit2)
