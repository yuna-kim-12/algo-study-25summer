const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim();

let calu = input.split('-');
let num = [];

for (let i of calu) {
    let sum = 0;
    let tmp = i.split('+');
    for (let j of tmp) {
        sum += parseInt(j);
    }
    num.push(sum);
}

let n = num[0];

for (let i = 1; i < num.length; i++) { 
    n -= num[i];
}

console.log(n);
