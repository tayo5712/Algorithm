import sys

sys.stdin = open("input_4698.txt", "r")

N = 10**6
primes = [False, False] + [True] * N # (0, 1 은 소수가 아니여서 먼저 False 처리)
for i in range(2, N+1): # int(N**0.5)+1 사용 가능 : N의 제곱근 까지만 검사
    if primes[i]:
        for j in range(i*2, N+1, i): # 에라토스테네스의 채 (소수의 배수는 소수 x)
            primes[j] = False

T = int(input())
for tc in range(1, T+1):
    D, A, B = map(int, input().split())
    cnt = 0
    for i in range(A, B+1):
        if primes[i] and str(D) in str(i):
            cnt += 1

    print(f"#{tc} {cnt}")