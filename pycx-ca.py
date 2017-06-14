import matplotlib
matplotlib.use("TkAgg")
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sys
import rules
from rules import *
import inspect

fns = inspect.getmembers(rules, inspect.isfunction)
fn_list = [fn[0] for fn in fns]
n = 50
p = 0.5 # probability value of placing 1
time = 0
states = [0,1] # grid states
default_grid = np.random.choice(states, n*n , p=[1-p,p]).reshape(n,n)

def initp(val=p):
    global p
    p = val
    return val

def init():
    global grid, next_grid, time, rule

    ### Prompts
    print('\nEnter one of the following rules to simulate:')
    for fn in fn_list: print('- ' + fn)
    usr_rule = input('\n>>> ')
    bad_input = True
    while bad_input == True:
        if usr_rule in fn_list:
            bad_input = False
            continue
        usr_rule = input('Please enter a valid rule!\n>>> ')
    if usr_rule == 'panic':
        rule = panic
        grid = default_grid
    elif usr_rule == 'conway':
        rule = conway
        print('\nSelect one of the following initial conditions or press enter for default:\n- glider\n')
        initial_grid = input('>>> ')
        if initial_grid == 'glider':
            grid = np.zeros((n,n))
            cx = int(n/2) if n%2 == 0 else int((n-1)/2)
            cy = cx
            grid[cx,cy] = 1
            grid[cx-1,cy+1] = 1
            grid[cx-2,cy-1] = 1
            grid[cx-2,cy] = 1
            grid[cx-2,cy+1] = 1
        else:
            grid = default_grid
    elif usr_rule == 'turing':
        rule = turing
        grid = default_grid
        states = [-1,1]
    else: 
        rule = panic

    next_grid = grid.copy()
    print('\nSimulating ' + usr_rule + '...')

def draw():
    plt.cla()
    plt.pcolor(grid, vmin = 0, vmax = 1, cmap = plt.cm.binary)
    plt.axis('image')
    plt.title('t = ' + str(time))
    plt.show()

def step():
    global grid, next_grid, time, rule
    time += 1
    for x in range(n):
        for y in range(n):
            if not rule(x,y,grid) == None:
                next_grid[x,y] = rule(x,y,grid)
                #print(rule(x,y,grid))
    grid = next_grid.copy()

import pycxsimulator
pycxsimulator.GUI(parameterSetters = [initp]).start(func=[init,draw,step]) 
