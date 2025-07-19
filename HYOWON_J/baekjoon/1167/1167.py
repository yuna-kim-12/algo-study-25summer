import sys
from collections import deque
sys.stdin = open("num.txt")

V = int(input())
check = [0] * (V+1)
distance = [0] * (V+1)
maps = [[] for _ in range(V+1)]

for _ in range(V):
    a = list(map(int, input().split()))
    for i in range(0, len(a)-2, 2):
        node = a[0]
        next_node = a[i+1]
        distance_num = a[i+2]
        maps[node].append([next_node,distance_num])

def BFS(start):
    box = deque()
    box.append(start)
    check[start] = 1

    while box:
        now = box.popleft()
        for i in maps[now]:
            if check[i[0]] == 0:
                check[i[0]] = 1
                box.append(i[0])
                distance[i[0]] = distance[now] + i[1]

#가장 멀리 있는 노드 확인
BFS(1)
max_node = 1
for i in range(2, V+1):
    if distance[i] > distance[max_node]:
        max_node = i
#BFS조건 초기화
check = [0] * (V+1)
distance = [0] * (V+1)

#가장 멀리는 노드로 거리탐색
BFS(max_node)
print(max(distance))
