class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        string = s.split(); 
        
        if (len(pattern) != len(string)):
            return False; 
    
        map1 = []; 
        word_indicies, pattern_indicies = {}, {}; 
        map2 = []; 
        for i in pattern:
            if i not in pattern_indicies:
                pattern_indicies[i] = len(pattern_indicies); 
            map1.append(pattern_indicies[i]); 
        for word in string:
            if word not in word_indicies:
                word_indicies[word] = len(word_indicies); 
            map2.append(word_indicies[word]); 
        
        return True if (map1 == map2) else False; 