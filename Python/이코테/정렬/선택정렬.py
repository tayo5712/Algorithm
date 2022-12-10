arr = [7, 6, 3, 1, 8, 4, 9, 2, 5]
for i in range(len(arr)-1):
    min_index = i
    for j in range(i+1, len(arr)):
        if arr[min_index] > arr[j]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]

print(arr)