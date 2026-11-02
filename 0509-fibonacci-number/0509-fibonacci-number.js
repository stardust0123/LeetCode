/**
 * @param {number} n
 * @return {number}
 */
var fib = function(n) {
    if (n === 0) {
        return 0;
    }

    let first_num = 0; 
    let second_num = 1;

    for (let i = 1; i < n; i++) {
        let next_num = first_num + second_num; 

        first_num = second_num;
        second_num = next_num;
    }
    return second_num;
};