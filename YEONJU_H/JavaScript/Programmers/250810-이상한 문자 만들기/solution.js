function solution(s) {
    // 짝수번째 -> 대문자
    // 홀수번째 -> 소문자

    let S = s.split(" ");

    for( let j = 0; j < S.length; j++ ) {
        let newS = "";
        for(let i = 0; i < S[j].length; i++) {
            let tmp = S[j][i];
            if(i % 2 == 0) {
                 newS += tmp.toUpperCase();

            } else {
                 newS += tmp.toLowerCase();
            }
        }
        S[j] = newS;
    }
    ans = S.join(" ");
    return ans;
}