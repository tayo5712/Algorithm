def p(t):
    if (t<=1):
        return 1
    else:
        return t *p(t-1)
n,a,b,c = map(int, input().split())

print(p(n)//(p(a)*p(b)*p(c)))
