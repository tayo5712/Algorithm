arr, swap = input().split()
n = len(arr)
swap = int(swap)
arr_set = {arr}     # 값을 담을 set 만들어 줌 (중복 값 제거), 처음 값은 arr
for _ in range(swap):       # swap 횟수만큼 진행
    for a in list(arr_set):     # set에 들어있는 값을 한 개 꺼낸다.
        arr_set.remove(a)       # 해당 값은 set에서 지워준다. (swap을 만족하는 값이 아니기 떄문에)
        a = list(a)             # 리스트로 바꿔준다. (서로 자리 바꾸기 위해서)
        for i in range(n - 1):
            for j in range(i + 1, n):
                a[i], a[j] = a[j], a[i]    # 값에서 위치를 서로 바꿔준다.
                k = tuple(a)               # 바꾼 값을 튜플 형태로 만들어준다. (set에 넣기 위해서)
                if int(k[0]):              # 만약 바꾼 값의 앞자리가 0이 아니라면
                    arr_set.add(tuple(a))  # 바꾼 값을 set에 넣어준다.
                    # -> 최종적으로 set에 들어있는 값은 swap횟수만큼 swap을 한 값뿐이다. (그 전의 값들은 remove로 제거되었다.)
                a[i], a[j] = a[j], a[i]    # 다시 원래 위치로 되돌린다.

if arr_set:     # set에 값이 들어있으면
    result = []
    for i in list(arr_set):     # 그 안에서 가장 높은 값을 출력한다.
        result.append(int(''.join(i)))
    print(max(result))

else:   # set에 값이 들어 있지 않는 경우는 값의 시작 숫자가 0일 경우이거나 한자리 숫자 일 때 이다.
    print(-1)