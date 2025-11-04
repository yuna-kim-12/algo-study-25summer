#include <stdio.h>

static int concat(int x, int y) {
    // y의 자릿수만큼 10을 곱해 x를 왼쪽으로 밀고 y를 더함
    int factor = 1;
    int t = y;
    while (t > 0) {
        factor *= 10;
        t /= 10;
    }
    return x * factor + y;
}

int solution(int a, int b) {
    int ab = concat(a, b);
    int ba = concat(b, a);
    // 같을 때 a⊕b를 반환해야 하므로 >= 사용
    return (ab >= ba) ? ab : ba;
}

/* 간단한 테스트 */
int main(void) {
    printf("%d\n", solution(9, 91));   // 991
    printf("%d\n", solution(89, 8));   // 898
    printf("%d\n", solution(12, 12));  // 1212 (동일하면 a⊕b)
    return 0;
}
