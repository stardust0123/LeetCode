class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """ 
        n = len(nums)
        expect_total = n*(n+1) // 2
        actual_total = sum(nums)
        missing_num = expect_total - actual_total 
        return missing_num

