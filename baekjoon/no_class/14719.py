h, w = map(int, input().split())
buildings = list(map(int, input().split()))

# 총 담기는 빗물의 양을 변수에 저장
water = 0

# 리스트의 각 인덱스를 돌면서 해당 칸에 담기는 빗물의 양을 구한다.
# 0번 인덱스와 마지막 인덱스는 빗물이 담기지 못하니깐 볼 필요가 없다.
for i in range(1, w - 1):
    # 현재 인덱스를 기준으로 양쪽에 가장 높은 건물의 위치를 구한다.
    left_max = max(buildings[:i])
    right_max = max(buildings[i+1:])

    # 현재 인덱스에 빗물이 담길 수 있는 높이
    result = min(left_max, right_max)

    '''
    현재 인덱스에 담기는 빗물의 양을 계산
    현재 인덱스에 빗물이 담길 수 있는 높이가 현재 인덱스 건물보다 높을 경우에만 
    빗물이 담길 수 있기 때문에 if 문으로 조건을 달고 조건에 부합하면 현재 인덱스에 빗물이 담길 수 있는 높이에서
    현재 인덱스 건물의 높이를 빼주면 해당 인덱스에 담기는 빗물의 양이 계산이 된다.
    그 값을 총 담기는 빗물의 양 변수에 더해준다.
    '''
    if result > buildings[i]:
        water += result - buildings[i]

print(water)
