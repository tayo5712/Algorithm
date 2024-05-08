def isPrime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

t = int(input())

for _ in range(t): 
    n = int(input())
    tmp = n // 2
    
    while tmp > 0:
        if isPrime(tmp):
            if isPrime(n - tmp):
                print(tmp, n-tmp)
                break
        tmp -= 1
