# Last updated: 25/04/2026, 20:27:25
1class Solution(object):
2    def searchInsert(self, nums, target):
3        """
4        :type nums: List[int]
5        :type target: int
6        :rtype: int
7        """
8        i = 0
9        
10        for i in range(len(nums)):
11            # Se o número atual for igual ao alvo, achamos a posição.
12            # Se o número atual for MAIOR que o alvo, o alvo deveria estar aqui.
13            if nums[i] >= target:
14                return i
15        
16        # Se o loop acabar e não encontrarmos nada, ele deve ser inserido no fim.
17        return len(nums)