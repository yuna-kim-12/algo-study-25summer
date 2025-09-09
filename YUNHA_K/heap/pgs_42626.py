def solution(scoville, K):
    import heapq
    answer = 0

    heapq.heapify(scoville)

    # 1. 스코빌 지수를 힙에 일단 넣어
    while len(scoville) > 1:
        first_food = heapq.heappop(scoville)
        # 2. 첫 번째 원소의 스코빌 지수가 K보다 작다면
        if first_food < K:
            # 2-1. 첫 번째, 두 번째 음식의 스코빌 지수 합을 구해서 다시 힙에 넣는다.
            second_food = heapq.heappop(scoville)
            mixed_food = first_food + second_food * 2
            heapq.heappush(scoville, mixed_food)
            # 넣은 후 answer += 1
            answer += 1
        # 3. 첫번 째 원소의 스코빌 지수가 K보다 크거나 같다면, answer 값 return
        else:
            return answer
    # 4. 예외) 원소가 1개인데, K이상이 아니라면, -1 return
    if scoville[0] < K:
        return -1
    return answer