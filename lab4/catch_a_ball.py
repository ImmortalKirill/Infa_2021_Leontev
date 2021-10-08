import pygame
from pygame.draw import *
from random import randint
import numpy as np
pygame.init()

FPS = 2

X = 1200
Y = 700
screen = pygame.display.set_mode((X, Y))

# colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

#counter constants
counter_font_size = 32
counter_top_left_corner_x, counter_top_left_corner_y = counter_top_left_corner = (10,10)


def new_ball():
    '''draws new ball with velocity'''
    global x, y, r, Vx, Vy, color
    x = randint(100, 1100)
    y = randint(100, 700)
    r = randint(10, 100)
    Vx = randint(1, 10)
    Vy = randint(1, 10)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)

def counter(screen, points, misses, x_cor, y_cor, font_size):
    """
    displays counter of points and misses on the screen
    :par points: number of points
    :par misses: number of points
    :par x_cor: 1 coordinate of top left corner of counter
    :par y_cor: 2 coordinate of top left corner of counter
    :par font_size: font size
    """     
    points_counter(screen, points, x_cor, y_cor, font_size)
    misses_counter(screen, misses, x_cor, y_cor+40, font_size)
    
def points_counter(screen, points, x_cor, y_cor, font_size):
    """
    displays counter of points at the right top corner of the screen
    :par points: number of points
    :par x_cor: 1 coordinate of top left corner of counter
    :par y_cor: 2 coordinate of top left corner of counter
    :par font_size: font size
    """
    font = pygame.font.Font('freesansbold.ttf', font_size)
    text = font.render('hits: '+str(points), True, GREEN, BLUE)
    textRect = text.get_rect()
    textRect.topleft = (x_cor, y_cor)
    screen.blit(text, textRect)
    
def misses_counter(screen, misses, x_cor, y_cor, font_size):
    """
    displays counter of points at the right top corner of the screen
    :par misses: number of points
    :par x_cor: 1 coordinate of top left corner of counter
    :par y_cor: 2 coordinate of top left corner of counter
    :par font_size: font size
    """
    font = pygame.font.Font('freesansbold.ttf', font_size)
    text = font.render('misses: '+str(misses), True, GREEN, BLUE)
    textRect = text.get_rect()
    textRect.topleft = (x_cor, y_cor)
    screen.blit(text, textRect)
    





pygame.display.update()
clock = pygame.time.Clock()
finished = False

Points = 0
Misses = 0
pygame.display.update()

while not finished:
    clock.tick(FPS)
    Misses += 1
    for event in pygame.event.get():
 
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:

            if (event.pos[0] - x)**2 + (event.pos[1] - y)**2 <= r**2: #checking if we hit the circle

                Points += 1
                Misses -= 1
                



      
    counter(screen, Points, Misses, counter_top_left_corner_x, counter_top_left_corner_y, counter_font_size)
    new_ball()
    pygame.display.update()
    screen.fill(BLACK)

                
pygame.quit()
