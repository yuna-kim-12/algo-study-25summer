function solution(n, lost, reserve) {
    let realLost = lost.filter(l => !reserve.includes(l))
    let realReserve = reserve.filter(r => !lost.includes(r))
    let answer = n - realLost.length;

    realReserve.sort((a,b) => a-b);
    realLost.sort((a, b) => a - b);

    for (let r of realReserve) {
        let idx = -1;

        for (let i = 0; i < realLost.length; i++) {
            if (Math.abs(r - realLost[i]) === 1) {
                idx = i;
                break
            }
        }
        if (idx !== -1) {
            realLost.splice(idx, 1); // 빌려줬으니 제거
            answer += 1;
        }
    }

    return answer;
}

console.log(solution(5, [2, 4], [1, 3, 5]));
console.log(solution(5, [2, 4], [3]));    
console.log(solution(3, [3], [1])); 