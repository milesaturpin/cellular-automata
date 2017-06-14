"""
RULE TEMPLATE

def rule(x,y,grid):
	# calculate total with
	# x: row of current cell
	# y: column of current cell
	# grid: current grid 
	total = 0
	# return value of new state
	# depending on value of total 
	return 1 or 0
"""
import numpy as np

def panic(x,y,grid):
	total = 0 
	for dx in range(-1,2):
		for dy in range(-1,2):
			total += grid[(x+dx) % grid.shape[0], (y+dy) % grid.shape[1]]
	return 1 if total > 4 else 0

def conway(x,y,grid):
	total = 0 
	for dx in range(-1,2):
		for dy in range(-1,2):
			if not (dx == 0 and dy == 0):
				total += grid[(x+dx) % grid.shape[0], (y+dy) % grid.shape[1]]
	if (grid[x,y] == 0 and total == 3): return 1
	if (grid[x,y] == 1 and total < 2): return 0
	if (grid[x,y] == 1 and total > 3): return 0
			
def turing(x,y,grid):
	infl_in = 1
	infl_out = -0.1
	rad = 4
	h = -2
	inner_total, outer_total = 0, 0
	for dx in range(-rad, rad+1):
		for dy in range(-rad, rad+1):
			if abs(dx)+abs(dy) > 2 and (not abs(dx) == abs(dy) == 1):
				outer_total += grid[(x+dx) % grid.shape[0], (y+dy) % grid.shape[1]]
			else:
				inner_total += grid[(x+dx) % grid.shape[0], (y+dy) % grid.shape[1]]
	return 1 if h + infl_in*inner_total + infl_out*outer_total >= 0 else 0

	