# Last updated: 02/05/2026, 10:33:47
1class Solution(object):
2    def lengthOfLastWord(self, s):
3        """
4        :type s: str
5        :rtype: int
6        """
7        sWords = s.split() 
8        num = len(sWords) -1
9        lastWord = sWords[num]
10
11        return len(lastWord)