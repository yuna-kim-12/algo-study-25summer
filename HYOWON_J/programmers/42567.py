def solution(participant, completion):
    dic = {}
    for p in participant:
        dic[p] = dic.get(p,0) + 1

    for c in completion:
        dic[c] -= 1

    for k, v in dic.items():
        if v > 0 :
            return k



print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "mislav", "mislav"]))