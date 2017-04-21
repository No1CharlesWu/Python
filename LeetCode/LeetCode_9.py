# https://leetcode.com/problems/palindrome-number/#/description
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        tmp = int(str(x)[::-1])
        return tmp == x
