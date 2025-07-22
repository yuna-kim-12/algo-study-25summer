# 문자열 붙여서 출력하기

'''
# 문제 설명
  두 개의 문자열 str1, str2가 공백으로 구분되어 입력으로 주어집니다.
  입출력 예와 같이 str1과 str2을 이어서 출력하는 코드를 작성해 보세요.

# 입출력 예
  입력 #1 apple pen
  출력 #1 applepen
'''

# 개념 정리 
# input(): 사용자에게 입력받음.
# .strip(): 입력한 문자열의 앞 뒤 공백 제거
# .split(' '): 문자열을 공백 기준으로 나눠서 리스트로 반환

str1, str2 = input().strip().split(' ')
print(str1+str2)