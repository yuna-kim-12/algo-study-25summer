
def dfs(n):
    global answer
    # 종료 조건
    if n == N:
        answer += 1
        return

    for j in range(N):
        if V1[j] == V2[n+j] == V3[n-j+N-1] == 0:
            V1[j], V2[n+j], V3[n-j+N-1] = 1, 1, 1
            dfs(n+1)
            V1[j], V2[n+j], V3[n-j+N-1] = 0, 0, 0

N = int(input())
answer = 0
V1 = [0]*N
V2 = [0]*(2*N-1)
V3 = [0]*(2*N-1)

dfs(0)
print(answer)

import sys

input = sys.stdin.readline


def dfs(i):
    global answer

    if i == N:
        answer += 1
        return

    for j in range(N):
        if v1[j] == v2[i + j] == v3[i - j + N - 1] == 0:
            v1[j] = v2[i + j] = v3[i - j + N - 1] = 1
            dfs(i + 1)
            v1[j] = v2[i + j] = v3[i - j + N - 1] = 0


N = int(input())
v1 = [0] * N
v2 = [0] * (2 * N - 1)
v3 = [0] * (2 * N - 1)
answer = 0

dfs(0)
print(answer)

