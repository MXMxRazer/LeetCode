class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False; 
        # hashMap = {};     
        hashMap = {word: s.count(word) for word in set(s)}
 
        # for word in s:
        #     if (word in hashMap):
        #         hashMap[word] += 1; 
        #     else: 
        #         hashMap[word] = 1; 
        for word in t:
            if (word in hashMap):
                hashMap[word] -= 1; 
            continue; 
        return True if (all(value == 0 for value in hashMap.values())) else False; 