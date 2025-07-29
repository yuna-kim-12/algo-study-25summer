# 문자열 섞기

# 문제 설명
'''
길이가 같은 두 문자열 str1과 str2가 주어집니다.
두 문자열의 각 문자가 앞에서부터 서로 번갈아가면서 한 번씩 등장하는 문자열을 만들어 return 하는 solution 함수를 완성해 주세요.

제한사항
1 ≤ str1의 길이 = str2의 길이 ≤ 10
str1과 str2는 알파벳 소문자로 이루어진 문자열입니다.
입출력 예
str1	str2	result
"aaaaa"	"bbbbb"	"ababababab"
'''

# 느낀점
# for문을 사용해야한다는 것은 알았는데, range를 떠올리지못해서 계속 막혔었다. 다른 사람의 풀이를 참고하고나서, range가 생각났고 적용해서 풀었다.
# for문을 사용하는 문제는 range가 많이 사용됐던 것 같다. 앞으로 잘 익혀야겠다.

def solution(str1, str2):
    answer = ''
    for i in range(0,len(str1)):
        answer += str1[i]+str2[i]
    return answer