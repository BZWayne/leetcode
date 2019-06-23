class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        
        dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        
        ans = 0
        for i in xrange(len(s) - 1):
            if dict[s[i]] >= dict[s[i + 1]]:
                ans += dict[s[i]]
            else:
                ans -= dict[s[i]]
        
        ans += dict[s[-1]]
        
        return ans
        
        
