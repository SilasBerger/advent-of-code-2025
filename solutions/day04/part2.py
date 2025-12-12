import numpy as np

MAX_NEIGHBORS = 3

with open('../inputs/day04.txt') as f:
    grid = np.matrix([[1 if c == '@' else 0 for c in line.strip()] for line in f.readlines()])


def remove(_grid):
    removal_count = 0
    for row in range(rows):
        for col in range(cols):
            if _grid[row, col] == 1:
                accessible = _grid[max(0, row-1):min(row+2, rows), max(0, col-1):min(col+2, cols)].sum() - 1 <= MAX_NEIGHBORS
                if accessible:
                    _grid[row, col] = 0
                    removal_count += 1
    if removal_count == 0:
        return 0
    return removal_count + remove(_grid)


rows, cols = grid.shape
removal_count = remove(grid)
print(removal_count)