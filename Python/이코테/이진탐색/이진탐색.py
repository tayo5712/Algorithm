
def binary(target, arr, st, ed):
    if st > ed:
        return None;
    mid = (st + ed) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary(target, arr, st, mid-1)
    else:
        return binary(target, arr, mid+1, ed)

n, m = map(int, input().split())
array = list(map(int, input().split()))
result = binary(m, array, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)


# def binary_search(array, target, start, end):
#     while start <= end:
#         middle = (start + end) // 2
#         if array[middle] == target:
#             return middle
#         elif array[middle] > target:
#             end = middle - 1
#         else:
#             start = middle + 1
#     return
#
# n, target = list(map(int, input().split()))
# array = list(map(int, input().split()))
#
# result = binary_search(array, target, 0, n-1)
# if result == None:
#     print('원소가 존재하지 않습니다.')
# else:
#     print(result + 1)


"""
10 7
1 3 5 7 9 11 13 15 17 19

10 7
1 3 6 8 9 10 11 14 17 19
"""