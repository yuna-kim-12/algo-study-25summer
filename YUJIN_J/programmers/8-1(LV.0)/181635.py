# 홀짝에 따라 다른 값 반환하기
# 문제설명
'''
양의 정수 n이 매개변수로 주어질 때, n이 홀수라면 n 이하의 홀수인 모든 양의 정수의 합을 return 하고 n이 짝수라면 n 이하의 짝수인 모든 양의 정수의 제곱의 합을 return 하는 solution 함수를 작성해 주세요.
'''

# 느낀점: range(시작, 끝, 간격)에서 저 간격부분을 까먹어서 어려웠음. 이젠 배웠다.

def solution(n):
    answer=0
    if n%2==1:
        for i in range(1, n+1, 2):
                answer += i
    else:
        for i in range(2, n+1, 2):
                answer += i*i
    return answer