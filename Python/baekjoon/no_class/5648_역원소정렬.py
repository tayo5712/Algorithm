n, *arr = input().split()
while len(arr) < int(n):
    arr2 = input().split()
    arr.extend(arr2)
answer = [int(a[::-1]) for a in arr]
answer.sort()
print(*answer, sep='\n')