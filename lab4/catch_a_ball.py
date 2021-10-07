import pygame
from pygame.draw import *
from random import randint
import numpy as np
pygame.init()

FPS = 2
# assigning values to X and Y variable
X = 1200
Y = 800
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
    y = randint(100, 800)
    r = randint(10, 100)
    Vx = randint(1, 10)
    Vy = randint(1, 10)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)
    
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
    :par points: number of points
    :par x_cor: 1 coordinate of top left corner of counter
    :par y_cor: 2 coordinate of top left corner of counter
    :par font_size: font size
    """
    font = pygame.font.Font('freesansbold.ttf', font_size)
    text = font.render('misses: '+str(misses), True, GREEN, BLUE)
    textRect = text.get_rect()
    textRect.topleft = (x_cor, y_cor)
    screen.blit(text, textRect)

def counter(screen, x_cor, y_cor, font_size):
    """
    displays counter of points and misses on the screen
    :par points: number of points
    :par x_cor: 1 coordinate of top left corner of counter
    :par y_cor: 2 coordinate of top left corner of counter
    :par font_size: font size
    """     
    points_counter(screen, points, x_cor, y_cor, font_size)
    misses_counter(screen, misses, x_cor, y_cor+40, font_size)
    pygame.display.update()
    
# set the pygame window name
pygame.display.set_caption('Catch a ball')





pygame.display.update()
clock = pygame.time.Clock()


points = 0
misses = 0
new_ball()
pygame.display.update()
finished = False
while not finished:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            misses+=1
            if (event.pos[0] - x)**2 + (event.pos[1] - y)**2 <= r**2: #checking if we hit the circle
                print('Ladies and gentlemen, we got em!')
                points += 1
                misses -= 1
                
                screen.fill(BLACK)
                
                new_ball()
                pygame.display.update()
               
            else:
                print('Goddamn, he escaped!')
        #counter of points and misses
        counter(screen, counter_top_left_corner_x, counter_top_left_corner_y, counter_font_size)

                
pygame.quit()
