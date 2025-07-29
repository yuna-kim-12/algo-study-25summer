// 백준 2903번 : 중앙 이동 알고리즘
// https://www.acmicpc.net/problem/2903

// 아이디어
// 1. 일반항 구하기 : (1 + 2**N)**2
// 2. 인풋 받아 대입하기
// 3. 답 출력하기

// 내 코드
const input = require("fs")
  .readFileSync(
    process.platform === "linux" ? "/dev/stdin" : "HANNA_O/7-4/input.txt"
  )
  .toString()
  .trim();

const answer = (1 + 2 ** Number(input)) ** 2;
console.log(answer);
