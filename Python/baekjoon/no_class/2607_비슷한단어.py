# 두 개의 단어가 같은 종류의 문자로 이루어져 있다.
# 같은 문자는 같은 개수 만큼 있다.

n = int(input())
target = list(input())
answer = 0
for _ in range(n-1):
    compare = target[:]
    word = input()
    cnt = 0
    for w in word:
        if w in compare:
            compare.remove(w)
        else:
            cnt += 1
    if cnt <= 1 and len(compare) <= 1:
        answer += 1
print(answer)
