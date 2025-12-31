import sys
sys.stdin = open("input.txt")

"""
인풋 : 
N, M X
시작 끝 소요시간


계획 
1. 모든 노드별 연결을 이차원 배열(변수명 maps)로 만든다. 배열의 값은 T로 넣는다. 
2. 매 집마다(1~N, X제외, 이 친구는 0이니까) 다익스트라 함수를 실행시켜 리턴한다. 
3. 함수 실행 리턴값을 받아 최댓값인지 확인해서 최댓값을 저장하고 마지막에 프린트한다. 

다익스트라 함수 
1.함수에는 스타트 지점과 X값, 그리고 maps를 받는다. 
2. 배열을 만든다. 1~N까지 있는 N+1개 크기 배열에 inf부여.
3. 방문 여부를 확인하는거
3. 현재 집에서 갈 수 있는 곳들을 확인해 거리를 업데이트 
4. 표에 다음 갈 수 있는 곳들을 확인해서, 해당 노드에서 타 노드로 가는 비용 계산해 비교, 최솟값 업이트

"""

import heapq

def djikstra(s, maps) : 
    route = [float("inf")*(N+1)] 
    # visited = [False]*(N+1)
    route[s] =0
    q = []
    heapq.heappush(q, (0, s))

    while q : 
        dist, now = heapq.heappop(q)
        if route[now] >= dist : 
            for next, val in maps[now] : 
                if dist +val < route[next] : 
                    heapq.heappush(q, (dist+val, next))
    return route



N, M, X = map(int, input().split())
# 학생 수 N 
# 단방향 도로 수 m 
# 도착 마을 X

# 지도 채우기
maps = [[0]*N for _ in range(N)] # 가로에서 세로로 가는 길
for i in range(M) : 
    a, b, t = map(int, input().split())
    maps[a].append([b, t]) 

result = djikstra(X, maps)
result[0] =  0
for i in range(1, N+1) : 
    if i !=X : 
        res = djikstra(i, maps)
        result[i] += res[X]

print(max(result))

