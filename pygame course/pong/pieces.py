#pieces
import pygame
import random

black = [0, 0, 0]

x_player = 5
y_player = 300
def drawPlayer(place, color, x, y):
	pygame.draw.rect(place, color, [x, y, 10, 60], 0)


x_ball = 400
y_ball = 300
def drawBall(place, color, x, y):
	if y > 0 or y < 590:
		pygame.draw.rect(place, color, [x, y, 10, 10]) 

x_enemy = 785
y_enemy = 300
def drawEnemy(place, color, x, y):
	pygame.draw.rect(place, color, [x, y, 10, 60], 0)

def drawPlayground(place, color):
	pygame.draw.rect(place, color, [0, 0, 800, 5], 0)
	pygame.draw.rect(place, color, [795, 0, 795, 600], 0)
	pygame.draw.rect(place, color, [0, 0, 5, 600], 0)
	pygame.draw.rect(place, color, [0, 600, 800, -5], 0)
	pygame.draw.rect(place, color, [397, 0, 5, 600], 0)
	pygame.draw.circle(place, color, [400, 300], 80, 5)
def randomTrajectory():
	trajectory = []
	trajectory.append(random.randrange(10,15))
	trajectory.append(random.randrange(10, 15))
	return trajectory

def randomVelocity():
	return random.uniform(0.5, 1.2)