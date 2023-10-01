while True:
    n = int(input())
    if n == -1:
        break
    nums = []
    for i in range(1, (n//2)+1):
        if n % i == 0:
            nums.append(i)
    if sum(nums) == n:
        print(f'{n} = 1', end="")
        for k in range(1, len(nums)):
            print(f' + {nums[k]}', end="")
        print()
    else:
        print(f'{n} is NOT perfect.')