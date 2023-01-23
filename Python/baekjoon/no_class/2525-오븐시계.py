hour, minute = map(int, input().split())
cook = int(input())

result = minute + cook
if result > 59:
    hour += result // 60
    result %= 60

if hour > 23:
    hour %= 24
print(hour, result)