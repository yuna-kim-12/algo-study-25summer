from collections import deque

def solution(n, results):
    win_graph = [[] for _ in range(n+1)]  # i가 이긴 사람 목록
    lose_graph = [[] for _ in range(n+1)] # i가 진 사람 목록

    for winner, loser in results:
        win_graph[winner].append(loser)
        lose_graph[loser].append(winner)

    answer = 0
    for player in range(1, n+1):
        win_visited = [False] * (n+1)
        lose_visited = [False] * (n+1)

        deq = deque([player])
        while deq:
            now = deq.popleft()
            for next_p in win_graph[now]:
                if not win_visited[next_p]:
                    win_visited[next_p] = True
                    deq.append(next_p)

        deq = deque([player])
        while deq:
            now = deq.popleft()
            for next_p in lose_graph[now]:
                if not lose_visited[next_p]:
                    lose_visited[next_p] = True
                    deq.append(next_p)

        if (sum(win_visited) + sum(lose_visited)) == n-1:
            answer += 1

    return answer

print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
