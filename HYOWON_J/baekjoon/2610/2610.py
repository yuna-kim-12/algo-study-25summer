from collections import defaultdict, deque


# 같은 팀 구하기
def bfs(start):
    # 멤버 저장
    member = []
    q = deque()
    q.append(start)
    visited[start] = True

    while q:
        x = q.popleft()
        member.append(x)

        for i in graph[x]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

    return member


# 의사 전달 시간 구하기
def cal(start):
    t_visited = [False] * (n + 1)
    t_visited[start] = True
    q = deque()
    q.append((start, 0))
    result = 0

    while q:
        x, cost = q.popleft()
        result = cost

        for i in graph[x]:
            if not t_visited[i]:
                q.append((i, cost + 1))
                t_visited[i] = True

    return result


n = int(input())
m = int(input())

graph = defaultdict(list)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
# 팀 별 멤버 저장
team = []
for i in range(1, n + 1):
    if not visited[i]:
        team.append(bfs(i))

answer = []

for t in team:
    result = int(1e9)
    leader = t[0]
    # 팀별로 의사 전달 시간 구하기 
    for i in t:
        cost = cal(i)
        # 가장 작은 사람 번호로 갱신 
        if result > cost:
            result = cost
            leader = i

    answer.append(leader)

print(len(answer))
answer.sort()
for i in answer:
    print(i)