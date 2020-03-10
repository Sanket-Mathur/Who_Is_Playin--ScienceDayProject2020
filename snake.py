import pygame
import random
import time

pygame.init()

screen = pygame.display.set_mode((640,660))

foodimg = pygame.image.load('fruit.png')

pygame.display.set_caption('SNAKE')

# Player
playerPos = [[300, 300], [300, 320], [300, 340]]
dir = 'u'
def player(pos):
    for x in pos:
        pygame.draw.rect(screen, (225, 225, 225), pygame.Rect(x[0], x[1], 20, 20))

auto = False
def self(dir, foodX, foodY, playerPos):
    if (playerPos[0][0] > foodX) and ([playerPos[0][0]-20,playerPos[0][1]] not in playerPos) and ((playerPos[0][0]-20)>=20):
        return 'l'
    elif (playerPos[0][0] < foodX) and ([playerPos[0][0]+20,playerPos[0][1]] not in playerPos) and ((playerPos[0][0]+20)<620):
        return 'r'
    elif (playerPos[0][1] < foodY) and ([playerPos[0][0],playerPos[0][1]+20] not in playerPos) and ((playerPos[0][1]+20)<620):
        return 'd'
    elif (playerPos[0][1] > foodY) and ([playerPos[0][0],playerPos[0][1]-20] not in playerPos) and ((playerPos[0][1]-20)>=20):
        return 'u'
    elif (dir=='r' or dir=='l') and ([playerPos[0][0],playerPos[0][1]+20] not in playerPos) and ((playerPos[0][1]+20)<620):
        return 'd'
    elif (dir=='r' or dir=='l') and ([playerPos[0][0],playerPos[0][1]-20] not in playerPos) and ((playerPos[0][1]-20)>=20):
        return 'u'
    elif (dir=='u' or dir=='d') and ([playerPos[0][0]-20,playerPos[0][1]] not in playerPos) and ((playerPos[0][0]-20)>=20):
        return 'l'
    elif (dir=='u' or dir=='d') and ([playerPos[0][0]+20,playerPos[0][1]] not in playerPos) and ((playerPos[0][0]+20)<620):
        return 'r'
    else:
        return dir

# Food
def add_food(x,y):
    screen.blit(foodimg, (x, y))

# Collision between food and snake
def eat(x, y, foodX, foodY):
    if (x == foodX) and (y == foodY):
        return True
    else:
        return False

# Collision between snake body or boundary
def crash(pos):
    l = [pos[x] for x in range(1, len(pos))]
    if pos[0] in l:
        return True
    elif (pos[0][0] >= 620) or (pos[0][0] < 20) or (pos[0][1] >= 620) or (pos[0][1] < 20):
        return True
    else:
        return False

# Game Over text
over_font = pygame.font.Font('freesansbold.ttf',64)
def game_over_text():
    over_text = over_font.render('GAME OVER', True, (255,255,255))
    screen.blit(over_text, (100,250))

autoplayfont = pygame.font.Font('freesansbold.ttf',15)
def autoplaytext(auto):
    if auto:
        autoplay = autoplayfont.render('AUTOPLAY: ON', True, (0, 0, 0))
    else:
        autoplay = autoplayfont.render('AUTOPLAY: OFF', True, (0, 0, 0))
    screen.blit(autoplay, (500, 643))

def timeplayed(cur, score):
    written = autoplayfont.render('Time: ', True, (0, 0, 0))
    timeplay = autoplayfont.render(str(int(cur)), True, (0, 0, 0))
    scorewritten = autoplayfont.render('Score: ', True, (0, 0, 0))
    scoretxt = autoplayfont.render(str(score), True, (0, 0, 0))
    screen.blit(written, (20, 643))
    screen.blit(timeplay, (62, 643))
    screen.blit(scorewritten, (300, 643))
    screen.blit(scoretxt, (350, 643))

foodX = random.randint(1, 30) * 20
foodY = random.randint(1, 30) * 20
eaten = False

score = 0
start = time.time()
pausetime = 0
running = True
while running:

    screen.fill((20,102,37))

    pygame.draw.rect(screen, (22,168,39), pygame.Rect(20, 20, 600, 600))
    pygame.draw.rect(screen, (22,107,107), pygame.Rect(0,640,640,20))

    autoplaytext(auto)
    current = time.time()
    timeplayed(current-start-pausetime, score)

    if auto:
        dir = self(dir, foodX, foodY, playerPos)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                dir = 'u'
            elif event.key == pygame.K_DOWN:
                dir = 'd'
            elif event.key == pygame.K_LEFT:
                dir = 'l'
            elif event.key == pygame.K_RIGHT:
                dir = 'r'
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
                    screen.blit(pause_text, (200, 250))
                    pygame.display.update()
                    if not pause:
                        ptime = time.time()
                        pausetime += (ptime-current)

    playerPos.insert(1,list(playerPos[0]))
    if dir == 'u':
        playerPos[0][1] -= 20
    elif dir == 'd':
        playerPos[0][1] += 20
    elif dir == 'l':
        playerPos[0][0] -= 20
    elif dir == 'r':
        playerPos[0][0] += 20
    if not eaten:
        playerPos.pop()

    if eaten:
        score += 1
        while True:
            foodX = random.randint(1, 30) * 20
            foodY = random.randint(1, 30) * 20
            if [foodX, foodY] not in playerPos:
                break
        eaten = False

    add_food(foodX,foodY)

    end = crash(playerPos)
    if end:
        game_over_text()
        running = False

    player(playerPos)

    eaten = eat(playerPos[0][0], playerPos[0][1], foodX, foodY)

    pygame.display.update()

    time.sleep(0.07)
