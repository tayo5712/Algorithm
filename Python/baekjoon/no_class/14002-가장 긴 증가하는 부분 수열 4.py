n = int(input())
arr = list(map(int, input().split()))
dp = [1] * n
for i in range(1, n):
    for j in range(i):  # i번 전까지 돌면서 arr[j]가 arr[i] 보다 작다면 dp 비교를 한다.
        if arr[i] > arr[j]: # 비교하는 값보다 작은 값이 나오면 계속 dp 체크
            dp[i] = max(dp[i], dp[j]+1)
result = max(dp)
print(result)

str_arr = []
for i in range(n-1, -1, -1):    # 뒤에서 부터 최대 dp값이랑 dp[i]값이 같은지 확인하고 같으면 결과 리스트에 추가한다.
    if dp[i] == result:
        str_arr.append(arr[i])
        result -= 1 # 그리고 최대 dp값을 -1 해준다.
    if result == 0:
        break
str_arr.reverse()   # 마지막에 리스트를 뒤집어주고 출력한다.
print(*str_arr)