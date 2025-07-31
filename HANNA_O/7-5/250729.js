// 백준 1260번 : DFS와 BFS
// https://www.acmicpc.net/problem/1260

// 아이디어
// - DFS 탐색 : 재귀 또는 스택
// 1. 시작 노드 방문 및 방문 표시
// 2. 현재 방문한 노드와 인접한 노드 중 방문하지 않은 노드 방문 및 방문 표시
// 3. 2번 반복 후 더 이상 반복할 노드가 없다면 이전 노드로 되돌아 가서 다른 노드 탐색
// - BFS 탐색 : 큐
// 1. 시작 노드 큐에 넣고 방문 표시
// 2. 큐가 빌 때까지 큐에서 노드를 꺼내고 해당 노드의 방문하지 않은 이웃들 큐에 넣고 방문 표시 반복

// 내 코드
function dfs(node) {
  visitedDfs[node] = 1;
  resultDfs.push(node);

  for (let next of graph[node]) {
    if (!visitedDfs[next]) {
      dfs(next);
    }
  }
}

function bfs(startNode) {
  const visitedBfs = Array(N + 1).fill(0);
  const resultBfs = [];
  const q = [];

  q.push(startNode);
  visitedBfs[startNode] = 1;

  while (q.length > 0) {
    const node = q.shift();
    resultBfs.push(node);

    for (let next of graph[node]) {
      if (!visitedBfs[next]) {
        visitedBfs[next] = 1;
        q.push(next);
      }
    }
  }
  return resultBfs;
}

const input = require("fs")
  .readFileSync(
    process.platform === "linux" ? "/dev/stdin" : "HANNA_O/7-5/input.txt"
  )
  .toString()
  .trim()
  .split("\n");

const [N, M, V] = input[0].split(" ").map(Number);
const graph = Array.from({ length: N + 1 }, () => []);
for (let i = 1; i <= M; i++) {
  const [u, v] = input[i].split(" ").map(Number);
  graph[u].push(v);
  graph[v].push(u);
}

// 각 리스트 정렬 : 정점 번호가 작은 것을 먼저 방문해야하기 때문
for (let i = 1; i <= N; i++) {
  graph[i].sort((a, b) => a - b);
}

visitedDfs = Array(N + 1).fill(0);
resultDfs = [];
dfs(V);
console.log(resultDfs.join(" "));

const finalResultBfs = bfs(V);
console.log(finalResultBfs.join(" "));

// 공부
// 1. Array.from({ length: N + 1 }, () => [])
// :JavaScript에서 특정 길이를 가진 배열을 만들고, 각 요소를 특정 값으로 초기화할 때 사용되는 유용한 구문
