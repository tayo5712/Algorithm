import math
n = int(input())
s = input()
chicken, others = 0, 0
for c in s:
    if c == 'C':
        chicken += 1
    else:
        others += 1
print(math.ceil(chicken / (others + 1)))
