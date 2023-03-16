input_data = input()
column = ord(input_data[0]) - ord('a') + 1
row = int(input_data[1])

cnt = 0
for dr, dc in ((1, 2), (-1, 2), (2, -1), (2, 1), (-2, -1), (-2, 1), (1, -2), (-1, -2)):
    nr, nc = row + dr, column + dc
    if 1 <= nr <= 8 and 1 <= nc <= 8:
        cnt += 1
print(cnt)