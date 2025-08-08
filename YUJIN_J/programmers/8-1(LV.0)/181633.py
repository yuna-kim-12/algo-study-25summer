# flag에 따라 다른 값 반환하기
# 문제설명
# 두 정수 a, b와 boolean 변수 flag가 매개변수로 주어질 때, flag가 true면 a + b를 false면 a - b를 return 하는 solution 함수를 작성해 주세요.

# 느낀점: 'true'처럼 첫글자를 소문자로 쓰면 안 된다. True라고 쓰거나 아니면 안 쓰고 : 로만 쓰는 것이 제법 파이썬같은 방법.

def solution(a, b, flag):
    if flag == True:
        answer = a+b
    else:
        answer = a-b
    return answer