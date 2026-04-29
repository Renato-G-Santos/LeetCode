# Last updated: 29/04/2026, 19:10:25
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unicos = sorted(list(set(nums)))
        
        # 2. Atualiza a lista original 'nums' com os valores únicos
        nums[:] = unicos
        
        # 3. O retorno PRECISA ser um inteiro (o tamanho da lista)
        return len(nums)
