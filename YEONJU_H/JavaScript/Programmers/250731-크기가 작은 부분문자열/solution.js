function solution(t, p) {
    let pLeng = p.length;

    let ans = 0;
    for(let i = 0; i < t.length - pLeng + 1; i++) {
        let tmp = t.slice(i,i+pLeng);
        if(Number(tmp) <= Number(p)) {
            ans++;
        }
    }

    return ans;
}