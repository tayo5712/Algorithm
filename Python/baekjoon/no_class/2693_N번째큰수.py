tc = int(input())
for _ in range(tc):
    arr = sorted(list(map(int, input().split())))
    print(arr[-3])
