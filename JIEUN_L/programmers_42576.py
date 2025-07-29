# 다른 사람 풀이다. collections.Counter 쓰는게 낫겠다. 

from collections import Counter
def solution(participant, completion):
    answer = Counter(participant)-Counter(completion)
    return list(answer.keys())[0]


print(solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"]))



