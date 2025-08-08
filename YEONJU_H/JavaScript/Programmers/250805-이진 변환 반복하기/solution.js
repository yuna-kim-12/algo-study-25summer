function solution(s) {
    /*
        x의 모든 0 제거
        x의 길이를 c라고 할 경우, x를 2진법으로 표현한 문자열로 변경
        이진 변환 횟수 및 제거된 0의 개수를 담아 return
    */
    let zeroCnt = 0;
    let binaryCnt = 0;

    let binary = s;
    let removedZero = "";
    let makeTo2 = 0;

    // console.log(binary);
    // console.log(parseInt(binary,2));
    while(parseInt(binary, 2) > 1) {
        // 최초 0의 개수
        if(binary.includes("0")) {
            zeroCnt += binary.split("0").length - 1;
            removedZero = binary.replaceAll(0,"");
            makeTo2 = removedZero.length;
        }
        else {
            removedZero = binary;
            makeTo2 = removedZero.length;
        }
        // console.log("binary : ", binary)
        binary = makeTo2.toString(2);
        binaryCnt++;
    }

    return [binaryCnt, zeroCnt];
}