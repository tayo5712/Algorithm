def solution(s):
    answer = []
    s = s[2:-2]
    s = s.split("},{")
    s.sort(key = lambda x : len(x))
    for i in range(len(s)):
        tmp = s[i].split(",")
        for t in tmp:
            if int(t) not in answer:
                answer.append(int(t))

    return answer

# 처음 양옆 {{ }} 없애기
# "},{"로 split 후 길이 순으로 정렬
# 첫 원소부터 넣음