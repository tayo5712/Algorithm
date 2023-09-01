n, k = map(int, input().split())
arr = list(input())
hamburgers = 0
for i in range(n):
    if arr[i] == "P":
        for j in range(i - k, i + k + 1):
            if 0 <= j < n:
                if arr[j] == "H":
                    hamburgers += 1
                    arr[j] = "X"
                    break
print(hamburgers)
