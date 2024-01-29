from itertools import permutations

n, w, k = map(int, input().split())
rails = list(map(int, input().split()))
answer = int(1e9)

for p in permutations(rails, n):
    weight = 0
    i = 0
    work = 0
    total_weight = 0
    while True:
        if work == k:
            answer = min(answer, total_weight)
            break
        if p[i % n] + weight <= w:
            weight += p[i % n]
        else:
            work += 1
            total_weight += weight
            weight = p[i % n]
        i += 1

print(answer)
