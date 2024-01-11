from itertools import combinations_with_replacement
from collections import Counter

max_difference = -1
ryan_log = dict()

def solution(n, info):
    answer = [0] * 11
    def compare_with_apeach(ryan):
        global max_difference
        global ryan_log
        # 어피치 화살 배열이랑 비교
        ryan_score = 0
        apeach_score = 0
        for i in range(11):
            # i를 점수로 생각
            if info[10 - i] < ryan[i]:
                ryan_score += i
            else:
                if info[10 - i]:
                    apeach_score += i
        # 라이언이 우승하면 해당 값 저장
        if ryan_score > apeach_score and ryan_score - apeach_score > max_difference:
            max_difference = ryan_score - apeach_score
            ryan_log = ryan

    # 라이언 n발 화살 쏘기

    for r in combinations_with_replacement([i for i in range(0, 11)], n):
        # 쏜 화살 배열 Counter로 딕셔너리
        compare_with_apeach(Counter(r))

    # 라이언이 우승한 기록이 있으면
    if max_difference != -1:
        for key, value in ryan_log.items():
            answer[10 - key] = value
    else:
        answer = [-1]

    return answer
