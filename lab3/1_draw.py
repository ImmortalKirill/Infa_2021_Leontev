import numpy as np
import pygame
from pygame.draw import *
pygame.init()

FPS = 30
screen = pygame.display.set_mode((500, 500))
screen.fill('grey')
#body
circle(screen, (0, 0, 0), (250,250),200, width=1)
circle(screen, (255, 255, 0), (250,250),199, width=199)
rect(screen, (0,0,0), (150, 350, 200, 30), width=0)

#left eye
circle(screen, (255, 255, 255), (180, 180), 40, width = 0)
for i in range(10):

    arc(screen, (255,0,0), (155,155, 2*25,2*25), 0, np.pi*2, width = 50)
circle(screen, (0, 0, 0), (180, 180), 20, width = 0)
#right eye
circle(screen, (255, 0, 0), (320, 175), 30, width = 0)
circle(screen, (0, 0, 0), (320, 175), 15, width = 0)

#left eyebrow

polygon(screen, 'black', [(225,160),(150, 110),(160,100),(232, 153), (225,160)], 0)

#right eyebrow

polygon(screen, 'black', [(275, 160),(350, 110),(340, 100),(250+18, 153),(275,160)], 0)
finished = False
pygame.display.update()
clock = pygame.time.Clock()
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

