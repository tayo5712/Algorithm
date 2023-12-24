n, m = map(int, input().split())
arr = list(map(int, input().split()))
if n == m:
    print("*")
else:
    for num in range(1, n+1):
        if num not in arr:
            print(num, end = " ")