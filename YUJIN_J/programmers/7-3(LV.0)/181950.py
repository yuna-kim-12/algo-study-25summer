# 문자열 반복해서 출력하기

# 문제 설명
# 문자열 str과 정수 n이 주어집니다. str이 n번 반복된 문자열을 만들어 출력하는 코드를 작성해 보세요.

# 입출력 예
# 입력 #1 string 5
# 출력 #1 stringstringstringstringstring

# 느낀점: 이건 수월하게 풀었다. 입력 받는 것만 다시 익히는 느낌.

str, n = input().strip().split(' ')
n = int(n)
print(str*n)