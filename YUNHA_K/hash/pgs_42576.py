participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]

from collections import Counter
# 1. 완주하지 못한 선수의 이름을 return
participant_counter = Counter(participant)
completion_counter = Counter(completion)

print(participant_counter.keys(), completion_counter)

result = ''

for key in participant_counter.keys():
    try:
        if participant_counter[key] != completion_counter[key]:
            result = key
            break
    except:
        result = key

print(result)