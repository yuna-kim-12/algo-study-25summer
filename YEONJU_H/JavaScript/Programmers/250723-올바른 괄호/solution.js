function solution(s){
    // stack 사용
    let ans = true;
    let stack = [];
    for(let char of s) {
        if(char === '(') {
            stack.push(char);
        } else if(char === ')') {
            if(stack.length === 0) {
                ans = false;
            }
            stack.pop();
        }
    }

    if(stack.length !== 0 ) {
        ans = false;
    }

    // 만약 (가 나오면 뒤에 짝이 맞는 )가 있는지 체크하고 방문처리 : 이중포문으로 효율성 0..
//     let sLeng = s.length;
//     let checked = new Array(sLeng).fill(false);

//     for(let i = 0; i < sLeng; i++) {
//         if( s[i] === '(' && !checked[i] ) {
//             for(j = i; j < sLeng; j++) {
//                 if(s[j] === ')' && !checked[j]) {
//                     checked[i] = true;
//                     checked[j] = true;
//                     break;
//                 }
//             }
//         }
//     }

//     let ans = true;
//     for(let c of checked) {
//         if(!c) ans = false;
//     }

    return ans;
}