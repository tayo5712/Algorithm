n, m = map(int, input().split())
s = [list(map(int, input().split())) for _ in range(n)]
s.sort(key=lambda x : (x[1], x[2], x[3]), reverse=True)
idx = 0
for i in range(n) :
    if s[i][0] == m:
       idx = i
       break

for i in range(n):
    if s[idx][1:] == s[i][1:]:
        print(i+1)
        break