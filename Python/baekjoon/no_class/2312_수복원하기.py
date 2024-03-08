tc = int(input())

def soin(num):
    nums = {}
    i = 2
    while i <= num:
        if num % i == 0:
            if i not in nums:
                nums[i] = 0
            nums[i] += 1
            num = num // i
        else:
            i += 1
    for key, value in nums.items():
        print(key, value)

for _ in range(tc):
    n = int(input())
    soin(n)
