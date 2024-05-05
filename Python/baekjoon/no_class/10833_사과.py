n = int(input())
result = 0
for _ in range(n):
	students, apples = map(int, input().split())
	result += apples % students

print(result)
