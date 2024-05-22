class Solution:
    def minOperations(self, s: str) -> int:
        counter1 = 0; 
        counter2 = 0; 

        for i in range(len(s)):
            if (i%2 == 0):
                if s[i] == '1':
                    counter1 += 1; 
                else: 
                    counter2 += 1; 
            else: 
                if s[i] == '0':
                    counter1 += 1; 
                else: 
                    counter2 += 1; 


        return min(counter1, counter2);  
