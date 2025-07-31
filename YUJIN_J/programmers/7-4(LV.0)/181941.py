# 문자 리스트를 문자열로 변환하기

# 문제 설명
'''
문자들이 담겨있는 배열 arr가 주어집니다. arr의 원소들을 순서대로 이어 붙인 문자열을 return 하는 solution함수를 작성해 주세요.

제한사항
1 ≤ arr의 길이 ≤ 200, arr의 원소는 전부 알파벳 소문자로 이루어진 길이가 1인 문자열입니다.

입출력 예
arr	result
["a","b","c"]	"abc"
'''

# 느낀점: 이번 문제는 꽤 평이했다. for문과 += 기호만 잘 쓰면 됐다. 이전에 푼 문자열섞기 문제를 떠올리면서 range를 사용한 것도 풀어봤다.
# 다른 사람들은 join을 활용해서 풀던데, 아직 join을 쓰기는 어려운 것 같다. for문과 range를 더 능숙하게 쓴 다음에 join을 활용해야겠다.

# 첫번째 풀이
def solution(arr):
    answer = ''
    for i in arr:
        answer += i
    return answer

# 두번째 풀이
def solution(arr):
    answer = ''
    for i in range(0,len(arr)):
        answer += arr[i]
    return answer

