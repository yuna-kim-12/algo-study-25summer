
"""
def solution(tickets):
    answer = []
    return answer
"""

def solution(tickets):
    tickets.sort()
    answer = []
    start = 0
    # start_airport = "KKK"
    visited = [False]*len(tickets)
    for i in range(len(tickets)) :
        if tickets[i][0] == "ICN" : 
            # start_airport = tickets[i][1]
            start = i
            break
    
    visited[start] = True
    answer = dfs(visited, start, ["ICN"], 1, tickets, len(tickets))    

    return answer


def dfs(visited, cur_idx, root, howmanypass, tickets, len_tickets): 

    if howmanypass == len_tickets : 
        # print("yay!", root)
        return root+[tickets[cur_idx][1]]
    
    for i in range(len_tickets) :
        if not visited[i] and tickets[cur_idx][1] == tickets[i][0] : 
            visited[i] = True
            root = dfs(visited, i, root+[tickets[cur_idx][1]], howmanypass+1, tickets, len_tickets)
            visited[i] = False 
            if root:
                return root
    
    # print(root, cur_idx)
    # return root

print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
# solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])


