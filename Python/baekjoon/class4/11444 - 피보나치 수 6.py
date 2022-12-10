import sys
sys.setrecursionlimit(100000)

def fibo(n):
    if not fibo_dict.get(n):
        if n % 2 == 1:  # 홀수 일 때 F[n] = F[(n+1)/2]^2 + F[(n+1)/2-1]^2
            fibo_dict[n] = (fibo((n+1)//2) ** 2 + fibo((n+1)//2-1) ** 2) % 1000000007
        else:   # 짝 수 일때 F[n] = F[n+1] - F[n-1]
            fibo_dict[n] = (fibo(n+1) - fibo(n-1)) % 1000000007
    return fibo_dict[n]

n = int(input())
fibo_dict = {0: 0, 1: 1, 2: 1}
print(fibo(n))