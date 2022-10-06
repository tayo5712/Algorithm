def placeBishop(board):
    dr = [1, 1]
    dc = [1, -1]
    id = [[[-1] * n for _ in range(n)] for _ in range(2)]
    count = [0, 0]
    for dir in range(2):
        for r in range(n):
            for c in range(n):
                if (board[r][c] == 1 and id[dir][r][c] == -1):
                    nr, nc = r, c
                    while 0 <= nr < n and 0 <= nc < n:
                        if board[nr][nc] == 1:
                            id[dir][nr][nc] = count[dir]
                        nr += dr[dir]
                        nc += dc[dir]
                    count[dir] += 1


    # a = count[0]
    # b = count[1]
    # adj = [[0] * b for _ in range(a)]
    # for r in range(n):
    #     for c in range(n):
    #         if board[r][c] == 1:
    #             adj[id[0][r][c]][id[1][r][c]] = 1
    #
    # print(adj)
    # return bipartiteMatch(a, b, adj)

# def dfs(i, visited, adj, aMatch, bMatch):
#     if visited[i]:
#         return False
#     visited[i] = 1
#     for j in range(b):
#         if adj[i][j] == 1:
#             if bMatch[j] == -1 or dfs(bMatch[j], visited, adj, aMatch, bMatch):
#                 aMatch[i], bMatch[j] = j, i
#                 return True
#     return False
#
#
# def bipartiteMatch(a, b, adj):
#     aMatch = [-1] * a
#     bMatch = [-1] * b
#     size = 0
#     for start in range(a):
#         visited = [0] * a
#         if dfs(start, visited, adj, aMatch, bMatch):
#             size += 1
#     return size

    print(id)

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
placeBishop(board)