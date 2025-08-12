function solution(number) {
    let ans = 0;
    let N = number.length;
    for(let a = 0; a < N; a++) {
        for(let b = a + 1; b < N; b++) {
            for(let c = b + 1; c < N; c++) {
                if(number[a] + number[b] + number[c] == 0) {
                    ans++;
                }
            }
        }
    }
    return ans;
}