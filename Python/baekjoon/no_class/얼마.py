tc = int(input())
for _ in range(tc):
    s = int(input())
    n = int(input())
    for _ in range(n):
        q, p = map(int, input().split())
        s += q * p
    print(s)
