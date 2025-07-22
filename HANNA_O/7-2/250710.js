// 올바른 괄호 (Lv2) 스택/큐
// https://school.programmers.co.kr/learn/courses/30/lessons/12909

// 문제
// 괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 닫혀야 한다는 뜻입니다.
// 예를 들어 "()()" 또는 "(())()" 는 올바른 괄호입니다. ")()(" 또는 "(()(" 는 올바르지 않은 괄호입니다.
// '(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 true를 return 하고,
// 올바르지 않은 괄호이면 false를 return 하는 solution 함수를 완성해 주세요.

// 아이디어
// 1. 처음부터 ')' 괄호 나오면 바로 false
// 2. '(' 괄호가 나오면 스택에 넣기
// 3. ')' 괄호가 나오면 '(' 괄호 스택에서 하나 빼기
// 4. 더이상 괄호가 없는데 스택에 괄호가 남아있다면 false
// 5. ')' 괄호 나왔는데 스택에 아무것도 없다면 false

// 내 코드
function solution(s) {
  let answer = true;

  let arr = s.split("");
  let stack = [];

  if (arr[0] === ")") {
    answer = false;
  } else {
    for (let i = 0; i < arr.length; i++) {
      if (arr[i] === "(") {
        stack.push("(");
      } else if (stack.length === 0) {
        answer = false;
        break;
      } else {
        stack.pop();
      }
    }

    if (stack.length !== 0) {
      answer = false;
    }
  }

  return answer;
}

// 다른 사람 코드
// 핵심 아이디어 : 열린 괄호 +1, 닫힌 괄호 -1, 누적값이 0이면 올바른 괄호
function solution(s) {
  let cum = 0;
  for (let paren of s) {
    cum += paren === "(" ? 1 : -1;
    // 누적값이 움수가 되면 닫는 괄호가 더 많은 거니까 무조건 false
    if (cum < 0) {
      return false;
    }
  }
  return cum === 0 ? true : false;
}

//
// 공부
// 1. for ...in : object에서 사용할 수 있는 반복문
const obj = {
  name: "이름",
  age: "나이",
};

for (const key in obj) {
  console.log(key); // key값 출력
  console.log(obj.name, obj.age); // value 값 출력

  console.log(`key 값 : ${key}`); // 1. key값 : 이름 // 2. key값 :age
  console.log(`value 값 : ${obj[key]}`); // 1. value 값 : 이름 // 2. value값 : 나이
}

// 2. for ...of : 반복 가능한 객체에서 사용할 수 있는 반복문(Array, Map, Set, String 등)
const array = ["1번", "2번", "3번"];

for (const element of array) {
  console.log(element); // 배열[0] ~ 끝까지 순차적 출력
  console.log(array); // 배열 전체 출력
}

// 3. forEach() : 배열에 사용되는 메서드
const arr = [1, 2, 3];
arr.forEach((elem) => {
  console.log(elem);
});
