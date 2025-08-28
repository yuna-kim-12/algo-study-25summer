import sys
input = sys.stdin.readline

# a부터 b까지 dfs로 가서 depth return 하기.
# 친척 관계가 전혀 없으면 -1 출력
def dfs(start_node, depth, visited):
    if start_node == b:
        return depth

    visited[start_node] = True

    for next_node in graph[start_node]:
        if not visited[next_node]:
            result = dfs(next_node, depth + 1, visited)
            if result != -1:
                return result

    return -1

# 입력
N = int(input()) # 전체 사람 수
a, b = map(int, input().split()) # 계산 해야 되는 사람 번호
M = int(input()) #부모 자식 간 관계 개수
visited = [0 for _ in range(N+1)]
graph = [[] for _ in range(N+1)]
parent = [ 0 for _ in range(N+1)]

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
    parent[y] = x

print(dfs(a,0,visited))