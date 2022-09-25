n = int(input())

def isPrime(num):
    for i in range(3, int(num**(1/2)+1)):   # 소수 확인은 제곱근 까지만 확인하면 됨
        if num % i == 0:
            return False
    return True

def dfs(num):
    if len(str(num)) == n:
        print(num)
    else:
        for i in range(1, 10, 2):   # 짝수는 볼 필요 없음
            if isPrime(num * 10 + i):   # i를 뒤에 붙인 수가 홀수이면서 소수 일 때
                dfs(num * 10 + i)       # 소수이면 자릿수 늘림

dfs(2)
dfs(3)
dfs(5)
dfs(7)

