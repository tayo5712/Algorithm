n, k = map(int, input().split())

arr = ["?"] * n
idx = 0
for _ in range(k):
    s, w = input().split()
    idx = ((n - (int(s) % n)) + idx) % n
    if arr[idx] == '?':
        if w in arr:
            print("!")
            break
        arr[idx] = w
    elif arr[idx] == w:
        continue
    else:
        print("!")
        break
else:
    for i in range(n):
        print(arr[(idx + i) % n], end='')
