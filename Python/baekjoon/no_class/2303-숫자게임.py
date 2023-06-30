from itertools import combinations

n = int(input())
myList = [list(map(int, input().split())) for _ in range(n)]
result = []

for i in range(n):
    coms = list(combinations(myList[i], 3))
    max0 = 0;
    for com in coms:
        num = int(str(sum(com))[-1])
        max0 = max(max0, num)
    result.append((max0, i+1))
result.sort(key=lambda x : (x[0], x[1]))
print(result[-1][-1])





