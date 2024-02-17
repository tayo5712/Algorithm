from itertools import combinations

nums = []
n = int(input())
if n >= 1023:
    print(-1)
else:
    for i in range(1, 11):
        for com in combinations(range(10), i):
            com = sorted(com, reverse=True)
            nums.append(int(''.join(map(str, com))))
    nums.sort()
    print(nums[n])
