import sys

sys.stdin = open("input_1248.txt", "r")

def find_parent(n, plst):           # 부모 찾기
    if tree[n][0]:                  # 해당 인덱스의 0번이 부모 노드 번호 이므로 0번이 있으면 부모 노드 정보를 부모 배열에 넣어주기
        plst.append(tree[n][0])
        find_parent(tree[n][0], plst)   # 부모의 부모를 찾기

def find_near_parent(n1_plst, n2_plst):     # 공통 조상 찾기
    for par in n1_plst:         # n1의 부모배열을 순회하며 해당 부모가 n2의 부모에도 있는지 확인
        if par in n2_plst:
            return par          # 있으면 리턴해줌, 0번 부터 순회하기 때문에 리턴되는 값은 항상 최솟값

def find_subtree(k):            # 서브트리 개수
    global cnt
    if k:
        cnt += 1
        find_subtree(tree[k][1])
        find_subtree(tree[k][2])

for tc in range(1, int(input())+1):
    v, e, n1, n2 = map(int, input().split())
    lst = list(map(int, input().split()))
    tree = [[0] * 3 for _ in range(v + 1)]      # 부모노드 번호, 자식1, 자식2
    for i in range(e):
        p, c = lst[i*2], lst[i*2+1]
        if not tree[p][1]:                      # 자식1부터 채우기
            tree[p][1] = c
        else:
            tree[p][2] = c
        tree[c][0] = p                          # 0번에 해당 인덱스의 부모노드 번호 넣기

    n1_parent = []      # n1의 부모노드 정보를 담을 배열
    n2_parent = []      # n2의 부모노드 정보를 담을 배열
    find_parent(n1, n1_parent)  # 부모 찾기
    find_parent(n2, n2_parent)
    cnt = 0                     # 서브트리 개수 담을 변수
    near_parent = find_near_parent(n1_parent, n2_parent)        # 두 노드의 가장 가까운 공통 조상 찾기
    find_subtree(near_parent)                                   # 공통조상의 서브트리 개수 찾기
    print(f"#{tc} {near_parent} {cnt}")

