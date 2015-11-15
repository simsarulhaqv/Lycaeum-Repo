SIZE = 3;

def getMatrix():
    # return a population of size SIZE
    return [[1,0,1],[1,0,0],[1,0,1]]

def getCell(number,matrix) :
    row = number/SIZE
    column = number%SIZE
    return matrix[row][column]

def getNeighbours(number,matrix) :
    row = number/SIZE
    column = number%SIZE
    # -1 means no neighbour
    count = 0
    neighbour = [-1 for i in range(8)]
    neighbour[count] = (((row-1)*SIZE)%SIZE) + ((column-1)%SIZE)
    count = count + 1
    neighbour[count] = (((row-1)*SIZE)%SIZE) + ((column)%SIZE)
    count = count + 1]
    neighbour[count] = (((row-1)*SIZE)%SIZE) + ((column+1)%SIZE)
    count = count + 1
    neighbour[count] = (((row+1)*SIZE)%SIZE) + ((column+1)%SIZE)
    count = count + 1
    neighbour[count] = (((row+1)*SIZE)%SIZE) + ((column)%SIZE)
    count = count + 1
    neighbour[count] = (((row+1)*SIZE)%SIZE) + ((column+1)%SIZE)
    count = count + 1
    neighbour[count] = (((row)*SIZE)%SIZE) + ((column-1)%SIZE)
    count = count + 1
    neighbour[count] = (((row)*SIZE)%SIZE) + ((column+1)%SIZE)
    return neighbour
    
