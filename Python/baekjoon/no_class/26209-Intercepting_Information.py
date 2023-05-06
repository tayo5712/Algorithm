bits = list(map(int, input().split()))
result = "S"
for bit in bits:
    if bit not in (0, 1):
        result = "F"
print(result)
