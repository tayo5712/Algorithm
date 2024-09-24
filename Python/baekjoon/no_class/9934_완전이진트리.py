n = int(input())
lst = list(map(int, input().split()))
tree = [[] for _ in range(n)]

def makeTree(arr, depth):
    mid = len(arr) // 2
    tree[depth].append(arr[mid])
    if len(arr) == 1:
        return
    makeTree(arr[:mid], depth + 1)
    makeTree(arr[mid + 1:], depth + 1)

makeTree(lst, 0)
for i in range(n):
    print(*tree[i])
