import sys

sys.stdin = open("input_5201.txt", "r")

for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    containner_list = sorted(list(map(int, input().split())))   # 오름차순 정렬
    truck_list = sorted(list(map(int, input().split())))        # 오름차순 정렬
    result = 0
    while truck_list:   # 트럭 리스트가 있으면
        truck = truck_list.pop()    # 트럭 리스트 에서 가장 무거운 트럭이 pop 되어 나온다.

        while containner_list:      # 컨테이너 리스트가 있으면
            containner = containner_list.pop()     # 컨테이너 리스트에서 가장 무거운 컨테이너가 pop되어 나온다.
            if truck >= containner:                # 만약 현재 가장 무거운 트럭이 현재 가장 무거운 컨테이너보다 무겁다면 컨테이너를 실어 나를 수 있다.
                result += containner               # 컨테이너 개수 추가
                break

    print(f'#{tc} {result}')