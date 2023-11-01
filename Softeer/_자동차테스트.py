import sys

def bisect(fe, m):
  st = 0
  ed = n - 1
  while st <= ed:
    mid = (st + ed) // 2
    if fe[mid] == m:
      return mid
    elif fe[mid] > m:
      ed = mid - 1
    else:
      st = mid + 1
  return -1

input = sys.stdin.readline
n, q = map(int, input().split())

fuel_efficiency = list(map(int, input().split()))
fuel_efficiency.sort()

for _ in range(q):
  m = int(input())

  idx = bisect(fuel_efficiency, m)
  if idx == -1:
    print(0)
  else:
    print(idx * (n - idx - 1))
