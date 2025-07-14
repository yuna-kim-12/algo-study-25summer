// 최소값 만들기 (Lv2) 연습문제
// https://school.programmers.co.kr/learn/courses/30/lessons/12941

// 문제
// 길이가 같은 배열 A, B 두개가 있습니다. 각 배열은 자연수로 이루어져 있습니다.
// 배열 A, B에서 각각 한 개의 숫자를 뽑아 두 수를 곱합니다.
// 이러한 과정을 배열의 길이만큼 반복하며, 두 수를 곱한 값을 누적하여 더합니다.
// 이때 최종적으로 누적된 값이 최소가 되도록 만드는 것이 목표입니다. (단, 각 배열에서 k번째 숫자를 뽑았다면 다음에 k번째 숫자는 다시 뽑을 수 없습니다.)

// 아이디어
// 1. 두 배열 정렬 시키기
// 2. A는 0번째부터 k번째까지, B는 반대로 뽑아서 곱한 후 누적합 구하기

// 내 코드 - 틀림
// sort()가 잘 작동되지 않았을 가능성 큼.
function solution(A, B) {
  var answer = 0;

  A.sort();
  B.sort();

  A.forEach((v, i) => {
    answer += v * B[B.length - 1 - i];
  });

  return answer;
}

// 내코드 - 맞음
function solution(A, B) {
  var answer = 0;

  A.sort((a, b) => a - b);
  B.sort((a, b) => b - a);

  A.forEach((v, i) => {
    answer += v * B[i];
  });

  return answer;
}

// 다른 사람 코드
function solution(A, B) {
  A.sort((a, b) => a - b);
  B.sort((a, b) => b - a);
  return A.reduce((total, val, idx) => total + val * B[idx], 0);
}

// 공부
// reduce() : 배열의 모든 요소를 누적해 하나의 값으로 줄이는 함수
arr.reduce((누적값, 현재값, 인덱스, 원본배열) => {
  return 누적값_업데이트;
}, 초기값);
