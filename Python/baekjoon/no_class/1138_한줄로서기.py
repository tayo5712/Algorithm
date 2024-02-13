n = int(input())
line = list(map(int, input().split()))
result = [0] * n

for i in range(n):
    cnt = 0
    left = line[i]
    for j in range(n):
        if result[j] == 0:
            if cnt == left:
                result[j] = i + 1
                cnt = 0
                break
            else:
                cnt += 1
print(*result)
