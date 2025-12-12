import numpy as np

MAX_NEIGHBORS = 3

with open('input.txt') as f:
    grid = np.matrix([[1 if c == '@' else 0 for c in line.strip()] for line in f.readlines()])

accessible_count = 0
rows, cols = grid.shape
for row in range(rows):
    for col in range(cols):
        if grid[row, col] == 1:
            if grid[max(0, row-1):min(row+2, rows), max(0, col-1):min(col+2, cols)].sum() - 1 <= MAX_NEIGHBORS:
                accessible_count += 1
            
print(accessible_count)