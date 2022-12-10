import sys
sys.setrecursionlimit(100001)
input = sys.stdin.readline

def dfs(x):
    global result
    cycle.append(x)
    visited[x] = 1
    if visited[student[x]]:
        if student[x] in cycle: # 사이클 발생 시 cycle 리스트에서 해당 index부터 끝까지 슬라이싱하여 결과에 더함
            result += cycle[cycle.index(student[x]):]
        return
    else:
        dfs(student[x])

T = int(input())
for _ in range(T):
    N = int(input().rstrip())
    student = [0] + list(map(int, input().split()))
    result = []
    visited = [0] * (N+1)
    for i in range(1, N+1):
        if not visited[i]:
            cycle = []
            dfs(i)
    print(N-len(result))