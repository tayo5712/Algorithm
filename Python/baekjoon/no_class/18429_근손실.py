N, K = map(int, input().split())
kit = list(map(int, input().split()))
chk = [0] * N
result = 0

def f(k, weight):
    global result
    if weight < 0:
        return
    if k >= N:
        result += 1
        return
    for i in range(N):
        if chk[i] == 0:
            chk[i] = 1
            f(k + 1, weight + kit[i] - K)
            chk[i] = 0
f(0, 0)
print(result)