def getMatrix():
    # return a population
    return [[1,0,1],[1,0,0],[1,0,1]]

def getCell(count,matrix) :
    row = count/3
    column = count%3
    return matrix[row][column]

def getNeighbours(row,column,matrix) :
    # -1 means no neighbour
    neighbour = [-1 for i in range(8)]
    # need to complete
    
