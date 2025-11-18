def solution(id_pw, db):
    answer = 'fail'
    id, pw = id_pw
    for lst in db:
        id_check, pw_check = lst
        if id == id_check:
            if pw == pw_check:
                answer = 'login'
                return answer
            else:
                answer = 'wrong pw'
    return answer