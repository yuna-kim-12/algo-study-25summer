from itertools import permutations

def solution(numbers):
    numbers = list(map(str, numbers))
    perm = list(permutations(numbers, len(numbers)))
    perm_join =  []
    # print(perm)

    for i in range((len(perm))) : 
        temp = ''
        for j in range(len(perm[0])) : 
            temp += perm[i][j]
        perm_join.append(temp)
    

    # numbers.sort(reverse=True)
    # print(perm_join)
    perm_join.sort(reverse=True)
    
    # print(answer)
    return perm_join[0]



# numb =  [6, 10, 2]	#"6210"
numb =  [3, 30, 34, 5, 9]	#"9534330"

print(solution(numb))


