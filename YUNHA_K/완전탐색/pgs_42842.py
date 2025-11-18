def solution(brown, yellow):
    # 1. yello의 약수로 for문을 돌림(1부터 yello까지 나머지가 0인 수)
    for i in range(1,yellow+1):
        if yellow % i == 0:
            num = yellow // i
            # 2. 길이1 : i / 길이2: 약수 / i*2 + ( 약수 + 2 )*2 = brown이면 길이 1, 길이 2 출력
            if i*2 + (num+2)*2 == brown:
                answer = [i+2, num+2]
                answer.sort(reverse=True)
                return answer
