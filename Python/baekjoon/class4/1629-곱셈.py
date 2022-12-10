
def solve(a, b):
    if b == 1:
        return a % c
    else:
        temp = solve(a, b//2)
        if b % 2 == 1:
            return temp * temp * a % c
        else:
            return temp * temp % c

a, b, c = map(int, input().split())
print(solve(a, b))