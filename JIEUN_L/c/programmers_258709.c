#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>


// 1.일단 expectation이 가장 높은 쪽의 숫자를 고르는게 맞다. 
// 2. 따라서 for 문으로 가장 exp 를 게산하도록 하자! 

// 기댓값으로 풀어보니 틀려따...! 다시 방법을 생각해보자!! 포인터 개어렵당.... ㅠ
// 결국 다른 사람 풀이를 보고 힌트를 구하기로 했다. ㄹㅇ 이 양반들도 전부 모든 경우의 수를 계산하는 방식으로 썼네...? 미친 문제여따!
// 1. 가장 먼저 주사위를 절반 뽑는 경우의 수를 계산. rowCrow/2 임. 이걸 미리 계산해줌. 그래야 배열을 미리 만드니까... ㅠ 






int compare(const void* a, const void* b);

// dice_rows는 2차원 배열 dice의 행 길이, dice_cols는 2차원 배열 dice의 열 길이입니다.
int* solution(int** dice, size_t dice_rows, size_t dice_cols) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    int* answer = (int*)malloc(sizeof(int)*(dice_rows/2)); // 일단 일케... 일케 잠시만 두장
    // int temp_arr[dice_rows][2];
    int **temp_arr = malloc(sizeof(int)*dice_rows);
    for(int i=0; i<dice_rows; i++){
        
    }
    // expectation 찾기 
    for(int i=0; i<dice_rows; i++){
        temp_arr[i]= malloc(sizeof(int)*2);
        int temp_sum = 0;
        for(int j=0; j<dice_cols; j++){
            temp_sum += dice[i][j];
        }
        // printf("temp_sum = %d, ", temp_sum);

        
        temp_arr[i][0] = (temp_sum*1000)/dice_cols; // 타입이 더블이 아니므로, 1000을 곱해서 소숫점 아래 3자리를 확인할 수 있도록 함. 
        // printf("expectation = %d \n", temp_arr[i][0]);
        temp_arr[i][1] = i;
    }
    // printf("정렬 전 출력");
    // for(int i=0; i<dice_rows; i++){
    //     printf("%d, %d \n", temp_arr[i][0], temp_arr[i][1]);
    // }
    
    // 이제 여기서 q sort 를 하면 될듯?
    qsort(temp_arr, dice_rows, sizeof(int*),compare);
    // printf("\n정렬 후 출력\n");
    for(int i=0; i<(dice_rows/2); i++){
        // printf("%d, %d, %d \n", i ,temp_arr[i][0], temp_arr[i][1]);
        answer[i] = temp_arr[i][1];
    }

    // printf("\n answer 실제 값 출력 \n");
    // for(int i=0; i<dice_rows; i++){
    //     printf("%d ", answer[i]);
    // }

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

int compare(const void* a, const void* b){
    const int * const * ai = (const int * const *) a;
    const int * const * bi = (const int * const *) b;

    return (**ai<**bi)-(**ai>**bi);
}