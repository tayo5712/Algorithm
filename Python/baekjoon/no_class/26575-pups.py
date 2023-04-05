n = int(input())
for _ in range(n):
    a, b, c = map(str, input().split())
    if b.startswith("."):
        b = "0" + b
    print(f'${(float(a) * float(b) * float(c)):.2f}')