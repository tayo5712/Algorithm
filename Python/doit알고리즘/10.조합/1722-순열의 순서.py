import sys
input = sys.stdin.readline

F = [0] * 21
S = [0] * 21
visited = [False] * 21
N = int(input())
F[0] = 1

for i in range(1, N+1): # 팩토리얼 초기화, 각 자릿수에서 만들 수 있는 경우의 수
    F[i] = F[i-1] * i

inputList = list(map(int, input().split()))

if inputList[0] == 1:   # K 번째 순열 구하기
    K = inputList[1]
    for i in range(1, N+1):
        cnt = 1                         # 해당 자리에서 몇 번째 숫자를 사용해야 할지를 정하는 변수
        for j in range(1, N+1):
            if visited[j]:              # 이미 사용한 숫자는 계산 x
                continue
            if K <= cnt * F[N-i]:       # 현재 순서가 < 해당 자리 순열 수 * cnt:
                K -= (cnt-1) * F[N-i]   # 현재 순서 = 현재 순서 - 해당 자리 순열 수 * ( cnt -1 )
                S[i] = j                # 현재 자리 (S[i])에 j값 저장
                visited[j] = True       # 숫자 j를 사용 숫자로 체크
                break
            cnt += 1     # cnt값 1 증가
        print(S)
    for i in range(1, N+1):
        print(S[i], end=' ')

else:   # 순열의 순서를 출력
    K = 1
    for i in range(1, N+1):
        cnt = 0
        for j in range(1, inputList[i]):
            if not visited[j]:  # 사용한 숫자가 아니면
                cnt += 1        # cnt값 1증가 (미사용 숫자 1 증가)
        K += cnt * F[N-i]       # 현재 자릿수에서 만들 수 있는 경우의 수
        visited[inputList[i]] = True    # inputList[i]번째 숫자를 사용 숫자로 변경
    print(K)