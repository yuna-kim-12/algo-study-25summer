function solution(s) {
    let strings = s.split(" ")

    // 처음엔 for ... of 를 적용했었다. 하지만, of는 복사본을 만들어 사용하는 것이므로, 직접 접근을 통한 변경이 불가해
    // index를 사용하거나 map을 사용해야 했다.

    for(let i = 0; i < strings.length; i++) {
        if(strings[i].length === 0) {  // 빈 문자열 체크 필수!
            continue;
        }

        let start = strings[i].charCodeAt(0);
        if( start >= 97 && start <= 122){
            strings[i] = strings[i][0].toUpperCase() + strings[i].slice(1).toLowerCase();
        } else {
            strings[i] = strings[i][0] + strings[i].slice(1).toLowerCase();
        }
    }

    // 묶어서 else 처리를 하니, 실패. 공백이 연속으로 나올 수 있다는 예외가 있었다. 즉, split한 요소 중 "" 이 있을 수 있음
    // 빈 문자열일 경우를 예외처리해준 뒤, 기존의 첫 글자가 대문자, 숫자일 경우를 처리한 조건을 제거. else 로 통일

    return strings.join(" ");
}