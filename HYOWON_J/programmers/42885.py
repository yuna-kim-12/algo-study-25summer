# def solution(people, limit):
#     answer = 0
#     people.sort()
#
#     boat = []
#     for i in range(len(people)):
#         boat.append(people[i])
#         if sum(boat) <= limit and len(boat) <= 2:
#             continue
#         else:
#             answer += 1
#             boat = []
#             boat.append(people[i])
#
#     if boat:
#         answer += 1
#     return answer

def solution(people, limit):
    answer = 0
    people.sort()
    i = 0
    j = len(people) - 1

    while i <= j:
        if people[i] + people[j] <= limit:
            i += 1
        j -= 1
        answer += 1

    return answer

print(solution([70, 50, 80, 50, 30, 40],100))
print(solution([40, 50, 60],100))
print(solution([40, 40, 40, 40], 100))
