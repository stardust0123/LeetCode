class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return  0

        first_num = 0
        second_num = 1
        i = 1
        while i < n: 
            next_num = first_num + second_num
            first_num = second_num
            second_num = next_num
            i +=1
        return second_num