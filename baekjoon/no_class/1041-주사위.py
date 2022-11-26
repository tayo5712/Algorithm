n = int(input())
a, b, c, d, e, f = map(int, input().split())

i, j, k = a+f, e+b, d+c
maxX = i
if j > maxX:
    maxX = j
elif k > maxX:
    maxX = k

