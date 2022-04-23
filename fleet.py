
from robot import Robot
from weapon import Weapon

class Fleet:

    def __init__(self):
        self.robot = []

    def create_fleet(self):
        self.robot.append(robot_one)
        self.robot.append(robot_two)
        self.robot.append(robot_three)

stick = Weapon('Stick', 1)
meta_knight_sword = Weapon('Meta Knight Sword', 10)
water_gun = Weapon('Water Gun', 5)

robot_one = Robot('Bang PD', water_gun)
robot_two = Robot('JYP', stick)
robot_three = Robot('YG', meta_knight_sword)

