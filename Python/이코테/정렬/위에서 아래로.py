n = int(input())
array = [int(input()) for _ in range(n)]
print(*sorted(array, reverse=True))

# n = int(input())
# lst = list(int(input()) for _ in range(n))
# print(*sorted(lst, reverse=True))