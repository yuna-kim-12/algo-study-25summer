// x만큼 간격이 있는 n개의 숫자
// https://school.programmers.co.kr/learn/courses/30/lessons/12954

// 함수 solution은 정수 x와 자연수 n을 입력 받아,
// x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 리턴해야 합니다.
// 다음 제한 조건을 보고, 조건을 만족하는 함수, solution을 완성해주세요.

// 아이디어
// + x에 1부터 n까지 곱하면서 리스트에 넣기

// 기억이 안나 정리하는 for문,,
// for ([초기문]; [조건문]; [증감문]) {
//   문장 
// }

// 내 코드
// 직관적이지만 길고 JS 함수형 스타일과 다소 거리 있음
function solution(x, n) {
  let answer = [];

  for(let i = 1; i <= n; i++) {
    answer.push(x*i)
  }

  return answer;
}

// 다른 사람 코드
// 짧고 함수형 스타일을 잘 사용함
function solution2(x, n) {
  // Array(n) : 길이 n인 배열 생성(값 비어있음)
  // .fill(x) : 모든 요소를 x로 채움
  // map((v, i) => (i + 1) * v) : i는 인덱스(0부터 시작), v는 값(x)
  return Array(n).fill(x).map((v, i) => (i + 1) * v)
}