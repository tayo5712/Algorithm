def solution(strs, t):
    n = len(t)
    INF = int(1e9)
    dp = [INF] * (n + 1)
    dp[0] = 0
    strs = set(strs)
    
    for i in range(1, n + 1): # i 인덱스 끝나는것 까지 확인하기
        for j in range(1, 6): # 단어 조각의 길이는 5까지
            if i == 2 and j == 2:
                print(t[i-j:i])
            if i - j >= 0 and t[i-j:i] in strs:
                dp[i] = min(dp[i], dp[i-j] + 1)
    print(dp)
    if dp[n] != INF:
        return dp[n]
    else:
        return -1
