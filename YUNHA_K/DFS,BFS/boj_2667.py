import sys

input = sys.stdin.readline

# 1. 맵을 순회하다가 1을 만나면, visited 처리 됐는지 확인하고 그때부터 bfs 시작.
    # bfs 할 때, 단지 수 count.
        # 변수 -> 단지 : danji = 0, count = 0, apartment = {}
        # dir로 사방 확인. vistied = 0 이면 count += 1

    # dictionary에 넣고 나중에 items로 print 하기.

# 2. 만약에 끝나면 계속 순회.
def bfs(apart):
    from collections import deque
    visited = [[0]*N for _ in range(N)]
    dirs = ((-1,0), (1,0), (0,-1), (0,1))
    apartment = []
    danji = 0

    # 아파트 전체 순회
    for i in range(N):
        for j in range(N):
            # 1이면 탐색 시작.
            if apart[i][j] == 1:
                # 이미 순회했으면 pass
                if visited[i][j]:
                    continue
                queue = deque([(i,j)])
                visited[i][j] = 1
                # 처음 방문처리 해줘야 하나?
                danji += 1
                count = 0

                while queue:
                    ci, cj = queue.popleft()
                    count += 1

                    for dir in dirs:
                        ni, nj = ci + dir[0], cj + dir[1]
                        if 0 <= ni < N and 0 <= nj < N:
                            if apart[ni][nj] == 1 and not visited[ni][nj]:
                                queue.append([ni,nj])
                                visited[ni][nj] = 1

                apartment.append(count)
    return danji, apartment

# 입력 1 : 지도 크기 N
# 입력 2 : 정사각형
N = int(input())
apart = []
for _ in range(N):
    apart.append(list(map(int, input().strip())))

# 출력 1 : 총 단지 수
# 출력 2 : 각 단지내 집의 수를 오름차순으로 정렬해 한 줄에 하나씩 출력
danji, apartment = bfs(apart)
print(danji)
for val in sorted(apartment):
    print(val)