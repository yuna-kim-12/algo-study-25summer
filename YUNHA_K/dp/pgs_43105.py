def solution(triangle):
    # 1. 저장할 값 테이블 생성.
    N = len(triangle)
    calculated = [[0]*i for i in range(1,(N+1))]

    # 2. 각 행을 돌면서,
    # 첫 행은 (0,0) 값으로 초기화.
    calculated[0][0] = triangle[0][0]
    for i in range(1,N):
        M = len(triangle[i])
        for j in range(M):
            val = triangle[i][j]
            # 0열 값 -> (행-1,0) 값만 저장, N열 값 -> (행-1, N-1) 값만 저장
            if j == 0:
                val += calculated[i-1][j]
            elif j == M-1:
                val += calculated[i-1][M-2]
            # 나머지는 (행-1,자기열-1), (행-1, 자기열)과 비교
            else:
                val += (calculated[i-1][j-1] if calculated[i-1][j-1] > calculated[i-1][j] else calculated[i-1][j])

            # 이미 계산한 값과 비교해서 더 큰 값을 저장할 테이블에 저장.
            if val > calculated[i][j]:
                calculated[i][j] = val

    return max(calculated[N-1])