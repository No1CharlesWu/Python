# https://leetcode.com/problems/reverse-integer/#/description
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        sign = int(x / abs(x))
        tmp = abs(x)
        tmp_str = str(tmp)
        re_str = tmp_str[::-1]
        re = int(re_str)
        if re > 2**31 - 1:
            return 0
        else:
            return re * sign

test = Solution()
print(test.reverse(1243430))
