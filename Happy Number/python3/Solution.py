class Solution:
    def isHappy(self, n: int) -> bool:

        def ending(n, counter): 
            if (n == 1):
                return True; 
            if (counter > 10):
                return False; 
