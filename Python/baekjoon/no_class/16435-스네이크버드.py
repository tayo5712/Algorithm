n, height = map(int, input().split())
fruits = sorted(list(map(int, input().split())))
for fruit in fruits:
    if fruit <= height:
        height += 1
    else:
        break
print(height)