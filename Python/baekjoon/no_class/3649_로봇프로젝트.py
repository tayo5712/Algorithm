while True:
    try:
        hole = int(input()) * int(1e7)
        n = int(input())
        lego = sorted([int(input()) for _ in range(n)])

        left = 0
        right = n - 1
        answer = 0

        while left < right:
            mid = (lego[left] + lego[right])
            if mid == hole:
                answer = ['yes', lego[left], lego[right]]
                break
            elif mid > hole:
                right -= 1
            else:
                left += 1

        if answer:
            print(f'{answer[0]} {answer[1]} {answer[2]}')
        else:
            print("danger")
    except:
        break
