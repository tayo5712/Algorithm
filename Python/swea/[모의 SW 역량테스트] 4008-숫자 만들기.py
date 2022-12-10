import sys
sys.stdin = open("input_4008.txt", "r")

def cal(a, b, oper):
    if oper == 0:
        return a + b
    elif oper == 1:
        return a - b
    elif oper == 2:
        return a * b
    else:
        return int(a / b)   # /로 나누고 int로 변환해서 음수에서 올림이 되도록 한다.

def solve(i, answer):
    global maxV, minV
    if i >= n-1:    # 모든 연산자 카드 다 쓰면
        maxV = max(maxV, answer)
        minV = min(minV, answer)
        return

    for j in range(4):  # 각 연산자로 dfs 해당 연산자 사용하면 1씩 줄여주기
        if operator[j]:
            operator[j] -= 1
            solve(i + 1, cal(answer, numbers[i+1], j))
            operator[j] += 1

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    operator = list(map(int, input().split()))
    maxV = -100000001
    minV = 100000001
    numbers = list(map(int, input().split()))
    solve(0, numbers[0])
    print(f'#{tc} {maxV-minV}')