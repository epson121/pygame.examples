#basic sprites

import pygame
import random

pygame.init()

black = [0,0,0]
white = [255,255,255]
red = [255,0,0]

screen_width=700
screen_height=400
screen=pygame.display.set_mode([screen_width,screen_height])

clock = pygame.time.Clock()
global score
score = 0
class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
    def reset_pos(self):
        self.rect.y = random.randrange(-100,-10)
        self.rect.x = random.randrange(0,screen_width)
    
    def update(self):
    # Move the block down one pixel
        self.rect.y += 1
        if self.rect.y > screen_height:
             self.reset_pos()
             global score
             score -=1;
block_list = pygame.sprite.RenderPlain()
all_sprites_list = pygame.sprite.RenderPlain()

for i in range(50):
    # This represents a block
    block = Block(black, 20, 15)
 
    # Set a random location for the block
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height)
     
    # Add the block to the list of objects
    block_list.add(block)
    all_sprites_list.add(block)

player = Block(red, 20, 15)
all_sprites_list.add(player)

done = False;

while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True;
    screen.fill(white)
    pos = pygame.mouse.get_pos()

    player.rect.x = pos[0]
    player.rect.y = pos[1]

    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, False)
    for elem in blocks_hit_list:
        score +=len(blocks_hit_list)
        elem.reset_pos()
        print(score)
    all_sprites_list.draw(screen)
    block_list.update()
    
    clock.tick(20)
    pygame.display.flip()
pygame.quit()
