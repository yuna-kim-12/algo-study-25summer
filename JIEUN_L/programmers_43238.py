# 근데 이거 꼭 이진탐색이어야 함? 이거 그냥 비율로 하면 될 것 같은데... 

# 1. a:b만큼의 시간이 차이가 나면 b:a비율로 인원수를 나누어가지는게 맞음.
# 2. 하지만 b:a로 나눠 가진다고 정수가 나올 가능성이 낮으니, 일단 아래 수식대로 계산. 소숫점 떄문에 미리 계산은 금물. 
# round(nb/(a+b)) : round(na/(a+b))
# 여기서 a+b = n인지 확인하고, n보다 작다면a에 하나를 추가하고, n보다 크다면 b에서 하나를 뺸다.
# 3. 일단 저 round후 int 로 바꿔서 일단 정수로 바꾸지만,소숫점 때문에 틀릴 수도 있으니 한가지 추가 작업을 더 함. a-1, a+1 의 경우에 대해서도 계산을 해서최소를 재확인 하는 것. 




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

    minus_1,plus_1 = 0, 0

    answer = max(times[0]*counter_1, times[1]*counter_2)
    minus_1 = max(times[0]*(counter_1-1) , times[1]*(counter_2+1))
    plus_1 = max(times[0]*(counter_1+1), times[1]*(counter_2-1))

    # print(answer, minus_1, plus_1)


    return min(answer, minus_1, plus_1)


print(solution(6, [7, 10]))