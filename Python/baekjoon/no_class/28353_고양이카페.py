n, k = map(int, input().split())
cats = sorted(list(map(int, input().split())))

st = 0
ed = n-1
answer = 0
while st < ed:
    if cats[st] + cats[ed] <= k:
        answer+=1
        st +=1
        ed -=1
    else:
        ed -=1
print(answer)
