import sys
sys.stdin = open('1613.txt')

def fw(n, graph):

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if graph[i][k] and graph[k][j]:
                    graph[i][j] = 1

    return graph


n, k = map(int, input().split())
graph = [[0 for _ in range(n+1)] for _ in range(n+1)]

for _ in range(k):
    a, b = map(int, input().split())
    graph[a][b] = 1

s = int(input())

fw(n, graph)

for _ in range(s):
    case1, case2 = map(int, input().split())
    if graph[case1][case2]:
        print(-1)
    elif graph[case2][case1]:
        print(1)
    else:
        print(0)
