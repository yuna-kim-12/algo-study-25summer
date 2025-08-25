#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int n, int w, int num) {
    int answer = 0;
    int num_col, row,num_row, leftover, col_leftover,start=-1, end = -1;

    row = n/w;
    leftover = n%w;
    col_leftover = (num-1)%w;  // 인덱스 수정

    // 만약에 남는게 있다면?
    if(leftover > 0){
        row +=1; // 이게 실제 행의 갯수, 즉 높이임.
        if(row%2== 0){
            // 반대방향
            end = w-1;
            start = w-leftover;
            // printf("%d, %d, %d", row, start, leftover);
        }
        else{
            // 제 방향 
            end = leftover-1;
            start = 0;
        }
    }

    // 남는게 없다면 그냥 row 그대로 가면 되는 노릇임. 
    
    num_row = (num-1) /w;  // 인덱스 수정


    printf("num dividedd by w = %d \n",leftover);
    if(num_row %2 != 0){
        // 반대 방향인 것.
        num_col = w-1-col_leftover;
        printf("w = %d, num_col = %d leftover = %d \n", w, num_col, col_leftover);
    } 
    else{
        // 제 방향인 것. 
        num_col = col_leftover;
    }
    
    //만약 전체 블록 중에 남는 블록이 없다면 그냥 높이만 재도 그만임. 
    if(end != -1 && num_row == row - 1 && (num_col < start || num_col > end)){
        answer = row - 1 - num_row;
    }
    else{
        // printf("here we are, \n");
        answer = row - num_row;
    }

    printf("row = %d, col = %d, num_row = %d, num_col = %d, start = %d, end = %d \n",row, w, num_row, num_col, start, end);

    return answer;
}

int main(){
    int ans = 0;
    ans = solution(22, 6, 13);
    printf("%d", ans);
}