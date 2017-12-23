import numpy as np

INPUT_FILE_NAME = 'input'
START_ROW       = 0
START_DIR       = np.array([1, 0])
START_SYMBOL    = '|'
JUNCTION_SYMBOL = '+'
SPACE_SYMBOL    = ' '


def turn_left(x):         return np.array([-x[1],  x[0]])
def turn_right(x):        return np.array([ x[1], -x[0]])
def symbol(grid, x):      return grid[tuple(x)]
def is_inside(grid, x):   return symbol(grid, x) != SPACE_SYMBOL
def is_junction(grid, x): return symbol(grid, x) == JUNCTION_SYMBOL
def get_start_pos(grid):  return np.array([START_ROW, np.argmax(grid[START_ROW] == START_SYMBOL)])


def path():
    grid = np.asarray(list(map(list, open(INPUT_FILE_NAME))))
    x = get_start_pos(grid)
    v = START_DIR

    while is_inside(grid, x):
        x += v
        yield symbol(grid, x)
        if is_junction(grid, x):
            v = turn_left(v) if is_inside(grid, x + turn_left(v)) else turn_right(v)


[print(symbol, end='') for symbol in path() if symbol.isalpha()]
