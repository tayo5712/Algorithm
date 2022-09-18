t = int(input())
for _ in range(t):
    n = int(input())
    num_list = sorted(list(input() for _ in range(n)))    # 문자열 숫자를 sort 하면 숫자의 순서를 기준으로 정렬
    for i in range(len(num_list)-1):
        if num_list[i+1].startswith(num_list[i]):       # 다음 문자열이 현재 문자열로 시작하는지?
            print('NO')
            break
    else:
        print('YES')
