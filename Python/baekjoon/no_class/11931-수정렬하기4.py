n = int(input())
nums = []
for _ in range(n):
    num = int(input())
    nums.append(num)
nums.sort(reverse=True)
for num in nums:
    print(num)