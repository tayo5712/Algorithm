def find_set(k):    # 부모 찾기
    if parent[k] != k:
        parent[k] = find_set(parent[k])
    return parent[k]

def union(x, y):    # 서로 합치기
    a = find_set(x)
    b = find_set(y)
    print(a, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())
m = int(input())
tree = [list(map(int,  input().split())) for _ in range(n)]
plan = list(map(int, input().split()))
parent = list(range(n+1))

for i in range(n):      # 유니온 연산
    for j in range(n):
        if tree[i][j]:
            union(i+1, j+1)

answer = 'YES'
check = parent[plan[0]]
for i in range(1, m):   # 플랜 속의 번호가 전부 같은 대표를 가르키면 연결되어 있는 것 이다.
    if check == parent[plan[i]]:
        continue
    answer = 'NO'

# check = find_set(plan[0])
# for i in range(1, m):
#     if check == find_set(plan[i]):
#         continue
#     answer = 'NO'

print(answer)
