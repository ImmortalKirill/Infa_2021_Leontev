import pygame
from pygame.draw import *
import numpy as np
pygame.init()

def ellipseRotate(screen,color, x, angle, width):
    """x = (koордината центра по х,координата центра по у, длина, ширина)
       angle - угол поворота против часовой стрелки
       
       """
    f1 = [(n,x[3]*np.sqrt(1-n**2/x[2]**2)) for n in np.linspace(-x[2],x[2],100)]
    f2 = [(-n,-x[3]*np.sqrt(1-n**2/x[2]**2)) for n in np.linspace(-x[2],x[2],100)]
    f = f1 + f2
    z = [(f[i][0]*np.cos(angle)-f[i][1]*np.sin(-angle), f[i][1]*np.cos(angle)+f[i][0]*np.sin(-angle)) for i in range(200)]
    polygon(screen, color, [(z[i][0]+x[0],z[i][1]+x[1]) for i in range(200)], width)
    

def home(screen, r, x):
    """r- радиус дома
       х - координаты центра дома"""
    circle(screen, (0,0,0), (x[0],x[1]),r,width = 1)
    circle(screen,'grey',(x[0],x[1]), r-2, width = 0)
    rect(screen, 'white',(x[0]-r,x[1],2*r,r),width = 0)
    line(screen, 'black',((1-np.sqrt(8)/3)*r+x[0]-r, 2/3*r+x[1]-r),((1+np.sqrt(8)/3)*r+x[0]-r, 2/3*r+x[1]-r))
    line(screen, 'black',((1-np.sqrt(5)/3)*r+x[0]-r, 1/3*r+x[1]-r),((1+np.sqrt(5)/3)*r+x[0]-r, 1/3*r+x[1]-r))
    for i in range(3):
        line(screen, 'black', (r/2+r*i/2+x[0]-r, 2/3*r+x[1]-r),(r/2+r*i/2+x[0]-r, 3/3*r+x[1]-r))
    for i in range(2):
        line(screen, 'black', (3*r/4+r*i/2+x[0]-r, 1/3*r+x[1]-r),(3*r/4+r*i/2+x[0]-r, 2/3*r+x[1]-r))
    line(screen, 'black', (r+x[0]-r, 0+x[1]-r), (r+x[0]-r, r/3+x[1]-r))

    
def man(screen, r, x):
    """ r - радиус головы
        х - координаты центра головы"""
    #head
    ellipse(screen,'brown', (x[0]-r, x[1]-r/2*3/2, 2*r, r*3/2), width = 0)

    #body
    ellipse(screen,'red',(x[0]-r-r/32, x[1], 2*r+r/16, 6*r*(5/7)), width  = 0)
    rect(screen, 'white',(x[0]-r-r/32,x[1]+3*r*5/7, 2*r+r/16, 6*r*5/7), width = 0)

        #left leg
    ellipseRotate(screen,'grey', (x[0]-3*r*3/14,x[1]+3*r*6/7, r/6, r/3), 0, 0 )
    ellipseRotate(screen,'grey', (x[0]-3*r*4/14*16/17,x[1]+3*r*6/7*16/15, r/6, r/3), np.pi/2, 0 )

    #right leg
    ellipseRotate(screen,'grey', (x[0]+3*r*3/14,x[1]+3*r*6/7, r/6, r/3), 0, 0 )
    ellipseRotate(screen,'grey', (x[0]+3*r*4/14*16/17,x[1]+3*r*6/7*16/15, r/6, r/3), np.pi/2, 0 )

    #clothes
    rect(screen,'blue',(x[0]-r-r/32,x[1]+3*r*5/7, 2*r+r/16, r/4),width = 0)
    rect(screen, 'blue',(x[0]-r/8,x[1],r/4,3*r*5/7),width = 0)

    #face
    ellipse(screen,'black', (x[0]-r*3/4, x[1]-r/2*3/4*3/2, 6/4*r, 3/4*r*3/2), width = 0)
    ellipse(screen,'grey', (x[0]-r/2*5/4, x[1]-r/4*5/4, 5/4*r, 1/2*r*5/4), width = 0)
    line(screen, 'black', (x[0]+r/8, x[1]-r/16),(x[0]+r/8+r/4,x[1]-r/16-r/8))
    line(screen, 'black', (x[0]-r/8, x[1]-r/16),(x[0]-r/8-r/4,x[1]-r/16-r/8))
    lines(screen, 'black', False, [(x[0]-r/2/(5/2), x[1]+r/4/(5/2)),(x[0] - 4/5*r/2/(5/2),x[1]+4/5*r/4/(5/2)),(x[0]+r/2*15/16/(5/2),x[1]+r/4/(5/2)),(x[0]+r/2*4/3/(5/2),x[1]+r/4/(5/2)+r/16/(5/2))], width = 1)

    #left arm

    ellipseRotate(screen, 'red', (x[0]-15/16*r, x[1]+3*r*5/14, r/2, r/6), (2/3+1/6)*np.pi, 0)
    
    #right arm
    ellipseRotate(screen, 'red', (x[0]+15/16*r, x[1]+3*r*5/14, r/2,r/6), -np.pi/6, 0)

    #stick
    line(screen, 'black', (x[0]-r*18/15,x[1]-r/3),(x[0]-r*18/15, x[1]+3*r*7/8),1)

    
