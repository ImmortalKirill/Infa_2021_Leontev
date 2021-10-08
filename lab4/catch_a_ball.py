import pygame
from pygame.draw import *
from random import randint
import numpy as np
pygame.init()

FPS = 30

X = 1200
Y = 700
screen = pygame.display.set_mode((X, Y))

#play-field
RECT = left_wall, up_wall, right_wall, down_wall = (250, 50, 1150, 650)
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
    '''draws new ball with velocity
'''
    global x, y, r, Vx, Vy, color
    x = randint(260, 1140)
    y = randint(100, 640)
    r = randint(10, 100)
    Vx = randint(-10, 10)
    Vy = randint(-10, 10)
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
    
def move_ball(screen, x_cor, y_cor, vx, vy, Color):
    """ moves a ball from position x_cor, y_cor to position x_cor+vx, y_cor+vy
       :par screen: where you want to draw it
       :par x_cor: initial x coordinate of a ball
       :par y_cor: initial y coordinate of a ball
       :par vx: x - shift
       :par vy: y - shift
       :par color: color of a ball

    """
    screen.fill(BLACK)
    circle(screen, Color, (x_cor+vx, y_cor+vy), r)
def change_ball_pars(x_cor, y_cor, vx, vy, rect):
    """
    shifts coorditates
    checks if a ball hitted an edge of play-field and changes its velocity
    :par x_cor: initial x coordinate of a ball
    :par y_cor: initial y coordinate of a ball
    :par vx: x - shift
    :par vy: y - shift
    :par rect: = (x1 ,y1, x2, y2) =
    x, y - top left corner of play-field
    x2, y2 -down right corner of play-field
    Returns new x coordinate, y coordinate, vx, vy
    """
    if (x_cor < rect[0]) or x_cor > rect[2]:
        vx = -vx
    if y_cor < rect[1] or y_cor > rect[3]:
        vy = -vy
    x_cor += vx
    y_cor += vy
    return x_cor, y_cor, vx, vy
        



pygame.display.update()
clock = pygame.time.Clock()
finished = False
new_ball()
Points = 0
Misses = 0
pygame.display.update()

while not finished:
    clock.tick(FPS)

    for event in pygame.event.get():
 
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            Misses += 1
            if (event.pos[0] - x)**2 + (event.pos[1] - y)**2 <= r**2: #checking if we hit the circle

                Points += 1
                Misses -= 1
                screen.fill(BLACK)
                new_ball()



    
    move_ball(screen, x, y, Vx, Vy, color)
    x ,y, Vx, Vy = change_ball_pars(x, y, Vx, Vy, RECT)
    #Refreshing screen with new points
    counter(screen, Points, Misses, counter_top_left_corner_x, counter_top_left_corner_y, counter_font_size)
    
    pygame.display.update()

               
pygame.quit()
