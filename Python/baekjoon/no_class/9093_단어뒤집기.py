n = int(input())
for _ in range(n):
    texts = list(map(str, input().split()))
    for text in texts:
        print(text[::-1], end=" ")
