def binary(target, array, st, ed):
    if st > ed:
        return None
    mid = (st + ed) // 2
    if array[mid] == target:
        return mid + 1
    elif array[mid] > target:
        return binary(target, array, st, ed-1)
    else:
        return binary(target, array, st+1, ed)


n = int(input())
arr = list(map(int, input().split()))
m = int(input())
check = list(map(int, input().split()))
arr.sort()
for i in check:
    result = binary(i, arr, 0, n-1)
    if result == None:
        print("no", end=" ")
    else:
        print("yes", end=" ")

"""
5
8 3 7 9 2
3
5 7 9
"""