import pygame
import random
import time

pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('FLAPPY BIRD')
background = pygame.image.load('fbback.png')

fly = False
bird_up = pygame.image.load('bird_up.png')
bird_down = pygame.image.load('bird_down.png')
y_change = 2
y_axis = 390
def player(y_axis):
    if fly:
        screen.blit(bird_up, (40, y_axis))
    else:
        screen.blit(bird_down, (40, y_axis))

pipe_up = pygame.image.load('pipe_up.png')
pipe_down = pygame.image.load('pipe.png')
obsX = 800
obsX_change = -4
obsY = random.randint(-250, 0)
def obs(obsX, obsY):
    screen.blit(pipe_up, (obsX, obsY))
    screen.blit(pipe_down, (obsX, obsY+505))

c = False
def crash(obsX, obsY, y_axis):
    if obsX <= 100 and obsX >= -20:
        if (y_axis >= obsY + 350) and (y_axis <= obsY + 445):
            return False
        else:
            return True
    elif y_axis <= 0 or y_axis >= 535:
        return True
    else:
        return False

over_font = pygame.font.Font('freesansbold.ttf',64)
def game_over_text():
    over_text = over_font.render('GAME OVER', True, (255,255,255))
    screen.blit(over_text, (200,250))

score_font = pygame.font.Font('freesansbold.ttf', 40)
def placescore(score):
    text = score_font.render('SCORE: ', True, (225, 225, 225))
    score_text = score_font.render(str(score), True, (225, 225, 225))
    screen.blit(text, (20, 20))
    screen.blit(score_text, (180, 20))

def autoplay(obsY, y_axis):
    if y_axis >= obsY + 444:
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

self = False
start = time.time()
pausetime = 0
score = 0
f_var = 0
running = True
while running:

    screen.blit(background, (0, 0))
    current = time.time()
    showtime(current-start-pausetime)
    placescore(score)
    autoplaytext(self)

    if self and not fly:
        fly = autoplay(obsY, y_axis)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not fly:
                fly = True
            if event.key == pygame.K_TAB:
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

    if f_var <= 30 and fly:
        y_change = -3
        f_var += 1
    elif f_var >= 10:
        f_var = 0
        y_change = 2
        fly = False

    if obsX < -100:
        obsY = random.randint(-250, 0)
        obsX = 800
        score += 1

    obsX += obsX_change
    obs(obsX, obsY)

    # if obsX == -20:
    #     score += 1

    c = crash(obsX, obsY, y_axis)
    if c:
        game_over_text()
        running = False

    if score >= 40:
        obsX_change = -8
    elif score >= 20:
        obsX_change = -6

    y_axis += y_change
    player(y_axis)

    showtime(current - start - pausetime)
    placescore(score)
    autoplaytext(self)

    pygame.display.update()