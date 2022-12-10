n, m = map(int, input().split())
trees = list(map(int, input().split()))
st = 1
ed = sum(trees)
while st <= ed:
    mid = (st + ed) // 2    # 중간값
    cut = 0                 # 잘린 나무
    for tree in trees:
        if tree > mid:
            cut += tree - mid
    if cut >= m:            # 잘린 나무가 가져가야하는 나무보다 많으면 자르는 높이를 높인다.
        st = mid + 1
    else:                   # 잘린 나무가 가져가야하는 나무보다 적으면 자르는 높이를 낮춘다.
        ed = mid - 1
        mid += 1

print(ed)