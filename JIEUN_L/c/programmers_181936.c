#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int number, int n, int m) {
    int answer = 0;
    if(number%n ==0 && number%m==0){
        answer= 1;
    }
    return answer;
}

int main(){

    printf("%d", solution(8, 2, 3));
}