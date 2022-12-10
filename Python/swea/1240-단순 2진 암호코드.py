import sys

sys.stdin = open("input_1240.txt", "r")

for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    arr = [input() for _ in range(n)]

    for i in range(n):
        if '1' in arr[i]:
            pos = arr[i][::-1].index('1')       # 오른쪽 부터 1찾기
            break

    code = arr[i][::-1][pos:pos+56][::-1]       # 찾은 1의 인덱스를 기준으로 56개까지가 암호임

    pattern = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']
    # 암호 패턴 순서대로 0~9

    result = []
    for i in range(0, len(code), 7):        # 패턴의 인덱스가 해당 암호
        result.append(pattern.index(code[i:i+7]))

    even_sum = result[1] + result[3] + result[5] + result[7]
    odd_sum = result[0] + result[2] + result[4] + result[6]

    if (odd_sum * 3 + even_sum) % 10 == 0:      # 홀수 더한거 *3 + 짝수 더한거 가 10의 배수이면 암홍
        print(f'#{tc} {odd_sum + even_sum}')
    else:
        print(f'#{tc} 0')


