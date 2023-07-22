GroupNum = 1
while True:
    n = int(input())
    if n == 0: break
    print(f'Group {GroupNum}')
    arr = list(list(input().split()) for _ in range(n))
    result = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] == "N":
                result.append(arr[((i+(n-1)) % n) - (j-1)][0] + " was nasty about " + arr[i][0])
    if len(result) != 0:
        for answer in result:
            print(answer)
    else:
        print("Nobody was nasty")
    GroupNum += 1
    print()