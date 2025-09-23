def solution(n, computers):
    graph = [i for i in range(n)]

    def union(x, y):
        x = find(x)
        y = find(y)

        if x > y:
            graph[x] = y
        else:
            graph[y] = x

        return

    def find(x):
        if x != graph[x]:
            graph[x] = find(graph[x])
        return graph[x]

    for i in range(n):
        for j in range(n):
            if computers[i][j]:
                union(i, j)

    for i in range(n):
        graph[i] = find(i)

    answer = len(set(graph))

    return answer


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))