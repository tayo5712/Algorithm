import sys

N, K = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
print(sum(sorted(nums, reverse=True)[:K]) - sum(range(K)))
