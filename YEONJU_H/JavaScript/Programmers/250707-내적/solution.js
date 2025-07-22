function solution(a, b) {
    // let arrLength = a.length;
    let sum = 0;
//     for(let i = 0; i < arrLength; i++) {
//         sum += a[i] * b[i];
//     }
    
    return a.reduce((sum, curr, idx) => sum += curr * b[idx], 0);
    // return sum;
}

// 근소한 차이로 for문이 좀더 빠름