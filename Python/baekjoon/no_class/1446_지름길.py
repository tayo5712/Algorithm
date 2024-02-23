n, d = map(int, input().split())
road = [list(map(int, input().split())) for _ in range(n)]
dist = [i for i in range(d + 1)]

for i in range(d + 1):
    if i > 0:
        dist[i] = min(dist[i], dist[i-1] + 1)
    for s, e, rd in road:
        if i == s and e <= d and dist[e] > dist[s] + rd:
            dist[e] = dist[s] + rd

print(dist[d])
