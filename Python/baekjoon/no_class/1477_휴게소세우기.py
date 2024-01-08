N, M, L = map(int, input().split())
arr = [0] + sorted(list(map(int, input().split()))) + [L]

result = 0
st = 1
ed = L - 1
while st <= ed:
    mid = (st + ed) // 2 # 주유소 사이의 최대 거리
    count = 0

    for i in range(N+1):
        if arr[i + 1] - arr[i] > mid:
            count += (arr[i + 1] - arr[i] - 1) // mid
    
    if count <= M:
        ed = mid - 1
        result = mid
    else:
        st = mid + 1

print(result)


