function solution(n) {
    let to3 = n.toString(3); // 10진수 -> 다른 진수로 변환할 때 사용하는 기법
    let reverse3 = to3.split("").reverse().join("");  // js 에서 문자열은 불변이므로 왼쪽과 같은 처리 필요
    let to10 = parseInt(reverse3,3); // 다른 진수 -> 10진수로 변환할 때 사용하는 기법
    return to10;
}