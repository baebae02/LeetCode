#9. Palindrome Number
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        else : 
            return x == int(str(x)[::-1])
        # return False if x < 0 else x == int(str(x)[::-1])
        
