import math

n = int(input())
x = math.ceil(n/4)
for _ in range(x):
    print("long", end=" ")
print("int")