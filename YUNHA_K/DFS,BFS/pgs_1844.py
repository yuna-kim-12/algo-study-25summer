def solution(maps):
    from collections import deque
    n = len(maps)
    m = len(maps[0])
    visited = [[0]*m for _ in range(n)]
    
    visited[0][0] = 1
    queue = deque()
    queue.append((0,0))

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    while queue:
        x, y = queue.popleft()    
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<n and 0<=ny<m:
                if not visited[nx][ny] and maps[nx][ny] == 1:
                    visited[nx][ny] = 1
                    queue.append((nx,ny))
                    maps[nx][ny] = maps[x][y] + 1
    
    answer = maps[n-1][m-1]        
    return answer if answer != 1 else -1