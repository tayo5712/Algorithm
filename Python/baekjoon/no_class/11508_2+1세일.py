n = int(input())
lst = sorted([int(input()) for _ in range(n)], reverse = True)
cost = 0
for i in range(0, len(lst), 3):
    if i + 2 < len(lst):
        cost += lst[i] + lst[i + 1]
    else:
        cost += sum(lst[i::])
print(cost)
