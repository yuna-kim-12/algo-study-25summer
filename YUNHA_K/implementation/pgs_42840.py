def solution(answers):
    answer_count = [0,0,0]
    supo_1=[1,2,3,4,5]*8*250
    supo_2=[2,1,2,3,2,4,2,5]*5*250
    supo_3=[3,3,1,1,2,2,4,4,5,5]*4*250
    
    len_answers = len(answers)
    
    for i in range(len_answers):
        if answers[i] == supo_1[i]:
            answer_count[0] += 1
        if answers[i] == supo_2[i]:
                    answer_count[1] += 1
        if answers[i] == supo_3[i]:
                    answer_count[2] += 1
    
    answer = []
    max_answer = max(answer_count)
    for i in range(3):
        if max_answer == answer_count[i]:
            answer.append(i+1)
    
    return answer
