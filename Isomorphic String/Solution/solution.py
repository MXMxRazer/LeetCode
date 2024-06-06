class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return self.mask(s) == self.mask(t)
    
    def mask(self, text: str):
        d = {}
        msk = []
        for i in range(len(text)):
            if text[i] in d:
                msk.append(d[text[i]])
            else:
                d[text[i]] = i
                msk.append(i)
        return msk