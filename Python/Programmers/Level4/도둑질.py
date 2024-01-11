def solution(money):
    answer = 0
    
    # 경우의 수
    
    # 1 번 인덱스에서 시작한 경우 -> 마지막 인덱스 사용 불가능
    # 첫 번째 집을 털었을 경우 -> 마지막 집 못텀
    
    # 0 번 인덱스에서 시작한 경우 -> 마지막 인덱스 사용 가능
    # 첫 번째 집을 안털었을 경우 -> 마지막 집 털 수 있음
    
    # 두개의 케이스로 나눠서
    
    # 첫 번째 집을 털었을 경우
    dp1 = [0] * len(money)
    dp1[0] = money[0]
    
    for i in range(len(money) - 1):
        dp1[i] = max(dp1[i-1], dp1[i-2] + money[i])
    
    # 첫 번째 집 안 털었을 경우
    dp2 = [0] * len(money)
    
    for i in range(1, len(money)):
        dp2[i] = max(dp2[i-1], dp2[i-2] + money[i])
    
    return max(dp1[-2], dp2[-1])
