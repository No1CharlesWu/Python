# https://leetcode.com/problems/valid-parentheses/#/description
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for c in s:
            if c in d.keys():
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                else:
                    c_left = stack.pop()
                    if d[c_left] != c:
                        return False
        else:
            if len(stack) == 0:
                return True
            else:
                return False

test = Solution()
print(test.isValid('(){}([])'))
