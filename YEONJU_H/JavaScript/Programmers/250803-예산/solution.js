function solution(d, budget) {
    // 부서별로 최대한 많은 부서 물품을 구매해줄 수 있도록 한다
    // 물품 구매 시에는 각 부서가 신청한 금액 만큼 지원
    // 부서별 신청 금액이 있는 배열 d와 예산 budget이 매개변수로 주어질 때, 최대 몇 개의 부서에 물품을 지원할 수 있는지
    // 아이디어 모든 경우의 수를 더해본다

    d.sort((a, b) => a-b);
    let sum = 0;
    let cnt = 0;
    for(let i = 0; i < d.length; i++) {
        sum += d[i];
        if(sum > budget) { break }
        else { cnt++};
    }

    return cnt;
}