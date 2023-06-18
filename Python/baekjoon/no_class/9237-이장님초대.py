n = int(input())
trees = list(map(int, input().split()))
trees.sort(reverse=True)

maxDay = trees[0]

for i in range(1, n):
    if trees[i] + i > maxDay:
        maxDay = trees[i] + i

print(maxDay + 2)
