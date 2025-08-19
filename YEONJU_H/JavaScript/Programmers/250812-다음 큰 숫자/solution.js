function solution(n) {
    /*
        n의 다음 큰 수사
        조건 1. n의 다음 큰 숫자 = n보다 큰 자연수
        조건 2. n의 다음 큰 숫자 / n = 2진수로 변환했을 때 1의 갯수가 같습니다.
        조건 3. n의 다음 큰 숫자는 조건 1,2를 만족하는 수 중 가장 작은 수 입니다.

        방법 : 1씩 증가시키면서 check
    */
    let ans = 0;
    let N = n;
    let howMany1 = n.toString(2).split(1).length - 1;
    while(true) {
        N++;
        let nTo2 = N.toString(2);
        let nTo2HowMany1 = nTo2.split(1).length - 1;

        if(howMany1 === nTo2HowMany1 && n < N) {
            ans = N;
            break;
        }
    }

    return ans;
}