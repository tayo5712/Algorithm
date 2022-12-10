# 2740-행렬곱셈
# 1629-곱셈
# 두개 풀면 접근 쉬움

def multi(A, B):
    new_arr = [[0] * N for _ in range(N)]
    for i in range(N):  # 행렬의 곱
        for j in range(N):
            for k in range(N):
                new_arr[i][j] += A[i][k] * B[k][j]
            new_arr[i][j] %= 1000

    return new_arr

def divide(arr, b):
    if b == 1:  # 제곱해야하는 수가 1이면 mod 하고 그냥 출력
        for i in range(N):
            for j in range(N):
                arr[i][j] %= 1000
        return arr
    else:
        temp = divide(arr, b // 2)  # 제곱해야하는 수를 절반으로 쪼갬
        if b % 2 == 1:  # 제곱해야 하는 수가 홀 수 이면 temp * temp * initial
            return multi(multi(temp, temp), initial)
        else:   # 짝 수 이면 temp * temp
            return multi(temp, temp)

N, B = map(int, input().split())
initial = [list(map(int, input().split())) for _ in range(N)]   # 첫 행렬

result = divide(initial, B)

for i in range(N):
    for j in range(N):
        print(result[i][j], end = ' ')
    print()