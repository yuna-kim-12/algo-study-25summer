import sys
sys.stdin = open('n.txt')

n, m = map(int, input().split())
INF = 10**9
arr = [[INF]*(n+1) for _ in range(n+1)]

#끊어진 곳이면 INF로 갈수없게하기
for _ in range(m):
    u, v, b = map(int, input().split())
    if b == 1:
        arr[u][v] = 0
        arr[v][u] = 0
    #단방향인 경우
    else :
        arr[u][v] = 0
        arr[v][u] = 1

for i in range(1, n+1):
    arr[i][i] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if arr[i][j] > arr[i][k] + arr[k][j]:
                arr[i][j] = arr[i][k] + arr[k][j]

k = int(input())
for _ in range(k):
    s, e = map(int, input().split())
    print(arr[s][e])