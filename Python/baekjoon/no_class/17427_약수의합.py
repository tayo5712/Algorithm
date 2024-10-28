n = int(input())

sumV = 0
for i in range(1, n+1):
    sumV += (n//i)*i

print(sumV)
