N = int(input())
FirstTurn = [0] * (N + 1)
FirstTurn[1] = 1
FirstTurn[2] = 0
FirstTurn[3] = 1
FirstTurn[4] = 1
for i in range(5, N + 1):
    if FirstTurn[i - 1] == 0 or FirstTurn[i - 3] == 0 or FirstTurn[i - 4] == 0:
        FirstTurn[i] = 1
    else:
        FirstTurn[i] = 0

if FirstTurn[N] == 1:
    print('SK')
else:
    print('CY')
