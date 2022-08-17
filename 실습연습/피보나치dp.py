# def fibo(n):
#     table[0] = 0
#     table[1] = 1
#     for i in range(2, n+1):
#         table[i] = table[i-1] + table[i-2]
#
#     return
#
# table = [0] * 101
# fibo(100)
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     print(f'#{tc} {table[N]}')

# 변수 3개 만으로 피보dp 구현 (계속 꺼낼 필요가 없을 때)
a = 0
b = 1
n = 20
for _ in range(n-1):
    a, b = b, a + b
print(b)
