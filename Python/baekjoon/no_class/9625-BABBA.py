n = int(input())
a = [1, 0]
b = [0, 1]

for i in range(2, n+1):
    numA = a[i-1] + a[i-2]
    numB = b[i-1] + b[i-2]
    a.append(numA)
    b.append(numB)
print(a[n], b[n])
