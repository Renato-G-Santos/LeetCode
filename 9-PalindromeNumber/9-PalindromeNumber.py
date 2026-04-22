# Last updated: 22/04/2026, 15:59:07
1class Solution(object):
2    def isPalindrome(self, x):
3        """
4        :type x: int
5        :rtype: bool
6        """
7        if x < 0:
8            z = list(str(x*-1))
9        else:
10            z = list(str(x))
11        z = reversed(z)
12        z = "".join(z)
13        z = int(z)
14        print(z)
15        print((x))
16
17        if z == x:
18            return True
19        else:
20            return False
21
22        
23
24        
25        
26        