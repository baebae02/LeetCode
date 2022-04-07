#13. Roman to Integer
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        s = s[::-1]
        temp = 1
        sum = 0
        for i in s:
            if roman[i] < temp:
                sum = sum - roman[i]
            else:
                temp = roman[i]
                sum = sum + roman[i]
        return sum
