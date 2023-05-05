n = int(input())
words = input()
result = 0
for word in words:
    if word in ("a", "e", "i", "o", "u",):
        result += 1
print(result)
