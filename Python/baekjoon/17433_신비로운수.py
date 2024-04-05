def GCD(x, y):
    while y != 0:
        x, y = y, x % y
    return x

for _ in range(int(input())):
    n = int(input())
    num = list(map(int, input().split()))
    num.sort()

    diff = set()
    for i in range(1, n):
        diff.add(num[i]-num[i-1])
    diff = list(diff)

    if diff == [0]:
        print('INFINITY')
        continue

    x = diff[0]
    for i in range(1, len(diff)):
        tmp = GCD(x, diff[i])
        x = tmp
    print(x)
