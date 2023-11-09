a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

n = 0
if a < 0:
    n = -a * c + b * e + d
else:
    n = (b - a) * e

print(n)