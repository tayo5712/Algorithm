n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr2 = sorted(arr, key=lambda x : (x[1], x[0]))             # 튜플로 정렬 우선 순위 정해줌
for i in arr2:
    print(*i)