L = int(input())
nums = list(map(int, input().split()))
target = int(input())

nums.append(0)
nums.sort()

answer = 0
if target not in nums:
    for i in range(len(nums)-1):
        if nums[i] < target and target < nums[i+1]:
            answer = (target - nums[i]) * (nums[i+1] - target) - 1
            break

print(answer)
