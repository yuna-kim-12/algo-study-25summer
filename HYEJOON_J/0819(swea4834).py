# 숫자카드
# 8:43~ 
# 입력: 0~9 숫자의 N장 카드와 N 개의 숫자
# 출력: 가장 많은 카드에 적힌 숫자와 장 수 
# 조건: 카드 장수 같을 경우 더 큰 숫자 출력

for tc in range(1,int(input())+1):
    N = int(input())
    nums_str = input()
    nums_lst = [int(n) for n in nums_str] 
    cards = [0] * 10
    
    
    max_count = 0 
    max_num = -1 
    for i in nums_lst:
        cards[i] += 1 
    
    for j in range(10):
        if cards[j] >= max_count:
            max_count = cards[j]
            if j > max_num:
                max_num = j 

    print(f"#{tc}", max_num, max_count )