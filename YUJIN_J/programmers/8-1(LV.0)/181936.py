# 공배수
# 문제설명
# 정수 number와 n, m이 주어집니다. number가 n의 배수이면서 m의 배수이면 1을 아니라면 0을 return하도록 solution 함수를 완성해주세요.

# 느낀잠: 어려움 없이 풀었음

def solution(number, n, m):
    if number%n==0 and number%m==0:
        answer = 1
    else:
        answer = 0
    return answer