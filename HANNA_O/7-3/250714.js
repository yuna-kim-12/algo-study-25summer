// 카펫 (Lv2) 완전탐색
// https://school.programmers.co.kr/learn/courses/30/lessons/42842

// Leo는 카펫을 사러 갔다가 아래 그림과 같이 중앙에는 노란색으로 칠해져 있고 테두리 1줄은 갈색으로 칠해져 있는 격자 모양 카펫을 봤습니다.
// Leo는 집으로 돌아와서 아까 본 카펫의 노란색과 갈색으로 색칠된 격자의 개수는 기억했지만, 전체 카펫의 크기는 기억하지 못했습니다.
// Leo가 본 카펫에서 갈색 격자의 수 brown, 노란색 격자의 수 yellow가 매개변수로 주어질 때 카펫의 가로, 세로 크기를 순서대로 배열에 담아 return 하도록 solution 함수를 작성해주세요.

// 아이디어
// brown = 가로 * 세로 - yellow
// yellow = (가로 - 2) * (세로 - 2)
// 1. 가로 세로 조합 찾기
// 1-1. 1부터 전체 격자 수(brown + yellow)의 제곱근 만큼 반복하기
// 1-2. i로 전체 격자 수를 딱 떨어지게 나눴을 때 후보로 넣기
// 2. 각 조합을 계산했을 때 yellow와 같으면 정답

// 내 코드
function solution(brown, yellow) {
  var answer = [];
  n = brown + yellow;
  c = [];

  // 3*3 같은 경우 있을 수 있어서 제곱근 값과 같을 때까지 구해야함.
  for (let i = 1; i <= Math.sqrt(n); i++) {
    if (n % i == 0) {
      c.push([i, n / i]);
    }
  }

  for (val of c) {
    cal = (val[0] - 2) * (val[1] - 2);
    if (cal == yellow) {
      // 가로가 세로보다 큼
      answer = [val[1], val[0]];
      break;
    }
  }
  return answer;
}

// 다른 사람 코드
// 약수 쌍을 구하지 않고 반복문 안에서 조건 검사 + 정답 도출
function solution(brown, yellow) {
  var answer = [];
  // i = 세로길이 후보
  for (var i = 3; i <= (brown + yellow) / i; i++) {
    // x = 가로길이 = 전체격자수 / 세로
    var x = Math.floor((brown + yellow) / i);
    if ((x - 2) * (i - 2) === yellow) {
      break;
    }
  }

  return [x, i];
}

// 공부
// 1. Math.sqrt() : 제곱근(루트) 구하는 함수
// 2. Math.floor() : 내림 함수
