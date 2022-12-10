import sys

sys.stdin = open("input_1232.txt", "r")

def order(v):
    if 1 <= v <= n:     # 노드의 범위설정
        if not str(tree[v]).isnumeric():        # 노드에 들어있는 값이 연산자 이면
            left = order(ch1[v])                # 해당 노드를 부모로 가지는 자식 두명을 데려온다.
            right = order(ch2[v])
            oper = tree[v]
            if oper == "+":                     # 자식에 들어있는 값을 부모에 들어있는 연산자로 계산 후 그 값을 부모에 넣어준다.
                tree[v] = left + right
            elif oper == "-":
                tree[v] = left - right
            elif oper == "*":
                tree[v] = left * right
            else:
                tree[v] = left / right
        return tree[v]

T = 10
for tc in range(1, T+1):
    n = int(input())
    tree = [0] * (n+1)      # 트리 배열
    ch1 = [0] * (n+1)       # 자식 1
    ch2 = [0] * (n+1)       # 자식 2
    for _ in range(n):
        node, value, *child = input().split()   # 입력 개수가 다르므로 가변인자 사용
        if not value.isnumeric():   # value 값이 연산자 이면
            ch1[int(node)] = int(child[0])     # 부모와 자식간의 관계 정의
            ch2[int(node)] = int(child[1])
            tree[int(node)] = value            # 트리 해당 인덱스에 연산자 넣어주기

        else:
            tree[int(node)] = int(value)       # value 값이 연산자가 아니면 해당 인덱스의 값이므로 트리에 넣어주기

    print(f'#{tc} {int(order(1))}')


# def post_order(num):
#     if tree[num][1].isdigit():
#         return int(tree[num][1])
#
#     a = post_order(int(tree[num][2]))
#     b = post_order(int(tree[num][3]))
#     op = tree[num][1]
#
#     if op == '+':
#         return a + b
#     if op == '-':
#         return a - b
#     if op == '*':
#         return a * b
#     return a // b
#
#
# for i in range(10):
#     n = int(input())
#     tree = [0] + [input().split() for _ in range(n)]
#
#     print(f'#{i + 1} {post_order(1)}')