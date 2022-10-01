import sys
sys.stdin = open("input_1952.txt", "r")

t = int(input())
for tc in range(1, t+1):
    cost = list(map(int, input().split()))
    plan = [0] + list(map(int, input().split()))
    dp = [0] * 13  # 해당 월까지 오는데 최소 값을 담은 배열
    for i in range(1, 13):  # 1월 부터 12월 까지
        tmp = [0, 0, cost[2]*4, cost[3]]    # 무슨 이용권으로 한 것이 최소인지 비교, 3달이용권은 3달이용권을 4번 이용한것이 최대, 1년 이용권은 사용하면 그게 최대
        tmp[0] = dp[i-1] + plan[i] * cost[0]    # 전달 + 해당월을 일일 이용권으로 이용한 경우
        tmp[1] = dp[i-1] + cost[1]  # 전달 + 해당월을 월 이용권으로 이용한 겨우
        if i >= 2:  # 2달 이상인 경우에만 3달 이용권 사용함
            tmp[2] = dp[i-3] + cost[2]  # 3달전 까지의 이용료 합산에 3개월치 이용권을 더한 값을 넣어줌
        dp[i] = min(tmp)    # 해당 월을 이용 하는데 최소값 비교

    print(f'#{tc} {dp[12]}')
