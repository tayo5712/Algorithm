n = int(input())
nlist = list(map(int, input().split()))
nlist.sort()
m = int(input())
mlist = list(map(int, input().split()))

def binary(x):
    low, high = 0, n - 1
    while low <= high:
        mid = (low + high) // 2
        if nlist[mid] == x:
            return True
        elif nlist[mid] > x:
            high = mid - 1
        else:
            low = mid + 1
    return None

for m in mlist:
    if binary(m) == True:
        print(1, end=' ')
    else:
        print(0, end=' ')