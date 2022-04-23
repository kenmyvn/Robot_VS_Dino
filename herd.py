
from dino import Dinosaur

class Herd:

    def __init__(self):
        self.dino = []

    def create_herd(self):
        self.dino.append(dinosaur_one)
        self.dino.append(dinosaur_two)
        self.dino.append(dinosaur_three)

dinosaur_one = Dinosaur('Jamie', 2)
dinosaur_two = Dinosaur('David Lynch', 3)
dinosaur_three = Dinosaur('Jungkook', 7)