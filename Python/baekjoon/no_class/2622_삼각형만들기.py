n = int(input())
cnt = 0
for x in range((n+1)//3, (n+1)//2):
    cnt += x - (n-x+1)//2 + 1
print(cnt)