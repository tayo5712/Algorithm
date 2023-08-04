import sys
input = sys.stdin.readline

while True:
    n = input().rstrip('\n')
    if not n:
        break
    else:
        so = dae = num = sp = 0
        for word in n:
            if word.islower():
                so += 1
            elif word.isupper():
                dae += 1
            elif word.isdigit():
                num += 1
            elif word.isspace():
                sp += 1
        print(so, dae, num, sp)