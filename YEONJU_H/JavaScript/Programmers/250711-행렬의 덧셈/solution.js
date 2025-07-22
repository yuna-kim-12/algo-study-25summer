function solution(arr1, arr2) {

    // 3차 코드
    // return arr1.map((arr,idx1) => { return arr.map((a,idx2) => { return a + arr2[idx1][idx2]})});
    return arr1.map((arr,idx1) => arr.map((a,idx2) => a + arr2[idx1][idx2]));

    // 2차 코드
    let ans = [];
    for(let i = 0; i < arr1.length; i++) {
        let sumArr = [];
        for(let j = 0; j < arr1[i].length; j++) { // i로 고쳐서 유연성 부여
            let sum = arr1[i][j] + arr2[i][j];
            sumArr.push(sum);
        }
        ans.push(sumArr);
    }

    // 1차 코드
    let ans = [];
    for(let i = 0; i < arr1.length; i++) {
        let sumArr = [];
        for(let j = 0; j < arr1[0].length; j++) {
            let sum = arr1[i][j] + arr2[i][j];
            sumArr.push(sum);
        }
        ans.push(sumArr);
    }

    return ans;
}