
def solution(phone_book):
    phone_book.sort()
    dict_p = {}

    for i in phone_book:
        dict_p[i] = 1
    for j in phone_book:
        tmp = ""
        for k in j:
            tmp += k
            if tmp in dict_p and tmp != j:
                return False

    return True

# def solution(phone_book):
#     phone_book.sort()
#     len_p = len(phone_book)
#
#     for i in range(len_p):
#         for j in range(i+1, len_p):
#             if phone_book[i] == phone_book[j][0:len(phone_book[i])]:
#                 return False
#
#     return True
#

print(solution(["119", "97674223", "1195524421"]))
print(solution(["123", "456", "789"]))