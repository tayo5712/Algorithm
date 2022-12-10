def fibo(n):
    zero = [1]      # n = 0일 때 0호출 개수 1
    one = [0]       # n = 1일 때 1호출 개수 0
    for i in range(1, n+1):
        zero.append(one[i-1])
        one.append(zero[i-1]+one[i-1])
    print(zero[-1], one[-1])

t = int(input())
for _ in range(t):
    n = int(input())
    fibo(n)

'''    zero    one
f(0)    1       0               # f(n)의 0 호출 개수는 f(n-1)의 1 호출 개수과 같고 
f(1)    0       1               # f(n)의 1 호출 개수는 f(n-1)의 0호출 + 1호출의 개수와 같다.
f(2)    1       1
f(3)    1       2
f(4)    2       3
f(5)    3       5
f(6)    5       8
f(7)    8       13
f(n-1)  x       y
f(n)    y       x+y
'
'
'
'''
