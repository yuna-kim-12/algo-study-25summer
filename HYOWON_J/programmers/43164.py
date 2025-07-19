## 이 방법은 알파벳 순서대로 다음 경로 찾는건 잘함. 근데 그 다음 경로가 계속 이어지는지는 알 수 없음
# def solution(tickets):
#     answer = []
#     answer.append("ICN")
#     check = [False] * len(tickets)
#     route = []
#     route.append("ICN")
#
#     while tickets:
#         now = route.pop()
#         next = []
#         for i in range(len(tickets)):
#             if now == tickets[i][0] and check[i] == False:
#                 next.append([tickets[i][1], i])
#
#         if len(next) == 1:
#             route.append(next[0][0])
#             answer.append(next[0][0])
#             check[next[0][1]] = True
#
#         elif len(next) > 1:
#             next_sorted = sorted(next, key= lambda x: x[0][0])
#             route.append(next_sorted[0][0])
#             answer.append(next_sorted[0][0])
#             check[next_sorted[0][1]] = True
#
#         else:
#             break
#
#     return answer

#DFS
def solution(tickets):
    #처음부터 정렬
    tickets.sort()
    visited = [False] * len(tickets)
    path = ["ICN"]

    def DFS(now, cnt):
        if cnt == len(tickets):
            return path
        for i, (a, b) in enumerate(tickets):
            if not visited[i] and a == now:
                visited[i] = True
                path.append(b)
                result = DFS(b, cnt+1)
                if result:
                    return result
                path.pop()
                visited[i] = False

    return DFS("ICN", 0)

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
print(solution([["ICN", "A"], ["A", "B"], ["B", "ICN"], ["ICN", "A"], ["A", "C"]]))