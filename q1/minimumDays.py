def checkEveryThingUpdated(rows,columns,grid):
    for r in range(rows):
        for c in range(columns):
            if grid[r][c] == 0:
                return False
    return True


def minimumDays(rows, columns, grid):
    # WRITE YOUR CODE HERE
    sum=0
    for c in range(columns):
        for r in range(rows):
            sum+= grid[r][c]
    if sum==0:
        return -1 #no updated server, will take forever
    iteretionsNeeded = 0
    while True:
        if checkEveryThingUpdated(rows, columns, grid):
            return iteretionsNeeded
        else:
            iteretionsNeeded+=1
            grid = iterateGrid(rows,columns,grid)


def iterateGrid(rows,columns,grid):
    #manually copy grid
    newGrid = [[grid[r][c] for c in range(columns)] for r in range(rows)]
    for c in range(columns):
        for r in range(rows):
            if grid[r][c] == 1:
                newGrid[min(r+1, rows-1)][c] = 1
                newGrid[max(0,r-1)][c] = 1
                newGrid[r][min(c+1,columns-1)] = 1
                newGrid[r][max(0,c-1)] = 1
    return newGrid
