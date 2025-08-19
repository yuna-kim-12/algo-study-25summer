import sys
import heapq
input = sys.stdin.readline
INF = float('inf')

def dijkstra(r, c):
    # 거리 정보
    distance = [[INF]*N for _ in range(N)]
    heap = [(grid[0][0],r,c)]
    distance[0][0] = grid[0][0]

    while heap:
        cur_dist, r, c = heapq.heappop(heap)

        if r == N-1 and c == N-1:
            return cur_dist

        if distance[r][c] < cur_dist:
            continue

        for k in range(4):
            nr, nc = directions[k][0] + r, directions[k][1] + c
            if 0<= nr < N and 0 <= nc < N:
                next_dist = cur_dist + grid[nr][nc]
                if next_dist < distance[nr][nc]:
                    distance[nr][nc] = next_dist
                    heapq.heappush(heap, (next_dist, nr, nc))

    return grid[N-1][N-1]

# 입력
T = int(input())
for t in range(1,T+1):
    N = int(input())
    # 지도 받기
    grid = []
    for _ in range(N):
        grid.append(list(map(int, input().strip())))
    # 탐색
    directions = [(-1,0), (1,0), (0,-1), (0,1)]

    # 다익스트라 실행
    result = dijkstra(0,0)
    # 출력 : #T 최단거리
    print(f'#{t} {result}')