class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:                
        magazineDict = defaultdict(int); 
        output = ""; 

        for i in magazine:
            magazineDict[i] += 1; 

        for i in range(len(ransomNote)): 
            if (ransomNote[i] in magazineDict and magazineDict[ransomNote[i]] > 0):
                magazineDict[ransomNote[i]] -= 1; 
                output += ransomNote[i]

        if (output == ransomNote):
            return (True)
        else: 
            return (False)
