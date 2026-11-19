class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
# (1) check length of 2 strings, (2) after that count the frequencies of characters in two strings
# (3) initialize hash map (?)
# (4) compare 




        count_s = { }
        count_t = { }

        for c in s: 
            if c in count_s: 
                count_s[c] += 1
            else: 
                count_s[c] = 1
  
        for c in t: 
            if c in count_t: 
                count_t[c] += 1
            else:
                count_t[c] = 1
        
        if count_t == count_s:
            return True
        return False
        
