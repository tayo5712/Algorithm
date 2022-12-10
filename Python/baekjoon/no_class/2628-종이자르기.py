garo, sero = map(int, input().split())
line = int(input())
# 가로 값과, 세로 값을 저장할 리스트를 만들고 0과 가로끝, 세로끝 점을 넣어준다.
row = [0, sero]
col = [0, garo]
for _ in range(line):
    d, num = map(int, input().split())
    if d == 0:
        row.append(num)
    else:
        col.append(num)

# 데이터를 입력받고 오름차순 정렬
row.sort()
col.sort()
maxR = 0
maxC = 0

# 현재 인덱스의 값과 전 인덱스의 값의 차이를 비교하여 가장 큰값을 찾는다.
for i in range(1, len(row)):
    if row[i]-row[i-1] > maxR:
        maxR = row[i]-row[i-1]

for i in range(1, len(col)):
    if col[i]-col[i-1] > maxC:
        maxC = col[i]-col[i-1]

# 가장 긴 가로 * 가장 긴 세로
print((maxR) * (maxC))