n = int(input())
num = int(input())
if num == 0:                    # 고장난 버튼이 0개 일때 (이 처리 안해주면 EOFError남)
    broken = set()
else:
    broken = set(map(str, input().split()))

cnt = abs(100-n)            # 처음 100채널에서 +/-만을 이용해 이동할 경우
for i in range(1000001):    # 가고자하는 채널이 500000이고 1,2,3,4,5버튼이 고장났다면 채널 범위를 500000으로 설정했을 시 100채널에서 이동해야하므로 채널범위를 1000000까지로 넓힘
    for j in str(i):
        if j in broken:     # 눌러야 하는 번호가 고장났으면 break
            break

    else:                   # 채널 이동 가능하면 번호를 누른 개수와 +/- 누른 개수를 cnt와 비교하여 최소값을 넣는다
        cnt = min(cnt, len(str(i)) + abs(i - n))

print(cnt)

