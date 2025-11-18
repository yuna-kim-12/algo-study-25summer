def solution(board):
    N = len(board)
    dir = [[-1,0],[1,0],[0,-1],[0,1],[-1,-1],[-1,1],[1,-1],[1,1]]
    for i in range(N):
        for j in range(N):
            # 지뢰면 위험 지역 2로 표시
            if board[i][j] == 1:
                for di in dir:
                    ni, nj = i + di[0], j + di[1]
                    if 0<= ni < N and 0<= nj <N:
                        if board[ni][nj] == 0:
                            board[ni][nj] = 2
    answer = 0
    for lst in board:
        answer += lst.count(0)
    return answer