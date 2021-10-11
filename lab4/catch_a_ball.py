import pygame
from pygame.draw import *
from random import randint
import numpy as np
pygame.init()

FPS = 30
# screen size
X = 1200
Y = 700
screen = pygame.display.set_mode((X, Y))

#start button
start_font_size = 200

#game_over
game_over_size = 180
menu_button_size = 100
restart_button_size = 100
Points_size = 100
#coordinates of the center of buttons
start_x_cor = X/2
start_y_cor = Y/2

menu_y_cor = 80/100*Y
#play-field
RECT = left_wall, up_wall, right_wall, down_wall = (250/1200*X, 10/700*Y, 1190/1200*X, 690/700*Y)
# colors
WHITE = (255, 255, 255)
GOLD = (255,215,0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, WHITE, GREEN, MAGENTA, CYAN]

#counter constants
counter_font_size = 32
counter_top_left_corner_x, counter_top_left_corner_y = counter_top_left_corner = (10/1200*X,10/700*Y)

#game pars
Number_of_balls = 2
Number_of_small_balls = 3
Supa_ball_radius = 70
Small_ball_radius = 15

Small_ball_time = 2000

def new_ball_pars():
    '''gives parameters of a new ball
return: x, y, r, Vx, Vy, color
x - 1 cor of a ball
y - 2 cor of a ball
r - radius
Vx - velocity in x direction
Vy - velocity in y direction
color - color of a ball
'''
    x = randint(340, 1100)
    y = randint(140, 600)
    r = randint(15, 50)
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
    rect(screen, BLUE, (0, 0, left_wall, down_wall), 0)
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
    text = font.render('Points: '+str(points), True, GREEN, BLUE)
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
    """ moves ball from position x_cor, y_cor to position x_cor+vx, y_cor+vy
        checks if ball hitted an edge of the play-field and changes its velocity
       :par screen: where you want to draw it
       :par x_cor: initial x coordinate of a ball
       :par y_cor: initial y coordinate of a ball
       :par vx: x - shift
       :par vy: y - shift
       :par color: color of a ball
        returns: x_cor, y_cor, vx, vy
        new coordinates and velocity
    """
    if (x_cor < rect[0]+r) or x_cor > rect[2]-r:
        vx = -vx
    if y_cor < rect[1]+r or y_cor > rect[3]-r:
        vy = -vy
    
    
    circle(screen, BLACK,(x_cor, y_cor), r) 
    circle(screen, Color, (x_cor+vx, y_cor+vy), r)

    x_cor += vx
    y_cor += vy
    return x_cor, y_cor, vx, vy
        
def supa_ball(screen):
    """ draws supa ball on the screen
    gives parameters of a new supa_ball
    :par screen: display
    return: color, x, y, r, Vx, Vy
    x - 1 cor of a ball
    y - 2 cor of a ball
    r - radius
    Vx - velocity in x direction
    Vy - velocity in y direction
    color - color of a ball
    """
    x = randint(340, 1100)
    y = randint(140, 600)
    r = Supa_ball_radius
    Vx = randint(-10, 10)
    Vy = randint(-10, 10)
    circle(screen, GOLD, (x, y), r)
    return [GOLD, x, y, r, Vx, Vy]
def small_ball(screen, x_cor, y_cor, r):
    """draws small_ball of the screen
    gives parameters of a new small_ball
    :par screen: display
    :par x_cor: 1 coordinate of supa_ball which produced this small ball
    :par y_cor: 2 coordinate of supa_ball which produced this small ball
    :par r: radius of supa_ball which produced this small ball
    return: color, x, y, r, Vx, Vy
    x - 1 cor of a ball
    y - 2 cor of a ball
    r - radius
    Vx - velocity in x direction
    Vy - velocity in y direction
    color - color of a ball
    """
    r = Small_ball_radius
    Vx = randint(-10, 10)
    Vy = randint(-10, 10)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x_cor, y_cor), r)
    return [color, x_cor, y_cor, r, Vx, Vy]    

def menu_screen(screen):
    """
    draws menu screen
    :par screen: display
    """
    global Start_button_width, Start_button_length    
    Start_button_width, Start_button_length = button('Start', GREEN, BLUE, start_x_cor, start_y_cor, start_font_size)
    button('Menu', RED, WHITE, X/2, Y/5, 100)
    

def button(name, name_color, background_color, x, y, font_size):
    """
    draws button 'name' with center in (x,y) cor
    returns: width and length of button
    """

    font = pygame.font.Font('freesansbold.ttf', font_size)
    text = font.render(name, True, name_color, background_color)
    textRect = text.get_rect()
    textRect.center = (x, y)
    screen.blit(text, textRect)
    return font.size(name)

