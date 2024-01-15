def solution(board):
    answer = 1234
    n = len(board)
    m = len(board[0])
    DP = [[0 for _ in range(m)] for _ in range(n)]
     
    DP[0] = board[0]
    for i in range(n):
        DP[i][0] = board[i][0]
    
    for i in range(1, n):
        for j in range(1, m):
            if board[i][j]:
                DP[i][j] = min(DP[i][j-1], DP[i-1][j], DP[i-1][j-1]) + 1
    
    result = 0
    for i in range(n):
        result = max(result, max(DP[i]))
            
    answer = result * result

    return answer
