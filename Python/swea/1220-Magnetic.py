for tc in range(1, 11):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    answer = 0
    for i in range(n):
        check = ""
        for j in range(n):
            if arr[j][i]:
                check += str(arr[j][i])
        answer += check.count("12")
    print(f'#{tc} {answer}')