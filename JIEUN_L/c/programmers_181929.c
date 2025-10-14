#include <stdio.h>

int solution(const int *num_list, int n) {
    int sum = 0;
    int prod = 1;
    for (int i = 0; i < n; ++i) {
        sum += num_list[i];
        prod *= num_list[i];
    }
    return (prod < sum * sum) ? 1 : 0;
}


int main(void) {
    int a[] = {3,4,5,2,1};
    int b[] = {5,7,8,3};
    printf("%d\n", solution(a, 5)); // 1
    printf("%d\n", solution(b, 4)); // 0
    return 0;
}
