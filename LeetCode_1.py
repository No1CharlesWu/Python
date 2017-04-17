# https://leetcode.com/problems/two-sum/#/description
class Solution(object):
    def twosum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return False
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i is not j and nums[i] + nums[j] == target:
                    return [i, j]

    def twosum_hash(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return False
        buf_dict = {}
        for i in range(len(nums)):
            if nums[i] in buf_dict:
                return [buf_dict[nums[i]], i]
            else:
                buf_dict[target - nums[i]] = i

    def twosum_enumerate(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i, num in enumerate(nums):
            if num in dic:
                return [dic[num], i]
            else:
                dic[target - num] = i


test = Solution()
print(test.twosum([3, 2, 4], 6))
print(test.twosum_hash([3, 2, 4], 6))
print(test.twosum_enumerate([3, 2, 4], 6))
