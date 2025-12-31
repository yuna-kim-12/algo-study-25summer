import sys
sys.stdin = open("input.txt")



from collections import deque
# 이건 무조건 BFS 가 유리한뎅 


def BFS(maps, start, N, M) : 
    cnt_area = 1
    q = deque([start])
    maps[start[0]][start[1]] = 2
    dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while q :
        cur = q.popleft()
        for i in range(4) :
            next = (cur[0]+dir[i][0], cur[1]+dir[i][1]) 
            if 0 <= next[0] < M and 0 <= next[1] < N and maps[next[0]][next[1]] ==0 : 
                maps[next[0]][next[1]] = 2
                cnt_area += 1
                q.append(next)

    return cnt_area
                


M, N, K = map(int, input().split())

locs = [list(map(int, input().split())) for _ in range(K)]
maps = [[0]*N for _ in range(M)]
area_cnt = []
area = 0

# 영역 칠하기
for k in range(K) : 
    for i in range(locs[k][1], locs[k][3]) : 
        for j in range(locs[k][0], locs[k][2]) : 
            maps[i][j] = 1

# 칠한 영역 0을 찾아 영역 찾기
for i in range(M) : 
    for j in range(N) : 
        if maps[i][j] == 0 :
            area += 1
            area_cnt.append(BFS(maps, (i,j), N, M))

# 오름차순 정렬
area_cnt.sort()

print(area)

print(*area_cnt)




            
    
