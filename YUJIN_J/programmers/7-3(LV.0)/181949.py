# 대소문자 바꿔서 출력하기

# 문제 설명
# 영어 알파벳으로 이루어진 문자열 str이 주어집니다. 각 알파벳을 대문자는 소문자로 소문자는 대문자로 변환해서 출력하는 코드를 작성해 보세요.

# 느낀점: islower, isupper 완전 까먹고 있다가 새록새록 기억이 난다. if else문도 까먹어서 처음엔 else문에도 조건 달았음.. 기초부터 차근차근 리마인드 하겠습니다~!!


str = input()
for i in str:
    if i.islower():
        print(i.upper(),end='')
    else:
        print(i.lower(),end='')