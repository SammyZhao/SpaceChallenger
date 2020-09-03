import pygame
import random
from . import game

# more enemy
enemyIcon = []
enemyX = []
enemyY = []
enemyX_move = []
enemyY_move = []
num_of_enemies = 8

for num in range(num_of_enemies):
    # Enemy
    enemyIcon.append(pygame.image.load('./src/alien.png'))
    # Where player appears
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50,150))
    enemyX_move.append(4)
    enemyY_move.append(40)


def enemy(x, y, i):
    game.screen.blit(enemyIcon[i], (x, y))