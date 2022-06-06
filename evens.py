# Evens is a puzzle published in the Telegraph newspaper.
# A 4x4 grid is presented with each row and column having a total number
# Each cell in the grid is either an even or an odd number (indicated by shading - shaded cell = even number)
# The user must fill in the grid with numbers 1 - 9 , so that the rows and columns add up to the total.
# Each number may only be used once in a row/column.

# This program asks the user to enter a copy of a puzzle and then provides the solution.

# Create grid and ask user to input a puzzle (even/odd cells, row and column totals). Display grid to user for checking.

import populate_cells

Row1 = [' '] * 5
Row2 = [' '] * 5
Row3 = [' '] * 5
Row4 = [' '] * 5

UserInputGrid = []
RowTotalGrid = [] # populated with possible numbers based on row totals
ColumnTotalGrid = [] # populated with possible numbers based on column totals
ComparedGrid = [] # row and colum grids compared

def getCellOddOrEven(cell): # *** needs to allow user to quit ***
    """Allows user to enter (E)ven or (O)dd for each cell in a row"""
    answer = ' '
    while not (answer == 'E' or answer == 'O'):
        print("Is cell " + str(cell) + " odd or even? O/E")
        answer = input().upper()
    return answer

def getRowTotal(): # *** refactor to row or column total
    """Allows user to enter the total for a row"""
    total = ' '
    while not (isinstance(total, int)):
        print("What is the total of this row") # *** identify each row / column
        userInput = input()
        if userInput.isdigit():
            total = int(userInput)
        else:
            print("Please enter a number")
    return total

def createRow(row):
    """Return a row based on user input"""
    for cell in range(4):
        row[cell] = getCellOddOrEven(cell)
    row[4] = getRowTotal()
    return row

def createGrid():
    """Return grid of 4 rows"""
    grid = [Row1, Row2, Row3, Row4]
    for row in grid:
        createRow(row)

# following can be deleted once column totals are in hand.
#    for cell in range(4):
#        print(grid[4])
#        grid[4][cell] = getRowTotal() # uses getRowTotal to get column totals from user.
    
    for row in grid:
        print(row)

    response = ' '
    while not (response == 'Y' or response == 'N'):
        print("Is this correct? y/n")
        response = input().upper()
    if response == 'N':
        createGrid()
    
    return grid

# Create copy of grid and populate each cell in each row with allowable numbers

def populate_rows(grid):
    """Return a copy of the grid with possible numbers"""
    for i in grid:
        RowTotalGrid.append(populate_cells.populateCells(i))
    for row in RowTotalGrid:
        print(row)
    return RowTotalGrid

populate_rows(createGrid())

# Create another copy of grid and populate each cell in each column with allowable numbers

def transpose_grid(RowTotalGrid): # Return a transposed copy of the grid inputted by the user
    pass

def populate_rows(): # Return a copy of the populated grid
    pass

transpose_grid()
populate_rows()
transpose_grid()

# Cross reference grids and delete numbers not appearing in both

# Present the final grid to the user to solve fully

# v2 - checking duplicated numbers and eliminating across rows and columns to present a fully solved grid




#todo: insert row name before each request for input.




