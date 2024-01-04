class Solution:
    def romanToInt(self, s: str) -> int:
        roman_val = {
                        "I": 1, 
                        "V": 5, 
                        "X": 10, 
                        "L": 50, 
                        "C": 100, 
                        "D": 500, 
                        "M": 1000
                    }; 
        sum = 0; 
        for i in range(len(s)):
            if i < len(s) - 1 and roman_val[s[i]] < roman_val[s[i + 1]]:
                sum -= roman_val[s[i]]; 
            else:
                sum += roman_val[s[i]]; 
        return sum;  
