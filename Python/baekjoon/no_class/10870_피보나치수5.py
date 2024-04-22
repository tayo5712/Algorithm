n = int(input())
fibo_arr = [0] * (n + 1)
if n == 0:
    print(0)
else:
    fibo_arr[1] = 1

    for i in range(2, n + 1):
        fibo_arr[i] = fibo_arr[i - 1] + fibo_arr[i - 2]
    print(fibo_arr[n])
