import math
n = int(input())
answer = 0
lst = list(map(int, input().split()))
b, c = map(int, input().split())
for i in range(n):
    a = lst[i]
    answer += math.ceil(((a - b) if a - b > 0 else 0)/ c) + 1
print(answer)
