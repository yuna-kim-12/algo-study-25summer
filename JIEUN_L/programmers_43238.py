# 걍 쉬운 방법써봐야지 하.....


# 1. 이전에 비율로 짠 코드의 인원수로 시작한다. 
# 2. 비율로 최적해 비슷한걸 찾고, 양쪽으로 본다.

def solution(n, times):
    answer = 0

    if n == 1 : 
        return min(times[1], times[0])

    counter_1 = round(n*times[1]/(times[1]+times[0]))
    counter_2 = round(n*times[0]/(times[1]+times[0]))

    if counter_1 + counter_2 > n : 
        if counter_1 >= counter_2 : 
            counter_1 = counter_1 - (counter_2 + counter_1 -n)
        else : 
            counter_2 = counter_2 - (counter_2 + counter_1 -n)
    elif counter_1 + counter_2 < n :
        if counter_1 >= counter_2 : 
            counter_2 = counter_2 + n-(counter_2 + counter_1)
        else : 
            counter_1 = counter_1 + n-(counter_2 + counter_1)

    # 일단은 갯수는 맞춰줌.

    # minus_1,plus_1 = 0, 0

    answer = max(times[0]*counter_1, times[1]*counter_2)
    # minus_1 = max(times[0]*(counter_1-1) , times[1]*(counter_2+1))
    # plus_1 = max(times[0]*(counter_1+1), times[1]*(counter_2-1))

    # print(answer, minus_1, plus_1)

    # 여기서 이제 양쪽으로 탐색해가는거지.
    
    while counter_1 >= 2  : 
        counter +=1 
        pass
        


    # return min(answer, minus_1, plus_1)
