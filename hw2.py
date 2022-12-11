class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.health_points = health_points
        self.nickname = nickname
        self.superpower = superpower
        self.catchphrase = catchphrase

    def name_hero(self):
        print(f'{self.name}')

    def health_hero(self):
        self.health_points *= 2

    def __str__(self):
        return f'Прозвище:{self.nickname}' \
               f'Суперспособность: {self.superpower}' \
               f'Здоровье: {self.health_points}'

    def __len__(self):
        return len(self.catchphrase)

hero = SuperHero("Volodimir\n", "Zelenskiy\n", "X2 gold\n", 150, "Peremoga")
hero.name_hero()
hero.health_hero()
print(hero)
print(f'Catchphrase: {len(hero.catchphrase)}')

class Hero2(SuperHero):
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage = False, fly = False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly

    def h(self):
        zdorovie = self.health_points ** 2
        self.health_points = zdorovie

    def f(self):
        self.fly = True

    def phrase(self):
        print('fly in the True_phrase')

X = Hero2('WWW\n', 'W\n', 'QWE\n', 1000, 'sssssss')
X.h()
print(X)
print(f'Damage: {X.damage}')
X.f()
print(f'Fly: {X.fly}')
X.phrase()

class Hero3(SuperHero):
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage=False, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly

    def h(self):
        honk = self.health_points ** 2
        self.health_points = honk

    def f(self):
        self.fly = True

    def phrase(self):
        print('fly in the True_phrase')

honk = Hero3('123\n', '456\n', '789\n', 2000, 'qwerty')
honk.h()
print()
print(f'Damage: {honk.damage}')
honk.f()
print(f'Fly: {honk.fly}')
honk.phrase()

class Villain(Hero2):
    people = 'monster'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage=False, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)

    def gen_x(self):...

    def crit(self):
        print(f'Crit dm: {self ** 2}')

YYY = Villain('ooo\n', 'rrr\n', 'uuu\n', 700, 'ppp')
print(YYY)
YYY.gen_x()
Villain.crit(X.damage)