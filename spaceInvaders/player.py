import pygame


class Player:
    def __init__(self, image_path, x, y):
        self.image = pygame.image.load(image_path)
        self.x = x
        self.y = y
        self.x_change = 0

    def handle_keys(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.x_change = -2
            if event.key == pygame.K_RIGHT:
                self.x_change = 2

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                self.x_change = 0

    def move(self):
        self.x += self.x_change
        # Boundary checking
        self.x = max(0, min(self.x, 736))

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
