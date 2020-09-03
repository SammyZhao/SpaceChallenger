import pygame
import random
import math
from . import player
from . import enemy
from . import bullet
from pygame import mixer

# Initialize pygame
pygame.init()

# genereate a screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('./src/background.png')

# background music
mixer.music.load('./src/background.wav')
mixer.music.play(-1)
# score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10

# Game over text font
game_over_font = pygame.font.Font('freesansbold.ttf', 64)


def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (200, 200, 200))
    screen.blit(score, (x, y))


# game over
def game_over_display():
    game_over = game_over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(game_over, (200, 250))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


def gameDisplay():
    # Game Caption and Icon
    pygame.display.set_caption("SpaceChallenger")
    icon = pygame.image.load('./src/spaceship.png')
    pygame.display.set_icon(icon)


def playGame():
    global score_value
    running = True
    while running:
        # setting the background
        screen.fill((80, 80, 80))

        # background image
        screen.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # checking left or right key keystroke is pressed.
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.playerX_move = -5
                if event.key == pygame.K_RIGHT:
                    player.playerX_move = 5
                if event.key == pygame.K_SPACE:
                    if bullet.bullet_state is "ready":
                        bullet_sound = mixer.Sound('./src/laser.wav')
                        bullet_sound.play()
                        bullet.bulletX = player.playerX
                        bullet.fireBullet(bullet.bulletX, player.playerY)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player.playerX_move = 0

        # player movement

        player.playerX += player.playerX_move
        if player.playerX <= 0:
            player.playerX = 0
        elif player.playerX >= 736:
            player.playerX = 736

        player.player(player.playerX, player.playerY)

        # enemy movement
        for i in range(enemy.num_of_enemies):

            # Game over
            if enemy.enemyY[i] > 480:
                for j in range(enemy.num_of_enemies):
                    enemy.enemyY[j] = 2000
                game_over_display()
                break

            enemy.enemyX[i] += enemy.enemyX_move[i]
            if enemy.enemyX[i] <= 0:
                enemy.enemyX_move[i] = 5
                enemy.enemyY[i] += enemy.enemyY_move[i]
            elif enemy.enemyX[i] >= 736:
                enemy.enemyX_move[i] = -5
                enemy.enemyY[i] += enemy.enemyY_move[i]

            # checking collission
            collision = isCollision(enemy.enemyX[i], enemy.enemyY[i], bullet.bulletX, bullet.bulletY)
            if collision == True:
                explosion_sound = mixer.Sound('./src/explosion.wav')
                explosion_sound.play()
                bullet.bulletY = 480
                bullet.bullet_state = "ready"
                score_value += 1
                enemy.enemyX[i] = random.randint(0, 735)
                enemy.enemyY[i] = random.randint(50, 150)

            enemy.enemy(enemy.enemyX[i], enemy.enemyY[i], i)

        # bullet movement
        if bullet.bulletY <= 0:
            bullet.bulletY = 480
            bullet.bullet_state = "ready"

        if bullet.bullet_state is "fire":
            bullet.fireBullet(bullet.bulletX, bullet.bulletY)
            bullet.bulletY -= bullet.bulletY_move

        player.player(player.playerX, player.playerY)
        show_score(textX, textY)
        pygame.display.update()
