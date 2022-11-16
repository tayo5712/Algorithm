result = set()
for _ in range(10):
    num = int(input())
    result.add(num % 42)

print(len(result))