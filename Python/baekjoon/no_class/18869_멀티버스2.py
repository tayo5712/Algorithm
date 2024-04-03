from collections import defaultdict
m, n = map(int, input().split())
universe = defaultdict(int)
result = 0

for _ in range(m):
    planets = list(map(int, input().split()))
    sorted_planets = sorted(list(set(planets)))
    rank = {sorted_planets[i]: i for i in range(len(sorted_planets))}
    universe[tuple([rank[i] for i in planets])] += 1

# n개 중 2개 뽑기
for i in universe.values():
    result += (i * (i - 1)) // 2

print(result)
