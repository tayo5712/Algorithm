def solve(n, sq):
    if n in sq: # n이 제곱수 배열안에 있으면 1리턴
        return 1

    for i in range(1, int(n**0.5)+1):
        if (n - i**2) in sq:    # n 에서 어떤 제곱 수를 뺀 값이 제곱 수 이면 2 리턴
            return 2
                                        
    for i in range(1, int(n**0.5)+1):   # n에서 어떤 제곱 수 두 개를 뺀 값이 제곱 수 이면 3 리턴
        for j in range(i, int(n**0.5)+1):
            if (n - i**2 - j**2) in sq:
                return 3
    
    return 4    # 위에 해당없으면 4 리턴

n = int(input())
sq = [i*i for i in range(int(n**0.5)+1)]    # n까지의 제곱 수를 담은 배열
print(solve(n, sq))
print(sq)