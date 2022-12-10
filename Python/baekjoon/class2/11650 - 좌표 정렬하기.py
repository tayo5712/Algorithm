import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr2 = sorted(arr)
for i in arr2:
    print(*i)