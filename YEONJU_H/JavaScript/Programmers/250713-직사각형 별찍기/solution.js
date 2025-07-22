process.stdin.setEncoding('utf8');
process.stdin.on('data', data => {
    const n = data.split(" ");
    const a = Number(n[0]), b = Number(n[1]);

    let line = '';
    for(let i = 0; i < b; i++) {
        line = '';
        for(let j = 0; j < a; j++) {
            line += '*';
        }
        console.log(line);
    }

    // 메서드를 사용한 좀더 simple 한 코드
//    const row = '*'.repeat(a)
//    for(let i =0; i < b; i++){
//        console.log(row)
//    }
});