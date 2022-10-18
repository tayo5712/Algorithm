for tc in range(1, int(input())+1):
    n = int(input())
    tree = list(map(int, input().split()))
    answer = 0
    max_tree = 0
    for i in range(n):
        max_tree = max(max_tree, tree[i])   # 제일 높은 나무의 높이 찾기

    odd = 0     # 홀수 개수
    even = 0    # 짝수 개수

    for i in range(n):  # max_tree - tree[i] 는 그 나무가 자라야하는 높이
        odd += (max_tree - tree[i]) % 2     # 나무가 자라야하는 높이에서 2로 나눈 나머지는 홀수 날짜의 개수
        even += (max_tree - tree[i]) // 2   # 나무가 자라야하는 높이에서 2로 나눈 몫은 짝수 날짜의 개수

    # 짝수 날짜와 홀수 날짜의 균형이 맞아야 물을 안주는 날이 적으므로 최소날짜가 나온다.
    average = max(even - odd, 0) // 3   # 짝수날이 홀수날보다 3개이상 많으면 짝수날을 홀수날에 한개 준다
    odd += average * 2  # 짝수 날은 물의 양이 2이므로 짝수 꺼를 가져갈 떄 *2를 해서 가져가야한다.
    even -= average     # 홀수 날이 가져간 날짜만큼 뺴준다.

    cycle = min(odd, even)  # 1과 2의 쌍(홀수날 한개 짝수날 한개)으로 3의 배수 (1->2)를 만든 다면 2일 연속 성장을 만들 수 있으므로 짝수 날, 홀수 날 두값의 최소값을 연속 성장 기간으로 본다.
    '''그리고 홀수 날이 남아있다면 홀수 날은 (1->0->1)식으로 홀수 날에만 더해줘야 하므로 ((odd-cycle)*2-1)로 표시 가능하다.
    남는 odd가 0일 수도 있으므로 max를 통해 0과 비교한다.
    그리고 짝수 날이 남아있는 경우는 짝수 날이 2일 남았을 때랑 1일 남았을 때가 있다.
    짝수 날이 2일 남았다면 (1->2->1)식으로 3일이 소요된다. (even-cycle)//2 * 3
    짝수 날이 1일 남았다면 (0->2)식으로 2일이 소요된다. (even-cycle)%2 * 2
    '''
    answer = cycle * 2 + max((odd-cycle) * 2 - 1, 0) + ((even-cycle) // 2 * 3) + ((even-cycle) % 2 * 2)

    print(f'#{tc} {answer}')

# 교수님 코드드
# C = int(input())
# for tc in range(1, TC):
#     N = int(input())
#     Tree = list(map(int, input().split()))
#     maxV = max(Tree)
#     cnt1 = 0
#     cnt2 = 0
#     for i in range(N):
#         cnt1 += (maxV-Tree[i])//2
#         cnt2 += (maxV-Tree[i])%2
#
#     result = max(cnt1*2, cnt2*2-1)
#     while result >= max(cnt1*2, cnt2*2-1):
#         result = max(cnt1*2, cnt2*2-1)
#         cnt1 -= 1
#         cnt2 += 2
#
#         print(f'#{tc} {result}')
