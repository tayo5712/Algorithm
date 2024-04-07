from collections import deque

n, m = map(int, input().split())
index_arr = list(map(int, input().split()))

# 1 번째 원소 뽑기
# 2 왼쪽으로 한칸 이동 rotate(-1)
# 3 오른쪽으로 한칸 이동 rotate()

data = deque(list(i for i in range(1, n + 1)))
count = 0

for idx in index_arr:
    while True:
        if data[0] == idx:
            data.popleft()
            break
        else:
            if data.index(idx) <= len(data) // 2:
                data.rotate(-1)
            else:
                data.rotate()
            count += 1

print(count)


