// 최대값과 최솟값
// https://school.programmers.co.kr/learn/courses/30/lessons/12939

// 문제
// 문자열 s에는 공백으로 구분된 숫자들이 저장되어 있습니다.
// str에 나타나는 숫자 중 최소값과 최대값을 찾아 이를 "(최소값) (최대값)"형태의 문자열을 반환하는 함수, solution을 완성하세요.
// 예를들어 s가 "1 2 3 4"라면 "1 4"를 리턴하고, "-1 -2 -3 -4"라면 "-4 -1"을 리턴하면 됩니다.

// 아이디어
// 1. 문자열 스플릿하고 숫자로 바꾸기
// 2. 0번째 숫자와 1번째 숫자 비교해서 최대, 최소값에 넣기
// 3. 그 다음 수와 최대, 최소 비교해서 그 값이 최대 또는 최소라면 갱신
// 4. 마지막 수까지 비교하고 최소, 최대 수 문자열로 만들기

// 공부
// 1. map 함수
// const array1 = [1, 4, 9, 16];
// const map1 = array1.map((x) => x * 2);
// console.log(map1); // [2, 8, 18, 32];

// 내코드
function solution(s) {
  let answer = "";

  let str = s.split(" ").map((s) => Number(s));
  let min = str[0];
  let max = str[0];

  if (str[0] > str[1]) {
    min = str[1];
  } else if (str[0] < str[1]) {
    max = str[1];
  }

  for (let i = 2; i < str.length; i++) {
    if (min > str[i]) {
      min = str[i];
    } else if (max < str[i]) {
      max = str[i];
    }
  }

  answer = `${min} ${max}`;

  return answer;
}

// 다른 사람 코드
function solution(s) {
  const arr = s.split(" ");

  // 스프레드 연산자 사용한 후 최소값, 최대값 바로 찾기
  return Math.min(...arr) + " " + Math.max(...arr);
}
