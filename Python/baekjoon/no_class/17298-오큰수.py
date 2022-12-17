n = int(input())
A = list(map(int, input().split()))
answer = [-1] * n
stack = []

for i in range(n):  # 인덱스를 차례로 스택에 push
    while stack and A[stack[-1]] < A[i]:    # 해당 인덱스의 값과 오른 쪽의 값을 비교해 가면서 결과값에 추가
        answer[stack.pop()] = A[i]
    stack.append(i)
print(*answer)