import pygame
import random

# Define some colors
black    = (   0,   0,   0)
white    = ( 255, 255, 255)
green    = (   0, 255,   0)
red      = ( 255,   0,   0)
 
pygame.init()
  
# Set the width and height of the screen [width,height]
size=[700,500]
screen=pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
#Loop until the user clicks the close button.
done=False
 
# Used to manage how fast the screen updates
clock=pygame.time.Clock()
 
rect_change_x = 10;
rect_change_y = 10;
rect_x = 50;
rect_y = 50;
while done==False:
    # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
    # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT
  
  
    # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT
 
    # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT
 
     
 
    # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
    screen.fill(white)
    screen.fill(black);

    pygame.draw.rect(screen, white, [rect_x, rect_y, 50, 50]);
    rect_x += rect_change_x
    rect_y += rect_change_y
    if rect_y > 450 or rect_y < 0:
        rect_change_y = rect_change_y * -1;
    if rect_x >650 or rect_x < 0:
        rect_change_x = rect_change_x * -1;


    for i in range(50):
        x=random.randrange(0,700)
        y=random.randrange(0,500)
        pygame.draw.circle(screen,white,[x,y],2)
    pygame.display.flip()
 
    # Limit to 20 frames per second
    clock.tick(45)
     
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit ()
