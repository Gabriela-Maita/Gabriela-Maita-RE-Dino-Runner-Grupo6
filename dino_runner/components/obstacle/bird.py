from dino_runner.components.obstacle.obstacle import Obstacle

class Bird(Obstacle):
    def __init__(self, image, rect_y):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = rect_y
        self.fly_index = 0

    def draw(self, screen):
        if self.fly_index >= 13:
            self.fly_index = 0
        screen.blit(self.image[self.fly_index // 7], self.rect)
        self.fly_index += 1


        

