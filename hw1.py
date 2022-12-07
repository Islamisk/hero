class SuperHero:
    people = "people"
    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self. health_points = health_points
        self.catchphrase = catchphrase
    def name_hero(self):
        print(self.name)
    def health_hero(self):
        self.health_points *= 2
        print(self.health_points)
    def str(self):
        print(f'Прозвище: {self.nickname}, Суперспособность: {self.superpower}, Здоровье: {self.health_points}')
    def len(self):
        print(len(self.catchphrase))
Hero = SuperHero("Volodimir", "Zelenskiy", "X2 gold", 1500, "Peremoga")
Hero.name_hero()
Hero.health_hero()
Hero.str()
Hero.len()