def fish(screen, r, x, angle):

    # body of the fish
    ellipseRotate(screen, (0,0,0), (x[0],x[1], r, r/2), angle, 2) 
    ellipseRotate(screen, (153, 204, 255), (x[0],x[1], r-2, r/2-2), angle, 0)
    f = [(3/4*r,r*np.sqrt(7/64)),(r+r/4,0),(3/4*r,-r*np.sqrt(7/64))]
    polygon(screen, (153, 204, 255), [(f[i][0]*np.cos(angle)-f[i][1]*np.sin(-angle)+x[0], f[i][1]*np.cos(angle)+f[i][0]*np.sin(-angle)+x[1]) for i in range(3)])
    lines(screen,'black',False,  [(f[i][0]*np.cos(angle)-f[i][1]*np.sin(-angle)+x[0], f[i][1]*np.cos(angle)+f[i][0]*np.sin(-angle)+x[1]) for i in range(3)], 2)
    f = [(-7/8*r,r/16*np.sqrt(15)),(-r-r/16,0),(-7/8*r,-r/16*np.sqrt(15))]
    polygon(screen, (153, 204, 255), [(f[i][0]*np.cos(angle)-f[i][1]*np.sin(-angle)+x[0], f[i][1]*np.cos(angle)+f[i][0]*np.sin(-angle)+x[1]) for i in range(3)])
    lines(screen,'black',False,  [(f[i][0]*np.cos(angle)-f[i][1]*np.sin(-angle)+x[0], f[i][1]*np.cos(angle)+f[i][0]*np.sin(-angle)+x[1]) for i in range(3)], 2)
    #eye
    f = (r/2+r/8, -r/4+r/8)
    circle(screen, 'blue',(f[0]*np.cos(angle)-f[1]*np.sin(-angle)+x[0], f[1]*np.cos(angle)+f[0]*np.sin(-angle)+x[1]), r/7, 0,)
    f = (r/2+r/8, -r/4+r/8+r/30)
    circle(screen, 'black',(f[0]*np.cos(angle)-f[1]*np.sin(-angle)+x[0], f[1]*np.cos(angle)+f[0]*np.sin(-angle)+x[1]), r/12, 0,)
    f = (r/2+r/8-r/25, -r/4+r/8-r/25)
    ellipseRotate(screen, 'white', (f[0]*np.cos(angle)-f[1]*np.sin(-angle)+x[0], f[1]*np.cos(angle)+f[0]*np.sin(-angle)+x[1], r/20, r/50), -np.pi/2, width = 0)
    #fins
    
        #back fin
    f = [(-r-r/16, 0),(-r-r/16-r/2, 3/4*r/2),(-r-r/16-r/2+r/8, -3/4*r/2+r/16) ]
    polygon(screen, (153, 204, 255), [(f[i][0]*np.cos(angle)-f[i][1]*np.sin(-angle)+x[0], f[i][1]*np.cos(angle)+f[i][0]*np.sin(-angle)+x[1]) for i in range(3)])
    polygon(screen,'black', [(f[i][0]*np.cos(angle)-f[i][1]*np.sin(-angle)+x[0], f[i][1]*np.cos(angle)+f[i][0]*np.sin(-angle)+x[1]) for i in range(3)], 2)

        #up fin
    f = [(r/2, -np.sqrt(3)/4*r),(r/2, -np.sqrt(3)/4*r-r/8),(r/2-7*r/4/2, -np.sqrt(3)/4*r-r/4*15/13),(0, -r/2)]
    polygon(screen, 'orange', [(f[i][0]*np.cos(angle)-f[i][1]*np.sin(-angle)+x[0], f[i][1]*np.cos(angle)+f[i][0]*np.sin(-angle)+x[1]) for i in range(4)])
    polygon(screen,'black', [(f[i][0]*np.cos(angle)-f[i][1]*np.sin(-angle)+x[0], f[i][1]*np.cos(angle)+f[i][0]*np.sin(-angle)+x[1]) for i in range(4)], 2)    
        #down fin
    f = [(r/2, r/4*np.sqrt(3)),(r/2+r/8, r/4*np.sqrt(3)+r/4),(r/2+r/8-r/2, r/4*np.sqrt(3)+r/4),(0, r/2)]
    polygon(screen, 'orange', [(f[i][0]*np.cos(angle)-f[i][1]*np.sin(-angle)+x[0], f[i][1]*np.cos(angle)+f[i][0]*np.sin(-angle)+x[1]) for i in range(4)])
    polygon(screen,'black', [(f[i][0]*np.cos(angle)-f[i][1]*np.sin(-angle)+x[0], f[i][1]*np.cos(angle)+f[i][0]*np.sin(-angle)+x[1]) for i in range(4)], 2)  

    
