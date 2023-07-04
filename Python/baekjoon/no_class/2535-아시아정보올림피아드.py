n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
lst.sort(key=lambda x : x[2], reverse=True)
country = [0] * (n+1)
for i in range(n):
    if sum(country) >= 3:
        break
    if country[lst[i][0]] < 2:
        country[lst[i][0]] += 1
        print(lst[i][0], lst[i][1])