def solution(keymap, targets):
    answer = []
    dic = {}
    for word in keymap:
        for i in range(len(word)):
            if word[i] not in dic:
                dic[word[i]] = i + 1
            else:
                if dic[word[i]] > i + 1:
                    dic[word[i]] = i + 1
    for word in targets:
        cnt = 0
        for i in range(len(word)):
            if word[i] in dic:
                cnt += dic[word[i]]
            else:
                cnt = -1
                break
        answer.append(cnt)
    return answer
