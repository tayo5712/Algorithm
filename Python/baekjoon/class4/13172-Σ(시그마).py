def mul(a, b):  # 분할 정복 곱셈
    if b == 1:
        return a % x
    else:
        temp = mul(a, b//2)
        if b % 2 == 1:
            return temp * temp * a % x
        else:
            return temp * temp % x

x = 1000000007
n = int(input())
result = 0
for _ in range(n):
    n, s = map(int, input().split())
    result += s * mul(n, x-2) % x   # 모듈러 계산
    result %= x

print(result)