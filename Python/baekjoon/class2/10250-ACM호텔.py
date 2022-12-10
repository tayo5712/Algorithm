T = int(input())
for _ in range(T):
    h, w, n = map(int, input().split())
    a = []
    for i in range(w):
        a += list(range(101+i, 101 + (100 * (h - 1)) + 1 + i, 100))
    print(a[n-1])

