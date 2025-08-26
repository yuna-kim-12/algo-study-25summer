#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// num_list_len은 배열 num_list의 길이입니다.
int* solution(int num_list[], size_t num_list_len, int n) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    int* answer = (int*)malloc(sizeof(int)*num_list_len);
    // for(int i=n; i<num_list_len; i++){
    //     answer[i-n] = num_list[i];
    // }
    // for(int i=0; i<n; i++){
    //     answer[num_list_len - n + i] = num_list[i];
    // }
    int len = num_list_len -n;
    memcpy(answer, &num_list[n], sizeof(int)*len);
    memcpy(answer, &num_list[n], sizeof(int)*n);


    return answer;
}