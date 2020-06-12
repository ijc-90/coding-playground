UP    = "UP"
DOWN  = "DOWN"
LEFT  = "LEFT"
RIGHT = "RIGHT"

def trailingZeros(n):
    zerosFound = 0
    if int(n) <= 0:
        return 0
    while (True):
        if (n%10 == 0):
            zerosFound = zerosFound+1
        else:
            return zerosFound
        n //= 10

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def tryPath(matrix, posX, posY, direction,acummulator, alreadyTurned, maxSoFar):
    M = len(matrix)
    N = len(matrix[0])
    if (posX >= N) or posY >= M or posX < 0 or posY < 0:
        return maxSoFar
    acummulator *= matrix[posY][posX]
    maxSoFar = max(maxSoFar, trailingZeros(acummulator))
    if (direction == UP):
        maxSoFar = max(tryPath(matrix, posX, posY+1,UP, acummulator, alreadyTurned,maxSoFar), maxSoFar)
        if not alreadyTurned:
            maxSoFar = max(tryPath(matrix, posX+1, posY,RIGHT, acummulator,True,maxSoFar), maxSoFar)
            maxSoFar = max(tryPath(matrix, posX-1, posY,LEFT, acummulator,True,maxSoFar), maxSoFar)
    if (direction == DOWN):
        maxSoFar = max(tryPath(matrix, posX, posY - 1, DOWN, acummulator, alreadyTurned, maxSoFar), maxSoFar)
        if not alreadyTurned:
            maxSoFar = max(tryPath(matrix, posX + 1, posY, RIGHT, acummulator, True, maxSoFar), maxSoFar)
            maxSoFar = max(tryPath(matrix, posX - 1, posY, LEFT, acummulator, True, maxSoFar), maxSoFar)
    if (direction == RIGHT):
        maxSoFar = max(tryPath(matrix, posX + 1, posY , RIGHT, acummulator, alreadyTurned, maxSoFar), maxSoFar)
        if not alreadyTurned:
            maxSoFar = max(tryPath(matrix, posX, posY + 1, UP, acummulator, True, maxSoFar), maxSoFar)
            maxSoFar = max(tryPath(matrix, posX, posY - 1, DOWN, acummulator, True, maxSoFar), maxSoFar)
    if (direction == LEFT):
        maxSoFar = max(tryPath(matrix, posX - 1, posY, LEFT, acummulator, alreadyTurned, maxSoFar), maxSoFar)
        if not alreadyTurned:
            maxSoFar = max(tryPath(matrix, posX, posY + 1, UP, acummulator, True, maxSoFar), maxSoFar)
            maxSoFar = max(tryPath(matrix, posX, posY - 1, DOWN, acummulator, True, maxSoFar), maxSoFar)
    return maxSoFar

def solution(A):
    maxFoundSoFar = 0
    M = len(A)
    N = len(A[0])
    #Test All paths
    for x in range(N):
        for y in range(M):
            maxFoundSoFar = max(tryPath(A, x, y, UP, 1, False, maxFoundSoFar), maxFoundSoFar)

            maxFoundSoFar = max(tryPath(A, x, y, DOWN, 1, False, maxFoundSoFar), maxFoundSoFar)

            maxFoundSoFar = max(tryPath(A, x, y, RIGHT, 1, False, maxFoundSoFar), maxFoundSoFar)

            maxFoundSoFar = max(tryPath(A, x, y, LEFT, 1, False, maxFoundSoFar), maxFoundSoFar)
    # write your code in Python 3.6
    return maxFoundSoFar;



#print(trailingZeros(1301329000))

print(solution([[10, 100, 10], [1, 10, 1], [1, 10, 1]]))