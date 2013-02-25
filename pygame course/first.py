import pygame;
pygame.init();

#create lists that represent colors
black = (0, 0, 0);
white = (255, 255, 255);
green = (0, 255, 0);
red = (255, 0, 0);

pi = 3.141592653;

#show screen
size = [700, 500];
screen = pygame.display.set_mode(size);

#show screen title
pygame.display.set_caption("Cool game");

done = False;
clock = pygame.time.Clock();

while done == False:
    for event in pygame.event.get():
        #if user clicked close
        if event.type == pygame.QUIT:
            done = True;
    screen.fill(white);

    pygame.draw.rect(screen, red, (20, 20, 100, 120), 0);
    '''
    for x in range (0, 750, 200):
        for i in range (0, 500, 25):
            #pygame.draw.line(screen, green, [350, 250], [x, i], 1);
            pygame.draw.rect(screen, red, (350, 250, x, i), 3);
    x_offset = 0;
    y_offset = 0;
    while y_offset < 360:
        pygame.draw.rect(screen, red, (350, 250, x, i), 3);
        y_offset=y_offset+10

    pygame.draw.arc(screen,green,[100,100,250,200],  pi/2,     pi, 2)
    pygame.draw.arc(screen,black,[100,100,250,200],     0,   pi/2, 2)
    pygame.draw.arc(screen,red,  [100,100,250,200],3*pi/2,   2*pi, 2)
    pygame.draw.arc(screen,red, [100,100,250,200],    pi, 3*pi/2, 2)
    '''
    #pygame.draw.ellipse(screen, red, [300, 300, 200, 100], 2);

    #pygame.draw.arc(screen, green, [100, 100, 250, 20], pi, pi, 2);
    #pygame.draw.arc(screen,green,[100,100,250,200],  pi/2,     pi, 2)

    pygame.draw.polygon(screen, red, [[10, 10], [10, 50],[50, 50], [50, 10]], 2);
    

    #------Using fonts ---------#
    font = pygame.font.Font(None, 25);

    text = font.render("My text", True, black);

    screen.blit(text, [250, 250]);
    pygame.display.flip()

    #20 fps
    clock.tick(20);

pygame.quit()
