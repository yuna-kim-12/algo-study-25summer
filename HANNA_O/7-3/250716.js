// 귤 고르기
// https://school.programmers.co.kr/learn/courses/30/lessons/138476

// 문제
// 경화는 과수원에서 귤을 수확했습니다. 경화는 수확한 귤 중 'k'개를 골라 상자 하나에 담아 판매하려고 합니다.
// 그런데 수확한 귤의 크기가 일정하지 않아 보기에 좋지 않다고 생각한 경화는 귤을 크기별로 분류했을 때 서로 다른 종류의 수를 최소화하고 싶습니다.
// 예를 들어, 경화가 수확한 귤 8개의 크기가 [1, 3, 2, 5, 4, 5, 2, 3] 이라고 합시다. 경화가 귤 6개를 판매하고 싶다면, 크기가 1, 4인 귤을 제외한 여섯 개의 귤을 상자에 담으면, 귤의 크기의 종류가 2, 3, 5로 총 3가지가 되며 이때가 서로 다른 종류가 최소일 때입니다.
// 경화가 한 상자에 담으려는 귤의 개수 k와 귤의 크기를 담은 배열 tangerine이 매개변수로 주어집니다.
// 경화가 귤 k개를 고를 때 크기가 서로 다른 종류의 수의 최솟값을 return 하도록 solution 함수를 작성해주세요.

// 아이디어
// 1. 크기별로 개수 세기
// 2. 개수가 많은 것부터 k개가 될 때까지 담기
// 3. 크기의 종류 세서 정답 맞추기

// 내 코드 -> gpt랑 품,,,
function solution(k, tangerines) {
  const counter = {};

  for (const tangerine of tangerines) {
    counter[tangerine] = (counter[tangerine] || 0) + 1;
  }

  const counts = Object.values(counter).sort((a, b) => b - a);

  let total = 0;
  let type = 0;

  for (count of counts) {
    total += count;
    type++;
    if (total >= k) break;
  }

  return type;
}

// 공부
// 1. Object.values() : 객체의 value 값만 뽑아내기
