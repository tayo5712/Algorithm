t = int(input())
result = []
for _ in range(t):
    input()
    a, b, c, d = map(int, input().split())
    a, b, c = sorted((a, b, c))
    s = a + b + c - d
    tmp = min(s // 3, a)
    a1 = tmp
    s -= tmp
    tmp = min(s // 2, b)
    print(a1*tmp*(s-tmp))