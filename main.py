import pygame
import subprocess
import webbrowser
import time
import os

def snake():
    #os.system('python3 snake.py 1')
    subprocess.call('python3 snake.py 1', shell=True)

def space_invadors():
    #os.system('python3 space_invadors.py 1')
    subprocess.call('python3 space_invadors.py 1', shell=True)

def jump_n_tuck():
    #os.system('python3 jump_n_tuck.py 1')
    subprocess.call('python3 jump_n_tuck.py 1', shell=True)

def flappy_birds():
    #os.system('python3 flappy_birds.py 1')
    subprocess.call('python3 flappy_birds.py 1', shell=True)

def webpage():
    webbrowser.open('file:///home/sanket/PycharmProjects/Science%20Day%20Project%20-%20Sanket%20Mathur/WebPage/index.html')
    #add the location of the project accordingly
    
pygame.init()

screen = pygame.display.set_mode((600,700))

pygame.display.set_caption('SCIENCE DAY PROJECT')

background = pygame.image.load('background.jpg')

t_font = pygame.font.Font('Montague.ttf', 85)
m_font = pygame.font.Font('albas.ttf', 31)
def title():
    t_text = t_font.render('WHO IS PLAYIN\'?', True, (76, 224, 170))
    m_text = m_font.render('Play Yourself OR Let The Computer Do It', True, (61, 179, 136))
    screen.blit(t_text, (5, 0))
    screen.blit(m_text, (5,85))

head_font = pygame.font.Font('GenghisKhan.ttf', 23)
text_font = pygame.font.Font('GenghisKhan.ttf', 18)
textI_font = pygame.font.Font('GenghisKhan.ttf', 20)
def text():
    h1 = head_font.render('Programming Language Used:', True, (225, 225, 225))
    t1 = text_font.render('Python', True, (225, 225, 225))
    h2 = head_font.render('Framework Used:', True, (225, 225, 225))
    t2 = text_font.render('Pygame', True, (225, 225, 225))
    h3 = head_font.render('Libraries Used:', True, (225, 225, 225))
    t31 = text_font.render('math', True, (225, 225, 225))
    t32 = text_font.render('random', True, (225, 225, 225))
    t33 = text_font.render('time', True, (225, 225, 225))
    t34 = text_font.render('subprocess', True, (225, 225, 225))
    t35 = text_font.render('webbrowser', True, (225, 225, 225))
    h4 = head_font.render('IDE Used:', True, (225, 225, 225))
    t4 = text_font.render('PyCharm', True, (225, 225, 225))
    h5 = head_font.render('Made By:', True, (225, 225, 225))
    t51 = text_font.render('NAME: Sanket Mathur', True, (225, 225, 225))
    t52 = text_font.render('ROLLO: 1902229', True, (225, 225, 225))
    t53 = text_font.render('COLLEGE: Chandigarh Group of Colleges', True, (225, 225, 225))
    t54 = text_font.render('WEBSITE: learningprogrammer.ga', True, (225, 225, 225))

    screen.blit(h1, (5, 285))
    screen.blit(t1, (15, 310))
    screen.blit(h2, (5, 335))
    screen.blit(t2, (15, 360))
    screen.blit(h3, (5, 385))
    screen.blit(t31, (15, 410))
    screen.blit(t32, (15, 430))
    screen.blit(t33, (15, 450))
    screen.blit(t34, (15, 470))
    screen.blit(t35, (15, 490))
    screen.blit(h4, (5, 515))
    screen.blit(t4, (15, 540))
    screen.blit(h5, (5, 565))
    screen.blit(t51, (15, 590))
    screen.blit(t52, (15, 610))
    screen.blit(t53, (15, 630))
    screen.blit(t54, (15, 650))

snake_font = pygame.font.Font('planetbe.ttf',45)
space_font = pygame.font.Font('BroadcastTitling.ttf', 45)
jnt_font = pygame.font.Font('WedgieRegular.ttf', 50)
flappy_birds_font = pygame.font.Font('CheapSign.ttf', 60)
web_font = pygame.font.Font('Montague.ttf', 67)
def placebuttons(posX, posY, click):
    pygame.draw.rect(screen, (217, 59, 35), pygame.Rect(300, 150, 250, 100))
    pygame.draw.rect(screen, (217, 59, 35), pygame.Rect(300, 290, 250, 100))
    pygame.draw.rect(screen, (217, 59, 35), pygame.Rect(300, 430, 250, 100))
    pygame.draw.rect(screen, (217, 59, 35), pygame.Rect(300, 570, 250, 100))
    pygame.draw.rect(screen, (217, 59, 35), pygame.Rect(20, 150, 250, 100))

    if posX >= 300 and posX <= 550 and posY >= 150 and posY <= 250:
        pygame.draw.rect(screen, (255, 65, 41), pygame.Rect(300, 150, 250, 100))
        if click != (0, 0, 0):
            snake()
    if posX >= 300 and posX <= 550 and posY >= 290 and posY <= 390:
        pygame.draw.rect(screen, (255, 65, 41), pygame.Rect(300, 290, 250, 100))
        if click != (0, 0, 0):
            space_invadors()
    if posX >= 300 and posX <= 550 and posY >= 430 and posY <= 530:
        pygame.draw.rect(screen, (255, 65, 41), pygame.Rect(300, 430, 250, 100))
        if click != (0, 0, 0):
            jump_n_tuck()
    if posX >= 300 and posX <= 550 and posY >= 570 and posY <= 670:
        pygame.draw.rect(screen, (255, 65, 41), pygame.Rect(300, 570, 250, 100))
        if click != (0, 0, 0):
            flappy_birds()
    if posX >= 20 and posX <= 270 and posY >= 150 and posY <= 250:
        pygame.draw.rect(screen, (255, 65, 41), pygame.Rect(20, 150, 250, 100))
        if click != (0, 0, 0):
            webpage()
            time.sleep(1)

    snake_title = snake_font.render('SNAKE', True, (255, 248, 59))
    space_title = space_font.render('SPACE', True, (255, 248, 59))
    invador_title = space_font.render('INVADORS', True, (255, 248, 59))
    jump_title = jnt_font.render('JUMP', True, (255, 248, 59))
    n_title = jnt_font.render('AND', True, (255, 248, 59))
    tuck_title = jnt_font.render('TUCK', True, (255, 248, 59))
    web_title = web_font.render('WEBSITE', True, (255, 248, 59))
    flappy_title = flappy_birds_font.render('FLAPPY', True, (255, 248, 59))
    birds_title = flappy_birds_font.render('BIRDS', True, (255, 248, 59))

    screen.blit(snake_title, (340, 170))
    screen.blit(space_title, (350, 290))
    screen.blit(invador_title, (315, 335))
    screen.blit(jump_title, (302, 429))
    screen.blit(n_title, (390, 458))
    screen.blit(tuck_title, (457, 480))
    screen.blit(flappy_title, (305, 573))
    screen.blit(birds_title, (425, 620))
    screen.blit(web_title, (25, 160))

running = True
while running:

    screen.blit(background, (0, 0))
    screen.blit(background, (0, 600))

    title()
    text()

    posX, posY = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    placebuttons(posX, posY, click)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
