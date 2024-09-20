alphabet = list(range(97, 123))

for i in range(1, int(input()) + 1):
    pangram = input().lower()
    check = [0] * 26
    for p in pangram:
        if ord(p) in alphabet:
            check[ord(p) - 97] += 1

    if min(check) == 0:
        print(f'Case {i}: Not a pangram')
    elif min(check) == 1:
        print(f'Case {i}: Pangram!')
    elif min(check) == 2:
        print(f'Case {i}: Double pangram!!')
    else:
        print(f'Case {i}: Triple pangram!!!')
