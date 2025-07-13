# dfs로 굴려보자! 

# 1. for문으로 target 단어가 있는지 검사
# 1.1 만일 있다면 DFS 함수 실행, 없다면 그대로 0을 리턴함

# 2. FOR문에서 단어가 있는 경우 
# 2.1 재귀 함수로 부름. 

# 재귀함수(dfs)
# VISITED, WORDS, INDEX, cnt 를 넘겨줌
# 종료 조건 : 글자를 찾았다면 CNT를 글로벌로 넘기고 종료
# 종료 조건 : 만일 CNT 가 WORDS의 갯수만큼 돌았는데 못갔으면 걍 0 리턴
# FOR문에서 단어의 글자 한개만 변경되었으면서, 방문하지 않았던 경우 Dfs 호출
# FOR문에서 만일 VISITED가 아니면 dfs호출하면서, 해당 위치를 vISITED 처리 & index & cnt +1를 변수 넘겨줌
# 만일 FOR문을 돌았는데 방문할 곳이 없다면 0 리턴.

count = 60

def DFS(target, current, len_word, len_wordlist,visited, words, index, cnt) : 
    global count
    if current == target : 
        count = min(count, cnt)
        # print("current == target and the count is", count, cnt)
        return 
    if cnt == len_wordlist : 
        # print("cnt == len_wordlist")
        count = 0
        return 
    
    
    next = ""
    for i in range(len_wordlist) :
        wrong = 0
        # print(f"{i} is the current index and {current} is current word")
        if visited[i] : #방문한 적이 있다면 pass 
            continue
        next = words[i] # 매번 주소값 2번 참조하기보단 그냥 할당해버림.. 두번 참조하는게 나으려나
        for j in range(len_word) : 
            if current[j] != next[j] :
                wrong += 1
                if wrong > 1 :
                    break 
                
        if wrong == 1: 
            # print(f"here we are, wrong 1, and heading to {words[i]}")
            visited[i] = True           
            DFS(target, next, len_word, len_wordlist, visited, words, i, cnt+1)
            visited[i] = False
    
    # count = 0 # 이게 맞으려나? 
    return 0


def solution(begin, target, words):

    if target not in words : 
        return 0
    else :
        DFS(target, begin, len(begin), len(words), [False]*len(words), words,0, 0)
        return count
    
words = ["hit", "hot"]
print(solution("hut", "hot", words))
# words = ["hot", "dot", "dog", "lot", "log", "cog"]
# print(solution("hit", "cog", words))
