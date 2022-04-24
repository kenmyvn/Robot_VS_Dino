
from dino import Dinosaur

class Herd:

    def __init__(self):
        self.dino = []
        self.create_herd()

    def create_herd(self):
        self.dino.append(dinosaur_one)
        self.dino.append(dinosaur_two)
        self.dino.append(dinosaur_three)

dinosaur_one = Dinosaur('Jamie the Dinosaur', 2)
dinosaur_two = Dinosaur('David Lynch the Dinosaur', 3)
dinosaur_three = Dinosaur('Jungkook the Dinosaur', 7)