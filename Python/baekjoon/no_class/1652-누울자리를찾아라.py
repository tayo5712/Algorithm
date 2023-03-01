def findRow(list):
    count = 0
    rowCount = 0
    for char in list:
        if char in '.':
            count += 1
        else:
            count = 0
        if count == 2:
            rowCount += 1
    return rowCount

def findCol(list):
    colCount = 0
    for i in range(len(list)):
        count = 0
        for j in range(len(list)):
            if list[j][i] == '.':
                count += 1
            else:
                count = 0
            if count == 2:
                colCount += 1
    return colCount

list = []
rowCount, colCount = 0, 0

for N in range(int(input())):
    list.append(input())
    rowCount += findRow(list[N])
colCount += findCol(list)

print(rowCount, colCount)