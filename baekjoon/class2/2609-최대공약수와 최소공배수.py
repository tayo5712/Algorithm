def getGcd(a, b):               # 유클리드 호제법 : a, b의 최대공약수는 a와 a%b의 최대공약수와 같다
    while b != 0:
        a, b = b, a % b
    return a

a, b = map(int, input().split())
gcd = getGcd(a, b)
lcm = a * b // gcd
print(gcd)
print(lcm)

