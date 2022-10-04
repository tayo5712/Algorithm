import sys
input = sys.stdin.readline

M = int(input())
S = set()

for _ in range(M):
    order = input().split()

    if len(order) == 1:
        order = order[0]
    else:
        order, num = order[0], order[1]

    if order == "add":
        S.add(int(num))

    elif order == "remove":
        if int(num) in S:
            S.remove(int(num))

    elif order == "check":
        if int(num) in S:
            print(1)
        else:
            print(0)

    elif order == "toggle":
        if int(num) in S:
            S.remove(int(num))
        else:
            S.add(int(num))

    elif order == "all":
        S = {1,2,3,4,5,6,7,8,9,10,
             11,12,13,14,15,16,17,18,19,20}

    else:
        S.clear()