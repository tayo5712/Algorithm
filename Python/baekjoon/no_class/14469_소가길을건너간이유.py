n = int(input())
cows = sorted([list(map(int, input().split())) for _ in range(n)], key = lambda x : x[0])
result = 0
for arrive, check in cows:
    if result < arrive:
        result = arrive + check
    else:
        result += check
print(result)
