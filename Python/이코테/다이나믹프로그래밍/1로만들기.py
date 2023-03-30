"""
26
"""

n = int(input())
dp = [0] * (n+1)
for i in range(2, n+1):
    # 1을 더해 주는 이유는 함수의 호출 횟수를 구해야 하기 때문.
    # 현재 수에서 1을 빼는 경우
    dp[i] = dp[i - 1] + 1
    if i % 2 == 0: # 현재의 수가 2로 나누어 떨어지는 경우
        dp[i] = min(dp[i], dp[i//2] + 1)
    if i % 3 == 0: # 현재의 수가 3로 나누어 떨어지는 경우
        dp[i] = min(dp[i], dp[i//3] + 1)
    if i % 5 == 0: # 현재의 수가 5로 나누어 떨어지는 경우
        dp[i] = min(dp[i], dp[i//5] + 1)
print(dp[n])