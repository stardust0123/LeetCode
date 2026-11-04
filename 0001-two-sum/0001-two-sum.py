class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        pair = { }

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in pair:
                return [pair[complement], i]
            pair[nums[i]] = i