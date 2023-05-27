n, m = map(int, input().split())
boong = [input() for _ in range(n)]
for i in range(n):
    print(boong[i][::-1])
