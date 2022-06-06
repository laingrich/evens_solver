#row 0 cell 0 = row 0 cell 0
#row 0 cell 1 = row 1 cell 0
#row 0 cell 2 = row 2 cell 0
#row 0 cell 3 = row 3 cell 0
#row 1 cell 0 = row 0 cell 1
#row 1 cell 1 = row 1 cell 1...

RowTotalGrid = [
    ['O', 'O', 'O', 'O', 16],
    ['O', 'O', 'O', 'O', 18],
    ['O', 'O', 'O', 'O', 18],
    ['E', 'E', 'E', 'E', 20]]

TransposedGrid = [
    [[], [], [], []],
    [[], [], [], []],
    [[], [], [], []],
    [[], [], [], []],
    [[], [], [], []],]

def transpose_grid(grid): # Return a transposed copy of a grid
    for row in range(4):
        for cell in range(5):
            TransposedGrid[cell][row] = grid[row][cell]
    for row in TransposedGrid:
        print(row)

transpose_grid(RowTotalGrid)


