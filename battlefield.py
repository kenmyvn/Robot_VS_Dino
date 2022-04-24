
from fleet import Fleet
from herd import Herd

class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()
        self.robot_lives_left = 0
        self.dino_lives_left = 0

    def run_game(self):
        print('Welcome to the Battlefield')
        print('Begin fighting!')
        self.battle()

    def battle(self):
        while len(self.fleet.robot) > 0 and len(self.herd.dino) > 0:
            if self.fleet.robot[0].health > 0 or self.herd.dino[0].health > 0:
                self.robo_turn()  # First turn team
            if self.herd.dino[0].health <= 0:
                print(f'{self.herd.dino[0].name} is eliminated.')
                self.herd.dino.remove(self.herd.dino[0])
            elif self.fleet.robot[0].health <= 0:
                print(f'{self.fleet.robot[0].name} is eliminated.')
                self.fleet.robot.remove(self.fleet.robot[0])

            if len(self.fleet.robot) == 0:
                self.display_winners()
                return
            elif len(self.herd.dino) == 0:
                self.display_winners()
                return

            self.dino_turn()

            if self.herd.dino[0].health <= 0:
                print(f'{self.herd.dino[0].name} is eliminated.')
                self.herd.dino.remove(self.herd.dino[0])
            elif self.fleet.robot[0].health <= 0:
                print(f'{self.fleet.robot[0].name} is eliminiated.')
                self.fleet.robot.remove(self.fleet.robot[0])

            if len(self.fleet.robot) == 0:
                self.display_winners()
                return
            elif len(self.herd.dino) == 0:
                self.display_winners()
                return

    def dino_turn(self):
        self.show_dino_opponent_options()
        self.herd.dino[0].attack(self.fleet.robot[0])

    def robo_turn(self):
        self.show_robo_opponent_options()
        self.fleet.robot[0].attack(self.herd.dino[0])

    def show_dino_opponent_options(self):
        i = 1
        for element in self.fleet.robot:
            print(f'{element.name} has {element.health} health.')
            i += 1


    def show_robo_opponent_options(self):
        i = 1
        for element in self.herd.dino:
            print(f'{element.name} has {element.health} health.')
            i += 1


    def display_winners(self):
        print("You already know who is best!")