a, b = map(int, input().split())
n = int(input())
f_list = list(int(input()) for _ in range(n)) # 즐겨찾기 리스트

button_cnt = 0  # 버튼 누르는 횟수
m_list = []    # 두 채널 간의 차이를 담을 리스트
m_list.append(abs(b-a))      # m_list에 a에서 b까지의 거리의 절댓값을 추가
for i in f_list:             # 즐겨찾기 리스트의 요소만큼 반복
    m_list.append(abs(b-i))          # b - 즐겨찾기 각 요소의 절댓값을 추가
min_dif = min(m_list)                # min_dif는 가장 차이가 작은 요소를 할당
if min_dif != m_list[0]:             # min_dif가 a에서 b까지의 거리랑 다르다면,
    button_cnt += 1                  # 즐겨찾기 버튼을 누르는 것이므로 버튼 누르는 횟수 1 증가
button_cnt += min_dif                # min_dif 만큼 버튼 누르는 횟수 증가

print(button_cnt)