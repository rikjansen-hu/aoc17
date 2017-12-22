import numpy as np

def left(x):       return np.array([-x[1], x[0]])
def right(x):      return np.array([x[1], -x[0]])
def isSpace(x):    return x == ' '
def isJunction(x): return x == '+'

grid = np.asarray(list(map(list, open("input"))))
cur = '|'
x = np.array([0, np.argmax(grid[0] == cur)])
v = np.array([1, 0])

while not isSpace(cur):
    x += v
    cur = grid[tuple(x)]
    if cur.isalpha(): print(cur, end='')
    if isJunction(cur):
        v = left(v) if not isSpace(grid[tuple(x + left(v))]) else right(v)