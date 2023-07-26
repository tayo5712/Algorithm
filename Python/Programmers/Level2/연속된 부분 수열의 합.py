def solution(sequence, k):
    lt = 0
    rt = 0
    sumV = sequence[0]
    answer = [0, 999999]
    while 0 <= lt <= rt < len(sequence):
        if sumV == k:
            if (rt - lt) < answer[1] - answer[0]:
                answer = [lt, rt]
            sumV -= sequence[lt]
            lt += 1
        elif sumV < k:
            rt += 1
            if rt < len(sequence):
                sumV += sequence[rt]
        elif sumV > k:
            sumV -= sequence[lt]
            lt += 1

    return answer

# 투 포인터
# 수열의 합이 k 값이면 최소길이임을 판단하여 정답 배열로 넣어준다.