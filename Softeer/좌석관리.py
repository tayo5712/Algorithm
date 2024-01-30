import sys

input = sys.stdin.readline

n, m, q = map(int, input().split())
eat = [0] * 10001
table = [[0] * (m + 2) for _ in range(n + 2)]

def dist(r, c):
    minV = 1000
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if table[i][j] == 1:
                tmp = (r - i) ** 2 + (c - j) ** 2
                if tmp < minV:
                    minV = tmp
    return minV
def trySeat(id):
    maxV = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if table[i][j] == 0 and table[i-1][j] == 0 and table[i+1][j] == 0 and table[i][j+1] == 0 and table[i][j-1]==0:
                tmp = dist(i, j)
                if tmp > maxV:
                    maxV = tmp
                    eat[id] = [i, j]
    if maxV:
        table[eat[id][0]][eat[id][1]] = 1
        return True
    else:
        return False

for _ in range(q):
    flag, id = input().split()
    id = int(id)
    if flag == "Out":
        if eat[id] == 0:
            print(f'{id} didn\'t eat lunch.')
        elif eat[id] == 1:
            print(f'{id} already left seat.')
        else:
            print(f'{id} leaves from the seat ({eat[id][0]}, {eat[id][1]}).')
            table[eat[id][0]][eat[id][1]] = 0
            eat[id] = 1
    else:
        if eat[id] == 0:
            if trySeat(id):
                print(f'{id} gets the seat ({eat[id][0]}, {eat[id][1]}).')
            else:
                print("There are no more seats.")
        elif eat[id] == 1:
            print(f'{id} already ate lunch.')
        else:
            print(f'{id} already seated.')
