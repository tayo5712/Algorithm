from collections import deque

def divide(arr):



n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
print(arr)
divide(arr)