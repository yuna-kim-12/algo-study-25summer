function solution(price, money, count) {

//    let requiredCost = 0;
//
//    for(let i = 1; i <= count; i ++) {
//        requiredCost += price * i;
//    }
//
//    if(requiredCost > money) {
//        return requiredCost - money;
//    }

    let result = (price * count * (count + 1)/2) - money;
    return result > 0 ? result : 0;
}