# 덧셈식 출력하기

# 문제 설명
# 두 정수 a, b가 주어질 때 다음과 같은 형태의 계산식을 출력하는 코드를 작성해 보세요. a + b = c

# 느낀점: f스트링 까먹고 있어서 계속 print('a+b=c') 로 하고 있었음.. 그래도 한 번 푸니까 생각난다.

a, b = map(int, input().strip().split(' '))
c = a+b
print(f'{a} + {b} = {c}')