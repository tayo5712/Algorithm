def DFS(t):
    global answer
    if len(t) < len(S):
        return
    if t == S:
        answer = 1
        return
    if t[-1] == "A":
        DFS(t[:-1])
    if t[0] == "B":
        DFS(t[1:][::-1])

S = input()
T = input()
answer = 0
DFS(T)
print(answer)

