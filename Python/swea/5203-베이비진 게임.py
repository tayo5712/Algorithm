import sys

sys.stdin = open("input_5203.txt", "r")

def play():
    p1 = []
    p2 = []
    for idx in range(0, len(card_arr), 2):
        p1.append(card_arr[idx])    # 플레이어 1 한테 첫 번째 카드 분배
        if len(p1) >= 3:    # 가지고 있는 카드가 3장 이상이라면
            p1.sort()       # 카드 배열 오름차순 정렬
            for i in range(len(p1)-2):  # triplet 확인
                if p1[i] == p1[i+1] and p1[i+1] == p1[i+2]:
                    return 1
            p1_set = sorted(list(set(p1)))  # run 확인위해 set으로 중복제거
            if len(p1_set) >= 3:            # 중복제거한 카드가 3장 이상이면
                for i in range(len(p1_set)-2):  # run 확인
                    if p1_set[i]+1 == p1_set[i+1] and p1_set[i+1]+1 == p1_set[i+2]:
                        return 1

        p2.append(card_arr[idx+1])  # 플레이어 2 한테 두 번째 카드 분배
        if len(p2) >= 3:
            p2.sort()
            for i in range(len(p2)-2):
                if p2[i] == p2[i+1] and p2[i+1] == p2[i+2]:
                    return 2
            p2_set = sorted(list(set(p2)))
            if len(p2_set) >= 3:
                for i in range(len(p2_set)-2):
                    if p2_set[i]+1 == p2_set[i+1] and p2_set[i+1]+1 == p2_set[i+2]:
                        return 2
    return 0

for tc in range(1, int(input())+1):
    card_arr = list(map(int, input().split()))
    result = play()
    print(f'#{tc} {result}')