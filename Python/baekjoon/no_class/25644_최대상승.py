n = int(input())
lst = list(map(int, input().split()))
minV = lst[0]
answer = 0
for i in range(1, n):
    if lst[i] < minV:
        minV = lst[i]
    else:
        answer = max(answer, lst[i] - minV)
print(answer)
