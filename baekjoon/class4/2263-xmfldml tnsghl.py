def find_tree(l_in, r_in, l_post, r_post):
    if l_in > r_in or l_post > r_post:
        return

    root = post_order[r_post]
    print(root, end=' ')
    idx = position[root]
    count = idx - l_in

    # 왼쪽 서브트리
    find_tree(l_in, idx - 1, l_post, (l_post + count) - 1)
    # 오른쪽 서브트리
    find_tree(idx + 1, r_in, l_post + count, r_post - 1)

N = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))
position = [0 for _ in range(N+1)]

for i in range(N):
    position[in_order[i]] = i

find_tree(0, N-1, 0, N-1)

'''- 먼저 중위 순회와 후위 순회의 결과를 입력받는다.
- 중위 순회했을 때 특정 노드를 몇 번째로 방문했는지에 대한 정보를 position에 저장한다.
- position을 활용하여 루트 노드를 기준으로 왼쪽 서브트리와 오른쪽 서브트리를 나누는데 사용된다.
- 이제 find_tree함수에 중위 순회와 후위 순회의 처음 위치와 마지막 위치를 전달한다.
- find_tree를 통해 전위 순회의 결과를 출력한다.
- 먼저 r_post는 후위 순회의 결과 중 가장 마지막으로 방문한 노드를 가리키고 있기 때문에 이를 활용하여 루트 노드를 구한다.
- 그리고 전위순회이기 때문에 구한 루트 노드를 바로 출력한다.
- 이제 루트 노드를 통해 중위 순회에서 왼쪽과 오른쪽 서브트리를 구해야한다.
- 루트 노드가 중위 순회에서 몇 번째로 방문했는지를 찾아 idx에 저장하고
- idx를 기준으로 왼쪽 서브트리에는 몇 개의 노드가 있는지 count에 저장한다.
- 이제 idx와 count를 활용하여 왼쪽 서브트리와 오른쪽 서브트리를 구한다.
- 첫 번째 재귀 호출은 왼쪽 서브트리의 루트 노드를 구하기 위한 것이다.
- 항상 중위 순회와 후위 순회의 범위를 맞춰주어야 한다.
- 이렇게 재귀호출을 통해 반복을 하여 전위 순회의 결과를 구할 수 있다.
'''