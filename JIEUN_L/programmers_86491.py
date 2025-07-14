# 초깃값을 일단 첫 값으로 잡아둠. 넓이, 가로, 세로..
# 1. for문을 명함 갯수-1 만큼 돌린다. 초깃값이 첫 값이기 떄문이다.
# 2. for 문 안에서 가로와 세로(area1), 세로와 가로(area2)를 비교해서, 조금 더 큰 값을 써서 넓이를 구한다. 
# 3. 넓이가 조금 더 작은 쪽의 값을 선택한다.
# ㄴㄴ... 가로를 큰 값, 세로를 작은 값으로 설정하면 됨.

def solution(sizes):
    # 가로를 큰 값, 세로를 작은 값으로 설정
    length, width = 0, 0
    for i in range(len(sizes)) : 
        print(sizes[i])
        if sizes[i][0] >= sizes[i][1] : 
            length = max(length, sizes[i][0])
            width = max(width, sizes[i][1])
        else : 
            length = max(length, sizes[i][1])
            width = max(width, sizes[i][0])
        print(length, width)

    return length*width

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))