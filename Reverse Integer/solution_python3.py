class Solution:
    def reverse(self, x: int) -> int:
        if x>0:
            res=int(str(x)[::-1])
        else:
            res=int("-"+str(abs(x))[::-1])
        if res>=-2147483648 and res<=2147483647:
            return res
        else:
            return 0
