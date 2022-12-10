# def factorial(n):
#     if n == 1:
#         return 1
#
#     t = factorial(n-1)
#     return n*t
#
# print(factorial(5))

# def fib(n):
#     if n < 2:
#         return n
#
#     t1 = fib(n-1)
#     t2 = fib(n-2)
#     return t1 + t2
#
# print(fib(5))

# def f(i, N):
#     if i == N:
#         return
#     else:
#         B[i] = A[i]
#         print(B)
#         f(i+1, N)
#
# N = 3
# A = [1, 2, 3]
# B = [0] * N
# f(0, N)

def f(i, N):
    if i == N:
        print(i)
        return
    else:
        print(i)
        f(i+1, N)

N = 1000
A = [1, 2, 3]
B = [0] * N
f(0, N)