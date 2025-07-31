// JadenCase 문자열 만들기
// https://school.programmers.co.kr/learn/courses/30/lessons/12951

// 문제
// JadenCase란 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자인 문자열입니다.
// 단, 첫 문자가 알파벳이 아닐 때에는 이어지는 알파벳은 소문자로 쓰면 됩니다. (첫 번째 입출력 예 참고)
// 문자열 s가 주어졌을 때, s를 JadenCase로 바꾼 문자열을 리턴하는 함수, solution을 완성해주세요.

// 아이디어
// 1. 공백을 기준으로 단어 나누기
// 2. 단어들 소문자로 만들기
// 3. 단어의 첫 문자가 숫자가 아니라면 대문자로 바꾸기
// 4. 단어 사이에 공백 넣어 문장으로 묶기

// 내 코드1 -> 많은 경우 런타임 에러
// 공백 문자가 연속해서 나올 수 있는 경우 고려 안함.
function solution(s) {
  const arr = s.split(" ");
  arr.forEach((val, idx) => {
    val = val.toLowerCase();

    if (isNaN(parseInt(val[0]))) {
      arr[idx] = val[0].toUpperCase() + val.slice(1);
    }
  });

  return arr.join(" ");
}

// 내 코드2 -> 빈 문자열인지 확인 하는 코드 추가 했지만 1 케이스 틀림
// 숫자로 시작하지만 중간에 대문자가 있는 경우 고려 안 함.
function solution(s) {
  const arr = s.split(" ");
  arr.forEach((val, idx) => {
    val = val.toLowerCase();

    if (val[0] && isNaN(parseInt(val[0]))) {
      arr[idx] = val[0].toUpperCase() + val.slice(1);
    }
  });

  return arr.join(" ");
}

// 내 코드3
function solution(s) {
  const arr = s.split(" ");

  arr.forEach((val, idx) => {
    val = val.toLowerCase();

    if (val[0] && isNaN(parseInt(val[0]))) {
      arr[idx] = val[0].toUpperCase() + val.slice(1);
    } else {
      arr[idx] = val; // 숫자로 시작하거나 빈 문자열이면 그대로 소문자로
    }
  });

  return arr.join(" ");
}

// 다른 사람 코드
// 첫 번째는 대문자로, 나머지는 소문자로 바로 바꾸기,,
function solution(s) {
  return s
    .split(" ")
    .map((v) => v.charAt(0).toUpperCase() + v.substring(1).toLowerCase())
    .join(" ");
}

// 공부
// 1. forEach 안에서 val은 복사된 값이어서 arr 배열 안의 값이 바뀌지 않음
arr.forEach((val) => {
  val.toLowerCase();
});
// 2. charAt(idx) : 문자열에서 지정한 인덱스의 문자 반환
// "".charAt(0)이 ""이므로, 빈 문자열에도 안전하게 동작함
const str = "hello";
console.log(str.charAt(0)); // "h"
console.log(str.charAt(1)); // "e"
// 3. substring(start, end?) : 문자열의 일부분을 잘라서 반환(시작, 끝(생략하면 문자열 끝까지))
console.log(str.substring(1)); // "ello"
console.log(str.substring(1, 3)); // "el"

// charAt() vs [] : 안정성이 중요할 때 charAt() 추천, 짧고 빠른 코드엔 []도 괜춘
// substring() vs slice() : slice()가 더 유연하게 쓰일 수 있음. substing은 고전적인 코드에서 많이 사용됨.
