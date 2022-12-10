def htob(arr):
    answer = ''
    for i in arr:
        if i.isdecimal():
            intC = int(i)
        else:
            intC = ord(i) - ord('A') + 10

        result = ''
        for i in range(4):
            result = str(intC % 2) + result
            intC //= 2

        answer += result
    return answer


for tc in range(1, int(input()) + 1):
    n, arr = map(str, input().split())
    print(f'#{tc} {htob(arr)}')