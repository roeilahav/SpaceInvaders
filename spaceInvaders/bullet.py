import pygame

class Bullet:
    def __init__(self, screen, image_path, x, y, y_change):
        self.screen = screen
        self.image = pygame.image.load(image_path)
        self.x = x
        self.y = y
        self.y_change = y_change
        self.state = "ready"  # "ready" - You can't see the bullet, "fire" - Bullet is moving

    def fire(self, x, y):
        self.state = "fire"
        self.x = x
        self.y = y
        self.draw()

    def move(self):
        if self.state == "fire":
            self.draw()
            self.y -= self.y_change

        if self.y <= 0:
            self.y = 480
            self.state = "ready"

    def draw(self):
        if self.state == "fire":
            self.screen.blit(self.image, (self.x + 16, self.y + 10))

   