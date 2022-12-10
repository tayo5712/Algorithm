from queue import PriorityQueue

def prim():
    value = [2000001] * n
    q = PriorityQueue()
    q.put((0, 0))
    check = [0] * n
    while check.count(1) < n:
        w, curV = q.get()
        if not check[curV]:
            check[curV] = 1
            for i in range(n):
                if not check[i] and 0 < dist[curV][i] < value[i]:
                    value[i] = dist[curV][i]
                    q.put((value[i], i))

    return sum(value[1:])

n = int(input())
x = []
y = []
dist = [[0] * n for _ in range(n)]

for _ in range(n):
    a, b = map(float, input().split())
    x.append(a)
    y.append(b)

for i in range(n):
    for j in range(n):
        dist[i][j] = ((x[i]-x[j])**2 + (y[i]-y[j])**2)**0.5

print(f'{prim():.2f}')

