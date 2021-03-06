import random

class Warrior:
    def __init__(self, health=100, stamina=100):
        self.__health = health
        self.__stamina = stamina

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, new_health):
        if new_health > 100:
            self.__health = 100
        elif new_health < 0:
            self.__health = 0
        else:
            self.__health = new_health

    def introduces(self):
        print('---------------')
        print(f'Class: {self.__class__.__name__}',
              f'\nHealth: {self.__health}',
              f'\nStamina: {self.__stamina}')
        print('---------------')

    def heals(self, target):
        print('---------------')
        print(f'{self.__class__.__name__} накладывает повязку из',
              f'целебных трав {target.__class__.__name__}')
        self.__stamina -= 20
        target.health += 10
        print(f'Здоровье у {target.__class__.__name__} повышено до {target.health}',
              f'\nУ {self.__class__.__name__} осталось {self.__stamina} единиц запаса сил')
        print('---------------')

    def attacks(self, target):
        print('---------------')
        print(f'{self.__class__.__name__} наносит урон мечом {target.__class__.__name__}')
        target.health -= 3
        print(f'Здоровье у {target.__class__.__name__}: {target.health}')

    def _set_health(self, health):
        self.__health = health


class Mage:
    def __init__(self, health=60, mana=120):
        self.health = health
        self.mana = mana

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, new_health):
        if new_health > 60:
            self.__health = 60
        elif new_health < 0:
            self.__health = 0
        else:
            self.__health = new_health

    def introduces(self):
        print('---------------')
        print(f'Class: {self.__class__.__name__}',
              f'\nHealth: {self.health}',
              f'\nMana: {self.mana}')
        print('---------------')

    def heals(self, target):
        print('---------------')
        print(f'{self.__class__.__name__} применяет заклинание лечения',
              f'к {target.__class__.__name__}')
        target.health += 10
        self.mana -= 20
        print(f'Здоровье у {target.__class__.__name__} повышено до {target.health}',
              f'\nУ {self.__class__.__name__} осталось {self.mana} единиц магии')
        print('---------------')

    def attacks(self, target):
        print('---------------')
        print(f'{self.__class__.__name__} наносит урон магией {target.__class__.__name__}')
        target.health -= 3
        print(f'Здоровье у {target.__class__.__name__} понижено до {target.health}')
        print('---------------')


class Knight(Warrior):
    def __init__(self, health=100, armor=100, stamina=100):
        super().__init__(health, stamina)
        self.__armor = armor

    def _set_health(self, points):
        # ⭐ Лечение
        if points > 0:
            super()._set_health(points)
        elif points < 0:
            # ⭐⭐ Ситуация #1
            if self.__armor > abs(points):
                self.__armor += points
                print(f'Броня у {self.__class__.__name__} понижена до {self.__armor}')
            # ⭐⭐ Ситуация #2
            elif self.__armor < abs(points) and self.__armor > 0:
                self.__armor = 0
                print(f'Броня у {self.__class__.__name__} уничтожена')
            # ⭐⭐ Ситуация #3
            else:
                super()._set_health(points)

    def attacks(self, target):
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