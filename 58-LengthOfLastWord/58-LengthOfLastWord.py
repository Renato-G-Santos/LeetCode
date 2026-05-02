# Last updated: 02/05/2026, 10:36:47
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        sWords = s.split() 
        num = len(sWords) -1
        lastWord = sWords[num]

        return len(lastWord)