def cat(screen, x, r):
    """ x - координаты центра тела кота
        r - radius of the body"""
    #body
    ellipseRotate(screen, 'grey',(x[0],x[1], r, r/4), 0, 0)

    #back legs
    ellipseRotate(screen, 'grey',(x[0]+3/4*r*17/16,x[1]+3/4*r*5/16, r*3/5, r/10), (2/3+1/16)*np.pi,0)
    ellipseRotate(screen, 'grey',(x[0]+r+r/5,x[1]+r/4, r*3/5, r/10), (2/3+1/6)*np.pi,0)

    #tail
    ellipseRotate(screen, 'grey',(x[0]+r+r/5,x[1]-r/4, r*3/5, r/10), 1/6*np.pi,0)

    #front legs
    ellipseRotate(screen, 'grey',(x[0]-3/4*r*17/16,x[1]+3/4*r*5/16, r*3/5, r/10), -(2/3+1/16)*np.pi,0)
    ellipseRotate(screen, 'grey',(x[0]-r/5-r*15/16,x[1]+r/4, r*3/5, r/10), -(2/3+1/6)*np.pi,0)

    #fish
    fish(screen, r/3,(x[0]-r-r/8,x[1]-r/16), 2*np.pi/3+np.pi/6)
    #head
    ellipseRotate(screen,'grey', (x[0]-r,x[1]-r/4-r/8, r/4*3/2, r/4), 0, 0)

    #left eye
    ellipseRotate(screen,'white', (x[0]-r-3/16*r,x[1]-r/4-r/8-r/8, r/15*3/2/5*4*4/5, r/15/5*4), 0, 0)
    circle(screen,'black', (x[0]-r-3/16*r+r/15*3/2/5*4/2,x[1]-r/4-r/8-r/8), r/30,0)
    #right eye
    ellipseRotate(screen,'white', (x[0]-r+3/16*r-r/7,x[1]-r/4-r/8-r/8+r/10, r/15*3/2/5*4*4/5, r/15/5*4), 0, 0)
    circle(screen,'black', (x[0]-r+3/16*r+r/15*3/2/5*4/2-r/7,x[1]-r/4-r/8-r/8+r/10), r/30, 0)

    #left ear
    polygon(screen, 'grey', [(x[0]-r-3/32*r+r/16,x[1]-r/4-r/8-r/4+r/16-r/16),(x[0]-r-3/32*r-r/5+r/16,x[1]-r/4-r/8-r/4+r/16+r/10-r/16-r/32),(x[0]-r-3/32*r-r/5+r/5/10+r/16,x[1]-r/4-r/8-r/4+r/16+r/10-r/6-r/16)], 0)

    #right ear
    polygon(screen, 'grey', [(x[0]-r-(-3/32*r+r/16),x[1]-r/4-r/8-r/4+r/16-r/16),(x[0]-r-(-3/32*r-r/5+r/16),x[1]-r/4-r/8-r/4+r/16+r/10-r/16-r/32),(x[0]-r-r/10-(-3/32*r-r/5+r/5/10+r/16),x[1]-r/4-r/8-r/4+r/16+r/10-r/6-r/16)], 0) 
    #nose
    circle(screen, 'black', (x[0]-r-r/4*3/2/2,x[1]-r/4-r/16), r/50, 0)
    #right tooth
    polygon(screen, (255,0,0), [(x[0]-r*13/10+r/16,x[1]-r*3/8+r/6),(x[0]-r*13/10-r/20+r/16,x[1]-r*3/8+r/6-r/40),(x[0]-r*13/10-r/20+r/16,x[1]-r*3/8+r/6-r/40+r/7)], 0)
    #left tooth
    polygon(screen, (255,0,0), [(x[0]-r*13/10+r/16+r/10,x[1]-r*3/8+r/6+r/20),(x[0]-r*13/10-r/20+r/16+r/10,x[1]-r*3/8+r/6-r/40+r/20),(x[0]-r*13/10-r/20+r/16+r/10,x[1]-r*3/8+r/6-r/40+r/7+r/20)], 0)




 #main programm   
FPS = 30
screen = pygame.display.set_mode((500, 700))
screen.fill((230,230,230))
rect(screen, (255,255,255), (0, 300, 500, 400), 0)

home(screen, 100,(100, 350))
home(screen, 70,(90, 400))
home(screen, 120,(200, 450))

man(screen, 20,(450, 300))
man(screen, 40,(300, 360))
man(screen, 50,(420, 380))
man(screen, 25,(350, 500))

cat(screen, (400,650), 50)
cat(screen, (140,500), 70)
cat(screen, (200,580), 40)
cat(screen, (50,650), 80)


pygame.display.update()
finished = False
clock = pygame.time.Clock()
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
