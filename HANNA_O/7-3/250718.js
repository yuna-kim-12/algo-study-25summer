// 구명보트 (Lv2) 탐욕법
// https://school.programmers.co.kr/learn/courses/30/lessons/42885

// 문제
// 무인도에 갇힌 사람들을 구명보트를 이용하여 구출하려고 합니다. 구명보트는 작아서 한 번에 최대 2명씩 밖에 탈 수 없고, 무게 제한도 있습니다.
// 예를 들어, 사람들의 몸무게가 [70kg, 50kg, 80kg, 50kg]이고 구명보트의 무게 제한이 100kg이라면 2번째 사람과 4번째 사람은 같이 탈 수 있지만 1번째 사람과 3번째 사람의 무게의 합은 150kg이므로 구명보트의 무게 제한을 초과하여 같이 탈 수 없습니다.
// 구명보트를 최대한 적게 사용하여 모든 사람을 구출하려고 합니다.
// 사람들의 몸무게를 담은 배열 people과 구명보트의 무게 제한 limit가 매개변수로 주어질 때, 모든 사람을 구출하기 위해 필요한 구명보트 개수의 최솟값을 return 하도록 solution 함수를 작성해주세요.

// 아이디어1 -> 직관적일 수는 있지만 그리디 방식은 아님
// 1. 무거운 순대로 줄 세우기
// 2. 무거운 사람 먼저 구명 보트에 태우기
// 3. 무게 제한이 남았다면 탈 수 있는 사람 중 가장 무거운 사람이 타기
// 4. 더이상 탈 수 있는 사람이 없다면 다음 보트에 탈 사람 정하기

// 아이디어2
// 1. 무거운 순대로 줄 세우기
// 2. 가장 무거운 사람을 태운 후 가장 가벼운 사람이 탈 수 있는지 확인(투 포인터 사용)
// 3. 위의 과정을 거칠 때마다 보트수 +1

// 내 코드
function solution(people, limit) {
  let answer = 0;
  let start = 0;
  let end = people.length - 1;

  people.sort((a, b) => b - a);

  while (start <= end) {
    if (people[start] + people[end] <= limit) {
      start++;
      end--;
    } else {
      start++;
    }
    answer++;
  }

  return answer;
}

// 다른 사람 코드 -> 나와 같은데 더 간결함
function solution(people, limit) {
  people.sort(function (a, b) {
    return a - b;
  });
  for (let i = 0, j = people.length - 1; i < j; j--) {
    if (people[i] + people[j] <= limit) i++;
  }
  return people.length - i;
}
