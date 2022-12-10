def solve(i, result, sumV):
    global min_path
    if i == n:  # 고객 좌표를 전부 돌았으면
        sumV += abs(result[-1][0] - home[0]) + abs(result[-1][1] - home[1])   # 마지막 고객 좌표에서 집의 좌표의 거리를 구해서 이동거리 합에 더한다.
        min_path = min(min_path, sumV)  #  최소값 비교
        return

    if sumV >= min_path:    # 현재까지의 이동거리의 합이 최소값보다 크면 return
        return

    for j in range(n):
        if not visited[j]:     # 해당 고객 좌표에 방문 하지 않았을 경우
            visited[j] = 1      # 방문 처리
            result.append(customer[j])  # 방문 순서에 추가
            solve(i + 1, result, sumV + abs(result[-2][0] - result[-1][0]) + abs(result[-2][1] - result[-1][1]))    # 다음 방문 고객 번호와 방문 순서 리스트, 그리고 방문 리스트에서 맨 뒤에서 두번째 좌표와 맨 뒤에서 첫 번째 좌표의 거리를 구해서 이동거리 합에 더해서 넘겨준다.
            result.pop()    # 방문 취소
            visited[j] = 0


for tc in range(1, int(input()) + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    company = (arr[0], arr[1])      # 맨앞은 회사 좌표
    home = (arr[2], arr[3])         # 그 다음은 집 좌표
    customer = []
    for i in range(4, len(arr), 2): # 고객 좌표는 앞에 회사 좌표와 집 좌표를 뺀 4번 인덱스부터
        customer.append((arr[i], arr[i + 1]))
    visited = [0] * n
    result = [company]  # 방문 순서를 담을 리스트, 항상 회사에서 출발하므로 초기값으로 회사의 좌표를 넣어 놓는다.
    min_path = 100000
    solve(0, result, 0)

    print(f'#{tc} {min_path}')