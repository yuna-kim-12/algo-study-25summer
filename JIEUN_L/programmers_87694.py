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
                    if base_map[j][k]  == 0 :
                        pass
                    else : 
                        base_map[j][k] = 1
                else : 
                    base_map[j][k] = 0
        # # 디버깅 용 프린트 문
        # for i in range(0,50) : 
        #     for j in range(0,50) : 
        #         print(base_map[i][j], end="")
        #     print()
        # print()
        # print()

    return base_map
def debug_map(base_map) : 
    # # 디버깅 용 프린트 문
    for i in range(0,50) : 
        for j in range(0,50) : 
            print(base_map[i][j], end="")
        print()
    print()
    print()
    
    return 


def BFS(base_map,characterX, characterY, itemX, itemY) : 
    q = deque([(characterY, characterX)])
    base_map[characterY][characterX] = 2
    # print(q)
    direction = ((0, 1), (1, 0),(-1, 0), (0, -1))
    while q : 
        current = q.popleft()
        # print(current)
        if current[0] == itemY and current[1] == itemX :
            # print("we Fouuuuuuund!!!")
            return base_map[itemY][itemX] 
        for dir in direction : 
            next_y = current[0] + dir[0]  # Y 좌표로 수정
            next_x = current[1] + dir[1]  # X 좌표로 수정
            # print(f"next_y, next_x, basemap = {next_y}, {next_x}, {base_map[next_y][next_x]}")
            if next_y >= 0 and next_y <= 49 and next_x >= 0 and next_x <= 49 and base_map[next_y][next_x] == 1 :
                base_map[next_y][next_x] = base_map[current[0]][current[1]]+1
                # print(f"next_y, next_x = {next_y}, {next_x}")
                q.append((next_y, next_x))
    return  

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    map = make_map(rectangle)
    # debug_map(map)
    # print(map)
    answer = BFS(map,characterX, characterY, itemX, itemY)
    # debug_map(map)
    # print(answer)
    return answer-2

# 우하x 좌하y 우상x 우상 y
solution([[1, 1, 8, 4], [2, 2, 4, 9], [3, 6, 9, 8], [6, 3, 7, 7]], 9, 7, 6, 1)
# solution([[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]], 1, 3, 7, 8)



