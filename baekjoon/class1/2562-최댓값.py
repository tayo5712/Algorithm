num = [int(input()) for _ in range(9)]
maxV = 0
for i in range(9):
    if num[i] > maxV:
        maxV = num[i]
        pin = i
print(maxV)
print(pin+1)