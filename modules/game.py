import pygame
from . import player
from . import enemy

# Initialize pygame
pygame.init()

# genereate a screen
screen = pygame.display.set_mode((800, 600))


def gameDisplay():
    # Game Caption and Icon
    pygame.display.set_caption("SpaceChallenger")
    icon = pygame.image.load('./src/spaceship.png')
    pygame.display.set_icon(icon)


def playGame():
    running = True
    while running:
        # setting the background
        screen.fill((80, 80, 80))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # checking left or right key keystroke is pressed.
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.playerX_move = -0.3
                if event.key == pygame.K_RIGHT:
                    player.playerX_move = 0.3
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player.playerX_move = 0

        player.playerX += player.playerX_move
        if player.playerX <= 0:
            player.playerX = 0
        elif player.playerX >= 736:
            player.playerX = 736

        player.player(player.playerX, player.playerY)

        enemy.enemyX += enemy.enemyX_move
        if enemy.enemyX <= 0:
            enemy.enemyX_move = 0.3
            enemy.enemyY += enemy.enemyY_move
        elif enemy.enemyX >= 736:
            enemy.enemyX_move = -0.3
            enemy.enemyY += enemy.enemyY_move

        enemy.enemy(enemy.enemyX, enemy.enemyY)
        pygame.display.update()
