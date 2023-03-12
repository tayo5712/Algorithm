n, m, k = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
max1 = lst[-1] # 가장 큰 수
max2 = lst[-2] # 두 번째로 큰 수

result = 0

cycle = m // (k+1)  # 한 사이클 횟수
cycle_remain = m % (k+1)    # 사이클을 돌리고 남은 개수
cycle_sum = (max1 * k) + max2   # 한 사이클의 합

result += (cycle * cycle_sum) + (max1 * cycle_remain)   # (사이클 횟수 * 한 사이클의 합) + (사이클을 돌리고 남은 개수 * 배열 최대값)
print(result)

