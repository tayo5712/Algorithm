A, B = input().split()
min_value = 50

for i in range(len(B) - len(A) + 1):
    cnt = 0
    for j in range(len(A)):
        if A[j] != B[i + j]:
            cnt += 1
    min_value = min(min_value, cnt)

print(min_value)