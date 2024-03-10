tc = 1
while True:
    l, p, v = map(int, input().split())
    if l == p == v == 0:
        break
    else:
        a = v // p
        b = v % p
        if l < b:
            b = l
        print(f'Case {tc}: {(l * a) + b}')
        tc += 1
