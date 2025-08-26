def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b :
        parent[b] = a
    else:
        parent[a] = b

def kruskal(V, edges):
    parent = [ i for i in range(V+1)]
    edges.sort()
    min_cost = 0

    for cost, u, v in edges:
        if find(parent, u) != find(parent, v):
            union(parent, u, v)
            min_cost += cost
    return min_cost

T = int(input())
for tc in range(1,T+1):
    V, E = map(int, input().split())
    edges = []
    for _ in range(E):
        u, v, w = map(int, input().split())
        if u != v:
            edges.append((w,u,v))

    result = kruskal(V+1,edges)
    print(f'#{tc} {result}')