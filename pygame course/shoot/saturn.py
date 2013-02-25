import pygame
import random

pygame.init()

size = [700, 500]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Saturn")

clock = pygame.time.Clock()
black = [0,0,0]
white = [255, 255, 255]
red = [255, 0, 0]

#images
background_image = pygame.image.load("saturn_family1.jpg").convert()
player_image = pygame.image.load("player.png").convert()
player_image.set_colorkey(white)
pygame.mouse.set_visible(0)

#sounds
click_sound = pygame.mixer.Sound("click.wav")


done = False
while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            click_sound.play()
    player_position = pygame.mouse.get_pos()
    x = player_position[0]
    y = player_position[1]
    
    screen.blit(background_image, [0,0])
    screen.blit(player_image, [x, y])
    #screen.fill(white)
    pygame.display.flip()
    clock.tick(20)
    
pygame.quit()
