import sys
sys.stdin = open("input_5248.txt", "r")

def find_set(k):            # 대표 값 찾기
    while parent[k] != k:
        k = parent[k]
    return k

def union(x, y):            # 두개 대표 값 찾고 합치기
    x = find_set(x)
    y = find_set(y)
    parent[y] = x

for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    parent = list(range(n+1))
    for i in range(m):
        p, c = data[2*i], data[2*i+1]
        union(p, c)

    result = set()
    for i in range(1, n+1):         # 각 값의 대표값을 찾아서 set에 집어넣음, 맨 앞 0은 무시
        result.add(find_set(i))

    print(f'#{tc} {len(result)}')


