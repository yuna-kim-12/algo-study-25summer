// 백준 2869번 : 달팽이는 올라가고 싶다
// https://www.acmicpc.net/problem/2869

// 아이디어
// 하루를 올리간 높이(A) - 밤에 내려간 높이(B)로 계산하면 낮에 정상에 올라가는 경우 고려 안하게 됨
// 그러면 정상(V) - 올라간 높이(A)를 미리 뺀 수에서 올리간 높이(A) - 밤에 내려간 높이(B)로 나누고 +1을 하면 되지 않을까?
// 이때 소수점이 나오면 무조건 올림하기.
// input = A B V

// 내 코드
const input = require("fs")
  .readFileSync(
    process.platform === "linux" ? "/dev/stdin" : "HANNA_O/7-4/input.txt"
  )
  .toString()
  .trim()
  .split(" ")
  .map(Number);

const answer = Math.ceil((input[2] - input[0]) / (input[0] - input[1])) + 1;
console.log(answer);
