import sys

input = sys.stdin.readline
n, k = map(int, input().split())

for i in range(k):
    _ = input()
    books = list(map(int, input().split()))
    if books != sorted(books, reverse=True):
        print("No")
        exit(0)
print("Yes")
