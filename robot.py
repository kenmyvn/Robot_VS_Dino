
from weapon import Weapon

class Robot:

    def __init__(self, name, weapon):
        self.name = name
        self.health = 100
        self.weapon = Weapon
        self.attack_power = weapon.attack_power



    def attack(self, dino):
        dino.health -= self.attack_power
        print(f'{dino.name} health is now {dino.health}')


