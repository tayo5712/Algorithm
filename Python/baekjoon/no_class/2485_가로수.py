n = int(input())
trees = []
gaps = []
for i in range(n):
    trees.append(int(input()))
    if i > 0:
        gaps.append(trees[i] - trees[i - 1])

max_gap = 1
for k in range(2, min(gaps) + 1):
    flag = True
    for gap in gaps:
        if gap % k:
            flag = False
            break
    if flag:
        max_gap = max(max_gap, k)

print((trees[-1] - trees[0]) // max_gap + 1 - n)