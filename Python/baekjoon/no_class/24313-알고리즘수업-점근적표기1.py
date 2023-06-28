a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

flag = True
for n in range(n0, 101):
    if a1 * n + a0 > c * n:
        flag = False

if flag:
    print(1)
else:
    print(0)

