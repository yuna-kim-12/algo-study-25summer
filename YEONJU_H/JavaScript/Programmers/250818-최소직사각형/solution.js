function solution(sizes) {

    /*
        모든 명함의 길이들을 합친다. (set)
        sort로 오름차순 정렬
        가장 작은 것들부터 차례로 선택하면서 명함이 크기 안에 들어가는지 확인
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