import sys
sys.stdin = open("input_1267.txt", "r")

# 위상 정렬
for tc in range(1, 11):
    v, e = map(int, input().split())
    lst = list(map(int, input().split()))
    par = [[] for _ in range(v + 1)]        # 자식을 인덱스로 하여 부모 노드를 자식인덱스에 넣는다.
    for i in range(e):
        p, c = lst[i*2], lst[i*2+1]
        par[c].append(p)

    result = []             # 결과 담을 변수
    q = []                  # 부모 제거용 변수
    while len(result) != v:                         # result의 길이가 노드 개수와 같아질 때 까지.
        for j in range(1, v+1):
            if not par[j] and j not in result:      # 만약 자식 인덱스에 부모가 없으면 (진입차수가 0일 때) and result에 해당 인덱스(부모없는 자식 노드)가 들어 있지 않을 때
                result.append(j)                    # 결과 값에 해당 노드값 추가
                q.append(j)                         # 부모 제거 용에도 노드값 추가
        while q:                                    # 부모 제거용 안에 값이 있는 동안
            a = q.pop()                             # 부모가 사라졌으니 다음 자식의 진입 차수를 바꿔줘야함
            for j in range(1, v+1):
                if a in par[j]:                     # 진입차수가 0인 부모를 가지고 있는 자식 인덱스에서 부모를 제거 (진입차수 -1)
                    par[j].remove(a)

    print(f'#{tc}', end=' ')
    print(*result)



