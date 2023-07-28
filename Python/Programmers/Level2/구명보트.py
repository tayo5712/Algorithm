def solution(people, limit):
    people.sort()
    answer = 0
    lt = 0
    rt = len(people) - 1
    while lt < rt:  # 현재 남아있는 사람중 가장 무거운 사람과 가장 가벼운 사람 비교
        if people[lt] + people[rt] <= limit:
            answer += 1
            lt += 1
            rt -= 1
        else:
            answer += 1
            rt -= 1
    if lt == rt:   # lt와 rt가 같을 경우 무인도에 한명 남아있음
        answer += 1

    return answer