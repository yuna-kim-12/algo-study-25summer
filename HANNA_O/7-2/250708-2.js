// 나머지가 1이 되는 수 찾기
// https://school.programmers.co.kr/learn/courses/30/lessons/87389

// 자연수 n이 매개변수로 주어집니다.
// n을 x로 나눈 나머지가 1이 되도록 하는 가장 작은 자연수 x를 return 하도록 solution 함수를 완성해주세요.
// 답이 항상 존재함은 증명될 수 있습니다.

// 아이디어1 => 기각 : 1,000,000까지 있는데 언제 하나하나 계산해?
// 1. n에서 1 빼기
// 2. n-2인 수부터 n-1인 수 나눠보기 => 0 나올 때마다 갱신 

// 아이디어2 => 약수 어떻게 구해?
// 1. n에서 1 빼기
// 2. n-1의 약수 구하기
// 3. 약수 중 가장 작은 수가 답

// 아이디어3
// 1. 2부터 n-1인 수로 n 나누기
// 2. 나머지가 1인 수 나오면 멈추기


// while문 곤부,,
// while (조건문) {
//   문장
// }

// 내 코드
// for문 사용
function solution(n) {
  let answer = 0;

  for (let i = 2; i < n; i++) {
    if (n % i == 1) {
      answer = i
      break
    }
  }

  return answer;
}


// 다른 사람 코드
// 훨씬 간결,,,
function solution(n, x = 1) {    
  while (x++) {
    if (n % x === 1) {
      // 바로 리턴 박기
      return x;
    }
  }    
}
