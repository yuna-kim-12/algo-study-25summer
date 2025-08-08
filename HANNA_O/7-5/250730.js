// 백준 2178번 : 미로 탐색 (그래프 탐색)
// https://www.acmicpc.net/problem/2178

// 아이디어 : BFS
// 1. (0, 0)에서 출발
// 2. 갈 수 있는 위치 탐색하기
// 2-1. 안 가본 곳이라면 방문처리(0만들기)하고 카운트 +1 큐에 행, 열, 이동횟수 넣기
// 3. (N, M)에 도착했을 때 카운트 값 출력

// 내 코드
const input = require("fs")
  .readFileSync(
    process.platform === "linux" ? "/dev/stdin" : "HANNA_O/7-5/input.txt"
  )
  .toString()
  .trim()
  .split("\n");

const [N, M] = input[0].split(" ").map(Number);
let matrix = input.slice(1);
matrix = matrix.map((r) => r.split("").map(Number));

function bfs() {
  // 상하좌우
  const dr = [-1, 1, 0, 0];
  const dc = [0, 0, -1, 1];

  const q = [];

  // 시작점 큐에 넣고 방문 처리
  q.push([0, 0, 1]);
  matrix[0][0] = 0;

  while (q.length > 0) {
    const [r, c, cnt] = q.shift();

    // 만약 종료 지점에 도달하면 카운트 반환
    if (r === N - 1 && c === M - 1) {
      return cnt;
    }

    // 상하좌우 탐색
    for (let i = 0; i < 4; i++) {
      const nr = r + dr[i];
      const nc = c + dc[i];

      // 갈 수 있는 위치 탐색(+ 유효성 검사)
      if (nr >= 0 && nr < N && nc >= 0 && nc < M && matrix[nr][nc] === 1) {
        q.push([nr, nc, cnt + 1]);
        matrix[nr][nc] = 0;
      }
    }
  }
}

console.log(bfs());
