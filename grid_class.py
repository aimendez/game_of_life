import numpy as np
import pygame
import random
import sys
from pygame.locals import *



class grid_gof:

	def __init__(self):

		#initialize grid element = (cell state, active neighbors)
		self.rows = int(1000 / 25)
		self.cols = int(2000 / 25)
		self.grid = []
		for i in range(0, self.rows):
			row = []
			for j in range(0,self.cols):
				row.append( [0,0] )
			self.grid.append(row)	

		#cell geometru
		self.WIDTH = 25
		self.HEIGHT = 25
		self.MARGIN = 1
		self.myfont = pygame.font.SysFont('Arial', 15)

	def grid_coords(self, x, y):
		col = x//self.WIDTH 
		row = y//self.HEIGHT 
		return row, col

	def mark_cell(self, surface, x, y):
		row, col = self.grid_coords(x, y)
		if self.grid[row][col][0] == 0:
				self.grid[row][col][0] = 1
				color = 'green'
		else:
			self.grid[row][col][0] = 0
			color = 'black'

		
		pygame.draw.rect(surface, 
						pygame.Color(color), 
						( self.WIDTH*col+ self.MARGIN , self.HEIGHT*row +  self.MARGIN, 
						  self.WIDTH - 2*self.MARGIN, self.HEIGHT - 2*self.MARGIN),
						)



	def get_neighbors(self,row,col):
		neighborhood_tmp = []

		neighborhood_tmp = [
						[row-1, col-1],		 [row - 1, col],		 [row-1 , col+1],
						[row, col - 1], 							 [row, col + 1],
						[row + 1, col - 1],  [row + 1, col ], 		 [row + 1, col + 1]
						]

		sum_neighborhood = 0
		for row_aux, col_aux in neighborhood_tmp:
			try:
				sum_neighborhood += self.grid[row_aux][col_aux][0]
			except:
				pass

		return sum_neighborhood


	def display_grid(self, surface):
		for row in range(0, len(self.grid)):
			for col in range(0, len(self.grid[0])):
				pygame.draw.rect(surface, 
									pygame.Color('white'), 
									( self.WIDTH*col , self.HEIGHT*row,
									  self.WIDTH, self.HEIGHT),
									  self.MARGIN
									)


	def draw_cell(self, surface, row, col):

		pygame.draw.rect(surface, 
									pygame.Color('white'), 
									( self.WIDTH*col , self.HEIGHT*row,
									  self.WIDTH, self.HEIGHT),
									  self.MARGIN
									)

		neighbours	 = int(self.grid[row][col][1])
		cell_state = int(self.grid[row][col][0])

		if cell_state == 0:
			if neighbours == 3:
				self.grid[row][col][0] = 1
		elif cell_state == 1:
			if neighbours < 2:
				self.grid[row][col][0] = 0
			elif neighbours	> 3:
				self.grid[row][col][0] = 0
			elif neighbours	 == 2 or neighbours	 == 3:
				pass

		if cell_state == 0:
			color = 'black'
			pygame.draw.rect(surface, 
								pygame.Color(color), 
								( self.WIDTH*col + self.MARGIN , self.HEIGHT*row +  self.MARGIN, 
								  self.WIDTH - 2*self.MARGIN, self.HEIGHT - 2*self.MARGIN),
								)
				
		elif cell_state == 1:
				color = 'green'
				pygame.draw.rect(surface, 
								pygame.Color(color), 
								( self.WIDTH*col+ self.MARGIN , self.HEIGHT*row +  self.MARGIN, 
								  self.WIDTH - 2*self.MARGIN, self.HEIGHT - 2*self.MARGIN),
								)

		#text = self.myfont.render(f'{neighbours}', True, pygame.Color('white') , pygame.Color('black'))
		#text_2 = self.myfont.render(f'{int(cell_state)}', True, pygame.Color('white') , pygame.Color('black'))
		#surface.blit(text,(self.WIDTH*col + self.MARGIN + 2, self.HEIGHT*row +  self.MARGIN+ 2) )
		#surface.blit(text_2,(self.WIDTH*col + 10 + self.MARGIN + 2, self.HEIGHT*row +  self.MARGIN+2) )
	
	def check_end(self):
		if self.count_end == 0:
			return True

	def reset(self, surface):
		self.grid = []
		for i in range(0, self.rows):
			row = []
			for j in range(0,self.cols):
				row.append( [0,0] )
			self.grid.append(row)	
		self.update(surface)


	def update_grid(self):
		self.count_end = 0 
		for row in range(0, len(self.grid)):
			for col in range(0, len(self.grid[0])):
				self.grid[row][col][1] = self.get_neighbors(row,col)
				cell_state = self.grid[row][col][0]
				neighbours	 = self.grid[row][col][1]
				self.count_end += cell_state

	def update(self,surface):
		self.update_grid()
		for row in range(0, len(self.grid)):
			for col in range(0, len(self.grid[0])):
				self.draw_cell(surface, row, col)

		

