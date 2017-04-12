# https://leetcode.com/problems/two-sum/#/description
class Solution(object):
    def twoSum(self, nums, target):
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

    def twoSum_Hash(self, nums, target):
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

    def twoSum_enumerate(self, nums, target):
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


Solution.twoSum(Solution, [3, 2, 4], 6)
Solution.twoSum_Hash(1, [3, 2, 4], 6)
Solution.twoSum_enumerate(1, [3, 2, 4], 6)
