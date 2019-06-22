class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        integers = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
        romans = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
        res = ""
        
        i = 0
        # keep using the largest numerals possible, else increase i
        while num > 0:
            if num>=integers[i]:
                res+=romans[i]
                num-=integers[i]
            else:
                i+=1
        return res
