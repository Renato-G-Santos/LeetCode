# Last updated: 28/04/2026, 21:45:42
1class Solution(object):
2    def removeDuplicates(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        unicos = sorted(list(set(nums)))
8        
9        # 2. Atualiza a lista original 'nums' com os valores únicos
10        nums[:] = unicos
11        
12        # 3. O retorno PRECISA ser um inteiro (o tamanho da lista)
13        return len(nums)
14