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

from heapq import heapify, heappop

def solution(jobs):
    answer = 0 # 총 작업 시간을 여기에 더할 예정
    index, current_time, job_cnt = 0, 0, len(jobs)
    
    for i in range(job_cnt) : 
        jobs[i].append(i)
    
    # jobs : 작업이 요청되는 시간, 작업 소요 시간, 작업 번호

    heapify(jobs)
    
    
    while jobs:
        cur_job = heappop(jobs)
        print(cur_job)
        if current_time >= cur_job[0] :
            print("case 1, current_time : ", current_time+cur_job[1]," job_cnt : ",  (cur_job[0]-current_time)+cur_job[1])
            current_time += cur_job[1]
            
            job_cnt += (current_time-cur_job[0])+cur_job[1]
        else : 
            current_time = cur_job[0]+ cur_job[1]
            job_cnt += cur_job[1]
    
    print(job_cnt)


    return answer


solution([[0, 3], [1, 9], [3, 5]])