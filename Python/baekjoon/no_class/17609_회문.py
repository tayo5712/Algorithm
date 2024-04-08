n = int(input())
for _ in range(n):
    st = input().strip()
    lt, rt = 0, len(st) - 1
    check = 0
    flag = False
    while lt <= rt:
        if st[lt] != st[rt]:
            if not flag and lt <= rt - 1 and st[lt] == st[rt - 1] and st[lt:rt] == st[lt:rt][::-1]:
                rt -= 1

            elif not flag and lt + 1 <= rt and st[lt + 1] == st[rt] and st[lt + 1: rt + 1] == st[lt + 1: rt + 1][::-1]:
                lt += 1

            else:
                check = 2
                break
            flag = True
            check = 1

        lt += 1
        rt -= 1

    print(check)
