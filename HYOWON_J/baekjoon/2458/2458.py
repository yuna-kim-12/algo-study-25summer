import sys
sys.stdin = open('2458.txt')

N, M = map(int, input().split())
graph = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1

for k in range(1, N+1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1

box = {x:0 for x in range(1, N+1)}
# box = {}
# for x in range(1,N+1):
#     box[x]=0

for i in range(1, N+1):
    for j in range(1, N+1):
        if graph[i][j]:
            box[i] +=1
            box[j] +=1

answer = sum(1 for v in box.values() if v == N-1)
# for i in range(1, N+1):
#     if box[i] == N-1:
#         answer += 1

print(answer)