import sys
input = sys.stdin.readline

# 현재 Queue의 가장 앞에 있는 문서의 ‘중요도’를 확인한다.
# 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면,
# 이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치 한다. 그렇지 않다면 바로 인쇄를 한다.

def find_order(docs):
    from collections import deque, Counter
    order = 1
    priority = Counter(docs)
    queue = deque([])
    # 인덱스랑, 중요도를 같이 기록한 queue
    for idx, val in enumerate(docs):
        queue.append((val, idx))

    while queue:
        # key 중에 가장 큰 값 : 우선 순위
        if priority[max(priority.keys())] > 0:
            max_priority = max(priority.keys())
        else:
            priority.pop(max(priority.keys()))
            max_priority = max(priority.keys())

        pri, idx = queue.popleft()
        # 우선순위보다 내 값이 작으면, 뒤로 삽입.
        # pop한 값의 인덱스가 M과 같으면, 순서를 print(order = 1 )에서 부터 갱신.
        if pri == max_priority:
            if idx == M:
                return order
            priority[max_priority] -= 1
            order += 1
            continue
        else:
            queue.append((pri,idx))


def optimized_ver(docs,target):
    from collections import deque
    order = 0
    queue = deque([])
    for idx, val in enumerate(docs):
        queue.append((val, idx))

    while queue:
        pri, idx = queue.popleft()
        if any( p > pri for p, _ in queue ):
            queue.append((pri, idx))
        else:
            order += 1
            if idx == target:
                return order

T = int(input())
for _ in range(T):
    N, M = map(int, input().split()) # 맨 왼쪽은 0번째
    docs = list(map(int, input().split()))
    # print(find_order(docs))
    print(optimized_ver(docs,M))