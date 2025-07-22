# 문자열 겹쳐쓰

'''
문제 설명:
문자열 my_string, overwrite_string과 정수 s가 주어집니다.
문자열 my_string의 인덱스 s부터 overwrite_string의 길이만큼을 문자열 overwrite_string으로 바꾼 문자열을 return 하는 solution 함수를 작성해 주세요.

제한사항:
- my_string와 overwrite_string은 숫자와 알파벳으로 이루어져 있습니다.
- 1 ≤ overwrite_string의 길이 ≤ my_string의 길이 ≤ 1,000
- 0 ≤ s ≤ my_string의 길이 - overwrite_string의 길이

입출력 예
my_string	overwrite_string	s	result
"He11oWor1d"	"lloWorl"	2	"HelloWorld"
"Program29b8UYP"	"merS123"	7	"ProgrammerS123"
'''

# 느낀점: 와 처음에 함수쓰라고 해서 당황함.. 옛날부터 함수쓰는게 참 어렵다. 별다를 건 없는데 더 복잡한 느낌..
# 처음에는 인덱싱 끝부분의 자리는 포함 안 된다는 걸 까먹고 계속 s1=my_string[0:s-1], s2=my_string[l+s:-1]로해서 마지막 글자가 잘렸다.
# 이후 맨 끝 인덱싱은 포함 안 된다는 걸 알고 마지막엔 +1을 하고, :을 쓰면 끝까지 다 가져오는 걸 알아서 수정했다. 개념을 잘 기억해야겠다.

def solution(my_string, overwrite_string, s):
    l=len(overwrite_string)

    s1=my_string[0:s]
    s2=my_string[l+s:]
    
    answer = s1+overwrite_string+s2
    return answer
