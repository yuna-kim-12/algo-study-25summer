import  heapq

# 프림 알고리즘
def prim(si):
    heap = list()
    visited = [0]*N
    total_cost = 0
    heapq.heappush(heap,(0,si))

    while heap:
        cost, ci = heapq.heappop(heap)
        if visited[ci]:
            continue

        visited[ci] = 1
        total_cost += cost

        for ni in range(N):
            if visited[ni]:
                continue
            next_cost = get_cost(x_location[ci],y_location[ci],x_location[ni],y_location[ni])
            heapq.heappush(heap, (next_cost,ni))

    return int(round(total_cost, 0))

# 비용 구하는 함수
def get_cost(x1,y1, x2, y2):
    dist = (x1-x2)**2 + (y1-y2)**2
    return E*dist

# 입력
T = int(input())
for t in range(1,T+1):
    N = int(input())
    x_location = list(map(int, input().split()))
    y_location = list(map(int, input().split()))
    E = float(input())

    result = prim(0)
    print(f'#{t} {result}')
