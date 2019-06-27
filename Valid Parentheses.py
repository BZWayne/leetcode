class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        delta = len(s)
        while(delta != 0 and delta%2 == 0):
            s = s.replace("()", "")
            s = s.replace("[]", "")
            s = s.replace("{}", "")
        # breaks while loop if string was not altered during current pass
            delta = len(s) if delta > len(s) else 0
        return len(s) == 0
