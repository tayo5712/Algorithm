n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):  # 수를 비교해서 자기보다 몸무게, 키가 큰 사람의 수를 잰다
    cnt = 1
    for j in range(n):  # 등수는 1 + (자기보다 덩치가 큰사람의 수)
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            cnt += 1
    print(cnt, end=' ')