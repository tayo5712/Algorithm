# def isVPS(pack):
#     stack = 0
#     for i in pack:
#         if i == '(':  # 괄호가 열릴 때 마다 stack에 1을 추가
#             stack += 1
#         else:
#             stack -= 1
#             if stack < 0:  # stack이 0보다 작아지면 VPS를 만족하지 못하므로 즉시 리턴
#                 return 'NO'
#
#     if stack == 0:  # stack이 0이면 VPS 만족 (제대로 딱딱 닫혔다)
#         return 'YES'
#     else:  # stack이 1 이상이면 제대로 안닫혀서 VPS 불만족
#         return 'NO'

def isVPS(pack):

    stack = []
    for i in pack:
        if i == '(':                # 열린 괄호가 나오면 스택에 '(' 푸쉬
            stack.append('(')
        else:                        # i == ')'
            if stack:
                stack.pop()
            else:
                return 'NO'         # 닫힌 괄호가 나왔는데 스택에 '(' 열린 괄호가 없으면 NO

    if stack:                       # '(' 열린 괄호가 남아 있어도 NO
        return 'NO'
    return 'YES'                    # 다 딱딱 잘 맞아 떨어지면 YES


T = int(input())
for tc in range(1, T + 1):

    pack = input()
    print(isVPS(pack))