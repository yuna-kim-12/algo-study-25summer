function solution(s) {
    let sArrays = s.split(" ");
    sArrays = sArrays.map( arr => parseInt(arr));
    sArrays.sort((a,b) => a-b); // 초기 코드 : sArrays.sort(); sort 메서드는 number에 대한 올바른 정렬에는 a,b 비교함수 정의가 필요

//    let last = sArrays.pop(); // 초기 코드
//    return `${sArrays[0]} ${last}`;
    return `${sArrays[0]} ${sArrays[sArrays.length - 1]}`;
}