def button_hit(x_tap, y_tap, x_button, y_button, button_width, button_length):
    """
    checks if (x_tap, y_tap) is in rect (x_button, y_button, button_width, button_length) tapped on button
    :par x_tap: x cor of tap
    :par y_tap: y cor of tap
    :par x_button: x cor of the center of button
    :par y_button: y cor of the center of button
    returs: True or False
    """
    if abs(x_tap - x_button) < button_width/2 and abs(y_tap - y_button) < button_length/2:
        return True
    else: return False

def game_over(screen, Points):
    """
    draws game_over screen
    :par screen: display
    """
    global menu_button_width, menu_button_length, restart_button_width, restart_button_length
    screen.fill(BLACK)
    game_over_width, game_over_length = button('Game over', RED, WHITE, X/2, Y/5, game_over_size)
    if Points != 1:
        button('You scored: '+str(Points)+' Points', RED, WHITE, X/2, Y*45/100, Points_size)
    else: button('You scored: '+str(Points)+' Point', RED, WHITE, X/2, Y*45/100, Points_size)
    menu_button_width, menu_button_length = button('Menu', GREEN, BLUE, X/2, menu_y_cor, menu_button_size)
    restart_button_width, restart_button_length = button('Restart', GREEN, BLUE, X/2, menu_y_cor - menu_button_length - 5, restart_button_size)
    pygame.display.update()
    
Game_start = True   
finished = False


