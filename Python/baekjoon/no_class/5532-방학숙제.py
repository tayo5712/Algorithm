import math

L = int(input())
A,B,C,D = [int(input()) for i in range(4)]
print(L-max(math.ceil(A/C), math.ceil(B/D)))