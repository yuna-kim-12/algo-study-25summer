// 백준 1018번 : 체스판 다시 칠하기 (완전 탐색)
// https://www.acmicpc.net/problem/1018

// 아이디어
// 1. 인풋 값 2차원 배열로 받기
// 2. 모든 8*8 영역 순회하기
// 3. 검은색 또는 흰색을 기준으로 다시 칠해야 하는 칸 수 계산
// 4. 두 값 중 더 작은 값 선택
// 5. 지금까지 탐색한 것 중 가장 작은 값 갱신
// 6. 최소값 출력

// 내 코드
const input = require("fs")
  .readFileSync(
    process.platform === "linux" ? "/dev/stdin" : "HANNA_O/7-5/input.txt"
  )
  .toString()
  .trim()
  .split("\n");

const [M, N] = input[0].split(" ").map(Number);
const board = input.slice(1);

// 8*8칸으로 나눴을 때 칠해야하는 칸 수 세는 함수
function countRepaint(board, r, c, startColor) {
  let count = 0;

  for (let i = 0; i < 8; i++) {
    for (let j = 0; j < 8; j++) {
      // 기준 색 결정
      // 인덱스끼리 더했을 때 짝수면 startColor 홀수면 반대색
      const expected =
        (i + j) % 2 === 0 ? startColor : startColor === "W" ? "B" : "W";

      // 기준 색이 다르면 카운트하기
      if (board[r + i][c + j] !== expected) {
        count++;
      }
    }
  }

  return count;
}

let mini = Infinity;

for (let i = 0; i <= M - 8; i++) {
  for (let j = 0; j <= N - 8; j++) {
    const countW = countRepaint(board, i, j, "W");
    const countB = countRepaint(board, i, j, "B");
    const localMin = Math.min(countW, countB);
    mini = Math.min(mini, localMin);
  }
}

console.log(mini);
