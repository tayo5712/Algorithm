n, mile = map(int, input().split())
result = []
for _ in range(n):
    p, l = map(int, input().split())
    lst = list(map(int, input().split()))
    lst.sort(reverse=True)

    if p < l:
        result.append(1)
    else:
        result.append(lst[l - 1])
result.sort()
answer = 0
for m in result:
    if m <= mile:
        answer += 1
        mile -= m
    else:
        break
print(answer)
