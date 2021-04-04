class Warrior:
    def __init__(self, health, stamina):
        self.__health = health
        self.__stamina = stamina

    def _get_health(self):
        return self.__health
    def _set_health(self, points):
        self.__health += points
        if self.__health > 100:
            self.__health = 100
        if self.__health < 0:
            self.__health = 0

    def introduces(self):
        print("-----------")
        print(f'Class: {self.__class__.__name__}',
              f'\nHealth: {self.__health}',
              f'\nStamina: {self.__stamina}')
        print('-----------')

    def heal(self, target):
        if self.__health >=20:
            print('-----------')
            print(f'{self.__class__.__name__} bandage with herbs on '
                  f'{target.__class__.__name__}')
            target._set_health(10)
            self.__stamina -= 20
            print(f'Health of {target.__class__.__name__} upgraded to {target._get_health()}',
                  f'\nNow {self.__class__.__name__} have only {self.__stamina} stamina')
            print('------------')
        else:
            print("Not enough stamina for ths action")
    def attacks(self, target):
        if target._get_health() >= 3:
            print('-----------')
            print(f'{self.__class__.__name__} attack {target.__class__.__name__} with sword ')
            target._set_health(-3)
            print(f'Health of {target.__class__.__name__} lowed to {target._get_health()}')
            print('------------')
        else:
            print(self.__class__.__name__, "makes final punch and kills", target.__class__.__name__)
class Mage:
    def __init__(self, health, mana):
        self.__health = health
        self.__mana = mana
    def _get_health(self):
        return self.__health
    def _set_health(self, points):
        self.__health += points
        if self.__health > 60:
            self.__health = 60
        if self.__health < 0:
            self.__health = 0

    def introducesMage(self):
        print("-----------")
        print(f'Class: {self.__class__.__name__}',
              f'\nHealth: {self.__health}',
              f'\nmana: {self.__mana}')
        print('-----------')

    def heal(self, target):
        if self.__mana >= 20:
            print('-----------')
            print(f'{self.__class__.__name__} casts a heal spell on '
                  f'{target.__class__.__name__}')
            target._set_health(10)
            self.__mana -= 20
            print(f'Health of {target.__class__.__name__} upgraded to {target._get_health()}',
                  f'\nNow {self.__class__.__name__} have only {self.__mana} mana')
            print('------------')
        else:
            print("Not enough mana for this action")

    def attacks(self, target):
        if target._get_health() >= 3:
            print('-----------')
            print(f'{self.__class__.__name__} attack {target.__class__.__name__} with magic ')
            target._set_health(-3)
            print(f'Health of {target.__class__.__name__} lowed to {target._get_health()}')
            print('------------')
        else:
            print(self.__class__.__name__, "makes final punch and kills", target.__class__.__name__)
unit1 = Warrior(10, 50)
unit2 = Mage(10, 50)

