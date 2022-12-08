from dino_runner.components.obstacle.obstacle import Obstacle
from dino_runner.utils.constants import BIRD
import random

class Bird(Obstacle):
    def __init__(self, image, rect_y):
        self.type = random.randint(0, 1)
        super().__init__(image, self.type)
        self.rect.y = rect_y
    
        

