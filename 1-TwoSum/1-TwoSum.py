# Last updated: 20/04/2026, 19:23:59
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(len(nums)):
                if (nums[i] + nums[j]) == target and i != j:
                    return i, j