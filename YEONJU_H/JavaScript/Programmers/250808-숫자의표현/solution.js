function solution(n) {
    let count = 0;
    let start = 1;
    let end = 1;
    let sum = 1;

    while(end <= n) {
        if(sum === n) {
            count++;
            sum -= start++;
        } else if(sum < n) {
            sum += ++end;
        } else { // sum > n
            sum -= start++;
        }
    }

    return count;
}