import sys
sys.stdin = open("input_5205.txt", "r")

def partition(L, R):
    p = L
    i = L+1
    j = R
    while i <= j:
        while i <= j and arr[i] <= arr[p]:
            i += 1
        while i <= j and arr[j] >= arr[p]:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[p], arr[j] = arr[j], arr[p]
    return j

def qsort(L, R):
    if L < R:
        p = partition_H(L, R)
        qsort(L, p-1)
        qsort(p+1, R)

for tc in range(1, int(input())+1):
    n = int(input())
    arr = list(map(int, input().split()))
    qsort(0, n-1)

    print(f'#{tc} {arr[n//2]}')