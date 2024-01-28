import sys

input = sys.stdin.readline

n = int(input().rstrip())

print((1 + 2 ** n) * (1 + 2 ** n))
