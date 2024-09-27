n = int(input())
first = list(map(int, input().split()))
second = list(map(int, input().split()))

result = 0
for i in range(len(first)) :
  result += abs(first[i])

for i in range(len(second)) :
  result += abs(second[i])

print(result)