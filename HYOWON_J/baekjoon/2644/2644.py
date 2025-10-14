import sys
sys.stdin = open("n.txt")

n = int(input())
a, b = map(int, input().split())
m = int(input())
g = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    g[x].append(y)
    g[y].append(x)


def dfs(start, count):
    if start == b:
        return count

    visited[start] = 1

    for next in g[start]:
        if visited[next] == 0:
            # 값 반환하고 전달해야함.
            ans = dfs(next, count+1)
            if ans:
                return ans

    return False

answer = dfs(a, 0)

if answer:
    print(answer)
else:
    print(-1)