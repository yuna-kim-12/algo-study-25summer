from itertools import permutations
def solution(numbers):
    answer = ''
    comb = list(permutations(numbers, len(numbers)))
    comb.sort(reverse=True)
    for i in range(len(comb[0])) : 
        answer += comb[0][i]
    # print(answer)
    return answer

solution(["6", "10", "2"])