import numpy as np
from itertools import islice as first

INPUT_FILE_NAME = 'input'
START_DIR       = np.array([-1, 0])
INFECTED_SYMBOL = '#'
CLEAN_SYMBOL    = '.'
NR_BURSTS       = 10000

def file_to_2d_array(filename): return np.asarray(list(map(list, open(filename))))
def turn_left(x):     return np.array([-x[1],  x[0]])
def turn_right(x):    return np.array([ x[1], -x[0]])
def is_infection(a):   return a == INFECTED_SYMBOL
def get_center(grid): return np.asarray(grid.shape) // 2

def virus_trace():
    grid = file_to_2d_array(INPUT_FILE_NAME)
    infected_indices = set(map(tuple, np.asarray(np.where(grid == INFECTED_SYMBOL)).T))
    x = get_center(grid)
    v = START_DIR

    while True:
        tx = tuple(x)
        is_infected = tx in infected_indices
        v = turn_right(v) if is_infected else turn_left(v)
        infected_indices.remove(tx) if is_infected else infected_indices.add(tx)
        yield INFECTED_SYMBOL if is_infected else CLEAN_SYMBOL
        x += v


infect_actions = filter(is_infection, first(virus_trace(), NR_BURSTS))
nr_infects = sum(1 for _ in infect_actions)

print(nr_infects)
