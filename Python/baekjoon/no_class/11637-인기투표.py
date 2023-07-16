T = int(input())
answer = ""
for _ in range(T):
    answer = ""
    n = int(input())
    lst = list(int(input()) for _ in range(n))
    maxVal = max(lst)

    if lst.count(maxVal) > 1:
        answer = "no winner"
    else:
        idx = lst.index(maxVal) + 1
        answer = "majority winner " + str(idx) if sum(lst) - maxVal < maxVal else "minority winner " + str(idx)
    print(answer)
