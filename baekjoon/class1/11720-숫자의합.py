n = int(input())
k = list(map(int, input()))
sumV = 0
for i in range(n):
    sumV += k[i]
print(sumV)