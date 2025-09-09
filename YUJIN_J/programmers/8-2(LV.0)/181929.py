# 원소들의 곱과 합
'''
# 문제 설명
정수가 담긴 리스트 num_list가 주어질 때, 모든 원소들의 곱이 모든 원소들의 합의 제곱보다 작으면 1을 크면 0을 return하도록 solution 함수를 완성해주세요.

제한사항
2 ≤ num_list의 길이 ≤ 10
1 ≤ num_list의 원소 ≤ 9
입출력 예
num_list	result
[3, 4, 5, 2, 1]	1
[5, 7, 8, 3]	0
'''
# 느낀점: 곱셈은 선언할 때 0말고 1처리.
def solution(num_list):
    answer = 0
    a=1 #곱셈이니까
    b=0
    for i in range(len(num_list)):
        a*= num_list[i]
        b+= num_list[i]
    if a < b*b:
        answer =1
    elif a > b*b:
        answer =0
    return answer