def merge(list1, list2):
    global cnt
    merged_list = []
    i = 0
    j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] > list2[j]:
            cnt += len(list1) - i       # 현재 앞쪽 그룹의 남은 데이터 개수 만큼 더해 줌 (이동거리)
            merged_list.append(list2[j])
            j += 1
        else:
            merged_list.append(list1[i])
            i += 1

    if i == len(list1):
        merged_list += list2[j:]
    else:
        merged_list += list1[i:]
    return merged_list

# 병합 정렬
def merge_sort(my_list):
    if len(my_list) == 1:
        return my_list
    mid = len(my_list) // 2
    left_half = merge_sort(my_list[:mid])
    right_half = merge_sort(my_list[mid:])
    sort_list = merge(left_half, right_half)

    return sort_list

n = int(input())
arr = list(map(int, input().split()))
cnt = 0
result = merge_sort(arr)
print(cnt)