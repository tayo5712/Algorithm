N = int(input())  # 수열의 길이 입력받기
seq = []  # 수열을 저장할 리스트

# 수열 입력받기
for _ in range(N):
    seq.append(int(input()))

# 등차수열인지 판별
if seq[2] - seq[1] == seq[1] - seq[0]:  # 세 번째 수와 네 번째 수의 차이가 두 번째 수와 세 번째 수의 차이와 같으면 등차수열
    diff = seq[1] - seq[0]  # 등차수열의 공차 계산
    next_num = seq[-1] + diff  # 다음 수 계산

# 등비수열인지 판별
elif seq[2] / seq[1] == seq[1] / seq[0]:  # 세 번째 수와 네 번째 수의 비율이 두 번째 수와 세 번째 수의 비율과 같으면 등비수열
    ratio = seq[1] / seq[0]  # 등비수열의 공비 계산
    next_num = int(seq[-1] * ratio)  # 다음 수 계산

# 다음 수 출력
print(next_num)
