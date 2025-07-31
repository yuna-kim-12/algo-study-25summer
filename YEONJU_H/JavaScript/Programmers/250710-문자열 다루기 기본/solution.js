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

    // 로직 상 한줄로도 가능한 코드 ⭐ 알아두기
//    return s.length == 4 || s.length == 6 ? !isNaN(s) : false
    // 하지만 11번 테케에서 틀린다. ("1e22") 왜냐하면, 1e22 자체를 isNaN(숫자가 아닌가?)으로 검사하면, 지수의 과학적 표기법이라
    // 숫자로 인식되기 때문에 false 가 되어버린다.
}