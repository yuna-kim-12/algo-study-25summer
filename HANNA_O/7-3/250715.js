// 짝지어 제거하기 (Lv2)
// https://school.programmers.co.kr/learn/courses/30/lessons/12973

// 짝지어 제거하기는, 알파벳 소문자로 이루어진 문자열을 가지고 시작합니다.
// 먼저 문자열에서 같은 알파벳이 2개 붙어 있는 짝을 찾습니다.
// 그다음, 그 둘을 제거한 뒤, 앞뒤로 문자열을 이어 붙입니다.
// 이 과정을 반복해서 문자열을 모두 제거한다면 짝지어 제거하기가 종료됩니다.
// 문자열 S가 주어졌을 때, 짝지어 제거하기를 성공적으로 수행할 수 있는지 반환하는 함수를 완성해 주세요.
// 성공적으로 수행할 수 있으면 1을, 아닐 경우 0을 리턴해주면 됩니다.

// 아이디어
// 1. 스택 만들어서 스택의 가장 위 문자와 현재 문자 비교하기
// 2. 만약 같다면 스택에서 제거, 현재 것도 버리기
// 3. 다르다면 스택에 넣기
// 4. 끝났을 때 스택 길이가 0이라면 1, 아니라면 0 반환

// 내 코드 -> 효율성에서 1케이스 통과 못함.
function solution(s) {
  let stack = [];

  for (let char of s) {
    if (stack[stack.length - 1] == char) {
      stack.pop();
    } else {
      stack.push(char);
    }
  }

  return stack.length === 0 ? 1 : 0;
}

// 통과된 코드
// -> for ... of문에서 일반 for문으로 수정
function solution(s) {
  let stack = [];

  for (let i = 0; i < s.length; i++) {
    let char = s[i];
    if (stack[stack.length - 1] == char) {
      stack.pop();
    } else {
      stack.push(char);
    }
  }

  return stack.length === 0 ? 1 : 0;
}
