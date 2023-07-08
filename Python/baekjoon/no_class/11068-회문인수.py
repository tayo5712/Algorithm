def jinsu(a, b):
    tmp = []
    while a > 0:
        tmp.append(a % b)
        a = a // b
    tmp = tmp[::-1]
    return tmp


def fd(s):
    for i in range(len(s) // 2):
        if s[i] != s[-i - 1]:
            return False
    return True


n = int(input())
for _ in range(n):
    flag = False
    n = int(input())
    for i in range(2, 65):
        if fd(jinsu(n, i)):
            flag = fd(jinsu(n, i))
            break
    if flag:
        print(1)
    else:
        print(0)
