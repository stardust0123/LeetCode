/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let pair = { };
    for (let i = 0; i < nums.length; i++) {
        let complement = target - nums[i];
        if (complement in pair) {
            return [pair[complement], i];
        }
        pair[nums[i]] = i;
    }
};