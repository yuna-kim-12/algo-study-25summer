function solution(s) {
    let isNum = true;
    let sArray = s.split("");
    for( let c of sArray ) { // of 사용할 때 let 타입 정의 빼먹었었음..
        if(isNaN(c)) {
            isNum = false;
        }
    }
    // 처음에 이 조건을 안넣어서 틀렸었다.
    // 그런데, && 이랑 || 논리적으로 헷갈림.
    if(s.length !== 4 && s.length !== 6) {
        isNum = false;
    }

    return isNum;
}