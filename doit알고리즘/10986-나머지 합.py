import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
sum_arr = [0] * n  # 합 배열 저장 리스트
cnt = [0] * m      # 같은 나머지의 인덱스를 카운트 하는 리스트
result = 0         # 답 변수

sum_arr[0] = arr[0]    # 합 배열 0번 인덱스는 원래 배열의 0번과 동일
for i in range(1, n):       # 합 배열 저장
    sum_arr[i] = sum_arr[i-1] + arr[i]

for i in range(n):
    remainder = sum_arr[i] % m      # 합 배열을 m으로 나눈 나머지 값
    if remainder == 0:      # 현재 인덱스 까지의 합을 m으로 나눈 나머지 값이 0 이면 정답에 추가
        result += 1
    cnt[remainder] += 1     # 나머지 값을 인덱스로 카운트
                            # 합의 나머지 값이 같으면 (S[i] = S[j]) 원본 리스트에서 i + 1 부터 j 까지의 구간 합이 M으로 나누어떨어짐
for i in cnt:
    if i > 0:               # 나머지 값이 같은 원소들 중에서 2개를 뽑는 것 ( 구간 설정 ) 이므로 조합 사용
        result += (i * (i-1)) // 2

print(result)