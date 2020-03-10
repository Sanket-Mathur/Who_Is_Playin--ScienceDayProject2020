import pygame
import random
import math
import time

pygame.init()

screen = pygame.display.set_mode((1000, 560))

pygame.display.set_caption("JUMP AND TUCK")

back = pygame.image.load('backofskate.jpg')

playerimg_stand = pygame.image.load('skate.png')
playerimg_bent = pygame.image.load('skate_bent.png')
playerX = 60
playerY = 330
bent = False
def player(x, y, bent):
    if bent:
        screen.blit(playerimg_bent, (x, y+2))
    else:
        screen.blit(playerimg_stand, (x, y))

def chooseObs():
    return random.randint(1,2)

birdimg = pygame.image.load('bird.png')
trashimg = pygame.image.load('trash.png')
obsX = 1000
obsX_change = -10
def placeObs(x, obs):
    if obs == 1:
        screen.blit(birdimg, (x, 230))
    else:
        screen.blit(trashimg, (x, 390))

c = False
def crash(playerY, obsX, o, bent):
    if o == 1:
        if obsX >= 0 and obsX <= 107 and not bent:
            return True
    elif o == 2:
        dist = math.sqrt((obsX-60)**2 + (390-playerY)**2)
        if dist < 105:
            return True
    else:
        return False

over_font = pygame.font.Font('freesansbold.ttf',100)
def game_over_text():
    over_text = over_font.render('GAME OVER', True, (0,0,0))
    screen.blit(over_text, (200,230))

self = False
def auto(obsX, o):
    if o == 1 and obsX >= 0 and obsX <= 300:
        return 'tuck'
    elif o == 2 and obsX >= 0 and obsX <= 200:
        return 'jump'
    else:
        return 'none'

autoplayfont = pygame.font.Font('freesansbold.ttf',15)
def autoplaytext(auto):
    if auto:
        autoplay = autoplayfont.render('AUTOPLAY: ON', True, (225, 225, 225))
    else:
        autoplay = autoplayfont.render('AUTOPLAY: OFF', True, (225, 225, 225))
    screen.blit(autoplay, (800, 543))

def timeplayed(cur, score):
    written = autoplayfont.render('Time: ', True, (225, 225, 225))
    timeplay = autoplayfont.render(str(int(cur)), True, (225, 225, 225))
    scorewritten = autoplayfont.render('Score: ', True, (225, 225, 225))
    scoretxt = autoplayfont.render(str(score), True, (225, 225, 225))
    screen.blit(written, (20, 543))
    screen.blit(timeplay, (60, 543))
    screen.blit(scorewritten, (400, 543))
    screen.blit(scoretxt, (450, 543))

jump = False
fall = False
o = chooseObs()

obs1 = 0
obs2 = 1000

score = 0
start = time.time()
pausetime = 0
running = True
while running:

    screen.fill((0, 0, 0))

    screen.blit(back, (obs1, 0))
    screen.blit(back, (obs2, 0))
    obs1 += obsX_change//3
    obs2 += obsX_change//3
    if obs1 <= -1000:
        obs1 = 0
        obs2 = 1000


    autoplaytext(self)

    current = time.time()
    t = current-start
    timeplayed(current-start-pausetime, score)

    if self:
        comm = auto(obsX , o)
        if comm is 'jump':
            jump = True
        elif comm is 'tuck':
            bent = True
        elif comm is 'none':
            bent = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and not jump and not bent:
                jump = True
            elif event.key == pygame.K_DOWN and not jump:
                bent = True
            elif event.key == pygame.K_TAB:
                if self:
                    self = False
                else:
                    self = True
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
            if event.key == pygame.K_DOWN:
                bent = False

    placeObs(obsX, o)
    if obsX > -100:
        obsX += obsX_change
    else:
        obsX = 1000
        o = chooseObs()
        score += 1

    if jump:
        if playerY > 190 and not fall:
            playerY -= 10
        elif playerY < 330:
            playerY += 10
            fall = True
        else:
            jump = False
            fall = False

    if t >= 120:
        obsX_change = -22
    elif t >= 60:
        obsX_change = -19
    elif t >= 40:
        obsX_change = -16
    elif t >= 20:
        obsX_change = -13

    player(playerX, playerY, bent)

    c = crash(playerY, obsX, o, bent)

    if c:
        game_over_text()
        running = False

    pygame.display.update()

    #time.sleep(0.07)