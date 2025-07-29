function solution(A,B){

    let ans = 0;
    // [ 가정 ] 가장 큰값, 가장 작은 값 순으로 곱하고 더하는게 최소값 이다.
    A.sort((a,b) => a - b);
    B.sort((a,b) => b - a);

    for(let i = 0; i < A.length; i++) {
        ans += A[i]*B[i];
    }

    return ans;
//    return A.reduce((total, val, idx) => total + val * B[idx], 0);
}

// 100 : 정확성 69.6 , 효율성 30.4