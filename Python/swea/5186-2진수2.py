# 실수를 2진수로 만들려면 소수부분을 *2 했을 때의 정수부분을 쌓아서 만든다. (소수값이 0이 될 때까지)
for tc in range(1, int(input())+1):
    n = float(input())
    result = ''
    for _ in range(12):
        k = n * 2
        if k >= 1:
            result += '1'
            n = k - 1
        else:
            result += '0'
            n = k
        if n.is_integer():
            print(f'#{tc} {result}')
            break
    else:
        print(f'#{tc} overflow')