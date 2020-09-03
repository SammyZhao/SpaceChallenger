import pygame
from . import game

bulletIcon = pygame.image.load('./src/bullet.png')
# Where player appears
bulletX = 0
bulletY = 480
bulletX_move = 0
bulletY_move = 10

bullet_state = "ready"


def fireBullet(x, y):
    global bullet_state
    bullet_state = "fire"
    # To draw player on the screen
    game.screen.blit(bulletIcon, (x + 16, y + 10))
