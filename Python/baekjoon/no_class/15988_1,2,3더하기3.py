tc = int((input()))
arr = [1, 2, 4, 7]
for _ in range(tc):
    n = int(input())
    for i in range(len(arr), n):
        arr.append((arr[i - 3] + arr[i - 2] + arr[i - 1]) % 1000000009)
    print(arr[n - 1])
