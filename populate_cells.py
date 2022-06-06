# Populate each row with possible numbers
# Poss Odd Numbers = Total - Poss Even Numbers
# 

oneEven = {
    2: [2], 
    4: [4], 
    6: [6], 
    8: [8]}
twoEvens = {
    6:[2, 4], 
    8:[2, 6], 
    10:[2, 4, 6, 8], 
    12:[4, 8], 
    14:[6, 8]}
threeEvens = {
    12:[2, 4, 6],
    14:[2, 4, 8],
    16:[2, 6, 8],
    18:[4, 6, 8]}
fourEvens = {
    20:[2, 4, 6, 8]}
noOdds = {
    0: [0]}
oneOdd = {
    1:[1],
    3:[3],
    5:[5],
    7:[7],
    9:[9]}
twoOdds = {
    4:[1, 3],
    6:[1, 5],
    8:[1, 3, 5, 7],
    10:[1, 3, 7, 9],
    12:[3, 5, 7, 9],
    14:[5, 9],
    16:[7, 9]}
threeOdds = {
    9:[1,3,5],
    11:[1,3,7], 
    13:[1,3,5,7,9], # this is a combination of [1,3,9] and [1,5,7] - as a workaround.
    15:[1,3,5,7,9], # this is a combination of [1,5,9] and [3,5,7] - as a workaround.
    17:[3,5,9],
    19:[3,7,9],
    21:[5,7,9]}
fourOdds = {
    16:[1, 3, 5, 7],
    18:[1, 3, 5, 9],
    22:[1, 5, 7, 9],
    24:[3, 5, 7, 9]}
        
def numEvensInRow(row): # Returns number of even cells in a row.
    numEvens = 0
    for i in row:
        if i == 'E':
            numEvens = numEvens + 1
    return numEvens

def getTotal(row): # Returns total of a row
    return row[4]
    
def getEvensDict(numEvensInRow): # returns evens dictionary to use.
    if numEvensInRow == 1:
        return oneEven
    elif numEvensInRow == 2:
        return twoEvens
    elif numEvensInRow == 3:
        return threeEvens
    elif numEvensInRow == 4:
        return fourEvens

def getOddsDict(numEvensInRow): # returns odds dictionary to use.
    if numEvensInRow == 0:
        return fourOdds
    elif numEvensInRow == 1:
        return threeOdds
    elif numEvensInRow == 2:
        return twoOdds
    elif numEvensInRow == 3:
        return oneOdd
    elif numEvensInRow == 4:
        return noOdds

def getPossNumbers(row): # returns possible odd and even numbers for a cell in a row
    total = getTotal(row)
    numEvens = numEvensInRow(row)
    evens = getEvensDict(numEvens)
    odds = getOddsDict(numEvens)
    possOdds = []
    possEvens = []
    if numEvens == 4:
        possEvens = [2, 4, 6, 8]
    else:
        for oddNumber in odds:
            if oddNumber < total and numEvens != 0:
                for evenNumber in evens:
                    if oddNumber + evenNumber == total:
                        possOdds.append(odds[oddNumber])
                        possEvens.append(evens[evenNumber])
            elif oddNumber == total:
                possOdds.append(odds[oddNumber])
    return possOdds, possEvens

def populateCells(row): # returns a new row with cells populated with possible numbers
    rowCopy = [' '] * 5
    for i in range(4):
        if row[i] == 'E':
            rowCopy[i] = getPossNumbers(row)[1] # Populate cell with possible even numbers
        if row[i] == 'O':
            rowCopy[i] = getPossNumbers(row)[0] # Populate cell with possible odd numbers
    rowCopy[4] = [getTotal(row)] # Populate last cell of new row with row total
    return removeDuplicates(rowCopy)

def removeDuplicates(row): # Returns a new row with duplicates removed
    newRow = []
    for i in row:
        set1 = {0}
        if isinstance(i[0],list):
            for j in i:
                set1.update(set(j))   
            set1.discard(0)
            newRow.append(list(set1))
        else:    
            newRow.append(i)
    for x in newRow:
        x.sort()
    return newRow

#Row1 = ['O', 'E', 'O', 'E', 24] # test code

#print(populateCells(Row1))