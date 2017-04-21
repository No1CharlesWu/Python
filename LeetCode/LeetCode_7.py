# https://leetcode.com/problems/reverse-integer/#/description
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = False
        if x < 0:
            negative = True
        tmp = abs(x)
        tmp_str = str(tmp)
        re_str = tmp_str[::-1]
        re = int(re_str)
        if re > 2**31 - 1:
            return 0
        elif negative:
            return -re
        else:
            return re

test = Solution()
print(test.reverse(1243430))
