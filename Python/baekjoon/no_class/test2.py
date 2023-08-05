from itertools import combinations, permutations
a = ["a", "b", "c", "d"]
c = list(permutations(a, 2))
b = list(combinations(a, 2))
print(b)
print()
print(c)