import sys
input = sys.stdin.readline

t = int(input()) 

for _ in range(t):
    n, m = map(str, input().split())
    one = 0
    zero = 0
    for i in range(len(m)):
        if n[i] != m[i]:
            if m[i] == '1':
                one += 1
            else:
                zero += 1
    print(max(one, zero))
