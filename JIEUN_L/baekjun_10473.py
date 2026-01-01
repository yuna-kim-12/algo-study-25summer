import sys
sys.stdin = open("input.txt")

"""
계획 : 

일단 모든 대포들과 목표점을 노드에 넣고 전부 계산하는거임. 

변수 설정 
1. cannon에 [x, y]로 좌표로 넣는다. non-cannon에 시작점과 끝점을 넣는다.
2. 해당 좌표가 들어간 인덱스가 노드 번호이다. 최소거리 노드에 inf를 넣는다.
3. flag에 현재 내가 있는 곳이 대포인지 아닌지 Bool값으로 넣는다. 


다익스트라 알고리즘
1. 일단 현재 있는 노드에서 대포 및 목표 및 초기 목적지 로 갈 수 있는 시간을 잰다.(while 안에 for 문에서 대포 뿐만 아니라 끝점과 시작점도 넣어서 계산할 수 있도록  함. 
2. 1번에서 거리가 대포보다 멀면 그냥 50미터만 가고 내림. 그리고flag는 false로 넣음.
3. 만일 대포로 도착하면 해당 노드의 최소거리를 표에 넣음. 
4. 그리고 다시 모든 노드에 대해서 for문을 돌려서 거리 계산 해서 다음 위치로 감. 


결국 그냥 모든 대포가 노드인거임. 
"""
"""
개선 : 이거 업데이트 하는 모든 노드를 그렇게 heappush할 필요 없을듯.
왜냐하면 어차피최고로 시간이 덜 걸리는 노드만 업데이트 하면 되는거고, min값과 해당 인덱스만 기억하고 있으면 되는거임. 
근데 아직 개선 안함 
"""



from heapq import heappush, heappop
from math import hypot

def dijkstra(nodes) : 
    times = [float("inf")]*(N+2)
    times[0] = 0

    hq = [[0, nodes[0], 0]] # 시간, 위치, 현재 노드 인덱스
    while hq : 
        cur = heappop(hq)

        # 최신 버전의 시간인지 먼저 확인해야 함. 
        if cur[0] != times[cur[2]] : 
            continue

        # 대포(대포가 아닌 경우 : 0, N+1 번 인덱스)
        for i in range(0, N+2) :
            
            if cur[2] == i : #현재 노드는 계산 불필요, pass
                continue
            

            # 거리 및 시간 계산
            if cur[2] == 1 or cur[2] == 0 : # 마지막 노드에 있는 경우 
                new_time = hypot(cur[1][0]-nodes[i][0],cur[1][1]-nodes[i][1])/5
            else : 
                # 둘 사이의 거리를 잼. 
                length_btw = hypot(cur[1][0]-nodes[i][0],cur[1][1]-nodes[i][1])
                # 대포로 가는 길은 2초로 처리, 나머지는 걸어가는길(50미터 이상)
                new_time = 2+abs(length_btw-50)/5

            # 시간 계산한 것 반영 및 heap에 넣기
            if times[i] > new_time+cur[0] : 
                times[i] = new_time+cur[0]
                heappush(hq,[new_time+cur[0], nodes[i], i])

    return times
            

nodes = [] #0번은 나, 1번은 도착지 나머지는 cannon

nodes.append(list(map(float, input().split())))
nodes.append(list(map(float, input().split())))

N = int(input())

for i  in range(N) : 
    nodes.append(list(map(float, input().split())))
time = dijkstra(nodes)
print(time[1])
