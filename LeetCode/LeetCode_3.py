# https://leetcode.com/problems/longest-substring-without-repeating-characters/#/description
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest_substring = 0
        start = 0
        d = {}

        for i, c in enumerate(s):
            if c in d and d[c] >= start:
                start = d[c] + 1
            d[c] = i
            end = i
            longest_substring = max(longest_substring, end - start + 1)
        return longest_substring


test = Solution()
print(test.lengthOfLongestSubstring('abcade'))
