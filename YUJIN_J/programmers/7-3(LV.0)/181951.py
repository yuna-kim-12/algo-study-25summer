# a와 b 출력하기

# 문제 설명
# 정수 a와 b가 주어집니다. 각 수를 입력받아 입출력 예와 같은 형식으로 출력하는 코드를 작성해 보세요.

# 입출력 예
# 입력
# 4 5

# 출력
# a = 4
# b = 5

# 느낀점: 줄바꿀때 /n을 사용하는 건 나중에 다른사람 풀이를 보고 알았다. 너무 하드코딩인가 싶지만, 일단 푼대로 올린다...

a, b = map(int, input().strip().split(' '))
print('a =', a)
print('b =', b)