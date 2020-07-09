import numpy as np
import pygame
import random
import sys
from pygame.locals import *
import grid_class  


pygame.init()
FPS = 10
fpsClock = pygame.time.Clock()

WINDOWWIDTH = 2000 # size of window's width in pixels 
WINDOWHEIGHT = 1000 # size of windows' height in pixels
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT), 0, 32)
SURF_COLOUR = pygame.Color('black')

myfont = pygame.font.SysFont('Arial', 10)
print('GAME OF LIFE \n - Click into cells to activate them \n - Press Enter to start Game of Life \n - Press ESC to reset')

WIDTH = 25 
HEIGHT = 25
MARGIN = 1

#grid = np.zeros((21,21))
grid = grid_class.grid_gof()
start = False

i = 0
while True: # Main Simulation Loop
	#print('iteration ', i)
	############################
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

		elif event.type==pygame.KEYDOWN: ## START OF GAME
			if event.key == pygame.K_RETURN:
				start = True

			elif event.key == K_ESCAPE:
				start = False
				grid.reset(DISPLAYSURF)

		if start == False:
			if event.type == pygame.MOUSEBUTTONDOWN:
				x, y = pygame.mouse.get_pos() 
				grid.mark_cell(DISPLAYSURF, x, y) 
		
	
	############################
	if start == True:
		grid.update(DISPLAYSURF)
		if grid.check_end() == True:
			print('GAME OVER --- PRESS ESC TO RESTART')
			reset = False
			start = False
	############################
	grid.display_grid(DISPLAYSURF)
	pygame.display.flip()
	###########################
	#pygame.display.update()
	fpsClock.tick(FPS)
	i+=1









