Numbers = list(map(int, input().split()))

sumV = 0
for number in Numbers:
    sumV += number**2

print(sumV%10)