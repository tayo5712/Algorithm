def solution(n, words):
    answer = []
    before = set([words[0]])

    for i in range(1, len(words)):
        if words[i][0] != words[i - 1][-1] or words[i] in before:
            answer = [i % n + 1, i // n + 1]
            break
        else:
            before.add(words[i])
    else:
        answer = [0, 0]
    return answer