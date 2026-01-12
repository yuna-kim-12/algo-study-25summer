import sys
sys.stdin = open("input.txt")

# # 그 유명한 N queen 문제. 이건 정석적인 풀이가 이미 존재함... 

"""
복사 시간 + queen을 전부 확인하는 것 떄문에 반드시 시간 초과가 나는 풀이
def check_attackable(queens, n_queen) :

    for q in queens : 
        #세로선 
        if q[1] == n_queen[1] or abs(q[0]-n_queen[0]) == abs(q[1]-n_queen[1]) : 
            return False
    
    return True


def queen(row, queens, y_visited) : 
    if row == N : 
        return 1 
    
    result = 0

    for i in range(N) : 
        if y_visited[i] : 
            continue

        if not check_attackable(queens, [row, i]) : 
            continue
        
        y_visited[i] = True
        result += queen(row+1, queens+[[row, i]], y_visited)
        y_visited[i] = False

    return result



N = int(input())

print(queen(0, [],[False]*N))
"""


def queen(row) : # m : x-y=k, p = x+y=k
    if row == N : 
        return 1
    
    result = 0
    for i in range(N) :
        if y_visited[i] or p_diagonal[i+row] or m_diagonal[i-row+N-1] : 
            continue
        
        y_visited[i] = True
        m_diagonal[i-row+N-1] =True
        p_diagonal[i+row] = True

        result += queen(row+1)
        
        y_visited[i] = False
        m_diagonal[i-row+N-1] =False
        p_diagonal[i+row] = False
    
    return result



N = int(input())
y_visited= [False]*N
m_diagonal = [False]*(2*N)
p_diagonal = [False]*(2*N)
print(queen(0))