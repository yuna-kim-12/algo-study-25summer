from collections import defaultdict

def solution(clothes):
    answer = 1
    dict_c = defaultdict(list)
    for i, j in clothes:
        dict_c[j].append(i)

    for items in dict_c.values():
        answer *= (len(items)+1)

    return answer - 1

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))