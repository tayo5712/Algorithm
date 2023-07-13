n = int(input())
lst = list(map(int, input().split()))
lst.sort()
for l in lst:
    print(l, end=' ')