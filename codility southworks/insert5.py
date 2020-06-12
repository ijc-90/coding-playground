#escribir funcion que toma un numero, le encaja un 5 y devuelve el mayor numero. sirve para negativos
#999 => 9995
# 0 => 50
# -10 => -105
# -999 => -5999
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(n):
    if (n>=0):
        stringn = str(n)
        max = int('5' + stringn)
        for pos in range(len(stringn)+1):
            posibleMax = int(stringn[:pos] + '5' + stringn[pos:])
            if posibleMax > max:
                max = posibleMax
        return max
    else:
        n = abs(n)
        stringn = str(n)
        min = int('5' + stringn)
        for pos in range(len(stringn)+1):
            posibleMax = int(stringn[:pos] + '5' + stringn[pos:])
            if posibleMax < min:
                min = posibleMax
        return -min

print(solution(-90))
