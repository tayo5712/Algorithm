n = int(input())
lst = list(map(int, input().split()))
result = 0
sumV = 0
for num in lst:
    result += sumV * num
    sumV += num
print(result)
