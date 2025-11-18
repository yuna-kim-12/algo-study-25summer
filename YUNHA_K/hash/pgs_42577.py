def solution(phone_book):
    phone_book.sort()
    s = set(phone_book)
    for phone in phone_book:
        for i in range(1,len(phone)):
            cut_phone = phone[:i]
            if cut_phone in s:
                return False
    return True