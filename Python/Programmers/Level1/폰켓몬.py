def solution(nums):
    n = len(nums)
    m = len(set(nums))
    return min(n // 2, m)