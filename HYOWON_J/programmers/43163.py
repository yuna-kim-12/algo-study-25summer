from collections import deque

def solution(begin, target, words):
    answer = 0
    if target not in words:
        return answer

    arr = deque()
    arr.append([begin, 0])

    while arr:
        now, cnt = arr.popleft()

        if now == target:
            return cnt

        for word in words:
            now_list = list(now)
            word_list = list(word)
            if len(set(now_list + word_list)) <= len(now) + 1:
                arr.append([word, cnt + 1])


begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(begin, target, words))
begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log"]
print(solution(begin, target, words))