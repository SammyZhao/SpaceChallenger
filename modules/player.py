import pygame
from . import game


playerIcon = pygame.image.load('./src/spaceship2.png')
# Where player appears
playerX = 370
playerY = 480
playerX_move = 0

def player(x, y):
    # To draw player on the screen
    game.screen.blit(playerIcon, (x, y))