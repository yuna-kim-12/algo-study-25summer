# 디스크 컨트롤러 
# 1. 먼저 받아놓은 작업 큐를 정렬함. 물론 1번 인덱스까지 포함해서 정렬!
# 2. 최소 힙을 구현해놓음. 여기다가 작업 넣을것.
# 3. 변수는 index(0에서 시작), 현재 시간(0에서 시작), 작업시간 합쳐놓은것들(0에서 시작 평균 계산하게
# for문으로 인덱스를 리스트 안에 집어넣어줌.
# 최소 heap 으로 전부 다 때려박음

# for 문으로 하나씩 빼면서 확인
#   뺴서 현재 시각 확인하고 현재 시간에 작업 시간을 더해서 할당해줌
#   현재 시간에서 요청 시간을 뺸걸 총 작업시간 합산 변수에 더해줌 
#   heap에 하나도 남지 않을 때 까지 반복
# 

from heapq import heapify, heappop, heappush

def solution(jobs):
    answer = 0 # 총 작업 시간을 여기에 더할 예정
    index, current_time, job_cnt = 0, 0, len(jobs)
    
    for i in range(job_cnt) : 
        jobs[i].append(i)
    
    # jobs : 작업이 요청되는 시간, 작업 소요 시간, 작업 번호
    jobs.sort() 

    # 작업 시간, 요청 시간, 일 순으로 heap에 집어넣음.)
    h = []
    heapify(h)
    # current_time = jobs[index][0]

    while index < job_cnt or h : 
        while index < job_cnt and jobs[index][0] <= current_time : 
            heappush(h, [jobs[index][1],jobs[index][0],jobs[index][2]] )
            print(h)
            index += 1

        if h : 
            cur_job = heappop(h)
            current_time += cur_job[0]
            answer += current_time-cur_job[1]
            print(f"current_time = {current_time}, answer = {answer}, cur_job = {cur_job}")
        
        else : 
            current_time = jobs[index][0]
            
            
    print(f"totoal answer = {answer}")
    return answer //job_cnt


print(solution([[0, 3], [100, 9], [101, 8]]))