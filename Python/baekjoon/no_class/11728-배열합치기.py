n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
result = a + b
print(*sorted(result))