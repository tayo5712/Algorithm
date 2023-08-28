def dfs(n):
    global answer
    if n == N:
        answer = max(answer, int("".join(map(str, nums))))
    else:
        for i in range(L-1):
            for j in range(i+1, L):
                nums[i], nums[j] = nums[j], nums[i]
                check = int(''.join(map(str, nums)))
                if (n, check) not in visited:
                    dfs(n+1)
                    visited[(n, check)] = 1
                nums[i], nums[j] = nums[j], nums[i]

T = int(input())
for tc in range(1, T + 1):
    nums, c = input().split()
    N = int(c)
    nums = list(map(int, nums))
    L = len(nums)
    answer = 0
    visited = {}
    dfs(0)
    print(f'#{tc} {answer}')