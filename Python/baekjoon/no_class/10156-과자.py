k, n, m = list(map(int, input().split()))

print(((k*n)-m) if ((k*n)-m) >= 0 else 0)