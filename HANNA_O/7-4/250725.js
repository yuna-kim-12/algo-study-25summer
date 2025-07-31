// 백준 1436번 : 영화감독 숌 (브루트 포스)
// https://www.acmicpc.net/problem/1436

// 아이디어 : 브루트 포스로 푸는 문제기 때문에 노가다가 답
// 1. 숫자를 665부터  1씩 증가 시키기
// 2. 그 숫자 안에 666이 포함되어 있는지 확인
// 3. 포함되어 있다면 카운트 +1
// 4. 카운트가 N과 같아지면 그때 숫자 출력

// 내코드
const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "")
  .toString()
  .trim();

let num = 665;
let count = 0;
while (Number(input) !== count) {
  num += 1;
  if (String(num).includes("666")) {
    count += 1;
  }
}

console.log(num);

// 최적화
const target = Number(input);
let count2 = 0;
let num2 = 666;

while (true) {
  if (num2.toString().includes("666")) {
    count2++;
    if (count2 === target) break;
  }
  num2++;
}

console.log(num2);
