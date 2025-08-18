function solution(sizes) {

    /*
        모든 명함의 길이들을 합친다. (set)
        sort로 오름차순 정렬
        가장 작은 것들부터 차례로 선택하면서 명함이 크기 안에 들어가는지 확인

        이 코드 방식은 필수로 시간초과가 뜰 것 같은데 왜 안뜰까?

        시간 초과가 안 나는 이유는 break + return 때문이에요.
        내부 루프에서 빠른 break
        어떤 (w, h) 조합이 안 맞으면 바로 break 해버림.
        즉, 10000개 명함을 다 확인하는 게 아니라 몇 개만 확인하고 탈출하는 경우가 많음.
        정답 발견 시 바로 return
        사실 이 문제는 max(짧은 변) × max(긴 변)이 답이라,
        (w, h) 후보를 조금만 돌다가 금방 정답에 도달함.
        즉, 2억 조합을 끝까지 다 확인하지 않음.
        "운 좋게 빠르게 답을 찾는 경우"에는 시간 초과가 안 뜸.

    */

    let nums = [];
    for(let s of sizes) {
        nums.push(s[0]);
        nums.push(s[1]);
    }

    nums.sort((a,b) => a-b);
    let w = 0;
    let h = 0;
    let isFit = true;
    for(let i = 0; i < nums.length-1; i++) {
        for(let j = i+1; j < nums.length; j++) {
            w = nums[i];
            h = nums[j];

            for(let s of sizes) {
                if((w >= s[0] && h >= s[1]) || (w >= s[1] && h >= s[0])) {
                    isFit = true;
                } else {
                    isFit = false;
                    break;
                }
            }
            if(isFit) return w*h;
        }
    }
}