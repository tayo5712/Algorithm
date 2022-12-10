n = int(input())
dice = list(map(int, input().split()))

side1 = 4*(n-1)*(n-2)+(n-2)**2  # 1면만 보이는 개수, 맨 윗줄을 제외하고 모서리를 제외한것
side2 = 4*(n-2)+4*(n-1) # 2면 보이는 개수, 모서리를 제외한 것
side3 = 4   # 3면 보이는 개수, 맨 윗줄의 모서리 4개

if n == 1:
    print(sum(sorted(dice)[:5]))    # 주사위 한개면 제일 큰 값을 뺀 나머지값의 합
else:
    pair = [min(dice[0], dice[5]), min(dice[1], dice[4]), min(dice[2], dice[3])]    # 마주보는 면 중 최소값을 담음
    pair.sort()
    print(pair[0]*side1 + (pair[0]+pair[1])*side2 + (pair[0]+pair[1]+pair[2])*side3)
    # 보여지는 면과 최소값을 곱하고 더해준다.