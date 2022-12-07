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
        print(int(self.health_points)*2)
    def __str__(self):
        return f'Прозвище: {self.nickname}, Суперспособность: {superpower}, Здоровье: {self.health_points}'
    def __len__(self, catchphrase):
        print(f'{self.catchphrase}')
Hero = SuperHero("Hero", "HeroX", "ult", 1500, "ya tvoyu maka ebal")
print(Hero)
