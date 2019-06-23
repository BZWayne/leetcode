class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        
        chart = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        
        ans = 0
        for i in xrange(len(s) - 1):
            if chart[s[i]] >= chart[s[i + 1]]:
                ans += chart[s[i]]
            else:
                ans -= chart[s[i]]
        
        ans += chart[s[-1]]
        
        return ans
        
        
