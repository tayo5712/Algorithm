n = int(input())
lst = list(int(input()) for _ in range(n))
print(*sorted(lst, reverse=True))