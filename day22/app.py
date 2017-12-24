import numpy as np
from itertools import islice as first

INPUT_FILE_NAME = 'input'
START_DIR       = np.array([-1, 0])
INFECTED_SYMBOL = '#'
INFECTED_ACTION = 1
CLEANED_ACTION  = 3
NR_BURSTS       = 10000000

def file_to_2d_array(filename): return np.asarray(list(map(lambda l: list(l.rstrip()), open(filename))))
def turn_right(x):    return np.array([ x[1], -x[0]])
def is_infection(a):  return a == INFECTED_ACTION
def get_center(grid): return np.asarray(grid.shape) // 2

def virus_trace():
    grid = file_to_2d_array(INPUT_FILE_NAME)
    idx_statuses = dict(map(lambda idx: (tuple(idx), 1), np.asarray(np.where(grid == INFECTED_SYMBOL)).T))
    x = get_center(grid)
    v = START_DIR

    while True:
        idx = tuple(x)
        idx_status = idx_statuses.get(idx, CLEANED_ACTION)
        for _ in range(0, idx_status): v = turn_right(v)
        idx_statuses[idx] = (idx_status + 1) % 4
        yield (idx_status + 1) % 4
        x += v


infections = filter(is_infection, first(virus_trace(), NR_BURSTS))
nr_infects = sum(1 for _ in infections)

print(nr_infects)
