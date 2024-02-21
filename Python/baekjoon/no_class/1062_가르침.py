def check():
    cnt = 0
    for word in words:
        flag = True
        for c in word:
            if not alpha[ord(c) - ord('a')]:
                flag = False
                break
        if flag:
            cnt += 1
    return cnt

def dfs(start, depth):
    global answer
    if depth == k:
        answer = max(answer, check())
    else:
        for i in range(start, 26):
            if not alpha[i]:
                alpha[i] = True
                dfs(i + 1, depth + 1)
                alpha[i] = False

alpha = [False for _ in range(26)]
n, k = map(int, input().split())
words = [input() for _ in range(n)]
answer = 0
if k < 5:
    print(answer)
elif k == 26:
    print(n)
else:
    for c in ('a', 'n', 't', 'i', 'c'):
        alpha[ord(c) - ord('a')] = True
    dfs(0, 5)
    print(answer)
