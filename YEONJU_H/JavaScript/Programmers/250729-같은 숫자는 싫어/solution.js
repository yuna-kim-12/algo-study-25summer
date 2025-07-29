function solution(arr)
{

    // 방법 [1] : 투포인터 방식 : 시간 복잡도 O(N), 공간 복잡도 O(1)
    let readPoint = 0;
    let writePoint = 1;
    for(readPoint = 1; readPoint < arr.length; readPoint++) {
        if(arr[readPoint] !== arr[readPoint-1]) {
            arr[writePoint] = arr[readPoint];
            writePoint++;
        }
    }
    arr.length = writePoint;
    return arr;

    // // 방법 [2] : 새로운 배열 생성 방식 : 시간 복잡도(O(n)) 공간 복잡도(O(n))
    // let ans = [arr[0]];
    // // 새로운 배열을 생성한다.
    //
    // for(let i = 1; i < arr.length; i++) {
    //     if(arr[i] !== arr[i-1])
    //     ans.push(arr[i]);
    // }
    // return ans;


//     for 문을 돌리면서, 중복된 것이 있으면 해당 index를 삭제한다
//     let i = 0;
//     while(i < arr.length - 1 ) {
//         if(arr[i] == arr[i+1]) {
//             arr.splice(i+1,1);
//         } else {
//             i++;
//         }
//     }
//     return arr;

}