import pygame
import random

pygame.init()

size = [255, 300]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Grids")
clock = pygame.time.Clock()

#colors
white = [255, 255, 255]
black = [0,0,0]
red = [255, 0, 0]

#variables
width = 20
height = 20
margin = 5

#2D array
grid = []
for row in range (10):
	grid.append([])
	for column in range (10):
		grid[row].append(0)

grid_x = 0
grid_y = 0
#functions
def gridPosition(xy):
	grid_x = xy[0]/25
	grid_y = xy[1]/25
	pos = [grid_X, grid_y]
	return pos

#font
font = pygame.font.Font(None, 25)
text = font.render("Save", True, black)
screen.blit(text, [10, 263])

done = False
while done == False:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		if event.type == pygame.MOUSEBUTTONDOWN:
			p = pygame.mouse.get_pos()
			if (p[1] < 250):
				print(str(int(p[0]/25)) + " " + str(int(p[1]/25)))
				grid[int(p[1]/25)][int(p[0]/25)] = 1
			if (p[0] > 5 and p[0] < 60 and p[1] > 260 and p[1] < 285):
				pygame.image.save(screen, "screenshot.jpeg")
	screen.fill(black)

	for column in range (0, 10):
		for row in range (0, 10):
			color = white
			if grid[row][column] == 1:
				color = red
			pygame.draw.rect(screen, color, [column*width + column*margin + margin , row*margin + row*height + margin, width, height], 0)
			pygame.draw.rect(screen, color, [5, 260, 55, 25], 0)
			screen.blit(text, [10, 263])
	pygame.display.flip()
	clock.tick(20)


pygame.quit()