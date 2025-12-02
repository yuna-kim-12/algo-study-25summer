function solution(s) {
    const answer = [];
    const lastPosition = {};

    for (let i = 0; i < s.length; i++) {
        const char = s[i];

        if (lastPosition[char] !== undefined) {
            answer.push(i - lastPosition[char]);
        } else {
            // 처음 나온 문자일 경우
            answer.push(-1);
        }

        lastPosition[char] = i;
    }

    return answer;
}