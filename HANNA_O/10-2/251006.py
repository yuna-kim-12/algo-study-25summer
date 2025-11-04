# programmers 모의고사 (완전탐색)

# 아이디어
# 1. 1-3번 수포자의 찍는 방식 리스트 만들기
# 2. 시험 문제 답과 찍는 방식 리스트를 비교하기
# 2-1. 찍는 번호와 답이 같으면 카운트 +1, 다르면 지나가기
# 3. 카운트가 가장 놓은 수포자 출력하기

def solution(answers):
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    cnt = [0] * 3

    for i, a in enumerate(answers):
        if a == p1[i % len(p1)]:
            cnt[0] += 1

        if a == p2[i % len(p2)]:
            cnt[1] += 1

        if a == p3[i % len(p3)]:
            cnt[2] += 1

    maxi = max(cnt)
    answer = []

    for i in range(3):
        if cnt[i] == maxi:
            answer.append(i + 1)

    return answer