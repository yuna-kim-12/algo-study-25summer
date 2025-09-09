
"""
def solution(tickets):
    answer = []
    return answer
"""

temp = []

def solution(tickets):
    tickets.sort()
    answer = []
    start = find_start(tickets)
    visited = [False]*len(tickets)
    
    visited[start] = True
    answer = dfs(visited, start, ["ICN"], 1, tickets, len(tickets))    

    return answer

def find_start(tickets) :
    for i in range(len(tickets)) :
        if tickets[i][0] == "ICN" : 
            return i
    return i
    
    

def dfs(visited, cur_idx, root, howmanypass, tickets, len_tickets): 

    if howmanypass == len_tickets : 
        # print("yay!", root)
        global temp
        temp.append(root+[tickets[cur_idx][1]])
        return None
    
    for i in range(len_tickets) :
        # print(i)
        if not visited[i] and tickets[cur_idx][1] == tickets[i][0] : 
            visited[i] = True
            # print(root,tickets[cur_idx][1], tickets[i][0],cur_idx, i )
            # print(visited)
            result = dfs(visited, i, root+[tickets[cur_idx][1]], howmanypass+1, tickets, len_tickets)
            if result:
                return result
            visited[i] = False 
    return None
            
tickets = [["ICN","A"], ["ICN","B"], ["A","ICN"], ["B","ICN"], ["ICN","C"]]
# tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
    
print(solution(tickets))
# solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])


