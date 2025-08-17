#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>


// 1.일단 expectation이 가장 높은 쪽의 숫자를 고르는게 맞다. 
// 2. 따라서 for 문으로 가장 exp 를 게산하도록 하자! 

int compare(const void* a, const void* b);

// dice_rows는 2차원 배열 dice의 행 길이, dice_cols는 2차원 배열 dice의 열 길이입니다.
int* solution(int** dice, size_t dice_rows, size_t dice_cols) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    int* answer = (int*)malloc(sizeof(int)*dice_rows); // 일단 일케... 일케 잠시만 두장
    // int temp_arr[dice_rows][2];
    int **temp_arr = malloc(sizeof(int)*dice_rows);
    for(int i=0; i<dice_rows; i++){
        
    }
    // expectation 찾기 
    for(int i=0; i<dice_rows; i++){
        temp_arr[i]= malloc(sizeof(int)*dice_cols);
        int temp_sum = 0;
        for(int j=0; j<dice_cols; j++){
            temp_sum += dice[i][j];
            // printf("%d ", dice[i][j]);
        }

        // printf("\n");
        temp_arr[i][0] = temp_sum/dice_cols;
        temp_arr[i][1] = i;
    }
    // 이제 여기서 q sort 를 하면 될듯?
    qsort(temp_arr, dice_rows, sizeof(int*),compare)

    return answer;
}

int main(){
    int initial[4][6] = {
        {1,2,3,4,5,6}, 
        {1,3,3,4,4,4}, 
        {1,3,3,4,4,4}, 
        {1,1,4,4,5,5}
    };
    int *dice[4];
    for (int i=0; i<4; i++){
        dice[i] = initial[i];
    }

    int *result = solution(dice, 4, 6);
    printf("%d",*result);
    return 0;

}

int compare(const void* a, const void*b){
    int x = *(const int)a;
    int y = *(const int)b;

    return (x>y) - (x<y);
}