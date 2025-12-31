import sys
sys.stdin = open("input.txt")


from heapq import heappop, heappush

def dijkstra(S, maps, banned) : # banned [시작, 끝 ]
    weight = [float("inf")]*(N+1)
    weight[S] = 0
    hq = [[0, S]] # 거리, 노드번호
    parent = [-1]*(N+1)

    while hq : 
        cur=heappop(hq)

        if cur[0] != weight[cur[1]]  : 
            continue

        for next in maps[cur[1]] : # next에서 꺼낸건 노드번호, 거리
            if banned and (banned[0] == cur[1] and banned[1] == next[0]) or (banned[1] == cur[1] and banned[0] == next[0]) :  
                continue
            new_weight = next[1]+cur[0]
            if new_weight < weight[next[0]] : 
                weight[next[0]] = new_weight
                parent[next[0]] = cur[1]
                heappush(hq, [new_weight, next[0]])
        
    return  weight, parent

def restore_path(parent) : 
    # print("parents ", parent)
    path = []
    start = N
    
    while start != -1 :
        path.append(start)
        start = parent[start] 
    path.reverse()

    if path[0] == 1 :
        return path

    return  



N, M = map(int, input().split())
maps = [[] for _ in range(N+1)]
result = 0
# print(maps)

for i in range(M) :
    a, b, t = map(int, input().split())
    maps[a].append([b, t])
    maps[b].append([a, t])

    
weight, path = dijkstra(1, maps, None)
# 1부터 N까지 최소 거리
min_w = weight[-1]
# print(min_w)
# print(weight, path)
path = restore_path(path)
# print(path)


for i in range(len(path)-1) : 
    
    weight, _  = dijkstra(1, maps, [path[i], path[i+1]])
    # print(weight, _)
    # print()
    # print(weight[N])
    if weight[N] == float("inf") : 
        result = -1
        break
    result = max(result, weight[N])

if result == -1 : 
    print(result) 
else : 
    print(result -min_w)






# 세로 : 시작점 # 가로 : 끝점 =