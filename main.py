import pygame

# Initialize pygame
pygame.init()

# genereate a screen
screen = pygame.display.set_mode((800, 600))

# Game Caption and Icon
pygame.display.set_caption("SpaceChallenger")
icon = pygame.image.load('./src/spaceship.png')
pygame.display.set_icon(icon)

# Player
playerIcon = pygame.image.load('./src/spaceship2.png')
# Where player appears
playerX = 370
playerY = 480

def player():
    # To draw player on the screen
    screen.blit(playerIcon, (playerX, playerY))

running = True
while running:
    # setting the background
    screen.fill((80,80,80))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player()
    pygame.display.update()