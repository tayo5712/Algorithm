n = int(input())
quote = list(map(int, input().split()))
quote.sort()

for k in range(n, -1, -1):
    if k <= quote[-k]:
        print(k)
        break
