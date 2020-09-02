# import pygame
# import random
#
# # Initialize pygame
# pygame.init()
#
# # genereate a screen
# screen = pygame.display.set_mode((800, 600))
#
# # Game Caption and Icon
# pygame.display.set_caption("SpaceChallenger")
# icon = pygame.image.load('./src/spaceship.png')
# pygame.display.set_icon(icon)
#
# # Player
# playerIcon = pygame.image.load('./src/spaceship2.png')
# # Where player appears
# playerX = 370
# playerY = 480
# playerX_move = 0
#
# # Enemy
# enemyIcon = pygame.image.load('./src/alien.png')
# # Where player appears
# enemyX = random.randint(0, 800)
# enemyY = random.randint(50,150)
# enemyX_move = 0.3
# enemyY_move = 40
#
#
# def player(x, y):
#     # To draw player on the screen
#     screen.blit(playerIcon, (x, y))
#
#
# def enemy(x, y):
#     screen.blit(enemyIcon, (x, y))
#
#
# running = True
# while running:
#     # setting the background
#     screen.fill((80, 80, 80))
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#         # checking left or right key keystroke is pressed.
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_LEFT:
#                 playerX_move = -0.3
#             if event.key == pygame.K_RIGHT:
#                 playerX_move = 0.3
#         if event.type == pygame.KEYUP:
#             if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
#                 playerX_move = 0
#
#     playerX += playerX_move
#     if playerX <= 0:
#         playerX = 0
#     elif playerX >= 736:
#         playerX = 736
#
#     player(playerX, playerY)
#
#     enemyX += enemyX_move
#     if enemyX <= 0:
#         enemyX_move = 0.3
#         enemyY += enemyY_move
#     elif enemyX >= 736:
#         enemyX_move = -0.3
#         enemyY += enemyY_move
#
#     enemy(enemyX, enemyY)
#     pygame.display.update()

####################################################################

from modules import game


game.gameDisplay()
game.playGame()