function solution(n, m) {

    let i = 0, minAns = 0, maxAns = 0;

    while(true) {
        if(i > Math.max(n,m)/2) break;
        if(n % i == 0 && m % i == 0) {
            minAns = i;
        }
        i++;
    }

    maxAns = (m/ minAns * n) ;
    return [minAns, maxAns];
}