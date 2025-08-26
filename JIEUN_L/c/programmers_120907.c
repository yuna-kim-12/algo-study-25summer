#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <ctype.h>

// quiz_len은 배열 quiz의 길이입니다.
// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
char** solution(const char* quiz[], size_t quiz_len) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    char** answer = (char**)malloc(sizeof(char)*quiz_len);
    char operator = NULL;
    bool equal = false;
    int start = 0;
    for(int i=1; i<quiz_len; i++){
        if(operator == NULL & !isdigit(quiz[i])){
            operator = quiz[i]
        }
    }
    return answer;
}