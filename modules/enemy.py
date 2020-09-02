import pygame
import random
from . import game


# Enemy
enemyIcon = pygame.image.load('./src/alien.png')
# Where player appears
enemyX = random.randint(0, 800)
enemyY = random.randint(50,150)
enemyX_move = 0.3
enemyY_move = 40

def enemy(x, y):
    game.screen.blit(enemyIcon, (x, y))