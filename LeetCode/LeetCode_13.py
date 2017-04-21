# https://leetcode.com/problems/roman-to-integer/#/description
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D':500, 'M': 1000}
        l = []
        for c in s:
            l.append(d[c])
        sum_num = 0
        for i in range(len(l) - 1):
            if l[i] < l[i+1]:
                sum_num -= l[i]
            else:
                sum_num += l[i]
        sum_num += l[-1]
        return sum_num

