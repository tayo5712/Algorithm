total = int(input())
N = int(input())
real = 0
for _ in range(N):
    price, num = map(int, input().split())
    real += (price * num)

if total == real:
    print("Yes")
else:
    print("No")