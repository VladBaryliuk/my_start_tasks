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
        if new_health > 100:
            self.__health = 100
        if new_health < 0:
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
        if target.health > 3:
            print('-----------')
            print(f'{self.__class__.__name__} attack {target.__class__.__name__} with sword ')
            target._set_health(-3)
            print(f'Health of {target.__class__.__name__} lowed to {target._get_health()}')
            print('------------')
        else:
            print(self.__class__.__name__, "makes final punch and kills", target.__class__.__name__)
class Mage:
    def __init__(self, health, mana):
        self.health = health
        self.mana = mana

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, new_health):
        if self.new_health > 60:
            self.__health = 60
        if self.new_health < 0:
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
    def __init__(self, health=100, armor=100, stamina=100, arrows=20):
        super().__init__(health, stamina)
        self.armor = armor
        self.arrows = arrows

    def _get_armor(self):
        return self.armor

    def _get_barrier(self):
        return self.barrier


    def attacs(self, target):
        chance = random.randint(1, 100)
        if chance <= 40:
            print('-----------')
            print(f'{self.__class__.__name__} attack {target.__class__.__name__} with sword and makes critical hit ')
            target._set_health(-10)
            if target.__class__.__name__ == 'Wizard':
                print(f'Health of {target.__class__.__name__} lowed to {target._get_health()}')
            print(f'Health of {target.__class__.__name__} lowed to {target._get_health()}')
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
class Wizard(Mage):
    def __init__(self, __health=50, __barrier=100, __mana=100):
        super().__init__(__health, __mana)
        self.barrier = __barrier

    def _get_barrier(self):
        return self.barrier
    def _get_armor(self):
        return self.armor



    def _set_health(self, points):
        global health, stamina, armor
        armor = self._get_armor()
        if armor <= points:
            print(self.__class__.__name__, "")
        elif armor > 0:
            if points <= 0:
                armor += points
        else:
            health += points

        if self.__health > 60:
            self.__health = 60
        if self.__health < 0:
            self.__health = 0

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
        chance = random.randint(1, 100)
        if chance <= 20:
            print('-----------')
            print(f'{self.__class__.__name__} attack {target.__class__.__name__} with magic and summon fire ball ')
            target._set_health(-15)
            if target.__class__.__name__ == 'Knight':
                print(f'Armor of {target.__class__.__name__} lowed to {target._get_armor()}')
            print(f'Health of {target.__class__.__name__} lowed to {target._get_health()}')
            print('------------')
        elif chance >= 21:
            print('-----------')
            print(f'{self.__class__.__name__} attack {target.__class__.__name__} with magic ')
            target._set_health(-3)
            if target.__class__.__name__ == 'Knight':
                print(f'Armor of {target.__class__.__name__} lowed to {target._get_armor()}')
            print(f'Health of {target.__class__.__name__} lowed to {target._get_health()}')
            print('------------')
        else:
            print(self.__class__.__name__, "makes final punch and kills", target.__class__.__name__)

unit1 = Warrior(50, 50)
print(unit1.health)
unit2 = Wizard(50, 50, 50)
unit1.attacks(unit2)
unit1.heal(unit2)