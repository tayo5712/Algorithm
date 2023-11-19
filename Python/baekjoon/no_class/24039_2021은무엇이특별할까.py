import math

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

n = int(input())
prime = []
num = 2
a = 0
b = 1
while True:
    if is_prime(num):
        prime.append(num)
        if len(prime) >= 2:
            if prime[a] * prime[b] > n:
                print(prime[a] * prime[b])
                break
            a += 1
            b += 1
    if num == 2:
        num += 1
    else:
        num += 2



