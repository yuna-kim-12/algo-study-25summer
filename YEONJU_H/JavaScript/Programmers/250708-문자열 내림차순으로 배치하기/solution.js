// 코딩테스트 연습 > 연습문제 > 문자열 내림차순으로 배치하기

function solution(s) {
    return s.split("").sort().reverse().join("");
}

// 기본적으로 sort() 하면 대문자가 우선. 