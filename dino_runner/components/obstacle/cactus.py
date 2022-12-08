from dino_runner.components.obstacle.obstacle import Obstacle
import random

class Cactus(Obstacle):
    def __init__(self, image, rect_y):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = rect_y
