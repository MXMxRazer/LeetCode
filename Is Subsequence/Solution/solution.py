class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index = 0; 
        subIndex = 0; 
        len_s = len(s);  
        while (index < len(t)):
            if (subIndex < len_s and s[subIndex] == t[index]): 
                subIndex += 1; 
            index += 1; 

        return True if subIndex == len_s else False; 
