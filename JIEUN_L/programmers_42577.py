# 전체 길이만큼 떼서 set에 넣는것. -> 길이가 줄어들면 startswith 가 있는거지 
# 이것도 시간 초과 나올 것 같은데. 

# 그럼, 걍 사전순대로 배열... 
def solution(phone_book):
    answer = True
    phone_book.sort()
    phone_length = len(phone_book)
    for i in range(phone_length-1) : 
        if phone_book[i+1].startswith(phone_book[i]) : 
            return False
    
    return answer





# 효율성 시간 초과
# def solution(phone_book):
#     answer = True
#     phone_book = sorted(phone_book, key=len)
#     phone_length = len(phone_book)
#     for i in range(phone_length-1) : 
#         for j in range(i+1, phone_length) : 
#             if phone_book[j].startswith(phone_book[i]) : 
#                 answer = False
#                 return answer
    
#     return answer



print(solution(["12","123","1235","567","88"]))