import pygame
import random
pygame.init()
size = (640, 480)
screen = pygame.display.set_mode(size, pygame.RESIZABLE, 32)

def rand():
	x = random.randint(0, size[0])
	y = random.randint(0, size[1])
	return x, y
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
		if event.type == pygame.VIDEORESIZE:
			size = event.size
			screen = pygame.display.set_mode(size, pygame.RESIZABLE,32)
	screen.lock()
	for i in range(10):
		x, y = rand()
		screen.set_at((x, y), (255, 0, 9))
	screen.unlock()
	pygame.display.update()

pygame.quit()