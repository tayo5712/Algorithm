def solution(targets):
    answer = 1
    targets.sort(key = lambda x: [x[1], x[0]])
    pre = targets[0]
    for i in range(1, len(targets)):
        if targets[i][0] >= pre[1]:
            answer += 1
            pre = targets[i]

    return answer

# 끝점을 기준으로 정렬