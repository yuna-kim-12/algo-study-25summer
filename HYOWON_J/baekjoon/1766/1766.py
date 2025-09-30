import  sys
sys.stdin = open('n.txt')
import heapq

#N개의 문제는 모두 풀어야 한다.
#먼저 푸는 것이 좋은 문제가 있는 문제는, 먼저 푸는 것이 좋은 문제를 반드시 먼저 풀어야 한다.
#가능하면 쉬운 문제부터 풀어야 한다.

n, m = map(int, input().split())
#둘째 줄부터 M개의 줄에 걸쳐 두 정수의 순서쌍 A,B가 빈칸을 사이에 두고 주어진다.
#이는 A번 문제는 B번 문제보다 먼저 푸는 것이 좋다는 의미이다.
g = [[] for _ in range(n + 1)]
indeg = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())  # a가 b보다 먼저
    g[a].append(b)
    indeg[b] += 1

hq = []
for v in range(1, n + 1):
    if indeg[v] == 0:
        heapq.heappush(hq, v)  # 쉬운 문제(번호 작은 것) 우선

ans = []
while hq:
    v = heapq.heappop(hq)
    ans.append(v)
    for nv in g[v]:
        indeg[nv] -= 1
        if indeg[nv] == 0:
            heapq.heappush(hq, nv)

print(*ans)