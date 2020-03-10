import pygame
import random
import math
import time

pygame.init()

screen = pygame.display.set_mode((800,600))

pygame.display.set_caption("SPACE ENEMY")

background = pygame.image.load('back.png')

auto = False
def selfaim(enemyX, enemyY, playerX, enemyX_change):
    maxY = max(enemyY)
    ind = enemyY.index(maxY)
    maxX = enemyX[ind]
    dir = enemyX_change[ind]
    try:
        d = round((480 - maxY) / (playerX - maxX), 2)
    except ZeroDivisionError:
        return 0
    if dir == 4:
        if d > 2.40:
            return 5
        elif d < 2.20:
            return -5
        else:
            return 0
    else:
        if d > -2.20:
            return 5
        elif d < -2.40:
            return -5
        else:
            return 0

# Player
playerImg = pygame.image.load('space-invaders.png')
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemy = 5

for i in range(num_of_enemy):
    enemyImg.append(pygame.image.load('character.png'))
    enemyX.append(random.randint(0,736))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(4)
    enemyY_change.append(40)

# Bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletY_change = 10
bullet_state = 'ready'

# Score
score_val = 0
font = pygame.font.Font('freesansbold.ttf',32)
textX = 10
textY = 10
def showScore(x,y):
    score = font.render('Score : ' + str(score_val), True, (255,255,255))
    screen.blit(score, (x,y))

over_font = pygame.font.Font('freesansbold.ttf',64)
def game_over_text():
    over_text = over_font.render('GAME OVER', True, (255,255,255))
    screen.blit(over_text, (200,250))

def player(x,y):
    screen.blit( playerImg , (x,y) )

def enemy(x,y,i):
    screen.blit( enemyImg[i] , (x,y) )

def fire_bullet(x,y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit( bulletImg, ( x + 16 , y + 10))

def crash(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX-bulletX, 2) + (math.pow(enemyY-bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

autoplayfont = pygame.font.Font('freesansbold.ttf',15)
def autoplaytext(auto):
    if auto:
        autoplay = autoplayfont.render('AUTOPLAY: ON', True, (225, 225, 225))
    else:
        autoplay = autoplayfont.render('AUTOPLAY: OFF', True, (225, 225, 225))
    screen.blit(autoplay, (650, 20))

def showtime(playtime):
    timewritten = autoplayfont.render('TIME: ', True, (225, 225, 225))
    timetxt = autoplayfont.render(str(int(playtime)), True, (225, 225, 225))
    screen.blit(timewritten, (650, 40))
    screen.blit(timetxt, (695, 40))


pausetime = 0
start = time.time()
running = True
while running:
    screen.blit( background , (0,0) )
    autoplaytext(auto)
    showScore(textX, textY)
    current = time.time()
    showtime(current-start-pausetime)

    if auto:
        playerX_change = selfaim(enemyX, enemyY, playerX, enemyX_change)
        if (playerX_change == 0) and (bullet_state is 'ready'):
            bulletX = playerX
            fire_bullet(bulletX, bulletY)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            elif event.key == pygame.K_RIGHT:
                playerX_change = 5
            elif event.key == pygame.K_SPACE:
                if bullet_state is 'ready':
                    bulletX = playerX
                    fire_bullet(bulletX,bulletY)
            elif event.key == pygame.K_TAB:
                if auto == False:
                    auto = True
                else:
                    auto = False
            elif event.key == pygame.K_p:
                pause = True
                while pause:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pause = False
                            running = False
                        elif (event.type == pygame.KEYDOWN) and (event.key == pygame.K_p):
                            pause = False
                    pause_text = over_font.render('PAUSED', True, (255, 255, 255))
                    screen.blit(pause_text, (250, 250))
                    pygame.display.update()
                    if not pause:
                        ptime = time.time()
                        pausetime += (ptime-current)
        if event.type == pygame.KEYUP:
            playerX_change = 0

    playerX += playerX_change
    if playerX < 0:
        playerX = 0
    elif playerX > 736:
        playerX = 736

    # Enemy movement
    for i in range(num_of_enemy):

        # Game Over
        if enemyY[i] > 440:
            for j in range(num_of_enemy):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] < 0:
            enemyX_change[i] = 4
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] > 736:
            enemyX_change[i] = -4
            enemyY[i] += enemyY_change[i]

        # Collision
        collision = crash(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state = 'ready'
            score_val += 1
            enemyX[i] = random.randint(0,736)
            enemyY[i] = random.randint(50,150)
        enemy(enemyX[i],enemyY[i], i)

    # Bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = 'ready'
    if bullet_state is 'fire':
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)

    pygame.display.update()