P, N = map(int, input().split())
A = sorted(list(map(int, input().split())))
cnt = 0

for i in range(N) :
    if P < 200 :
        cnt += 1
        P += A[i]
    else :
        break

print(cnt)
