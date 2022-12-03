n = int(input())
arr = list(map(int, input().split()))

# 처음과 끝 인덱스를 left와 right로 설정
left = 0
right = n-1
minV = 2000000000
a, b = 0, 0

while left < right: # left < right인 동안에만
    value = arr[left] + arr[right]  # 두 용액의 합
    value_a = abs(arr[left]+arr[right]) # 두 용액의 합의 절대 값
    if value_a < minV:  # 두 용액의 합의 절댓값이 최소값 보다 작으면 최소값보다 0에 가깝다는 소리
        minV = value_a  # 최소값과 두 용액 값 업데이트
        a, b = arr[left], arr[right]
    if value < 0:   # 두 용액의 합이 0보다 작으면
        left += 1   # 작은 쪽의 용액을 키워 준다.
    elif value > 0: # 두 용액의 합이 0보다 크면
        right -= 1  # 큰 쪽의 용액을 키워 준다.
    else:   # 두 용액의 합이 0 이면 완벽한 답이므로 break
        break

print(a, b)