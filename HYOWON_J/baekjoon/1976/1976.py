import sys
sys.stdin = open('1976.txt')

def union(x, y):
    x = find(x)
    y = find(y)

    if x > y :
        graph[x] = y
    else :
        graph[y] = x
    return

def find(x):
    if x != graph[x]:
        graph[x] = find(graph[x])
    return graph[x]


N = int(input())
M = int(input())
graph = [i for i in range(N)]

for i in range(N):
    arr = list(map(int, input().split()))
    for j in range(N):
        if arr[j]:
            union(i, j)

route = list(map(int, input().split()))

print(graph)

answer = 'YES'
for i in range(1, M):
    if graph[route[i]-1] != graph[route[0]-1]:
        answer = 'NO'
        break

print(answer)

