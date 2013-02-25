import pygame
import random

pygame.init()
black = [0,0,0]
white = [255, 255, 255]
red = [255, 0, 0]
size = [700, 500]

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snowman")

clock = pygame.time.Clock()

#functions
def draw_snowman(screen, x, y):
    pygame.draw.ellipse(screen, white, [35+x,0+y,25,25])
    pygame.draw.ellipse(screen,white,[23+x,20+y,50,50])
    pygame.draw.ellipse(screen,white,[0+x,65+y,100,100])

def draw_stick_figure(screen,x,y):
    # Head
    pygame.draw.ellipse(screen,black,[1+x,y,10,10],0)
  
    # Legs
    pygame.draw.line(screen,black,[5+x,17+y],[10+x,27+y],2)
    pygame.draw.line(screen,black,[5+x,17+y],[x,27+y],2)
  
    # Body
    pygame.draw.line(screen,red,[5+x,17+y],[5+x,7+y],2)
  
    # Arms
    pygame.draw.line(screen,red,[5+x,7+y],[9+x,17+y],2)
    pygame.draw.line(screen,red,[5+x,7+y],[1+x,17+y],2)

def draw_wall():
    pygame.draw.rect(screen, black, [0,0,700, 10], 4)
    pygame.draw.rect(screen, black, [700, 0, 500, 690], 4)
    pygame.draw.rect(screen, black, [10, 0, 10, 500], 4)
    pygame.draw.rect(screen, black, [0, 490, 700, 500], 4)

x_speed = 0
y_speed = 0

x_coord = 10
y_coord = 10

done = False
while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True;
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_speed = -3
            if event.key == pygame.K_RIGHT:
                x_speed = 3
            if event.key == pygame.K_DOWN:
                y_speed = 3
            if event.key == pygame.K_UP:
                y_speed = -3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                x_speed=0
            if event.key == pygame.K_RIGHT:
                x_speed=0
            if event.key == pygame.K_UP:
                y_speed=0
            if event.key == pygame.K_DOWN:
                y_speed=0
    draw_wall()
    pygame.draw.rect(screen, red, [60, 60,50,50])
    x_coord += x_speed
    y_coord += y_speed
    screen.fill(white)
    if x_coord > 690:
        x_coord = 690
    if y_coord > 490:
        y__coord = 490
    if x_coord < 10:
        x_coord = 10
    if y_coord < 10:
        y_coord = 10
    #pos = pygame.mouse.get_pos()
    #x = pos[0]
    #y = pos[1]
    #draw_snowman(screen, 10, 10)
    #draw_snowman(screen,300,10)
    #draw_snowman(screen,10,300)
    draw_stick_figure(screen, x_coord, y_coord)
    pygame.mouse.set_visible(0)
    pygame.display.flip()
    clock.tick(20);

pygame.quit()
