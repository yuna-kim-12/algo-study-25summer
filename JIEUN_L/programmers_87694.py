# 1. 맵 만들기 
# 외부는 -1, 테두리는 1로 만듬. 내부는 0
# ractangle 전체를 돌면서 X 의 max, min, Y의 min, max를 찾는다.
# 맵은 x의 min, x의 max, y의 max, y의 min만큼의 크기이다.
# 전체 맵을 일단 0으로 만든다.(map) 
# 상자 하나를 만드는 법 : 해당 X, 해당 Y이면 1로 두고, 아니면 2로 지나간다.
# 두번쨰 이상 : 만일 0이 아니라면 그대로 두고 지나간다.0 이면 위 조건들대로 지나간다. 

# BFS로 찾아가기
# character는 x, y가 각각의 min만큼 빠진 상태이다. item도 마찬가지이다.
# 시작점을 그냥 2로 만들고 시작하자구.
# 1이면 안가본 곳으로 알고, 큐에 넣는다. 이 이후로는 그냥 BFS


from collections import deque
def make_map(rectangle) : 
    base_map = [[-1 for _ in range(50)] for _ in range(50)]
    for i in range(len(rectangle)) : 
        for j in range(rectangle[i][1],rectangle[i][3]+1 ) :
            for k in range(rectangle[i][0],rectangle[i][2]+1) : 

                if j == rectangle[i][1] or j==rectangle[i][3] or k==rectangle[i][0]or k==rectangle[i][2] : 
                    base_map[k][j] = 1
                else :
                    base_map[k][j] = 0
    return base_map


def BFS(base_map,characterX, characterY, itemX, itemY) : 
    q = deque([(characterX, characterY)])
    # print(q)
    direction = ((0, 1), (1, 0),(-1, 0), (0, -1))
    while q : 
        current = q.popleft()
        print(current)
        base_map[current[0]][current[1]] += 1
        if current[0] == itemX and current[0] == itemY :
            return base_map[itemX][itemY] 
        for dir in direction : 
            next_x = current[0] + dir[0]
            next_y = current[1] + dir[1]
            print(f"next_x, next_y, basemap = {next_x}, {next_y}, {base_map[next_x][next_y]}")
            if next_x >= 0 and next_x <= 49 and next_y >= 0 and next_y <= 49 and base_map[next_x][next_y] == 1 :
                print(f"next_x, next_y = {next_x}, {next_y}")
                q.append((next_x, next_y))
    return  

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    map = make_map(rectangle)
    print(map)
    answer = BFS(map,characterX, characterY, itemX, itemY)
    print(answer)
    return answer-2

solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]], 1, 3, 7, 8)



