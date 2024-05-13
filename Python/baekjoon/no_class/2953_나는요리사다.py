winner = 0
sumV = 0
for i in range(1, 6):
    lst = list(map(int, input().split()))
    if sum(lst) > sumV:
        winner = i
        sumV = sum(lst)
print(winner, sumV)
