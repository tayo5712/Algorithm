from itertools import permutations

n = int(input())
result = 999999

for per in permutations(list(str(n))):
    num = int(''.join(per))
    if n < num < result:
        result = num
if result == 999999:
    print(0)
else:
    print(result)
