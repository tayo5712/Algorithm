import sys

sys.stdin = open("input_1244.txt", "r")

for tc in range(1, int(input()) + 1):
    arr, swap = input().split()
    n = len(arr)
    swap = int(swap)
    arr_set = {arr}     # 값을 담을 set 만들어 줌 (중복 값 제거), 처음 값은 arr
    for _ in range(swap):   # swap 횟수만큼 진행
        for a in list(arr_set):  # set에 들어있는 값을 한 개 꺼낸다.
            arr_set.remove(a)  # 해당 값은 set에서 지워준다. (swap을 만족하는 값이 아니기 떄문에)
            a = list(a)  # 리스트로 바꿔준다. (서로 자리 바꾸기 위해서)
            for i in range(n - 1):
                for j in range(i + 1, n):
                    a[i], a[j] = a[j], a[i]  # 값에서 위치를 서로 바꿔준다.
                    arr_set.add(tuple(a))  # 바꾼 값을 set에 넣어준다.
                    # -> 최종적으로 set에 들어있는 값은 swap횟수만큼 swap을 한 값뿐이다. (그 전의 값들은 remove로 제거되었다.)
                    a[i], a[j] = a[j], a[i]  # 다시 원래 위치로 되돌린다.

    result = []
    for i in list(arr_set):
        result.append(int(''.join(i)))
    print(f'#{tc} {max(result)}')