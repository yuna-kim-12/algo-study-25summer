import sys, heapq
sys.stdin = open('n.txt')

N, E = map(int, input().split())
g = [[] for _ in range(N+1)]
INF = 10**15
case_u = 0
case_v = 0

for _ in range(E):
    a, b, c = map(int, input().split())
    g[a].append([b, c])
    g[b].append([a, c])
u, v = map(int, input().split())

def d(start):
    distance = [INF] * (N + 1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist :
            continue

        for next in g[now]:
            cost = dist + next[1]
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(q, (cost, next[0]))

    return distance

#1에서 u, v까지
distance = d(1)
case_v += distance[v]
case_u += distance[u]

#u에서 v까지, u에서 N까지
distance = d(u)
case_u += distance[v]
case_v += distance[N]

#v에서 u까지 , v에서 N까지
distance = d(v)
case_v += distance[u]
case_u += distance[N]

#정답처리 -> 거리가 INF와 같은 경우도 있음. 이전 >이것만 했을 땐 틀림.
ans = min(case_v, case_u)
if ans >= INF :
    print(-1)
else:
    print(ans)