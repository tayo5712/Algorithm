n = int(input())
arr = input()
sumV = 0
for i in range(n):
    sumV += (ord(arr[i])-ord('`')) * (31 ** i)

print(sumV % 1234567891)