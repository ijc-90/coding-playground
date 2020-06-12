print([0]*30)


def solution(n):
    d = [0] * 30
    l = 0
    while (n > 0):
        d[l] = n % 2
        n //= 2
        l += 1
    print(d)
    print(l)
    print(d[:l])
    for p in range(1, 1 + l):
        ok = True
        for i in range(l - p):
            if d[i] != d[i + p]:
                ok = False
                break
        if ok:
            if p<l:
                return p
            else:
                return -1
    return -1

print(solution(13372))
# n = 17
# print(n)
# n //= 2
# print(n)
# n //= 2
# print(n)
# n //= 2
# print(n)
# n //= 2
# print(n)
# n //= 2
# print(n)
# n //= 2
# print(n)