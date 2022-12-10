import sys
sys.stdin = open("input_5208.txt", "r")

def move(now, cnt):     # 현재 정거장, 충전 횟수
    global min_charge

    if now >= n-1:  # 버스가 마지막 정류장에 도착했을 때
        min_charge = min(min_charge, cnt)   # 최소값 비교
        return

    elif cnt >= min_charge:     # 현재까지 충전횟수가 최소충전횟수보다 크면 리턴
        return

    for battery in range(1, station[now]+1):    # 현재 정거장에 있는 배터리량만큼 1씩 이동하면서 확인 (충전횟수 1증가)
        move(now+battery, cnt+1)

for tc in range(1, int(input())+1):
    arr = list(map(int, input().split()))
    n = arr[0]     # 정류장 개수
    station = arr[1:]      # 각 정류장의 배터리 량
    min_charge = 10000

    move(0, 0)

    print(f'#{tc} {min_charge-1}')