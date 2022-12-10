from heapq import heappush, heappop

def find_set(x):
    if parent[x] != x:
        parent[x] = find_set(parent[x])
    return parent[x]

def union(a, b):
    a = find_set(a)
    b = find_set(b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

line = []
n = int(input())
total = 0

for i in range(n):      # 랜선 총 길이 저장
    arr = input()
    for j in range(n):
        temp = 0
        if 'a' <= arr[j] <= 'z':
            temp = ord(arr[j]) - ord('a') + 1
        if 'A' <= arr[j] <= 'Z':
            temp = ord(arr[j]) - ord('A') + 27
        total += temp
        if i != j and temp: # 자기 자신이 아니고 길이가 0이 아니면 heap에 push
            heappush(line, (temp, i, j))

parent = list(range(n))
line_min = 0
use = 0
while line: # 크루스칼
    w, a, b = heappop(line)
    if find_set(a) != find_set(b):
        union(a, b)
        line_min += w
        use += 1

if use == n-1:
    print(total - line_min)
else:
    print(-1)

