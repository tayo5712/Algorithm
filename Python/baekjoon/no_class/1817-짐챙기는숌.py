n, m = map(int, input().split())
if n == 0:
    print(0)

else:
    books = list(map(int, input().split()))
    weight = 0
    result = 1
    for i in range(n-1, -1, -1):
        weight += books[i]
        if weight > m:
            result += 1
            weight = books[i]

    print(result)