# Last updated: 29/04/2026, 19:10:04
1class Solution(object):
2    def twoSum(self, nums, target):
3        """
4        :type nums: List[int]
5        :type target: int
6        :rtype: List[int]
7        """
8        hmap = {}
9        for idx, vl in enumerate(nums):
10            if hmap.get(vl) is not None:
11                return [hmap.get(vl), idx]
12            hmap[target-vl] = idx