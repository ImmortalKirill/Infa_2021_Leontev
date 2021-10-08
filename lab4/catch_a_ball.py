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


Number_of_balls = 2


def new_ball_pars():
    '''gives parameters of a new ball
return: x - 1 cor of a ball
y - 2 cor of a ball
r - radius
Vx - velocity in x direction
Vy - velocity in y direction
color - color of a ball
'''
    x = randint(260, 1140)
    y = randint(100, 640)
    r = randint(10, 100)
    Vx = randint(-10, 10)
    Vy = randint(-10, 10)
    color = COLORS[randint(0, 5)]
    return x, y, r, Vx, Vy, color 

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
    
def move_ball(screen, Color, x_cor, y_cor, r, vx, vy, rect):
    """ moves a ball from position x_cor, y_cor to position x_cor+vx, y_cor+vy
        checks if a ball hitted an edge of play-field and changes its velocity
       :par screen: where you want to draw it
       :par x_cor: initial x coordinate of a ball
       :par y_cor: initial y coordinate of a ball
       :par vx: x - shift
       :par vy: y - shift
       :par color: color of a ball
        returns: x_cor, y_cor, vx, vy
        new coordinates and velocity
    """
    if (x_cor < rect[0]) or x_cor > rect[2]:
        vx = -vx
    if y_cor < rect[1] or y_cor > rect[3]:
        vy = -vy
    
    
    circle(screen, BLACK,(x_cor, y_cor), r) 
    circle(screen, Color, (x_cor+vx, y_cor+vy), r)

    x_cor += vx
    y_cor += vy
    return x_cor, y_cor, vx, vy
        



pygame.display.update()
clock = pygame.time.Clock()
finished = False

#lists for parameters of balls
x = [1 for i in range(Number_of_balls)]
y = [1 for i in range(Number_of_balls)]
r = [1 for i in range(Number_of_balls)]
Vx = [1 for i in range(Number_of_balls)]
Vy = [1 for i in range(Number_of_balls)]
color = [1 for i in range(Number_of_balls)]

#initial balls
for i in range(Number_of_balls):
    x[i], y[i], r[i], Vx[i], Vy[i], color[i] = new_ball_pars()
    circle(screen, color[i], (x[i], y[i]), r[i])
    




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
            for i in range(Number_of_balls):
                if (event.pos[0] - x[i])**2 + (event.pos[1] - y[i])**2 <= r[i]**2: #checking if we've hitted the ball

                    Points += 1
                    Misses -= 1
                    screen.fill(BLACK)
                    #changing the ball we've hitted
                    x[i], y[i], r[i], Vx[i], Vy[i], color[i] = new_ball_pars()


    # shifting each ball
    for i in range(Number_of_balls):
        x[i] ,y[i], Vx[i], Vy[i] =  move_ball(screen, color[i], x[i], y[i], r[i], Vx[i], Vy[i], RECT)

        
    #Refreshing screen with new points
    counter(screen, Points, Misses, counter_top_left_corner_x, counter_top_left_corner_y, counter_font_size)
    
    pygame.display.update()

               
pygame.quit()
