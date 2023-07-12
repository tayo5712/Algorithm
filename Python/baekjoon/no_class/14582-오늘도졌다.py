a = list(map(int, input().split()))
b = list(map(int, input().split()))

if sum(b) > sum(a):
    flag = False
    aSum = 0;
    bSum = 0;
    for i in range(9):
        aSum += a[i]
        if aSum > bSum:
            flag = True
            break
        bSum += b[i]
    if flag:
        print("Yes")
    else:
        print("No")
else:
    print("No")

