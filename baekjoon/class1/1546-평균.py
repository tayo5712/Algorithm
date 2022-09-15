n = int(input())
arr = list(map(int, input().split()))
high = max(arr)
sumV = 0
for i in arr:
    sumV += i/high*100

print(sumV/n)