pygame.display.update()
while not finished:
    clock = pygame.time.Clock()


    #lists for parameters of balls
    x = [1 for i in range(Number_of_balls)]
    y = [1 for i in range(Number_of_balls)]
    r = [1 for i in range(Number_of_balls)]
    Vx = [1 for i in range(Number_of_balls)]
    Vy = [1 for i in range(Number_of_balls)]
    color = [1 for i in range(Number_of_balls)]

    #super ball list of parameters
    supa_ball_pars = []
    #small ball list of parameters
    small_balls_pars = []

    #events for smallballs
    events = []
    #initial balls
    for i in range(Number_of_balls):
        x[i], y[i], r[i], Vx[i], Vy[i], color[i] = new_ball_pars()
    # displaying menu screen
    screen.fill(BLACK)
    menu_screen(screen)



    Points = 0
    Misses = 0


    pygame.display.update()
    supa_chance = randint(0,1)


    #game menu
    while Game_start:
        clock.tick(FPS)

        
        x_mouse, y_mouse = pygame.mouse.get_pos()
        
        if button_hit(x_mouse, y_mouse, start_x_cor, start_y_cor, Start_button_width, Start_button_length) == True:
            button('Start', BLUE, GREEN, X/2, Y/2, start_font_size)

            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
                Game_start = False
                Game_play = False
                Game_over = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                #checking if player tapped on start button
                
                if button_hit(event.pos[0], event.pos[1], start_x_cor, start_y_cor, Start_button_width, Start_button_length) == True:
                    Game_start = False
                    Game_play = True
                    
        
        pygame.display.update()
        button('Start', GREEN, BLUE, X/2, Y/2, start_font_size)    


                
    screen.fill(BLACK)   
    #game-play
    while Game_play:
        clock.tick(FPS)

            
        for event in pygame.event.get():
     
            if event.type == pygame.QUIT:
                finished = True
                Game_play = False
                Game_over = False

                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # condition of game over
                if Misses >= 3:
                    Game_play = False
                    Game_over = True
                Misses += 1
                
                #cheking simple balls
                for i in range(Number_of_balls):
                    if (event.pos[0] - x[i])**2 + (event.pos[1] - y[i])**2 <= r[i]**2: #checking if we've hitted the ball

                        Points += 1
                        Misses -= 1
                        screen.fill(BLACK)
                        #changing the ball we've hitted
                        x[i], y[i], r[i], Vx[i], Vy[i], color[i] = new_ball_pars()
                        #chance of getting new supa ball (33%)
                        supa_chance = randint(0,2)
                        
                        if supa_chance == 1:
                            supa_ball_pars.append(supa_ball(screen)) #adding new supa ball in list


                i = 0            
                while i < len(supa_ball_pars):
                    if (event.pos[0] - supa_ball_pars[i][1])**2 + (event.pos[1] - supa_ball_pars[i][2])**2 <= supa_ball_pars[i][3]**2:      #Cheking if we've hitted supa ball number i
                        Misses -= 1
                        #adding Number_of_small_balls in small_balls_pars
                        small_balls_pars.append([small_ball(screen, supa_ball_pars[i][1], supa_ball_pars[i][2], supa_ball_pars[i][3]) for k in range(Number_of_small_balls)] )

                        #making timer for this small balls
                        events.append(pygame.USEREVENT+len(events))
                        pygame.time.set_timer(events[len(events)-1], Small_ball_time, 1)

                        #deleting supa ball
                        circle(screen, BLACK, (supa_ball_pars[i][1], supa_ball_pars[i][2]), supa_ball_pars[i][3])
                        supa_ball_pars.pop(i)
                        i -= 1
                    i += 1
                    
                    #Checking about hitting small balls
                k = 0
                while k < len(small_balls_pars):

                    j = 0   
                    while j < len(small_balls_pars[k]):
                        #Cheking if we've hitted small ball number j, if so, delete this ball
                        if (event.pos[0] - small_balls_pars[k][j][1])**2 + (event.pos[1] - small_balls_pars[k][j][2])**2 <= small_balls_pars[k][j][3]**2:
                            Misses -= 1
                            circle(screen, BLACK, (small_balls_pars[k][j][1], small_balls_pars[k][j][2]), small_balls_pars[k][j][3])
                            small_balls_pars[k].pop(j)
                            j -= 1
                        j += 1

                    # adding points if player hitted all small balls from one supa ball
                    if len(small_balls_pars[k]) == 0:
                        Points += 10
                        small_balls_pars.pop(k)
                        events.pop(k)
                        k -= 1

                    k += 1
            
            i = 0
            #checking timer_events
            while i < len(events):       
                if event.type == events[i]:
                    # erasing each ball associated with this event
                    for j in range(len(small_balls_pars[i])):
                        circle(screen, BLACK, (small_balls_pars[i][j][1], small_balls_pars[i][j][2]), small_balls_pars[i][j][3])
                    # adding points if player hitted all small balls from one supa ball
                    small_balls_pars.pop(i)
                    events.pop(i)
                    i -= 1
                i += 1
                         
        # shifting each ball
        for i in range(Number_of_balls):
            x[i] ,y[i], Vx[i], Vy[i] =  move_ball(screen, color[i], x[i], y[i], r[i], Vx[i], Vy[i], RECT)
                           
        # shifting supa balls and small balls

        #moving each supa ball                       
        for i in range(len(supa_ball_pars)):

            supa_ball_pars[i][1], supa_ball_pars[i][2], supa_ball_pars[i][4], supa_ball_pars[i][5] =  move_ball(screen, supa_ball_pars[i][0], supa_ball_pars[i][1], supa_ball_pars[i][2], supa_ball_pars[i][3], supa_ball_pars[i][4], supa_ball_pars[i][5], RECT)

        #moving each small ball        
        for i in range(len(small_balls_pars)):
            for j in range(len(small_balls_pars[i])):

                small_balls_pars[i][j][1], small_balls_pars[i][j][2], small_balls_pars[i][j][4], small_balls_pars[i][j][5] =  move_ball(screen, COLORS[randint(0, 5)], small_balls_pars[i][j][1], small_balls_pars[i][j][2], small_balls_pars[i][j][3], small_balls_pars[i][j][4], small_balls_pars[i][j][5], RECT)


        #  highlighting play-field
        rect(screen, WHITE, (left_wall, up_wall, right_wall-left_wall, down_wall-up_wall), width = 5)
            
        #Refreshing screen with new points
        
        counter(screen, Points, Misses, counter_top_left_corner_x, counter_top_left_corner_y, counter_font_size)
        pygame.display.update()



    #displaying game_over screen
    game_over(screen, Points)
    #game-over
    while Game_over:
        clock.tick(FPS)

        
        #changing buttons if mouse pos is located on them
        x_mouse, y_mouse = pygame.mouse.get_pos()

        if button_hit(x_mouse, y_mouse, X/2, menu_y_cor, menu_button_width, menu_button_length) == True:
            button('Menu', BLUE, GREEN, X/2, menu_y_cor, menu_button_size)
        elif button_hit(x_mouse, y_mouse, X/2, menu_y_cor - menu_button_length - 5, restart_button_width, restart_button_length) == True:
            button('Restart', BLUE, GREEN, X/2, menu_y_cor - menu_button_length - 5, restart_button_size)

        pygame.display.update()
        button('Restart', GREEN, BLUE, X/2, menu_y_cor - menu_button_length - 5, restart_button_size)
        button('Menu', GREEN, BLUE, X/2, menu_y_cor, menu_button_size)

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Game_over = False
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                #checking if player tapped on menu button
                if button_hit(event.pos[0], event.pos[1], X/2, menu_y_cor, menu_button_width, menu_button_length) == True:
                    Game_over = False
                    Game_play = False
                    Game_start = True
                    # checking if player tapped on restart button
                elif button_hit(event.pos[0], event.pos[1], X/2, menu_y_cor - menu_button_length - 5, restart_button_width, restart_button_length) == True:
                    Game_over = False
                    Game_play = True
                    Game_start = False
                
               
pygame.quit()
