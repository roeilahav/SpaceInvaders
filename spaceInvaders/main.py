import pygame, random , math
from enemy import Enemy
from player import Player
from bullet import Bullet  

# Initialize Pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('pictures\space.png')

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('pictures\spaceship.png')
pygame.display.set_icon(icon)

# Player
player = Player('pictures\player.png', 370, 480)

# Enemies
enemies = [
    Enemy('pictures\comet.png', random.randint(0, 800), random.randint(50, 150), 1.5, 10),
    Enemy('pictures\comet2.png', random.randint(0, 800), random.randint(50, 150), 1.5, 10),
    Enemy('pictures\comet3.png', random.randint(0, 800), random.randint(50, 150), 1.5, 10)
]

# Bullet
bullet = Bullet(screen, 'pictures\missile.png', 0, 480, 3)

# var for keeping score
score_val = 0
font = pygame.font.Font('freesansbold.ttf',32)

textX = 10
textY = 10

def show_score(x,y):
    score = font.render("Score:" + str(score_val),True,(255,255,255))
    screen.blit(score,(x,y))

def isCollision(enemies, bullet):
    for enemy in enemies:
        distance = math.sqrt(math.pow(enemy.x - bullet.x, 2) + math.pow(enemy.y - bullet.y, 2))
        if distance < 27:  
            return True
    return False

# Game Loop
running = True
while running:
    # RGB
    screen.fill((0, 0, 0))
    
    # Background Image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        player.handle_keys(event)

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and bullet.state == "ready":
            bullet.fire(player.x, bullet.y)

    # Player Movement
    player.move()
    player.draw(screen)

    # Bullet Movement
    bullet.move()

    # Enemy Movement
    for enemy in enemies:
        enemy.move()
        enemy.draw(screen)


    # collison
    for enemy in enemies:
        enemy.move()
        enemy.draw(screen)
        if isCollision(enemies, bullet):
            # Handle collision (like resetting bullet and updating game state)
            bullet.state = "ready"
            bullet.y = 480
            score_val += 1
            print(score_val)
            enemy.x = random.randint(0,735)
            enemy.y = random.randint(50,150)

    show_score(textX,textY)

    pygame.display.update()
