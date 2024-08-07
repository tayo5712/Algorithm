n = int(input())
cows = {}
answer = 0
for _ in range(n):
    num, pos = map(int, input().split())
    if num in cows:
        if cows[num] != pos:
            answer += 1
            cows[num] = pos
    else:
        cows[num] = pos
print(answer)
