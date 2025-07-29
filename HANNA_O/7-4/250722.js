// 백준 2566번: 최대값
// https://www.acmicpc.net/problem/2566

// 아이디어
// 1. 2차원 배열로 인풋값 받아오기
// 2. 2중 for문으로 완전탐색하기
// 2-1. 현재 값이 지금까지의 최대값과 크다면 갱신하기
// 3. 완전탐색이 끝나면 최대값 출력하기

// 내 코드
const input = require("fs")
  .readFileSync(
    process.platform === "linux" ? "/dev/stdin" : "HANNA_O/7-4/input.txt"
  )
  .toString()
  .trim()
  .split("\n")
  .map((val) => val.split(" ").map(Number));

let maxi = 0;
let ij = [0, 0];

for (let i = 0; i < 9; i++) {
  for (let j = 0; j < 9; j++) {
    if (input[i][j] > maxi) {
      maxi = input[i][j];
      ij = [i, j];
    }
  }
}

console.log(maxi);
console.log(ij[0] + 1, ij[1] + 1);

// 공부
// 1. 백준에서 자바스크립트로 문제풀기
// https://minjo0n.tistory.com/2
