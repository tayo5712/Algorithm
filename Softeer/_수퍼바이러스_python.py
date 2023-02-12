k, p, n = map(int, input().split())

print((k * pow(p, 10*n, 1000000007)) % 1000000007)