# 더 크게 합치기

# 문제 설명
'''
연산 ⊕는 두 정수에 대한 연산으로 두 정수를 붙여서 쓴 값을 반환합니다. 예를 들면 다음과 같습니다.

12 ⊕ 3 = 123
3 ⊕ 12 = 312
양의 정수 a와 b가 주어졌을 때, a ⊕ b와 b ⊕ a 중 더 큰 값을 return 하는 solution 함수를 완성해 주세요.

단, a ⊕ b와 b ⊕ a가 같다면 a ⊕ b를 return 합니다.

제한사항
1 ≤ a, b < 10,000
입출력 예
a	b	result
9	91	991
89	8	898
'''

# 느낀점: 정수에는 슬라이싱이 안 된다는 걸 까먹어서 계속 a[0:],b[0:]을 쓰면서 문제를 풀었다. 계속 통과하질 못해서 gpt 도움을 얻었는데,
# int와 str을 활용하는 문제였다. 그리고 if나 max를 활용하는 문제였다. int와 str을 더 잘 활용해야할 것 같다. 

def solution(a, b):
    ab = int(str(a)+str(b))
    ba = int(str(b)+str(a))
    
    if ab >= ba:
        answer = ab
    else:
        answer = ba
    return answer

# 잘못된 풀이

def solution(a, b):
    if a[0]>b[0]:     
        answer=a*10^len(b)+b
    elif a[0]<b[0]:
        answer=b*10^len(a)+a
    else:
        a1=a*10^len(b)+b
        b1=b*10^len(a)+a
        if a1>=b1:
            answer=a1
        else:
            anser=b1
    return answer