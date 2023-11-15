from itertools import permutations
N = int(input())
res = permutations(range(1, N+1), N)
for perm in res:
    for i in perm:
        print(i, end=" ")
    print()