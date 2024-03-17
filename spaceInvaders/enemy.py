import pygame

class Enemy:
    def __init__(self, image_path, x, y, x_change, y_change):
        self.image = pygame.image.load(image_path)
        self.x = x
        self.y = y
        self.x_change = x_change
        self.y_change = y_change

    def move(self):
        self.x += self.x_change
        if self.x <= 0 or self.x > 736:
            self.x_change *= -1
            self.y += self.y_change

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def getX(self):
        return self.x