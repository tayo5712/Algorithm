for _ in range(int(input())):
    li = []
    n = int(input())
    for __ in range(n):
        li.append(int(input()))
    if n == 1:
        print(1)
    else:
        cnt = 2
        while 1:
            divli = []
            for i in range(len(li)):
                divli.append(li[i] % cnt)
            dd = set(divli)
            dd = list(dd)
            if len(li) == len(dd):
                print(cnt)
                break
            else:
                cnt += 1