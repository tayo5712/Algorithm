def solution(answers):
    answer = []
    one = [1, 2, 3, 4, 5]  # 5
    two = [2, 1, 2, 3, 2, 4, 2, 5]  # 8
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]  # 10
    score = [0, 0, 0]
    for i in range(len(answers)):
        if answers[i] == one[i % len(one)]:
            score[0] += 1
        if answers[i] == two[i % len(two)]:
            score[1] += 1
        if answers[i] == three[i % len(three)]:
            score[2] += 1
    maxV = max(score)
    for i in range(3):
        if score[i] == maxV:
            answer.append(i + 1)

    return answer