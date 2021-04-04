import random
class Warrior:
    def __init__(self, health, stamina):
        self.__health = health
        self.__stamina = stamina

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, new_health):
        if new_health > 100: # проверяем "новое здоровье", а не "старое"
            self.__health = 100
        elif new_health < 0:
            self.__health = 0
        else:
            self.__health = new_health


    @property
    def stamina(self):
        return self.__stamina


    @stamina.setter
    def stamina(self, new_stamina):
        self.__stamina = new_stamina

    def introduces(self):
        print("-----------")
        print(f'Class: {self.__class__.__name__}',
              f'\nHealth: {self.__health}',
              f'\nStamina: {self.__stamina}')
        print('-----------')


    def heal(self, target):
        if self.__stamina >=20:
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
        if target.health >= 3:
            print('-----------')
            print(f'{self.__class__.__name__} attack {target.__class__.__name__} with sword ')
            target._set_health(-3)
            print(f'Health of {target.__class__.__name__} lowed to {target._get_health()}')
            print('------------')
        else:
            print(self.__class__.__name__, "makes final punch and kills", target.__class__.__name__)


class Mage:
    def __init__(self, health, mana): # не надо ставить __ в параметрах
        self.health = health # здесь будет просто health, mana
        self.mana = mana

    @property
    def health(self):
        return self.__health # а вот тут __health

    @health.setter
    def health(self, new_health):
        if new_health > 60: # тут тоже проверяется new_health
            self.__health = 60
        if new_health < 0:
            self.__health = 0
        else:
            self.__health = new_health


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


class Knight(Warrior):
    def __init__(self, health=100, armor=100, stamina=100, arrows=20): # тут не ставим __
        super().__init__(health, stamina) # тут есть смысл вызвать конструктор класса-родителя, чтобы не повтрять код
        self.__armor = armor
        self.__arrows = arrows

    # Если ты хочешь новые переменные создать, то
    # сперва опиши их в конструкторе!

    #def _get_armor(self):
    #    return self.armor


    #def _get_barrier(self):
    #    return self.barrier


    # Сеттер и геттер уже есть в классе родителя
    #def _get_health(self):
    #    return self.__health

    #def _set_health(self, points):
    #    if self.armor <= points:
    #         print(self.__class__.__name__)
    #    elif self.armor > 0:
    #         if points <= 0:
    #             self.armor += points
    #    else:
    #        self.__health += points

    #   if self.__health > 60:
    #        self.__health = 60
    #    if self.__health < 0:
    #        self.__health = 0

    # Этот метод тоже есть у родителя
    #def heal(self, target):
    #    if self.__stamina >= 20:
    #        print('-----------')
    #        print(f'{self.__class__.__name__}  bandage with herbs on '
    #              f'{target.__class__.__name__}')
    #        target._set_health(10)
    #        self.__stamina -= 20
    #        print(f'Health of {target.__class__.__name__} upgraded to {target._get_health()}',
    #              f'\nNow {self.__class__.__name__} have only {self.__stamina} stamina')
    #        print('------------')
    #    else:
    #        print("Not enough stamina for this action")


    # А вот тут очень хорошо!
    def attacs(self, target):
        chance = random.randint(1, 100)
        if chance <= 40:
            print('-----------')
            print(f'{self.__class__.__name__} attack {target.__class__.__name__} with sword and makes critical hit ')
            target.__health -= 10
            if target.__class__.__name__ == 'Wizard':
                print(f'Health of {target.__class__.__name__} lowed to {target._get_health()}')
            print(f'Health of {target.__class__.__name__} lowed to {target._get_health()}')
            print('------------')
        elif chance >= 41:
            print('-----------')
            print(f'{self.__class__.__name__} attack {target.__class__.__name__} with sword ')
            target.__health -= 3
            if target.__class__.__name__ == 'Wizard':
                print(f'Health of {target.__class__.__name__} lowed to {target._get_health()}')
            print(f'Health of {target.__class__.__name__} lowed to {target._get_health()}')
            print('------------')
        else:
            print(self.__class__.__name__, "makes final punch and kills", target.__class__.__name__)


class Wizard(Mage):
    def __init__(self, health=50, barrier=100, mana=100):
        # Обычно первым вызывается родительский конструктор
        super().__init__(health, mana)
        self.__barrier = barrier


    def _get_barrier(self):
        return self.__barrier

    # Уже есть у родителя
    #@property
    #def health(self):
    #    return self.__health


    # У класса Mage нет stamina. Надо переписать этот метод:
    #def heal(self, target):
    #    if self.__sta >= 20:
    ##        print('-----------')
     #       print(f'{self.__class__.__name__} casts a heal spell on '
    #              f'{target.__class__.__name__}')
    #        target._set_health(10)
    #        self.__stamina -= 20
    #        print(f'Health of {target.__class__.__name__} upgraded to {target._get_armor}',
    #              f'\nNow {self.__class__.__name__} have only {self.__stamina} stamina')
    ##        print('------------')
     #   else:
     #       print("Not enough stamina for this action")

    # Можно определить это в родительском классе
    #def attacks(self, target):
    #    chance = random.randint(1, 100)
    #    if chance <= 20:
    #        print('-----------')
    #        print(f'{self.__class__.__name__} attack {target.__class__.__name__} with magic and summon fire ball ')
    #        target._set_health(-15) # нет сеттера - будет ошибка
    #        if target.__class__.__name__ == 'Knight':
    #            print(f'Armor of {target.__class__.__name__} lowed to {target._get_armor()}')
    #        print(f'Health of {target.__class__.__name__} lowed to {target._get_health()}')
    #        print('------------')
    #    elif chance >= 21:
    #        print('-----------')
    #        print(f'{self.__class__.__name__} attack {target.__class__.__name__} with magic ')
    #        target._set_health(-3) # аналогично - нет этого сеттера
    #        if target.__class__.__name__ == 'Knight':
    #            pass
    #            #print(f'Armor of {target.__class__.__name__} lowed to {target._get_armor()}')
    #        print(f'Health of {target.__class__.__name__} lowed to {target._get_health()}')
    #        print('------------')
    #    else:
    #        print(self.__class__.__name__, "makes final punch and kills", target.__class__.__name__)


unit1 = Warrior(50, 50)
print(unit1.health)
unit2 = Wizard(50, 50, 50)
unit1.attacks(unit2)
unit1.heal(unit2)
