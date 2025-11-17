def solution(arr, query):
    answer = arr[:]  
    for i, q in enumerate(query):
        if i % 2 == 0:      
            answer = answer[:q+1]
        else:               
            answer = answer[q:]
    return answer