import pygame
import pieces

pygame.init()

white = [255, 255, 255]
black = [0, 0, 0]
grey = [152,152,152]
green = [0, 255, 0]
size = [800, 600]
screen = pygame.display.set_mode(size, pygame.FULLSCREEN, 32)

clock = pygame.time.Clock()

velocity = pieces.randomTrajectory()

def checkCollisions():
	if pieces.y_ball < 5 or pieces.y_ball > 590:
		velocity[1] *= -1
	if pieces.x_ball < pieces.x_player + 10 and pieces.y_ball > pieces.y_player and pieces.y_ball < pieces.y_player+60:
		velocity[0] *= -1
	if pieces.x_ball + 10 > pieces.x_enemy and pieces.y_ball > pieces.y_enemy and pieces.y_ball < pieces.y_enemy+60:
		velocity[0] *= -1
def moveEnemy():
	if pieces.y_enemy  + 30 > pieces.y_ball:
		pieces.y_enemy -= 15
	if pieces.y_enemy + 30 < pieces.y_ball:
		pieces.y_enemy += 15


done = False
while done == False:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True;
		if event.type == pygame.MOUSEMOTION:
			mouse_pos = pygame.mouse.get_pos()
			if mouse_pos[1] > 0 and mouse_pos[1] < 540:
				pieces.y_player = mouse_pos[1]

	screen.fill(grey)
	pieces.drawPlayground(screen, green)
	pieces.x_ball += velocity[0]
	pieces.y_ball += velocity[1]
	if pieces.x_ball < 2 or pieces.x_ball > 798:
		background_image = pygame.image.load("GO.jpg").convert()
		screen.blit(background_image, [0,0])
		done = True
	moveEnemy()
	checkCollisions()
	pieces.drawPlayer(screen, black, pieces.x_player, pieces.y_player)
	pieces.drawBall(screen, black, pieces.x_ball, pieces.y_ball)
	pieces.drawEnemy(screen, black, pieces.x_enemy, pieces.y_enemy)
	clock.tick(20)
	pygame.display.flip()

pygame.time.wait(1000)
pygame.quit()