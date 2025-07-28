


def solution(tickets):
    answer = []
    start = 0
    start_airport = "KKK"
    visited = [False]*len(tickets)
    for i in range(len(tickets)) :
        if tickets[i][0] == "ICN" : 
            if tickets[i][1] <= start_airport : 
                start = i
                start_airport = tickets[i][1]
    
    visited[start] = True
    print(start)
    print(start_airport)
    dfs(visited, start, ["ICN", start_airport], 1, tickets, len(tickets))    


    return answer


def dfs(visited, cur_idx, root, howmanypass, tickets, len_tickets): 
    if howmanypass == len_tickets : 
        print("yay!", root)
        return root
    
    for i in range(len_tickets) : 
        if not visited[i] and tickets[cur_idx][1] == tickets[i][1] : 
            visited[i] = True
            dfs(visited, i, root.append(tickets[cur_idx][1]), howmanypass+1, tickets, len_tickets)
            visited[i] = False 
    
print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
# solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])


