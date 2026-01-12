import sys
sys.stdin = open("input.txt")

"""
BFS로 풀 수 있으나 일단은 다익스트라로 먼저 푼다. 연습 중이기 때문이지....

입력 : 
1. N 
2. N*N map

다익스트라 
1.maps를 N*N사이즈로 만든다. 전부 inf이지만, 0,0은 0으로 만들어준다. 
2.움직일 수 있는 칸이라면(dir 4개 방향 중) 값을 계산하고, 움직인다. 물론 heap에 넣도록 한다...


"""
"""
from heapq import heappush, heappop

def dijkstra(cave, N, cnt) : 
    loss = [[float("inf")]*N for _ in range(N)]
    loss[0][0] = cave[0][0]
    dir = [(0, 1),(1, 0), (0, -1), (-1, 0)]
    hq = [[loss[0][0], 0, 0]]  # loss, col, row
    while hq : 
        cur = heappop(hq)
        if loss[cur[1]][cur[2]] != cur[0] :  
            continue
        if cur[1] == N-1 and cur[2] == N-1 : 
            break

        for d in dir : 
            if 0<=cur[1]+d[0]<N and 0<=cur[2]+d[1]<N : 
                next_x = cur[1]+d[0]
                next_y = cur[2]+d[1]
                next_loss = cave[next_x][next_y]+cur[0]
                if loss[next_x][next_y] > next_loss : 
                    loss[next_x][next_y] = next_loss
                    heappush(hq, [next_loss, next_x, next_y])
    print(f'Problem {cnt}: {loss[N-1][N-1]}')
    return
    
    


cnt = 0
while True : 
    cnt+=1
    N = int(input())
    if N == 0 : 
        break

    cave = [list(map(int, input().split())) for _ in range(N)]
    dijkstra(cave, N, cnt)

######여기까지가 다익스트라로 푸는 방법##############

"""

#########여기서부터는 BFS로 푸는 방법 
from collections import deque

def BFS(cave, N, cnt) : 
    loss = [[0]*N for _ in range(N)]
    loss[0][0] = cave[0][0]
    dir = [(0, 1),(1, 0), (0, -1), (-1, 0)]
    q = deque([(0, 0)])
    while q :
        cur = q.popleft()
        for d in dir : 
            if 0<=cur[0]+d[0]<N and 0<=cur[1]+d[1]<N :
                next_x = cur[0]+d[0]
                next_y = cur[1]+d[1]
                if loss[cur[0]][cur[1]] + cave[next_x][next_y] < loss[next_x][next_y] or loss[next_x][next_y] == 0 : 
                    loss[next_x][next_y] = loss[cur[0]][cur[1]] + cave[next_x][next_y]
                    q.append([next_x, next_y])
    print(f'Problem {cnt}: {loss[N-1][N-1]}')



             
    
cnt = 0
while True : 
    cnt+=1
    N = int(input())
    if N == 0 : 
        break

    cave = [list(map(int, input().split())) for _ in range(N)]
    BFS(cave, N, cnt)
