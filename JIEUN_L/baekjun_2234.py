import sys
from collections import deque
sys.stdin = open("input.txt")

def BFS(start,wall ,visited, room_numb) : # 현재 좌표, 맵, 룸 넘버
    dir = [(0, -1),(-1, 0),(0, 1),(1, 0)] # 서 북 동 남 순서(1 2 4 8)
    # dir_exp = ["서(왼)1","북(위)2", "동(오)4","남(아)8" ]
    bits = [1,2,4,8]
    current = deque([start])
    cnt_room = 1
    visited[start[0]][start[1]] = room_numb

    while current : 
        cur = current.popleft()
        for i in range(4) :
            next_x = cur[0]+dir[i][0]
            next_y = cur[1]+dir[i][1]
            if next_x < M and  next_x >=0 and next_y >=0 and next_y < N : 
                if (wall[cur[0]][cur[1]] & bits[i])==0 and visited[next_x][next_y]==0 :
                    visited[next_x][next_y] = room_numb
                    cnt_room += 1
                    current.append([next_x,next_y])

    return cnt_room
    


def MERGE(visited,room_cnt) : 
    dir =   [(0, 1),(1, 0)] # 동 남 순서(4 8)
    max_merge_cnt = 0
    for i in range(M) : 
        for j in range(N) : 
            for k in range(2) :
                next_x = i+dir[k][0]
                next_y = j+dir[k][1]
                if next_x < M and next_y < N : 
                    if visited[i][j] != visited[next_x][next_y]:
                        max_merge_cnt = max(max_merge_cnt, room_cnt[visited[i][j]]+room_cnt[visited[next_x][next_y]])


    return max_merge_cnt

######본 로직#####


N, M = map(int, input().split())
wall = []

for i in range(M) :  
    wall.append(list(map(int, input().split())))
    
    
room_num = 1
room_cnt =[0]
max_one_room_size = 0
visited = [[0]*N for _ in range(M)]

for i in range(M) : 
    for j in range(N) : 
        if visited[i][j] == 0 : 
            one_room_cnt= BFS([i, j],wall, visited, room_num)
            room_num += 1
            room_cnt.append(one_room_cnt)

max_one_room_size = max(room_cnt)
max_merge_cnt = MERGE(visited,room_cnt)

# 1 : 이 성에 있는 방의 개수
# 2 : 가장 넓은 방의 넓이
# 3 : 하나의 벽을 제거하여 얻을 수 있는 가장 넓은 방의 크기
    
print(room_num-1)
print(max_one_room_size)
print(max_merge_cnt)




