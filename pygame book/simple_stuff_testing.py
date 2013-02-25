import pygame
pygame.init()
screen_size = [640, 480]
#screen = pygame.display.set_mode((640, 480), pygame.FULLSCREEN, 32)
screen = pygame.display.set_mode(screen_size, pygame.RESIZABLE, 32)
counter = 0
print(pygame.display.list_modes())

bgimage = pygame.image.load("allcolors.bmp").convert()
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
		if event.type == pygame.VIDEORESIZE:
			screen_size = event.size
			screen = pygame.display.set_mode(screen_size, pygame.RESIZABLE,32)
	#if counter == 1000:
	#	exit()	
	counter += 1	
	screen.fill(255, 255, 0)
	screen_width , screen_height = screen_size
	'''	
	for y in range (0, screen_height, bgimage.get_height()):
		for x in range (0, screen_width, bgimage.get_width()):
			screen.blit(bgimage, (x, y))
	'''
	pygame.display.update()

pygame.quit()