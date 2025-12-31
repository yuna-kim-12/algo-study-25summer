import sys
sys.stdin = open("input.txt")


from collections import deque

# 경로:이동 횟수로 만들고 
# 계속 경로를 넣음
# 경로를 넣다가 
status = []
for _ in range(3) : 
    status += tuple(map(int, input().split()))


final_status = list('123456780')
result = -1

for i in range(9) :
    if status[i] == 0 : 
        start = tuple(divmod(i, 3))

maps_integered = {
    (0, 0) : 0,
    (0, 1) : 1,
    (0, 2) : 2,
    (1, 0) : 3,
    (1, 1) : 4,
    (1, 2) : 5,
    (2, 0) : 6,
    (2, 1) : 7,
    (2, 2) : 8
}

status_saved = {tuple(status) : 0}


q = deque([[start, status]])
dir = [(0,1), (1, 0),(0,-1),(-1,0)] # 오, 아래,왼, 위
while q : 
    temp = q.popleft()
    cur = temp[0]
    cur_status = temp[1]
    # print(cur, cur_status)
    moved = status_saved[cur_status]
    print("location : ", cur, "moved : ", moved, cur_status)

    if cur_status == final_status : 
        result = moved
        break

    for i in range(4) :
        next_idx = (cur[0]+dir[i][0] ,cur[1]+dir[i][1] )

        if 0<= next_idx[0] <3 and 0<=next_idx[1] <3 : 
            # 현재 있는 위치와 다음 위치의 swap
            print(next_idx)
            list_cur_status = list(cur_status)
            list_cur_status[maps_integered[cur]], list_cur_status[maps_integered[next_idx]] =list_cur_status[maps_integered[next_idx]], list_cur_status[maps_integered[cur]]

            # 이제 변경된 status를 dict에 저장 전에 있는지 확인해야지
            # 만약에 있다면 그냥 pass 
            # 만약에 없다면 넣기
            if tuple(list_cur_status) not in status_saved : 
                
                status_saved.setdefault(tuple(list_cur_status),moved+1)
            
                # 다음 위치를 q에 넣기 
                q.append([next_idx, cur_status])
            
            # 변경된 status원복 
            cur_status[maps_integered[cur]], cur_status[maps_integered[next_idx]] = cur_status[maps_integered[next_idx]], cur_status[maps_integered[cur]]


print(status_saved)  
print(result)
