import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr2 = list(sorted(set(arr)))
dict_arr = {}
for i in range(len(arr2)):
    dict_arr[arr2[i]] = i

for i in range(n):
    print(dict_arr[arr[i]], end=' ')
